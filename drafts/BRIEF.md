# 에이치원(H-ONE) 홈페이지 시안 공통 브리프

## 배경
- ㈜JKE(jketech.co.kr, 부산 강서구 미음산단. 선박/해양플랜트용 배전반·MCC·정션박스 제조)의 사업을 승계하는 **에이치원(H-ONE)** 의 기업 홈페이지 시안.
- 클라이언트는 **기존 JKE 사이트 디자인을 마음에 들어함** → 톤(딥 네이비/보라 + 해양플랜트 야경 사진 + 화이트 타이포)을 존중하면서 현대적 모션 사이트로 재해석.
- **에셋과 콘텐츠는 JKE 것을 그대로 사용** (추후 협의로 교체). 브랜드명만 "에이치원 / H-ONE" 으로 표기(타이포 로고). 본문 카피 안의 "(주) JKE" 는 그대로 두어도 됨.
- 데스크톱 우선(1440 기준), 1024/모바일에서 깨지지 않을 정도의 반응형.
- **모션 필수**: GSAP(ScrollTrigger) 또는 anime.js. CDN 사용: `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js`, `.../gsap/3.12.5/ScrollTrigger.min.js`, `https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.2/anime.min.js`
- 폰트: 로컬 `../../assets/fonts/NotoSansCJKkr-Medium.otf`, `-Light.otf` 를 @font-face 로. 영문 디스플레이 폰트는 Google Fonts 허용.

## 산출물 규칙
- 각 시안 = **단일 HTML 파일** (CSS/JS 인라인). 위치: `drafts/<skill>/v1.html`, `v2.html` ...
- 에셋은 상대경로 `../../assets/...` 로 참조 (drafts/<skill>/ 기준). 파일을 복사하지 말 것.
- 메인 페이지 1장을 롱스크롤로 완성. 섹션: 헤더/GNB(메가메뉴) → 히어로(슬라이드 4장) → 사업분야 3 → 제품 라인업 → 연혁 → 인증/R&D → 파트너 로고 → 고객지원/연락처 → 푸터.
- 서브페이지는 만들지 않음(링크는 `#`).

## 사이트맵 (GNB)
기업소개(인사말·비전&방침·회사연혁·조직도·Tour·FAMILY·찾아오시는길) / 사업분야(OFFSHORE·SHIPBUILDING·BUILDING) / 제품소개(단체표준인증품(MAS)·SWITCHBOARD·MOTOR CONTROL CENTER·VFD·DISTRIBUTION BOARD·JUNCTION BOX·CONSOLE·BOOTH·NAVIGATION CONTROL·OTHERS) / R&D(보유기술&인증서·시험 및 검사장비) / PARTNER(PARTNER·고객사·DISTRIBUTION) / 고객지원(서비스 범위·Life-cycle 서비스·연락처·FAQ) / ENG·KOR

## 히어로 카피 (슬라이드 4)
| # | 배경 | 소제목 | 헤드라인 |
|---|---|---|---|
| 1 | `assets/kr/main-visual/bg01.jpg` | Electrical Safety | 고객의 안전에 진심을 담는 기업 |
| 2 | `bg02.jpg` | Off-Shore Electrical System | 경쟁력을 기본으로 세계를 앞서나가는 |
| 3 | `bg03.jpg` | Shipbuilding Electrical System | 고객의 상상을 현실로 만들어 드리는 기업 |
| 4 | `bg04_re.jpg` | Industry Electrical System | The best solution for your success |
(원본은 이미지 텍스트지만 시안에서는 **실제 텍스트**로 타이핑. 배경 1960x966)
원본 히어로 동작: 위로 슬라이드 아웃 + 페이드인, Ken Burns 10초 scale 1→1.1, 7초 자동재생, 우측 세로 도트 내비, 하단 퀵박스 4개(JKE TOUR / PRODUCT / CONTACT / FAMILY, 호버 시 이미지 `assets/common-ui/jke.gif, product.gif, contac.gif, family.gif` 330x125).

## 인사말 (CEO)
"JKE와 함께하면 생각이 현실이 됩니다." — 전기인의 자부심으로 끊임없이 연구 개발하여 국내 제일의 기업을 이루었고, 현재는 세계 일류 기업으로 성장하고 있습니다. 세 가지 진심: ①감사하는 마음 ②고객감동 ③고객 안전에 진심. 이미지 `assets/kr/content/sub_ceo.jpg`(800x430).

## 비전
"변화와 다양성"으로 전 세계 고객이 인정하는 "글로벌 일류 기업". 4가치: 신뢰와 존중 / 창의와 혁신 / 정도경영 / 전문성과 다양성. 4경영: 기업경영·품질경영·안전보건경영·환경경영. 아이콘 타일 `assets/kr/content/test01~04.png`(220x220).

## 사업분야
- **Off-Shore**: 검증된 설계능력과 기술력 / 비교할 수 없는 실적과 신뢰성 / Global 기업과의 Partnership / I.S.E.S Global Network. EPCI 선도, Off-Shore LV Electrical System 전담. 이미지 `assets/kr/content/sub02_01_top.gif`(800x310), `sub02_01_bottom.gif`(800x230)
- **Shipbuilding**: 최대 실적의 다양성 / 다각화된 설계능력·기술력·경쟁력 / 최적 Solution과 A/S. 이미지 `sub02_02_top.gif`, `sub02_02_bottom.gif`
- **Building**: 이미지 `sub02_03.gif`
- 히어로 배경 4장(bg01~04)도 사업분야 카드 배경으로 재활용 가능.

## 제품 라인업 (10) — 이미지 폴더 `assets/board-uploads/<table>/` (jpg/JPG, 155x210 썸네일 파일도 섞여 있음. 큰 파일 사용)
| 제품 | 폴더 |
|---|---|
| 단체표준인증품(MAS) | sub03_10 |
| SWITCHBOARD | sub03_01 (800x527 정면사진 있음) |
| MOTOR CONTROL CENTER | sub03_02 |
| VFD | sub03_03 |
| DISTRIBUTION BOARD | sub03_04 |
| JUNCTION BOX | sub03_05 |
| CONSOLE | sub03_06 |
| BOOTH (Safe/Telephone) | sub03_07 |
| NAVIGATION CONTROL | sub03_08 |
| OTHERS | sub03_09 |
※ 파일명은 해시라 `ls` 로 확인해서 하나씩 골라 쓸 것 (PIL로 사이즈 확인 가능).

## 연혁 (`content/bbs_board__bo_table-sub01_03.md` 전체 참조) 발췌
- 2020.02 단체표준제품인증 (고압/저압배전반·전동기제어반·분전반·태양광) / 04 정부조달 MAS 등록 / 06 ISO 9001·14001·45001
- 2019.07 Siemens LV Switchgear License Partner 계약 / 11 현대일렉트릭 품질평가 우수협력사 (배전반 1위)
- 2018.03 IECEx/ATEX Ex e, ia, tb IP66/67 인증 / 08 ISO 9001·14001:2015 전환
- 2017.04 Phoenix Mecano(ROSE) 한국 방폭 공장 등록 / 12 IECEx/ATEX 인증(Key Type)
- 2016.01 INNO-BIZ 인정 … 2002 창립

## R&D / 인증
카테고리 6: 경영시스템·기업인증서·라이센스·제품인증서·단체표준 인증서·표창. 인증서 스캔 `assets/board-uploads/ceri1/` (155x210 썸네일 + 원본). 시험장비 `assets/kr/content/sub04_02.gif`.

## 파트너 로고 19종
`assets/partner-logos/*.gif` (높이 40~45px). 타이틀 "THE BEST BUSINESS PARTNER".

## 고객지원
서비스 범위 `assets/kr/content/sub06_01.jpg`, Life-cycle `life_img.gif`, 연락처 `call_img.gif`.
FAMILY: ㈜JKE 2공장 `family_factory.jpg`, ㈜JK RST `family_rst.jpg`. Tour 대표 `assets/kr/tour-gallery/img_00__.jpg`(800x600) + tour_01~27.jpg(600x800).

## 연락처/푸터
부산광역시 강서구 미음산단로 105번길 34 (구랑동) / T. 051.974.9500 / F. 051.974.9595
EN: 34, Mieumsandan-ro 105beon-gil, Gangseo-gu, Busan, 46748 Korea
© 2026 H-ONE All rights reserved.

## 기존 디자인 토큰 (존중할 것)
- 브랜드 보라 `#29166e`, 진한 보라 `#1e0b67`, 보조 블루 `#0b5190`, 연혁 `#00417d` / `#079CCD`
- 다크 `#1e1f29`, 푸터 `#2b2b2b`, 회색 `#f9f9f9`/`#f7f7f7`, 선 `#ddd`
- 헤더 80px 투명 absolute, 하단 1px rgba(255,255,255,.3) 선, 메가드롭다운(전체 2뎁스가 한 번에 펼침, 검정 40% 배경, 헤더 흰색으로 전환)
- 로고: `assets/common-ui/logo_bg.png`(흰), `logo_bg02.png`(컬러) 167x29 — JKE 로고이므로 **참고만**, 에이치원은 타이포 로고로.
- 참고 스크린샷: `screenshots/index.png`, `index__gnb-hover.png`, `index__footbox-hover.png`, `index__slide2~4.png`

---

# ★ 2차 브리프 (2026-09-07 오후) — JKE 디자인 승계 조건 삭제

1차 12안이 전부 "투명 헤더 + 해양플랜트 야경 사진 풀블리드 히어로 + 네이비/보라" 로 수렴했다는 클라이언트 피드백.
**콘텐츠(카피·사이트맵·에셋)는 그대로 쓰되, 디자인은 JKE 를 전혀 참고하지 않고 시안마다 완전히 다른 디자인 시스템으로 만든다.**

## 공통 금지사항 (모든 시안)
- `bg01~04.jpg` 해양플랜트 사진을 **풀블리드 히어로 배경으로 쓰지 말 것** (본문 섹션 안에서 프레임/카드/작은 이미지로만 사용 가능)
- 투명 80px 헤더가 사진 위에 얹히는 구조 금지
- 보라 `#29166e` 계열, 네이비 `#1e1f29` 계열을 주색으로 쓰지 말 것
- 흰 텍스트 + 어두운 사진 히어로 조합 금지
- 다른 시안과 같은 헤드라인 폰트/팔레트/히어로 레이아웃 금지 — 각 시안은 아래 배정된 디자인 시스템을 엄격히 따른다

## 시안별 디자인 시스템 배정 (12개, 전부 다르게)
| # | 스킬 | 파일 | 디자인 시스템 | 팔레트 | 타이포 | 히어로 구조 |
|---|---|---|---|---|---|---|
| 1 | frontend-design | v1 | **Swiss Industrial** — 국제 타이포그래피 양식, 12칼럼 그리드 라인 노출, 좌측정렬, 룰 라인 | 순백 `#ffffff` + 검정 + 시그널 레드 `#e10600` 1색 | Helvetica 계열(Inter/Archivo) 그로테스크, 대문자 소형 라벨 | **타이포 히어로**: 사진 없음. 거대한 회사명/슬로건 텍스트 + 제품 카테고리 10개 목록이 히어로 |
| 2 | frontend-design | v2 | **Warm Editorial Paper** — 잡지 레이아웃, 드롭캡, 캡션, 세리프 | 크림 `#f3efe6` + 딥그린 `#123524` + 테라코타 `#c2603d` | 세리프 디스플레이(Playfair/Fraunces) + 산세리프 본문 | **매거진 커버형**: 좌 텍스트 컬럼 + 우측 작은 액자 사진(제품 사진), 발행호 표기 |
| 3 | frontend-design | v3 | **Neo-Brutalist** — 두꺼운 검정 테두리, 하드 섀도우, 마키, 스티커 | 일렉트릭 옐로 `#ffe500` + 검정 + 흰 | 모노스페이스(Space Mono/JetBrains) + 초굵은 산세리프 | **블록 히어로**: 노란 배경, 거대 굵은 텍스트, 검정 테두리 카드들, 하단 무한 마키 |
| 4 | apple-design | v1 | **Apple Store Light** — 제품이 주인공, 흰 배경 위 제품 사진 센터 | 흰 `#ffffff` / `#f5f5f7` + 그레이 텍스트 + 블루 링크 `#0066cc` | SF 계열(Inter Tight) 굵은 타이트 트래킹 | **제품 스테이지**: 배전반 제품 사진(sub03_01 정면) 흰 배경 중앙 + 위에 짧은 헤드라인, 스크롤 시 제품이 스케일/전환 |
| 5 | apple-design | v2 | **Soft Gradient Glass** — 메시 그라디언트, 글라스 카드, 24px 라운드 | 파스텔 블루 `#dbe9ff` → 라벤더 `#efe3ff` → 민트 `#dff7ee` 그라디언트, 텍스트 차콜 | 라운드 산세리프(Manrope/Plus Jakarta) | **그라디언트 히어로**: 사진 없이 부드러운 메시 그라디언트 배경 + 중앙 글라스 카드 안에 헤드라인/CTA |
| 6 | apple-design | v3 | **Technical Blueprint Light** — 도면 격자, 치수선, 코너마크, 라이트 | 아이스 블루 `#eef4fb` + 잉크 `#0f2a44` + 시안 `#00a3e0` | 컨덴스드 산세리프(Barlow Condensed) + 모노 라벨 | **도면 히어로**: 격자 배경 위 제품 사진을 치수선으로 감싼 '도면 시트' 구성, 우측 스펙 표 |
| 7 | design-taste-frontend | v1 | **Nordic Minimal** — 극단적 여백, 얇은 선, 소문자 | 오프화이트 `#faf9f7` + 스톤 `#8c8a84` + 세이지 `#6b7f6a` | 얇은 산세리프(Figtree Light) 큰 사이즈, 로우어케이스 | **여백 히어로**: 화면 70% 여백, 작은 텍스트 블록 하나, 우하단 작은 사진 |
| 8 | design-taste-frontend | v2 | **Terminal / Data** — 대시보드 감성, 모노 텍스트, 상태 표시등 | 차콜 `#111412` + 포스포 그린 `#3dff8f` + 그레이 (유일한 다크 시안) | 모노스페이스 전면(IBM Plex Mono) | **터미널 히어로**: 타이핑 애니메이션으로 회사 스펙이 출력되는 콘솔 + 우측 데이터 카드 |
| 9 | design-taste-frontend | v3 | **Bold Color Block** — 원색 블록 섹션, 기하 도형, 큼직한 숫자 | 오렌지 `#ff5a1f` + 코발트 `#1f3bff` + 검정/흰 | 지오메트릭 산세리프(Unbounded/Syne) 초대형 | **컬러블록 히어로**: 화면을 2~3개 원색 블록으로 분할, 각 블록에 사업분야 1개, 사진은 블록 안 작은 원형 |
| 10 | impeccable | v1 | **Corporate Clean SaaS** — 카드, 아이콘, 배지, 그림자, 국내 대기업 사이트 감성 | 흰 + 스카이블루 `#0a6cff` + 라이트그레이 `#f2f5f9` | Pretendard 느낌(Noto Sans KR Medium) + Inter | **분할 히어로**: 좌 텍스트+CTA 2개+신뢰 배지(ISO·MAS), 우측 라운드 카드 안 제품 사진 콜라주 |
| 11 | impeccable | v2 | **Steel & Copper** — 금속 질감, 얇은 구분선, 산업 재료 감성 | 스틸그레이 `#dfe3e8` / `#c9cfd6` + 카퍼 `#b87333` + 다크 슬레이트 텍스트 | 슬랩세리프(Roboto Slab/Zilla) 헤드 + 산세리프 | **재질 히어로**: 스틸그레이 배경 + 카퍼 룰 라인 + 좌 헤드라인, 우측 제품 사진 흑백 듀오톤 |
| 12 | impeccable | v3 | **Monochrome Magazine** — 흑백만, 거대 세리프, 사진 흑백 처리 | 검정 `#000` + 흰 `#fff` + 회색만 (컬러 0) | 초대형 세리프(Cormorant/Instrument Serif) + 소형 산세리프 | **타이포+흑백사진 히어로**: 화면 절반 거대 세리프 헤드라인, 절반 흑백 제품 사진, 굵은 수평선 |

## 공통 유지사항
- 섹션 구성(헤더/메가메뉴 → 히어로 → 사업분야 → 제품 10 → 연혁 → R&D/인증 → 파트너 → 고객지원 → 푸터)과 카피, 에셋 경로, GSAP/anime.js 모션, 단일 HTML, `../../assets/` 경로, `<script src="../_switcher.js"></script>` 를 `</body>` 직전에 포함 — 모두 1차와 동일.
- 파트너 로고 gif 는 흰 배경이 불투명하므로 라이트 시안은 그대로, 다크 시안은 `filter:invert(1)` 또는 `mix-blend-mode` 처리.
