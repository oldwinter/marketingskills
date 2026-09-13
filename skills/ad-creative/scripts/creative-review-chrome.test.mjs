import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const html = readFileSync(
  join(dirname(fileURLToPath(import.meta.url)), "../assets/creative-review-template.html"),
  "utf8",
);

assert.match(html, /color-scheme:\s*light dark/);
assert.match(html, /@media \(prefers-color-scheme:\s*dark\)/);
assert.match(html, /class="skip-link"/);
assert.match(html, /href="#preview"/);
assert.match(html, /id="preview"/);
assert.match(html, /role="tabpanel"/);
assert.match(html, /\.concept:focus-visible/);
assert.match(html, /\.seg button:focus-visible/);
assert.match(html, /\.thumb:focus-visible/);
assert.match(html, /\.headline-opt:focus-visible/);
assert.match(html, /prefers-reduced-motion:\s*reduce/);
assert.match(html, /ArrowRight/);
assert.match(html, /aria-controls="preview"/);
assert.match(html, /select a frame/);
assert.equal(html.includes("tap to jump"), false);
assert.equal(html.includes('id="post"'), false);
assert.match(html, /\.post \{ background: #ffffff;/);

console.log("creative-review chrome contract ok");
