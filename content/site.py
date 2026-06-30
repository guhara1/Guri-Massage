# 사이트 공통 설정
# 배포 도메인: Netlify
BASE_URL = "https://guri-massage.netlify.app"

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

# 내부 링크 강화 — 페이지별 "함께 보면 좋은 안내" 롱테일 교차 링크.
# 각 항목: (href, 앵커 텍스트(롱테일), 보조 설명). 빌드가 페이지 하단에 카드로 출력한다.
# key 는 페이지 path("" = 메인) 기준. 도어웨이가 아니라 실제 연관 페이지만 연결한다.
RELATED = {
    "": [
        ("/guri/guri-station-chuljangmassage/", "구리역 출장마사지", "경의중앙·8호선 환승권 인근 방문 안내"),
        ("/guri/sutaek-dong-chuljangmassage/", "수택동 홈타이", "장자호수공원·돌다리 대표 주거권"),
        ("/hometai/", "구리 홈타이 이용 가이드", "출장마사지와 홈타이 차이부터 진행 방식까지"),
        ("/reservation/", "구리 출장마사지 예약 안내", "방문 절차·이동비·결제·취소 기준"),
    ],
    "guri/galmae-dong-chuljangmassage/": [
        ("/guri/galmae-station-chuljangmassage/", "갈매역 출장마사지", "경춘선 갈매역 주거권 방문 안내"),
        ("/guri/donggu-dong-chuljangmassage/", "동구동 방문 관리", "왕숙천 건너 인접 생활권"),
        ("/hometai/", "갈매동 홈타이 가이드", "신도시 자택에서 받는 타이마사지"),
        ("/reservation/", "예약 안내", "갈매지구 단지 방문 차량 등록 기준"),
    ],
    "guri/donggu-dong-chuljangmassage/": [
        ("/guri/donggureung-station-chuljangmassage/", "동구릉역 출장마사지", "8호선 별내선 신설역 인근 안내"),
        ("/guri/inchang-dong-chuljangmassage/", "인창동 방문 관리", "남쪽으로 이어지는 도심 생활권"),
        ("/guri/galmae-dong-chuljangmassage/", "갈매동 홈타이", "왕숙천 동쪽 갈매지구 방면"),
        ("/reservation/", "예약 안내", "외곽 단독주택 방문 위치 안내 팁"),
    ],
    "guri/inchang-dong-chuljangmassage/": [
        ("/guri/guri-station-chuljangmassage/", "구리역 출장마사지", "인창동 도심 환승권 방문 안내"),
        ("/guri/donggureung-station-chuljangmassage/", "동구릉역 방문 관리", "인창동 북부로 이어지는 신설역"),
        ("/guri/sutaek-dong-chuljangmassage/", "수택동 홈타이", "남쪽 상권으로 연결되는 주거권"),
        ("/hometai/", "홈타이 가이드", "오피스텔·숙소에서 받는 방문 관리"),
    ],
    "guri/gyomun-dong-chuljangmassage/": [
        ("/guri/guri-station-chuljangmassage/", "구리역 출장마사지", "교문동 도심 이동 거점"),
        ("/guri/sutaek-dong-chuljangmassage/", "수택동 방문 관리", "동쪽으로 이어지는 대표 주거권"),
        ("/guri/jangja-lake-park-station-chuljangmassage/", "장자호수공원역 홈타이", "별내선 인근 생활권"),
        ("/guide/", "이용 전 확인사항", "아차산 인근 단지 방문 준비"),
    ],
    "guri/sutaek-dong-chuljangmassage/": [
        ("/guri/jangja-lake-park-station-chuljangmassage/", "장자호수공원역 출장마사지", "수택동·토평 별내선 거점"),
        ("/guri/guri-station-chuljangmassage/", "구리역 방문 관리", "서쪽 환승권 생활권"),
        ("/guri/gyomun-dong-chuljangmassage/", "교문동 홈타이", "북서쪽으로 이어지는 행정 생활권"),
        ("/hometai/", "홈타이 가이드", "한강·호수공원 운동 후 회복 관리"),
    ],
    "guri/guri-station-chuljangmassage/": [
        ("/guri/inchang-dong-chuljangmassage/", "인창동 출장마사지", "구리역 북·서쪽 도심 주거권"),
        ("/guri/sutaek-dong-chuljangmassage/", "수택동 홈타이", "구리역 남쪽 대규모 주거권"),
        ("/guri/gyomun-dong-chuljangmassage/", "교문동 방문 관리", "구리시청·교문사거리 생활권"),
        ("/reservation/", "예약 안내", "번화가 건물·주차 위치 전달 팁"),
    ],
    "guri/galmae-station-chuljangmassage/": [
        ("/guri/galmae-dong-chuljangmassage/", "갈매동 출장마사지", "갈매지구 신도시 단지 방문 안내"),
        ("/guri/donggu-dong-chuljangmassage/", "동구동 방문 관리", "왕숙천 건너 인접 생활권"),
        ("/hometai/", "홈타이 가이드", "자택 단지에서 받는 타이마사지"),
        ("/reservation/", "예약 안내", "단지 출입·차량 등록 기준"),
    ],
    "guri/donggureung-station-chuljangmassage/": [
        ("/guri/inchang-dong-chuljangmassage/", "인창동 출장마사지", "동구릉역 남·서쪽 도심 생활권"),
        ("/guri/donggu-dong-chuljangmassage/", "동구동 방문 관리", "동구릉 녹지 인근 주거권"),
        ("/guri/galmae-station-chuljangmassage/", "갈매역 홈타이", "경춘선 인접 역세권"),
        ("/reservation/", "예약 안내", "신설역 인근 위치 전달 팁"),
    ],
    "guri/jangja-lake-park-station-chuljangmassage/": [
        ("/guri/sutaek-dong-chuljangmassage/", "수택동 출장마사지", "장자호수공원역 대표 주거권"),
        ("/guri/gyomun-dong-chuljangmassage/", "교문동 방문 관리", "큰길 건너 서쪽 생활권"),
        ("/guri/guri-station-chuljangmassage/", "구리역 홈타이", "환승권으로 이어지는 도심"),
        ("/hometai/", "홈타이 가이드", "공원·강변 운동 후 회복 관리"),
    ],
    "reservation/": [
        ("/guide/", "이용 전 확인사항", "준비물·위생·안전 기준"),
        ("/hometai/", "홈타이 이용 가이드", "진행 방식과 추천 대상"),
        ("/support/", "고객센터", "변경·취소·문의 안내"),
        ("/", "구리 출장마사지 지역 안내", "행정동·역세권 전체 보기"),
    ],
    "guide/": [
        ("/reservation/", "예약 안내", "방문 절차·이동비·결제 기준"),
        ("/hometai/", "홈타이 이용 가이드", "진행 방식과 건강 확인"),
        ("/support/", "고객센터", "공지·자주 묻는 질문·문의"),
        ("/", "구리 출장마사지 지역 안내", "행정동·역세권 전체 보기"),
    ],
    "hometai/": [
        ("/reservation/", "예약 안내", "방문 절차·이동비·결제 기준"),
        ("/guide/", "이용 전 확인사항", "준비물·위생·안전 기준"),
        ("/guri/sutaek-dong-chuljangmassage/", "수택동 홈타이", "대표 주거권 방문 안내"),
        ("/", "구리 출장마사지 지역 안내", "행정동·역세권 전체 보기"),
    ],
    "support/": [
        ("/reservation/", "예약 안내", "방문 절차·이동비·결제 기준"),
        ("/guide/", "이용 전 확인사항", "준비물·위생·안전 기준"),
        ("/hometai/", "홈타이 이용 가이드", "진행 방식과 추천 대상"),
        ("/privacy/", "개인정보처리방침", "수집 항목·이용 목적·파기 기준"),
    ],
}
