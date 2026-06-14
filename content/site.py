# 사이트 공통 설정
# 배포 도메인: Cloudflare Pages
BASE_URL = "https://guri-massage.pages.dev"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# IndexNow 키 — 빙·네이버·얀덱스 즉시 색인 통보용. 빌드 시 루트에 {KEY}.txt 로 생성된다.
INDEXNOW_KEY = "c6a4568d7e47b218c91c24bac3659d6d"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
# 구조: 구리시 → 대표 행정동 → 지하철역. 행정동/역 허브 페이지는 따로 두지 않고
# 메인 페이지의 해당 섹션 앵커로 묶는다(얇은 페이지 방지).
NAV = [
    ("홈", "/", []),
    ("대표 행정동별 안내", "/#areas", [
        ("갈매동", "/guri/galmae-dong-chuljangmassage/"),
        ("동구동", "/guri/donggu-dong-chuljangmassage/"),
        ("인창동", "/guri/inchang-dong-chuljangmassage/"),
        ("교문동", "/guri/gyomun-dong-chuljangmassage/"),
        ("수택동", "/guri/sutaek-dong-chuljangmassage/"),
    ]),
    ("지하철역별 안내", "/#stations", [
        ("구리역", "/guri/guri-station-chuljangmassage/"),
        ("갈매역", "/guri/galmae-station-chuljangmassage/"),
        ("동구릉역", "/guri/donggureung-station-chuljangmassage/"),
        ("장자호수공원역", "/guri/jangja-lake-park-station-chuljangmassage/"),
    ]),
    ("예약 안내", "/reservation/", []),
    ("이용 전 확인사항", "/guide/", []),
    ("홈타이 이용 가이드", "/hometai/", []),
    ("고객센터", "/support/", []),
]
