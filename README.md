# Benson · Foley · Tremblay Family Tree

Live site: `https://northy329.github.io/family-tree/`

156 people, 125 photographs, six generations charted, fifteen more written out behind them.

---

## How to update it

**You edit one file: `content.json`.** Nothing else.

1. Open `content.json` on GitHub and click the pencil icon, or edit it locally.
2. Find the person. Search for their name.
3. Change the text.
4. Commit. The site rebuilds in about a minute.

### The one rule

**Never type a straight double-quote `"` inside any text.** It ends the field and breaks the file.

Use a curly quote `"` `"` or a single quote `'` instead. Everything else is safe: apostrophes, commas, accents, and HTML like `<b>bold</b>` or `<i>italic</i>` all work.

If you break it anyway, the build fails and GitHub emails you with the line number. The live site keeps showing the last good version until you fix it, so a mistake is never visible to the family.

### What a person looks like

```json
"lillian": {
  "name": "Lillian M. Tremblay",
  "life": "1926–2007",
  "role": "Horace's wife",
  "vitals": [
    ["Born", "<b>28 Jan 1926</b>, Attleboro, Massachusetts"],
    ["Died", "<b>2 Mar 2007</b>"]
  ],
  "bio": [
    { "t": "The seventh of nine children." },
    { "t": "Something we are not sure about.", "uncertain": true }
  ],
  "rel": ["horace", "raymond"],
  "photos": [ { "key": "lillian_conf", "cap": "Her confirmation, 1941." } ]
}
```

- `vitals` is the facts box. Each row is `["Label", "Value"]`. Add `true` as a third item to mark it uncertain.
- `bio` is the prose. Each paragraph is its own block. `"uncertain": true` renders it in the hedged style.
- `rel` links to other people by their id.
- `photos` refers to keys in the image manifest inside `index.html`.

### Adding a photograph

1. Upload the file to the repository root, alongside the other photographs.
2. In `index.html`, find `const IMG = {` and add `"my_key": "myfile.jpg",`
3. In `content.json`, add `{ "key": "my_key", "cap": "What it shows." }` to that person's `photos`.

### Adding a person

Copy an existing block, change the id and the contents. To make them appear on the chart rather than only in the extended-family lists, they also need a `kicker` matching one of the branch headings, or a `chip()` call in `index.html`.

---

## What gets built

| File | What it is |
|---|---|
| `index.html` | The site. Loads `content.json` at run time. |
| `content.json` | **The file you edit.** All 156 people. |
| the 125 `.jpg` files | The photographs and documents, in the repository root. |
| `family-tree-offline.html` | Single self-contained file, rebuilt automatically on every push. This is the one to email to relatives and keep as an archive copy. |
| `build_offline.py` | Makes that file. Run `python3 build_offline.py` to build locally. |

`index.html` will not work by double-clicking it from your desktop, because browsers block a local page from reading `content.json`. That is what `family-tree-offline.html` is for.

---

## The suggestion feature

Relatives can mark corrections and memories directly in the page. Bottom right, "Suggest an edit." Their notes stay in their own browser until they send them to you, either copied into an email or downloaded as a `.json` file.

Nothing they do changes the site. You decide what goes in.

When someone sends you suggestions, apply them by editing `content.json` and add a line to the `CHANGES` list in `index.html` so nobody sends the same thing twice.

---

## Setting up GitHub Pages

1. Create a public repository and push these files to `main`.
2. Settings → Pages → Source: **GitHub Actions**.
3. Push. The workflow validates `content.json`, checks every photo reference resolves, rebuilds the offline copy, and deploys.

---

## Sources

John Brennan, Dublin — Foley (rev. Oct 2024), Gore (Nov 2020) and O'Keeffe genealogies.
Michelle (Tremblay) Schulze — fifteen generations behind Marion Audette.
Don and Deborah Tremblay — Raymond's war record and the 2018 DNA results.
Cindy Benson — circulated the Raymond material to the family in June 2024.
Miriam O'Keeffe — donated Eoin O'Keeffe's papers to the National Library of Ireland (MS Acc. 11,221) and Josephine's 1931 letters to Imirce at the University of Galway, both in 2026.
