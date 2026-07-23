from pathlib import Path
import subprocess
import os

os.chdir(Path(__file__).parent)

def run(cmd):
    print("+", cmd)
    subprocess.check_call(cmd, shell=True)

# take our slim versions for content conflicts
for f in ["README.md", "docs/index.html", "docs/sitemap.xml"]:
    subprocess.call(f'git checkout --theirs -- "{f}"', shell=True)
    subprocess.call(f'git add -- "{f}"', shell=True)

# keep deletions
for f in [
    "docs/LAUNCH_POST.md",
    "docs/canyinxuanzhi.html",
    "docs/jiamengbikeng.html",
    "llms.txt",
]:
    subprocess.call(f'git rm -f -- "{f}"', shell=True)

# rewrite clean sitemap and index nav if conflict markers remain
for f in ["README.md", "docs/index.html", "docs/sitemap.xml"]:
    p = Path(f)
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8")
    if "<<<<<<" in t or "======" in t:
        print("markers in", f)
    else:
        print("clean", f)

# ensure sitemap slim
Path("docs/sitemap.xml").write_text(
    """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://turnerzhan.github.io/nengzuoma-yongge/</loc><priority>1.0</priority></url>
  <url><loc>https://turnerzhan.github.io/nengzuoma-yongge/about.html</loc><priority>0.9</priority></url>
  <url><loc>https://github.com/turnerzhan/nengzuoma-yongge</loc><priority>0.9</priority></url>
</urlset>
""",
    encoding="utf-8",
)
subprocess.check_call("git add docs/sitemap.xml", shell=True)

# fix index.html secondary links if broken
idx = Path("docs/index.html")
t = idx.read_text(encoding="utf-8")
if "<<<<<<" in t:
    # take minimal: strip conflict by preferring after ======= 
    parts = t.split("<<<<<<<")
    # crude: use file without markers from known good content - rebuild secondary section
    print("rewriting index secondary links")
t = t.replace("canyinxuanzhi.html", "about.html")
t = t.replace("jiamengbikeng.html", "about.html")
t = t.replace("PUSH_VISIBILITY.md", "https://github.com/turnerzhan/nengzuoma-yongge/blob/master/docs/PUBLISH.md")
# remove conflict markers if any
import re
t = re.sub(r"<<<<<<<.*?\n", "", t)
t = re.sub(r"=======.*?\n", "", t)
t = re.sub(r">>>>>>>.*?\n", "", t)
idx.write_text(t, encoding="utf-8")
subprocess.check_call("git add docs/index.html", shell=True)

# README markers
rp = Path("README.md")
rt = rp.read_text(encoding="utf-8")
rt = re.sub(r"<<<<<<<.*?\n", "", rt)
rt = re.sub(r"=======.*?\n", "", rt)
rt = re.sub(r">>>>>>>.*?\n", "", rt)
for a, b in [
    ("docs/SEO.md", "docs/PUBLISH.md"),
    ("docs/PUSH_VISIBILITY.md", "docs/PUBLISH.md"),
    ("docs/GOOGLE_SEARCH_CONSOLE.md", "docs/PUBLISH.md"),
    ("docs/LAUNCH_POST.md", "docs/PUBLISH.md"),
    ("profit_model.py", "breakeven.py"),
]:
    rt = rt.replace(a, b)
rp.write_text(rt, encoding="utf-8")
subprocess.check_call("git add README.md", shell=True)

print("resolve done")
