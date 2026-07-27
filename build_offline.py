#!/usr/bin/env python3
"""Build the single-file offline copy from index.html + content.json + images/.
Run:  python3 build_offline.py
Out:  family-tree-offline.html  (everything embedded, opens by double-click)"""
import json, base64, mimetypes, pathlib, sys

root = pathlib.Path(__file__).parent
html = (root/'index.html').read_text(encoding='utf-8')
content = json.loads((root/'content.json').read_text(encoding='utf-8'))

# find the image manifest and swap file paths for embedded data
i = html.find('const IMG = ')
s = html.find('{', i); d = 0; j = s
while True:
    c = html[j]
    if c == '{': d += 1
    elif c == '}':
        d -= 1
        if d == 0: break
    j += 1
man = json.loads(html[s:j+1])

def locate(rel):
    """Find the image whether it sits at the repo root or in images/."""
    name = pathlib.Path(rel).name
    for cand in (root/rel, root/name, root/'images'/name):
        if cand.exists():
            return cand
    return None

embedded, missing = {}, []
for key, rel in man.items():
    p = locate(rel)
    if p is None:
        missing.append(rel); continue
    mime = mimetypes.guess_type(rel)[0] or 'image/jpeg'
    embedded[key] = f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()
if missing:
    print(f'WARNING: {len(missing)} image files missing:', missing[:5], file=sys.stderr)

out = html[:s] + json.dumps(embedded, ensure_ascii=False) + html[j+1:]
# inject the people data so the page never needs to fetch
out = out.replace('<script>\nwindow.IMG = IMG;\n</script>',
                  '<script>\nwindow.IMG = IMG;\nwindow.P = ' + json.dumps(content['people'], ensure_ascii=False)
                  + ';\nwindow.__META = ' + json.dumps({k: v for k, v in content.items() if k != 'people'}, ensure_ascii=False)
                  + ';\n</script>', 1)

dest = root/'family-tree-offline.html'
dest.write_text(out, encoding='utf-8')
print(f'built {dest.name}  {dest.stat().st_size/1e6:.2f} MB  '
      f'({len(embedded)} images, {len(content["people"])} people)')
