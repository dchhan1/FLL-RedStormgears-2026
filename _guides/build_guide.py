#!/usr/bin/env python3
"""Build styled HTML twins for every markdown doc in the FLL workspace.

Self-contained (stdlib only). Run from anywhere:

    python3 _guides/build_guide.py

For each <name>.md (outside _guides/), writes <name>.html next to it with the
same visual system as coach-dashboard.html. Existing .html files that are NOT
markdown twins are left alone. Relative links between docs are rewritten from
.md to .html so the whole folder works from file:// or any static host.
"""
import os
import re
import html as html_mod

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the FLL folder

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
<style>{extra}</style>
</head>
<body>
<div class="wrap">
<header class="masthead">
  <div class="eyebrow">Red Stormgears · FLL Challenge · BIOGLOW 2026–27</div>
  <div class="crumbs">{crumbs}</div>
  <h1>{title}</h1>
</header>
<main>
{body}
</main>
<footer>
  Part of the Red Stormgears season workspace ·
  <a href="{dash}">← Coach dashboard</a> ·
  <a href="{checklist}">Master checklist</a>
  <br>Generated from <code>{srcname}</code> — edit the markdown, re-run
  <code>_guides/build_guide.py</code> to refresh this page.
</footer>
</div>
</body>
</html>
"""

# extra page-level css shared by every generated page
EXTRA = """
@import url('https://fonts.googleapis.com/css2?family=Bitter:wght@500;600;700&family=Archivo:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');
"""

CRUMB_LABELS = {
    "CHECKLIST.md": "Master checklist",
    "README.md": "Overview",
}


def esc(s):
    return html_mod.escape(s, quote=False)


def inline(s):
    """Render inline markdown: code, bold, italic, links, autolinks, ☐."""
    s = html_mod.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\"'>=\(])(https?://[^\s<)]+)", r'<a href="\1">\1</a>', s)
    s = s.replace("☐", '<input type="checkbox" aria-label="unchecked">')
    s = s.replace("✓", '<input type="checkbox" checked aria-label="checked">')
    return s


def _link(m):
    text, href = m.group(1), m.group(2)
    return '<a href="%s">%s</a>' % (href, text)


def relink(text):
    """Rewrite relative .md links to .html twins and folder links to index.html."""
    def sub(m):
        href = m.group(1)
        if href.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        if ".md" in href:
            return href.replace(".md", ".html")
        if href.endswith("/"):
            return href + "index.html"
        return href
    return re.sub(r'\(([^)\s]+)\)', lambda m: "(" + sub(m) + ")", text)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_table_line(line):
    return line.strip().startswith("|") and line.strip().endswith("|")


def is_sep(line):
    body = line.strip().strip("|")
    return bool(body) and all(re.fullmatch(r":?-{2,}:?", c.strip()) for c in body.split("|"))


def cell_html(text, header=False):
    tag = "th" if header else "td"
    return "<%s>%s</%s>" % (tag, inline(text), tag)


def convert(md):
    md = relink(md)
    # the masthead already shows the doc title; drop a leading '# ' duplicate
    md = re.sub(r"\A#\s+.+\n+", "", md)
    lines = md.splitlines()
    out, i, in_list = [], 0, None

    def flush_list():
        nonlocal in_list
        if in_list:
            out.append("</%s>" % in_list)
            in_list = None

    while i < len(lines):
        line = lines[i]

        # tables
        if is_table_line(line) and i + 1 < len(lines) and is_sep(lines[i + 1]):
            flush_list()
            heads = split_row(line)
            i += 2
            rows = []
            while i < len(lines) and is_table_line(lines[i]):
                rows.append(split_row(lines[i]))
                i += 1
            t = ['<div class="tblwrap"><table><thead><tr>']
            t.append("".join(cell_html(h, True) for h in heads))
            t.append("</tr></thead><tbody>")
            for r in rows:
                r = r + [""] * (len(heads) - len(r))
                t.append("<tr>" + "".join(cell_html(c) for c in r[: len(heads)]) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue

        # headings
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            flush_list()
            level = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline(m.group(2)), level))
            i += 1
            continue

        # hr
        if re.fullmatch(r"-{3,}", line.strip()):
            flush_list()
            out.append("<hr>")
            i += 1
            continue

        # blockquote
        if line.startswith(">"):
            flush_list()
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote><p>%s</p></blockquote>" % inline(" ".join(q for q in quote if q)))
            continue

        # list items (with nesting by 2-space indent, and task checkboxes)
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", line)
        if m:
            indent, marker, text = m.group(1), m.group(2), m.group(3)
            tag = "ol" if marker[0].isdigit() else "ul"
            nested = len(indent) >= 2
            if not nested and in_list != tag:
                flush_list()
                out.append("<%s>" % tag)
                in_list = tag
            task = re.match(r"^\[( |x|X)\]\s+(.*)", text)
            if task:
                checked = " checked" if task.group(1).lower() == "x" else ""
                out.append(
                    '<li class="task"><input type="checkbox"%s aria-label="task">'
                    "<span>%s</span></li>" % (checked, inline(task.group(2)))
                )
            else:
                out.append("<li>%s</li>" % inline(text) if not nested else '<li style="margin-left:18px">%s</li>' % inline(text))
            i += 1
            continue

        # blank
        if not line.strip():
            flush_list()
            i += 1
            continue

        # paragraph (fold consecutive lines)
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|\s*([-*]|\d+\.)\s)", lines[i]):
            para.append(lines[i])
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))

    flush_list()
    return "\n".join(out)


def collect():
    docs = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith((".", "_"))]
        for fn in filenames:
            if fn.endswith(".md"):
                docs.append(os.path.join(dirpath, fn))
    return sorted(docs)


def depth_prefix(path):
    rel = os.path.relpath(path, ROOT)
    return "../" * rel.count(os.sep)


def main():
    made = 0
    for md_path in collect():
        with open(md_path, encoding="utf-8") as f:
            md = f.read()
        m = re.search(r"^#\s+(.+)$", md, re.M)
        title = m.group(1).strip() if m else "Untitled"
        rel = os.path.relpath(md_path, ROOT)
        folder = os.path.dirname(rel)
        label = CRUMB_LABELS.get(os.path.basename(rel), os.path.basename(rel)[:-3].replace("-", " "))
        up = depth_prefix(md_path)
        if folder:
            crumbs = '<a href="%sindex.html">Workspace</a> / <span class="cur">%s</span>' % (up, esc(folder))
        else:
            crumbs = '<span class="cur">%s</span>' % esc(label if os.path.basename(rel) == "README.md" else label)
        page = PAGE.format(
            title=esc(title),
            body=convert(md),
            css=up + "_guides/guide.css",
            extra=EXTRA,
            crumbs=crumbs,
            dash=up + "coach-dashboard.html",
            checklist=up + "CHECKLIST.html",
            srcname=esc(os.path.basename(rel)),
        )
        out_path = md_path[:-3] + ".html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        made += 1
        print("built", os.path.relpath(out_path, ROOT))

    # index.html entry points: every folder (at any depth) that has a README,
    # so directory links (e.g. 03-Robot-Game/lessons/) resolve on any static host.
    # The site root lands on the dashboard — the natural front door.
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith((".", "_"))]
        if "README.md" in filenames:
            target = "coach-dashboard.html" if dirpath == ROOT else "README.html"
            redirect = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
                        '<meta http-equiv="refresh" content="0;url=%s">'
                        '<title>Redirect</title></head><body></body></html>' % target)
            with open(os.path.join(dirpath, "index.html"), "w", encoding="utf-8") as f:
                f.write(redirect)
            made += 1
            print("built", os.path.relpath(os.path.join(dirpath, "index.html"), ROOT))
    print("---\n%d pages" % made)


if __name__ == "__main__":
    main()
