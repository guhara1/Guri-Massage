#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스·Seznam 등 IndexNow 참여 엔진에 한 번에 전송.

사용법:
  python3 scripts/indexnow.py                 # sitemap.xml 의 모든 URL 통보
  python3 scripts/indexnow.py URL [URL ...]   # 지정한 URL만 통보 (글 추가/수정 시)

동작 원리:
  - 사이트 루트에 {INDEXNOW_KEY}.txt 파일이 있어야 한다(빌드가 자동 생성).
  - api.indexnow.org 로 보내면 참여 검색엔진 전체로 전달된다.
  - Google 은 IndexNow 미참여 → scripts/google_indexing.py 또는 Search Console 이용.
표준 stdlib 만 사용한다(외부 패키지 불필요).
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
ENDPOINT = "https://api.indexnow.org/indexnow"


def urls_from_sitemap() -> list:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls: list) -> None:
    if not urls:
        print("통보할 URL이 없습니다."); return
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow 응답: HTTP {resp.status}  ({len(urls)}개 URL 통보)")
            print("  200=성공, 202=수신됨(키 검증 대기), 400/403=키/형식 오류")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}")
    except Exception as e:  # noqa: BLE001
        print(f"전송 실패: {e}")


if __name__ == "__main__":
    submit(sys.argv[1:] if len(sys.argv) > 1 else urls_from_sitemap())
