"""Render the Hebrew assignment README to an RTL-correct PDF via headless Chrome."""

import markdown, pathlib, subprocess, tempfile, os

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "README.md"
PDF_OUT = HERE / "assignment-he.pdf"

body = markdown.markdown(
    SRC.read_text(encoding="utf-8"),
    extensions=["tables", "fenced_code", "sane_lists"],
)

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }

:root {
  --ink: #1A1814;
  --muted: #5C564D;
  --accent: #B85F44;
  --hair: #E0DAD0;
  --paper: #FAF7F2;
}

* { box-sizing: border-box; }

html { direction: rtl; }

body {
  direction: rtl;
  text-align: right;
  font-family: "Arial", "Heebo", "Helvetica Neue", sans-serif;
  font-size: 10.5pt;
  line-height: 1.65;
  color: var(--ink);
  margin: 0;
}

h1 {
  font-size: 24pt;
  font-weight: 700;
  margin: 0 0 6pt;
  letter-spacing: -0.2pt;
}

h1 + p strong { color: var(--muted); font-weight: 600; }

h2 {
  font-size: 15pt;
  font-weight: 700;
  margin: 22pt 0 8pt;
  padding-bottom: 5pt;
  border-bottom: 1.5pt solid var(--accent);
  page-break-after: avoid;
}

h3 {
  font-size: 11.5pt;
  font-weight: 700;
  margin: 14pt 0 4pt;
  color: var(--accent);
  page-break-after: avoid;
}

p { margin: 0 0 8pt; }

strong { font-weight: 700; }

hr {
  border: none;
  border-top: 1pt solid var(--hair);
  margin: 16pt 0;
}

ul, ol { margin: 0 0 10pt; padding-right: 18pt; padding-left: 0; }
li { margin-bottom: 4pt; }

/* Latin identifiers inside Hebrew prose.
   unicode-bidi: plaintext picks direction from the span's own first strong
   character, so `pdfplumber` renders LTR while a Hebrew filename ending in
   `.pdf` stays RTL with the extension in the right place. */
code {
  font-family: "Menlo", "Consolas", monospace;
  font-size: 9pt;
  background: var(--paper);
  border: 0.5pt solid var(--hair);
  border-radius: 3px;
  padding: 1pt 4pt;
  unicode-bidi: plaintext;
  white-space: nowrap;
}

pre {
  direction: ltr;
  text-align: left;
  unicode-bidi: isolate;
  background: var(--ink);
  color: #F5F1EB;
  padding: 11pt 13pt;
  border-radius: 5px;
  overflow-x: auto;
  page-break-inside: avoid;
  margin: 0 0 12pt;
}

pre code {
  background: none;
  border: none;
  padding: 0;
  color: inherit;
  font-size: 8.7pt;
  line-height: 1.55;
  white-space: pre;
}

table {
  direction: rtl;
  width: 100%;
  border-collapse: collapse;
  margin: 0 0 12pt;
  font-size: 9.5pt;
  page-break-inside: avoid;
}

th {
  background: var(--ink);
  color: #F5F1EB;
  font-weight: 700;
  text-align: right;
  padding: 6pt 8pt;
}

td {
  border-bottom: 0.5pt solid var(--hair);
  padding: 5.5pt 8pt;
  vertical-align: top;
}

tbody tr:nth-child(even) { background: var(--paper); }

blockquote {
  border-right: 3pt solid var(--accent);
  border-left: none;
  margin: 0 0 12pt;
  padding: 2pt 12pt;
  color: var(--muted);
}
"""

page = f"""<!doctype html>
<html lang="he" dir="rtl">
<head><meta charset="utf-8"><title>פרויקט הגמר</title><style>{CSS}</style></head>
<body>{body}</body>
</html>"""

with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as fh:
    fh.write(page)
    tmp_html = fh.name

try:
    subprocess.run([
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_OUT}",
        f"file://{tmp_html}",
    ], check=True, capture_output=True)
finally:
    os.unlink(tmp_html)

print("wrote", PDF_OUT, "|", PDF_OUT.stat().st_size, "bytes")
