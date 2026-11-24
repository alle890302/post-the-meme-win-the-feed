// Entry program for the make.fun bounty "Post the Meme, Win the Feed"
// (u-myronera-post-the-meme-win-the-feed-2de960bf).
//
// The entry itself is a post on X: a meme picture about make.fun, posted
// from a public account with the sponsor's mention and our play code in
// the post's text. This repository hands in the post's address, and this
// program's whole job is to carry that address to the grader: it reads
// POST.json from the repository root and writes it, byte for byte, to
// POST.json in the output directory. Nothing else is computed, and the
// two runs of an entry write the same bytes.
//
// The grader runs this inside its container, where the repository is
// /bot and the output directory is /output. Outside the container the
// MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR environment variables stand in
// for those two paths, e.g.:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
//
// Node 22, standard library only. No network, no clock, no randomness.

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const source = join(botDir, 'POST.json');
const target = join(outputDir, 'POST.json');

let payload: Buffer;
try {
  payload = readFileSync(source);
} catch (err) {
  console.error(`cannot read ${source}: ${(err as Error).message}`);
  process.exit(1);
}

// Validate before handing anything to the grader: POST.json must parse as
// JSON and carry a "url" string that points at a post on x.com (or the
// older twitter.com host). A malformed address would score zero anyway,
// so fail loudly here instead of copying bytes the grader cannot use.
let parsed: unknown;
try {
  parsed = JSON.parse(payload.toString('utf8'));
} catch (err) {
  console.error(`invalid POST.json: not valid JSON (${(err as Error).message})`);
  process.exit(1);
}
const url = (parsed as { url?: unknown } | null)?.url;
const isPostUrl =
  typeof url === 'string' &&
  (url.startsWith('https://x.com/') || url.startsWith('https://twitter.com/'));
if (!isPostUrl) {
  console.error(
    `invalid POST.json: "url" must be a string starting with https://x.com/ or https://twitter.com/ (got ${JSON.stringify(url)})`,
  );
  process.exit(1);
}

mkdirSync(outputDir, { recursive: true });
writeFileSync(target, payload);
