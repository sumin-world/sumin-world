from __future__ import annotations
import os, re, json
from pathlib import Path
from typing import List, Dict, Any, Tuple
from ytmusicapi import YTMusic

README = Path("README.md")
NUM_RECENT = int(os.environ.get("YTM_NUM_RECENT", 5))
NUM_LIKED  = int(os.environ.get("YTM_NUM_LIKED", 6))

ANCHOR_NOW   = "YTM-NOW-PLAYING"
ANCHOR_REC   = "YTM-RECENT"
ANCHOR_LIKED = "YTM-LIKED"

SECTION_TEMPLATE = (
    f"### 🎶 Now Playing (YouTube Music)\n"
    f"<!-- {ANCHOR_NOW}:START -->\n"
    f"[![YouTube Music](https://yt-music-profile.vercel.app/api?theme=dark)](https://music.youtube.com)\n"
    f"<!-- {ANCHOR_NOW}:END -->\n\n"
    f"### ⏱️ Recently Played\n"
    f"<!-- {ANCHOR_REC}:START -->\n"
    f"Loading...\n"
    f"<!-- {ANCHOR_REC}:END -->\n\n"
    f"### ❤️ Liked Songs\n"
    f"<!-- {ANCHOR_LIKED}:START -->\n"
    f"Loading...\n"
    f"<!-- {ANCHOR_LIKED}:END -->\n"
)

def md_escape(s: str) -> str:
    return s.replace("|", "\\|")

def make_list(items: List[Dict[str, Any]]) -> str:
    out = []
    for i, it in enumerate(items, 1):
        title = md_escape(it.get("title", ""))
        artists = ", ".join(a.get("name", "") for a in it.get("artists", []) if a)
        album = it.get("album", {}).get("name", "") if it.get("album") else ""
        vid = it.get("videoId")
        link = f"https://music.youtube.com/watch?v={vid}" if vid else ""
        bullet = f"{i}. [{title}]({link}) — {artists}" if link else f"{i}. {title} — {artists}"
        if album:
            bullet += f" (_{md_escape(album)}_)"
        out.append(f"- {bullet}")
    return "\n".join(out) if out else ""

def section_replace(content: str, key: str, new_block: str) -> str:
    pat = re.compile(rf"(<!-- {re.escape(key)}:START -->)(.*?)(<!-- {re.escape(key)}:END -->)", re.DOTALL)
    return pat.sub(lambda m: f"{m.group(1)}\n{new_block}\n{m.group(3)}", content)

def ensure_anchors(content: str) -> str:
    has_all = all(
        f"<!-- {k}:START -->" in content and f"<!-- {k}:END -->" in content
        for k in (ANCHOR_NOW, ANCHOR_REC, ANCHOR_LIKED)
    )
    if not has_all:
        sep = "\n\n---\n\n" if not content.rstrip().endswith("---") else "\n\n"
        return content.rstrip() + sep + SECTION_TEMPLATE
    return content

def fetch(ytm: YTMusic) -> Tuple[str, str]:
    # 최근 들은 노래
    try:
        hist = ytm.get_history() or []
    except Exception:
        hist = []
    rec = []
    for e in hist:
        if isinstance(e, dict) and e.get("videoId"):
            rec.append({
                "title": e.get("title",""),
                "artists": e.get("artists",[]),
                "album": e.get("album",{}),
                "videoId": e.get("videoId")
            })
            if len(rec) >= NUM_RECENT:
                break
    recent_md = make_list(rec) if rec else "_No recent tracks found_"

    # 좋아요 한 노래
    try:
        liked = ytm.get_liked_songs(limit=NUM_LIKED) or {}
    except Exception:
        liked = {}
    liked_items = []
    for tr in (liked.get("tracks", []) or [])[:NUM_LIKED]:
        liked_items.append({
            "title": tr.get("title",""),
            "artists": tr.get("artists",[]),
            "album": tr.get("album",{}),
            "videoId": tr.get("videoId")
        })
    liked_md = make_list(liked_items) if liked_items else "_No liked songs yet_"
    return recent_md, liked_md

def init_client() -> YTMusic:
    # 1) OAuth 우선
    oauth_path = Path(os.environ.get("YTM_OAUTH_PATH", "oauth.json"))
    if oauth_path.exists() and oauth_path.stat().st_size > 0:
        data = json.loads(oauth_path.read_text(encoding="utf-8"))
        # 중요: JSON 안의 credentials를 분리해 인자로 전달, JSON 쪽에서는 제거
        creds = data.pop("credentials", None)
        if not creds:
            # 파일에 없으면 환경변수로 보완
            cid  = os.environ.get("GOOGLE_CLIENT_ID")
            csec = os.environ.get("GOOGLE_CLIENT_SECRET")
            if not cid or not csec:
                raise SystemExit("[ERROR] oauth.json에 credentials가 없고, GOOGLE_CLIENT_ID/GOOGLE_CLIENT_SECRET도 없습니다.")
            creds = {"client_id": cid, "client_secret": csec}
        return YTMusic(data, oauth_credentials=creds)

    # 2) headers_auth.json (쿠키 방식) 폴백
    headers_path = Path(os.environ.get("YTM_HEADERS_PATH", "headers_auth.json"))
    if headers_path.exists() and headers_path.stat().st_size > 0:
        return YTMusic(str(headers_path))

    raise SystemExit("[ERROR] Neither oauth.json nor headers_auth.json found (or empty).")

def main() -> None:
    if not README.exists():
        raise SystemExit(f"[ERROR] README.md not found: {README.resolve()}")
    content = ensure_anchors(README.read_text(encoding="utf-8"))

    ytm = init_client()
    recent_md, liked_md = fetch(ytm)

    updated = section_replace(section_replace(content, ANCHOR_REC, recent_md), ANCHOR_LIKED, liked_md)
    if updated != content:
        README.write_text(updated, encoding="utf-8")
        print("[OK] README updated")
    else:
        print("[OK] No changes")

if __name__ == "__main__":
    main()
