# 전체 페이지 목록 집계
# 구조: 메인 1 + 대표 행정동 5 + 지하철역 4 + 안내 페이지 5 = 15
from . import main, areas, stations, info

PAGES = [main.PAGE] + areas.PAGES + stations.PAGES + info.PAGES
