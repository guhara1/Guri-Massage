#!/usr/bin/env python3
"""Google Indexing API — 개별 URL 즉시 색인 요청(URL_UPDATED) 또는 삭제(URL_DELETED).

⚠️ 공식적으로 Google Indexing API 는 JobPosting / BroadcastEvent 구조화 페이지만
   지원합니다. 일반 콘텐츠에는 공식 지원 대상이 아니며, 권장 경로는
   Search Console 등록 + sitemap.xml 제출 + (변경 시) URL 검사→색인 요청 입니다.
   그럼에도 URL 통보 용도로 사용하려면 아래 절차가 필요합니다.

준비:
  1) Google Cloud 프로젝트 생성 → "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 에서 사이트 '소유자'로 그 서비스 계정 이메일 추가
  4) pip install google-auth requests

사용법:
  GOOGLE_APPLICATION_CREDENTIALS=service-account.json \
  python3 scripts/google_indexing.py            # sitemap.xml 전체 URL_UPDATED
  python3 scripts/google_indexing.py URL ...     # 지정 URL만
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

API = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def urls_from_sitemap() -> list:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main(urls: list, kind: str = "URL_UPDATED") -> None:
    try:
        import requests
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("필요 패키지가 없습니다.  pip install google-auth requests")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("환경변수 GOOGLE_APPLICATION_CREDENTIALS 에 서비스 계정 JSON 경로를 지정하세요.")

    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    session = AuthorizedSession(creds)

    for u in urls:
        r = session.post(API, json={"url": u, "type": kind})
        print(f"{r.status_code}  {u}")
        if r.status_code != 200:
            print("   " + r.text[:200])


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    main(args or urls_from_sitemap())
