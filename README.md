# 간다GO — 구리 출장마사지·홈타이 안내 사이트

경기도 구리시 전지역 방문 관리(출장마사지·홈타이) 안내용 지역 SEO 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

구리시는 행정구가 없으므로 **구리시 → 대표 행정동 → 지하철역** 순서로 구성합니다.

- 정적 HTML 사이트 — GitHub Pages / Netlify / 일반 웹서버 어디서나 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·목차·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(간다GO)·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ WebPage/BreadcrumbList/Organization/FAQPage JSON-LD)
  areas.py          # 대표 행정동 5개 (갈매·동구·인창·교문·수택)
  stations.py       # 지하철역 4개 (구리·갈매·동구릉·장자호수공원)
  info.py           # 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·개인정보 처리방침
assets/             # CSS, 모바일 내비 JS, 파비콘, OG 이미지
```

## 페이지 구성 (총 15개)

| 구분 | 페이지 | URL |
|------|--------|-----|
| 메인 | 구리 출장마사지·홈타이 | `/` |
| 행정동 | 갈매동 | `/guri/galmae-dong-chuljangmassage/` |
| 행정동 | 동구동 | `/guri/donggu-dong-chuljangmassage/` |
| 행정동 | 인창동 | `/guri/inchang-dong-chuljangmassage/` |
| 행정동 | 교문동 (교문1·2동 통합) | `/guri/gyomun-dong-chuljangmassage/` |
| 행정동 | 수택동 (수택1·2·3동 통합) | `/guri/sutaek-dong-chuljangmassage/` |
| 역 | 구리역 (경의중앙·8호선 환승) | `/guri/guri-station-chuljangmassage/` |
| 역 | 갈매역 (경춘선) | `/guri/galmae-station-chuljangmassage/` |
| 역 | 동구릉역 (8호선) | `/guri/donggureung-station-chuljangmassage/` |
| 역 | 장자호수공원역 (8호선) | `/guri/jangja-lake-park-station-chuljangmassage/` |
| 안내 | 예약 안내 | `/reservation/` |
| 안내 | 이용 전 확인사항 | `/guide/` |
| 안내 | 홈타이 이용 가이드 | `/hometai/` |
| 정책 | 개인정보 처리방침 (noindex) | `/privacy/` |
| 안내 | 고객센터 | `/support/` |

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수와 색인 여부가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 모든 페이지 **메타 디스크립션 80자 이내**
- 행정동은 대표 동 단위만 — 번호 행정동(교문1동·수택1동 등) 개별 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역(구리역)도 URL 하나, 노선별·출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지)
- 실제 오프라인 매장 주소가 없으므로 **LocalBusiness 대신 Organization Schema** 사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경 → 현재 `https://guri-massage.pages.dev`
2. `python3 build.py` 재실행 (canonical·sitemap·rss·robots·IndexNow 키 파일에 반영됨)
3. 아래 "빠른 색인" 절차 진행

## 빠른 색인 (네이버·구글·빙)

빌드 시 자동 생성되는 색인 자산:

| 파일 | 용도 |
|------|------|
| `/sitemap.xml` | 색인 페이지 목록(lastmod·priority 포함) — 구글/네이버 제출용 |
| `/rss.xml` | 업데이트 피드 — 네이버·빙 등 피드 수집 가속 |
| `/robots.txt` | 주요 봇 허용 + 사이트맵 위치 안내(네이버 Yeti 포함) |
| `/{INDEXNOW_KEY}.txt` | IndexNow 키 검증 파일(루트에 위치해야 함) |

### 1) 검색엔진 등록 (최초 1회)
- **구글 Search Console**: 속성 등록(소유 확인) → 색인 > Sitemaps 에 `sitemap.xml` 제출
- **네이버 서치어드바이저**: 사이트 등록 → 요청 > 사이트맵 제출에 `sitemap.xml`, RSS 제출에 `rss.xml`
- **빙 Webmaster Tools**: 사이트 추가 → 사이트맵 `sitemap.xml` 제출

### 2) IndexNow — 빙·네이버·얀덱스 즉시 색인 통보 (글 추가/수정 때마다)
```bash
python3 scripts/indexnow.py                  # 사이트맵 전체 통보
python3 scripts/indexnow.py https://guri-massage.pages.dev/guri/...  # 특정 URL만
```
- 키 파일 `/{INDEXNOW_KEY}.txt` 가 배포되어 접근 가능해야 동작합니다(빌드가 생성).
- Cloudflare Pages 사용 시 대시보드 **Caching → Crawler Hints(IndexNow)** 를 켜면 변경분이 자동 통보되기도 합니다.

### 3) (선택) 구글 Indexing API — 개별 URL 즉시 요청
구글은 IndexNow 미참여. 공식적으로 Indexing API 는 JobPosting/BroadcastEvent 전용이라,
일반 페이지는 **Search Console 색인 요청**이 정석입니다. 그래도 쓰려면:
```bash
pip install google-auth requests
GOOGLE_APPLICATION_CREDENTIALS=service-account.json python3 scripts/google_indexing.py
```
서비스 계정 생성 → Indexing API 사용 설정 → Search Console 소유자로 추가가 선행되어야 합니다.

> 참고: 구글·빙의 익명 `sitemap ping` 엔드포인트는 2023~2024년에 폐기되어 더 이상 동작하지 않습니다.
> 따라서 빠른 색인은 **Search Console/서치어드바이저 제출 + IndexNow** 조합이 현재 표준입니다.
