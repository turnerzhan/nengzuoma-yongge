/**
 * 用 banana 中转站 Image2 (gpt-image-2) 生成「能做吗？勇哥」传播物料
 * 密钥读 projects/qian/.env 的 BANANA_API_KEY
 *
 * node scripts/gen-banana-assets.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "docs", "assets");

function loadEnvFile(p) {
  if (!fs.existsSync(p)) return;
  for (const line of fs.readFileSync(p, "utf8").split(/\r?\n/)) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)$/i);
    if (!m) continue;
    let v = m[2].trim();
    if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'")))
      v = v.slice(1, -1);
    if (!process.env[m[1]]) process.env[m[1]] = v;
  }
}

loadEnvFile(path.join(process.env.USERPROFILE || "", "projects", "qian", ".env"));
loadEnvFile(path.join(ROOT, ".env"));

const BASE = (process.env.BANANA_BASE_URL || "https://banana.aigenmedia.art").replace(/\/+$/, "");
const KEY = process.env.BANANA_API_KEY || process.env.BANANA_AIGENMEDIA_API_KEY || "";
const MODEL = process.env.BANANA_IMAGE_MODEL || "gpt-image-2";

if (!KEY) {
  console.error("缺少 BANANA_API_KEY");
  process.exit(1);
}

const JOBS = [
  {
    file: "logo.png",
    size: "1:1",
    prompt: `Ultra viral Chinese social media APP ICON, square, maximal punch.
A giant glossy vermillion rubber stamp SLAMMING down onto a tiny cartoon empty storefront,
impact stars, comic shockwaves, yellow and black hazard stripes in corners,
pop-art sticker style, pure black background, extreme contrast, meme energy.
NO landscape, NO scenery photo, NO photoreal street, NO people faces, NO readable text, NO letters, NO watermark.`,
  },
  {
    file: "cover-banner.png",
    size: "16:9",
    prompt: `Wide 16:9 viral Douyin thumbnail collage, NOT a landscape photo.
Left half: giant red circular seal with blank surface (no letters) crushing a mini shop icon.
Right half: red yellow black traffic-light orbs and torn franchise brochure fragments as flat stickers.
Dark void background, glitch sticker chaos, high saturation, scroll-stopping meme poster energy.
NO realistic city skyline, NO scenic photography, NO nature scenery, NO readable text, NO watermark.`,
  },
  {
    file: "hook-card.png",
    size: "1:1",
    prompt: `Square viral content card visual, exaggerated 3D cartoon.
An angry cartoon uncle silhouette pointing at camera, next to a huge glowing red STOP orb,
tiny broken shop signs and burning money stickers flying, comic speed lines,
black background, red yellow accent, pure meme cover art for anti-scam franchise content.
NO landscape, NO scenic photo, NO photoreal street, NO readable Chinese or English text, NO watermark.`,
  },
];

async function createTask(prompt, size) {
  const res = await fetch(`${BASE}/api/v1/images/generations`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: MODEL,
      prompt,
      size: size || "1:1",
      resolution: "4k",
      n: 1,
    }),
  });
  const text = await res.text();
  if (!res.ok) throw new Error(`create ${res.status}: ${text.slice(0, 400)}`);
  const data = JSON.parse(text);
  if (!data.task_id) throw new Error(`no task_id: ${text.slice(0, 400)}`);
  return data.task_id;
}

async function pollTask(taskId) {
  const url = `${BASE}/api/v1/images/tasks/${taskId}`;
  for (let i = 0; i < 100; i++) {
    const res = await fetch(url, {
      headers: { Authorization: `Bearer ${KEY}` },
    });
    const data = await res.json();
    if (data.status === "completed" && data.url) return data.url;
    if (data.status === "failed" || data.status === "error") {
      throw new Error(`failed: ${JSON.stringify(data).slice(0, 400)}`);
    }
    await new Promise((r) => setTimeout(r, 4000));
  }
  throw new Error("poll timeout");
}

async function download(url, dest) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`download ${res.status}`);
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(dest, buf);
  return buf.length;
}

async function main() {
  fs.mkdirSync(OUT, { recursive: true });
  const manifest = [];
  console.log(`Banana ${BASE} model=${MODEL}`);
  for (const job of JOBS) {
    console.log(`\n→ ${job.file} (${job.size})`);
    const taskId = await createTask(job.prompt, job.size);
    console.log(`  task ${taskId}`);
    const url = await pollTask(taskId);
    const dest = path.join(OUT, job.file);
    const bytes = await download(url, dest);
    console.log(`  saved ${(bytes / 1024).toFixed(0)} KB`);
    manifest.push({ file: job.file, taskId, url, at: new Date().toISOString() });
  }
  fs.writeFileSync(path.join(OUT, "banana-manifest.json"), JSON.stringify({ model: MODEL, jobs: manifest }, null, 2));
  console.log("\nDone → docs/assets/");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
