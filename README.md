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

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console / 네이버 서치어드바이저에 `sitemap.xml` 제출
