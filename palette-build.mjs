import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const out = path.join(root, 'dist');
const themePath = path.join(root, 'sole-theme.css');
const theme = fs.readFileSync(themePath, 'utf8');

fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

const files = fs.readdirSync(root, { withFileTypes: true });

for (const entry of files) {
  if (!entry.isFile()) continue;
  if (['vercel.json', 'palette-build.mjs'].includes(entry.name)) continue;

  const src = path.join(root, entry.name);
  const dest = path.join(out, entry.name);

  if (entry.name.endsWith('.html')) {
    let html = fs.readFileSync(src, 'utf8');
    if (!html.includes('id="sole-theme-palette"')) {
      const block = `\n<style id="sole-theme-palette">\n${theme}\n</style>\n`;
      html = html.replace('</head>', `${block}</head>`);
    }
    fs.writeFileSync(dest, html, 'utf8');
  } else {
    fs.copyFileSync(src, dest);
  }
}

console.log('SoleTasker palette build complete.');
