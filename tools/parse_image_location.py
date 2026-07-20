#!/usr/bin/env python3
"""Extract GPS from image EXIF if present. Stdout JSON. No third-party deps required for basic path;
tries Pillow if available for broader format support.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def _ratio_to_float(x) -> float:
    try:
        return float(x[0]) / float(x[1]) if isinstance(x, tuple) else float(x)
    except Exception:
        return float(x)


def dms_to_deg(dms, ref: str) -> float:
    d, m, s = (_ratio_to_float(x) for x in dms)
    deg = d + m / 60.0 + s / 3600.0
    if ref in ("S", "W"):
        deg = -deg
    return deg


def from_pillow(path: Path) -> dict | None:
    try:
        from PIL import Image
        from PIL.ExifTags import GPSTAGS, TAGS
    except ImportError:
        return None

    img = Image.open(path)
    raw = img._getexif() or {}
    if not raw:
        return {"ok": False, "error": "no_exif"}

    exif = {TAGS.get(k, k): v for k, v in raw.items()}
    gps_raw = exif.get("GPSInfo")
    if not gps_raw:
        return {"ok": False, "error": "no_gps"}

    gps = {GPSTAGS.get(k, k): v for k, v in gps_raw.items()}
    if "GPSLatitude" not in gps or "GPSLongitude" not in gps:
        return {"ok": False, "error": "incomplete_gps"}

    lat = dms_to_deg(gps["GPSLatitude"], gps.get("GPSLatitudeRef", "N"))
    lng = dms_to_deg(gps["GPSLongitude"], gps.get("GPSLongitudeRef", "E"))
    return {
        "ok": True,
        "latitude": round(lat, 6),
        "longitude": round(lng, 6),
        "location": f"{lng:.6f},{lat:.6f}",
        "source": "exif_pillow",
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(json.dumps({"ok": False, "error": "usage: parse_image_location.py <image>"}))
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(json.dumps({"ok": False, "error": "file_not_found"}))
        return 1

    result = from_pillow(path)
    if result is None:
        result = {
            "ok": False,
            "error": "pillow_not_installed",
            "hint": "pip install pillow",
        }
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
