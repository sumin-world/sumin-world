from __future__ import annotations
import os
import re
from pathlib import Path
from typing import List, Dict, Any
from ytmusicapi import YTMusic

README = Path("README.md")
HEADERS_PATH = Path(os.environ.get("YTM_HEADERS_PATH", "headers_auth.json"))
NUM_RECENT = int(os.environ.get("YTM_NUM_RECENT", 5))
NUM_LIKED  = int(os.environ.get("YTM_NUM_LIKED", 6))

ANCHOR_NOW   = "YTM-NOW-PLAYING"
ANCHOR_REC   = "YTM-RECENT"
ANCHOR_LIKED = "YTM-LIKED"

SECTION_TEMPLATE = f"""
### 🎶 Now Playing (YouTube Music)
<!-- {ANCHOR_NOW}:START -->
[![YouTube Music](https://yt-music-profile.vercel.app/api?theme=dark)](https://music.youtube.com)
<!-- {ANCHOR_NOW}:END -->

### ⏱️ Recently Played
<!-- {ANCHOR_REC}:START -->
Loading...
<!-- {ANCHOR_REC}:END -->

### ❤️ Liked Songs
<!-- {ANCHOR_LIKED}:START -->
Loading...
<!-- {ANCHOR_LIKED}:END -->
""".strip() + "\n"

def md_escape(text: str) -> str:
    return text.replace("|", "\\|")

def make_list(items: List[Dict[str, Any]]) -> str:
    lines: List[str] = []
    for i, it in enumerate(items, 1):
        title = md_escape(it.get("title", ""))
        artists = ", ".join(a.get("name", "") for a in it.get("artists", []) if a)
        album = it.get("album", {}).get("name", "") if it.get("album") else ""
        vid = it.get("videoId")
        link = f"https://music.youtube.com/watch?v={vid}" if vid else ""
        bullet = f"{i}. [{title}]({link}) — {artists}" if link else f"{i}. {title} — {artists}"
        if album:
            bullet += f" (_{md_escape(album)}_)"
        lines.append(f"- {bullet}")
    return "\n".join(lines) if lines else ""

def section_replace(content: str, key: str, new_block: str) -> str:
    pattern = re.compile(rf"(<!-- {re.escape(key)}:START -->)(.*?)(<!-- {re.escape(key)}:END -->)", re.DOTALL)
    if pattern.search(content):
        return pattern.sub(lambda m: f"{m.group(1)}\n{new_block}\n{m.group(3)}", content)
    return content

def ensure_anchors(content: str) -> str:
    has_any = any(
        f"<!-- {k}:START -->" in content and f"<!-- {k}:END -->" in content
        for k in (ANCHOR_NOW, ANCHOR_REC, ANCHOR_LIKED)
    )
    if not has_any:
        sep = "\n\n---\n\n" if not content.rstrip().endswith("---") else "\n\n"
        return content.rstrip() + sep + SECTION_TEMPLATE
    return content

def fetch_recent_and_liked(ytm: YTMusic) -> (str, str):
    try:
        history = ytm.get_history() or []
    except Exception:
        history = []
    recent_tracks: List[Dict[str, Any]] = []
    for entry in history:
        if isinstance(entry, dict) and entry.get("videoId"):
            recent_tracks.append({
                "title": entry.get("title", ""),
                "artists": entry.get("artists", []),
                "album": entry.get("album", {}),
                "videoId": entry.get("videoId"),
            })
            if len(recent_tracks) >= NUM_RECENT:
                break
    recent_md = make_list(recent_tracks) if recent_tracks else "_No recent tracks found_"

    try:
        liked = ytm.get_liked_songs(limit=NUM_LIKED)
    except Exception:
        liked = {}
    liked_items: List[Dict[str, Any]] = []
    for tr in (liked.get("tracks", []) or [])[:NUM_LIKED]:
        liked_items.append({
            "title": tr.get("title", ""),
            "artists": tr.get("artists", []),
            "album": tr.get("album", {}),
            "videoId": tr.get("videoId"),
        })
    liked_md = make_list(liked_items) if liked_items else "_No liked songs yet_"

    return recent_md, liked_md

def main() -> None:
    if not README.exists():
        raise SystemExit(f"[ERROR] README.md not found: {README.resolve()}")
    if not HEADERS_PATH.exists():
        raise SystemExit(f"[ERROR] headers_auth.json not found: {HEADERS_PATH.resolve()}")

    content = README.read_text(encoding="utf-8")
    content = ensure_anchors(content)
    ytm = YTMusic(str(HEADERS_PATH))
    recent_md, liked_md = fetch_recent_and_liked(ytm)
    updated = section_replace(content, ANCHOR_REC, recent_md)
    updated = section_replace(updated, ANCHOR_LIKED, liked_md)

    if updated != content:
        README.write_text(updated, encoding="utf-8")
        print("[OK] README updated")
    else:
        print("[OK] No changes")

if __name__ == "__main__":
    main()
