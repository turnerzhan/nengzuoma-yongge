#!/usr/bin/env python3
"""Banana 中转站 Image2 (gpt-image-2) 生成「能做吗？勇哥」物料。"""
from __future__ import annotations

import json
import os
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets"


def load_env(p: Path) -> None:
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)


load_env(Path.home() / "projects" / "qian" / ".env")
load_env(ROOT / ".env")

BASE = (os.environ.get("BANANA_BASE_URL") or "https://banana.aigenmedia.art").rstrip("/")
KEY = os.environ.get("BANANA_API_KEY") or os.environ.get("BANANA_AIGENMEDIA_API_KEY") or ""
MODEL = os.environ.get("BANANA_IMAGE_MODEL") or "gpt-image-2"

if not KEY:
    raise SystemExit("缺少 BANANA_API_KEY")

JOBS = [
    (
        "logo.png",
        "1:1",
        "Ultra viral Chinese social media APP ICON square. Giant glossy vermillion rubber stamp "
        "SLAMMING a tiny cartoon empty storefront, impact stars, comic shockwaves, yellow black "
        "hazard stripes, pop-art sticker, pure black background, extreme contrast. "
        "NO landscape NO scenery photo NO photoreal street NO faces NO readable text NO watermark.",
    ),
    (
        "cover-banner.png",
        "16:9",
        "Wide 16:9 viral Douyin thumbnail collage NOT landscape photo. Giant red blank seal crushing "
        "mini shop icon, red yellow black traffic-light orbs, torn brochure stickers, dark void, "
        "glitch sticker chaos, high saturation meme poster. NO realistic skyline NO nature scenery "
        "NO readable text NO watermark.",
    ),
    (
        "hook-card.png",
        "1:1",
        "Square viral meme cover. Angry cartoon uncle silhouette pointing at camera, huge glowing red "
        "STOP orb, broken shop signs and burning money stickers, comic speed lines, black bg red yellow "
        "accent. NO landscape NO scenic photo NO photoreal street NO readable text NO watermark.",
    ),
]


def api(method: str, url: str, data: dict | None = None, timeout: int = 180, tries: int = 6) -> dict:
    last: Exception | None = None
    for i in range(tries):
        try:
            body = None if data is None else json.dumps(data).encode("utf-8")
            req = urllib.request.Request(
                url,
                data=body,
                method=method,
                headers={
                    "Authorization": f"Bearer {KEY}",
                    "Content-Type": "application/json",
                    "User-Agent": "nengzuoma-yongge/0.1",
                },
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001 — network flaky on relay
            last = e
            print(f"  api retry {i + 1}: {type(e).__name__}")
            time.sleep(2 + i * 2)
    assert last is not None
    raise last


def download(url: str, dest: Path) -> int:
    last: Exception | None = None
    for i in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "nengzuoma-yongge/0.1"})
            with urllib.request.urlopen(req, timeout=300) as resp:
                raw = resp.read()
            dest.write_bytes(raw)
            return len(raw)
        except Exception as e:  # noqa: BLE001
            last = e
            print(f"  dl retry {i + 1}: {type(e).__name__}")
            time.sleep(2 + i)
    assert last is not None
    raise last


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"Banana {BASE} model={MODEL}")
    manifest = []
    for file, size, prompt in JOBS:
        print(f"\n→ {file} ({size})")
        created = api(
            "POST",
            f"{BASE}/api/v1/images/generations",
            {"model": MODEL, "prompt": prompt, "size": size, "resolution": "4k", "n": 1},
        )
        task_id = created.get("task_id")
        if not task_id:
            raise SystemExit(f"no task_id: {created}")
        print(f"  task {task_id}")
        url = None
        for _ in range(100):
            time.sleep(4)
            st = api("GET", f"{BASE}/api/v1/images/tasks/{task_id}")
            status = st.get("status")
            print(f"  status={status}")
            if status == "completed" and st.get("url"):
                url = st["url"]
                break
            if status in ("failed", "error"):
                raise SystemExit(st)
        if not url:
            raise SystemExit(f"timeout {file}")
        dest = OUT / file
        n = download(url, dest)
        print(f"  saved {dest.name} ({n/1024:.0f} KB)")
        manifest.append({"file": file, "task_id": task_id, "url": url})

    (OUT / "banana-manifest.json").write_text(
        json.dumps({"model": MODEL, "base": BASE, "jobs": manifest}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print("\nDone")


if __name__ == "__main__":
    main()
