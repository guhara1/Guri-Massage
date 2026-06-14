# 메인 페이지 — 구리시 전체 허브. 모든 키워드를 밀어 넣지 않고 하위 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY

# 검색엔진 사이트 소유확인 메타 (메인 페이지에만 출력).
_VERIFY = '<meta name="naver-site-verification" content="79edd398d8065164a504c96710b7785b394c75c2">\n'

# 실제 오프라인 매장 주소가 없으므로 LocalBusiness 대신 Organization 을 사용한다.
_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "구리 출장마사지·홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "description": "구리 출장마사지·홈타이 예약 전 행정동, 역세권, 이용 기준을 정리한 안내 페이지",
  "inLanguage": "ko-KR",
  "isPartOf": {{ "@type": "WebSite", "name": "{BRAND}", "url": "{BASE_URL}/" }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "구리 출장마사지·홈타이", "item": "{BASE_URL}/" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "telephone": "{PHONE}",
  "description": "경기도 구리시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{ "@type": "AdministrativeArea", "name": "경기도 구리시" }},
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "{PHONE}",
    "contactType": "reservations",
    "areaServed": "KR",
    "availableLanguage": "Korean"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "구리시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 갈매동, 동구동, 인창동, 교문동, 수택동 대표 행정동 기준으로 안내하며 토평·인접 지역도 위치에 따라 가능할 수 있습니다." }}
    }},
    {{
      "@type": "Question",
      "name": "구리역이나 장자호수공원역 인근도 가능한가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "구리역, 갈매역, 동구릉역, 장자호수공원역 역세권은 각 역 안내 페이지에서 주변 생활권과 함께 확인할 수 있습니다. 정확한 가능 여부는 예약 시 주소 기준으로 확인합니다." }}
    }},
    {{
      "@type": "Question",
      "name": "교문1·2동, 수택1·2·3동은 왜 따로 없나요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "번호로 나뉜 행정동은 교문동, 수택동 대표 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다." }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 몰릴 수 있어 사전 예약을 권장합니다." }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 무엇이 다른가요?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "출장마사지는 관리사가 자택·숙소·사무실로 방문하는 형태 전체를 가리키고, 홈타이는 그중 집에서 받는 타이마사지를 부르는 말입니다. 자세한 내용은 홈타이 이용 가이드에서 확인하세요." }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 경기도 구리시 전지역</p>
    <h1>구리 출장마사지 · 구리시 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/reservation/">예약 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>5개</strong><span>대표 행정동</span></li>
      <li><strong>4개</strong><span>역세권 안내</span></li>
      <li><strong>구리시</strong><span>전지역 방문</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<p class="lead">구리 출장마사지와 홈타이 예약을 찾는 분들을 위해 방문 가능 지역, 예약 절차, 이용 전 확인사항을 한곳에 정리했습니다. 이 페이지는 구리시 전체 구조를 설명하는 허브 역할을 하며, 자세한 내용은 대표 행정동별·지하철역별 안내에서 확인하실 수 있습니다.</p>

<section id="why">
<h2>구리시에서 출장마사지를 찾는 이유</h2>
<p>구리시는 서울 동북권과 남양주 생활권 사이에 자리한 도시라 이동 수요가 꾸준한 곳입니다. 구리역과 인창동 일대는 교통과 상권이 모이는 중심지이고, 수택동과 교문동은 대규모 주거지와 생활 상권이 함께 있는 지역입니다. 갈매동은 갈매지구 신도시 주거권과 갈매역 생활권이 연결되고, 동구동은 동구릉역과 인창동 북부 생활권을 함께 끼고 있습니다. 이렇게 동마다 성격이 달라서, 출장마사지를 찾는 분들도 본인 위치에서 가까운 방문 가능 지역을 먼저 확인하는 경우가 많습니다. 간다GO는 구리시 전지역을 대상으로 자택, 오피스텔, 숙소 어디든 관리사가 직접 방문하며, 샵을 오가는 이동 없이 계신 곳에서 바로 관리받고 그대로 쉴 수 있다는 점이 가장 큰 장점입니다.</p>
</section>

<section id="hometai">
<h2>구리 홈타이 이용 전 확인할 사항</h2>
<p>구리 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 홈타이는 집에서 받는 타이마사지를 가리키는 말로, 오일을 쓰지 않고 편한 옷차림으로 받는 지압·스트레칭 구성이라 샤워 부담이 적어 처음 이용하는 분도 시작하기 좋습니다. 출장마사지와 홈타이는 형태가 조금 다를 뿐 예약 절차와 이용 기준은 같으므로, 어느 쪽을 원하시든 위치와 희망 시간만 알려주시면 됩니다. 진행 방식과 추천 대상, 받기 전 건강 확인 사항은 <a href="/hometai/">홈타이 이용 가이드</a>에서 자세히 정리했습니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>구리시는 행정구가 없어 구리시 → 대표 행정동 → 지하철역 순서로 안내합니다. 지역 안내는 갈매동, 동구동, 인창동, 교문동, 수택동 다섯 개 대표 행정동을 기준으로 구성했습니다. 교문1동과 교문2동은 교문동으로, 수택1·2·3동은 수택동으로 통합해, 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하지 않도록 정리했습니다. 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/guri/galmae-dong-chuljangmassage/">갈매동</a></li>
<li><a href="/guri/donggu-dong-chuljangmassage/">동구동</a></li>
<li><a href="/guri/inchang-dong-chuljangmassage/">인창동</a></li>
<li><a href="/guri/gyomun-dong-chuljangmassage/">교문동</a></li>
<li><a href="/guri/sutaek-dong-chuljangmassage/">수택동</a></li>
</ul>
</section>

<section id="stations">
<h2>구리역·갈매역·동구릉역·장자호수공원역 안내</h2>
<p>역을 기준으로 위치를 설명하는 것이 편하시다면 역세권 안내를 참고하세요. 구리역은 경의중앙선과 8호선이 만나는 환승역이고, 갈매역은 경춘선, 동구릉역과 장자호수공원역은 2024년 개통한 8호선 별내선 구간입니다. 환승역이라도 노선별로 페이지를 따로 만들지 않고 역마다 한 페이지로 안내합니다.</p>
<ul class="card-grid">
<li><a href="/guri/guri-station-chuljangmassage/">구리역</a></li>
<li><a href="/guri/galmae-station-chuljangmassage/">갈매역</a></li>
<li><a href="/guri/donggureung-station-chuljangmassage/">동구릉역</a></li>
<li><a href="/guri/jangja-lake-park-station-chuljangmassage/">장자호수공원역</a></li>
</ul>
</section>

<section id="check">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비 여부, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인하시는 것이 좋습니다. 구리시는 면적이 크지는 않지만 갈매동·동구동의 외곽 택지와 인창동·수택동의 도심 생활권은 이동 동선이 다릅니다. 갈매동과 동구동은 차량 이동 기준이 중요하고, 구리역과 장자호수공원역 주변은 역세권 접근성이 중요합니다. 결제와 추가 비용, 변경·취소 기준 등 자세한 내용은 <a href="/reservation/">예약 안내</a>에서, 준비물과 위생·안전 기준은 <a href="/guide/">이용 전 확인사항</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="guide">
<h2>구리 출장마사지 사이트 이용 가이드</h2>
<p>이 사이트는 메인 페이지가 구리시 전체 안내를 맡고, 대표 행정동 페이지가 생활권별 안내를, 역세권 페이지가 역 주변 안내를 각각 담당하도록 구성했습니다. 본인에게 익숙한 기준이 동이라면 행정동 페이지를, 역이라면 역 페이지를 보시면 되며 예약 절차와 이용 기준은 어느 쪽이든 동일합니다. 모든 안내는 과장 없이 방문 가능 지역, 예약 절차, 취소 기준, 개인정보 처리 기준을 분명히 보여 드리는 것을 원칙으로 하며, 불법적이거나 무리한 요청은 어떤 경우에도 진행하지 않습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>구리시 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 갈매동, 동구동, 인창동, 교문동, 수택동 대표 행정동 기준으로 안내하며 토평·인접 지역도 위치에 따라 가능할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>구리역이나 장자호수공원역 인근도 가능한가요?</h3>
<p>구리역, 갈매역, 동구릉역, 장자호수공원역 역세권은 각 역 안내 페이지에서 주변 생활권과 함께 확인할 수 있습니다. 정확한 가능 여부는 예약 시 주소 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>교문1·2동, 수택1·2·3동은 왜 따로 없나요?</h3>
<p>번호로 나뉜 행정동은 교문동, 수택동 대표 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다. 예약은 주소 기준으로 진행되므로 행정동 번호를 모르셔도 됩니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 몰릴 수 있어 사전 예약을 권장합니다. 일정이 보이는 대로 미리 연락 주시면 대기 없이 받으실 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>홈타이와 출장마사지는 무엇이 다른가요?</h3>
<p>출장마사지는 관리사가 방문하는 형태 전체를, 홈타이는 그중 집에서 받는 타이마사지를 부르는 말입니다. 자세한 내용은 <a href="/hometai/">홈타이 이용 가이드</a>에서 확인하세요.</p>
</div>
</section>

<section id="contact" class="cta">
<h2>예약문의</h2>
<p>구리시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "구리 출장마사지｜구리시 홈타이 지역별 예약 안내",
    "desc": "구리 출장마사지·홈타이 예약 전 행정동, 역세권, 이용 기준을 정리했습니다.",
    "h1": "구리 출장마사지 · 구리시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _VERIFY + _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
