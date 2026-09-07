# jketech.co.kr 짜임 정리 (복제용 스펙)

- 대상: http://jketech.co.kr (㈜JKE, 부산 강서구 미음산단. 선박/해양 플랜트용 배전반·MCC·정션박스 제조)
- 수집일: 2026-09-07
- 플랫폼: 그누보드5(gnuboard) + 자체 PHP 템플릿. 정적 서브페이지(`/subNN/*.php`) + 게시판(`/bbs/board.php?bo_table=...`)
- 언어: KOR(`/`) / ENG(`/eng/`) 완전 이중 구조. 영문 게시판은 `bo_table` 뒤에 `_en` 접미사
- 반응형 아님. `<meta viewport width=1100px, initial-scale=.3>` 고정폭 데스크톱 사이트
- 텍스트 인코딩: 응답은 UTF-8이지만 서브페이지 소스 `<title>`은 EUC-KR 깨짐("�״�����5" = "그누보드5")

---

## 1. 사이트맵 (GNB 1·2뎁스)

| 1뎁스 | 2뎁스 (KR) | 2뎁스 (EN) | 페이지 유형 |
|---|---|---|---|
| 기업소개 / COMPANY | 인사말 | GREETING | 이미지 1장 (`sub_ceo.jpg`) |
| | 비전&방침 (탭 5개: 기업비전 · 기업경영방침 · 품질경영방침 · 안전보건방침 · 환경경영방침) | VISION & POLICY | 탭 + 이미지/아이콘 타일 |
| | 회사연혁 | HISTORY | 게시판 `sub01_03` (history 스킨, 연도별 타임라인) |
| | 조직도 | ORGANIZATION | 이미지 1장 (`sub01_ori.jpg`) |
| | JKE Tour | JKE TOUR | 대표 이미지 + 평면도, 27장 lightbox 갤러리 |
| | FAMILY (탭 2개: ㈜JKE 2공장 · ㈜JK RST) | FAMILY | 탭 + 텍스트 + 사진 |
| | 찾아오시는길 | LOCATION | 텍스트 + Daum 지도 퍼가기(800x300) |
| 사업분야 / BUSINESS AREAS | OFFSHORE · SHIPBUILDING · BUILDING | 동일 | 이미지(top) + LV Electrical System 링크 리스트 + 이미지(bottom). BUILDING은 이미지 1장 |
| 제품소개 / INTRODUCTION | 단체표준인증품(MAS) (탭 4: 고압배전반·저압배전반·전동기제어반·분전반) | STANDARDS OF PRIVATE | 게시판 `sub03_10` product 스킨 |
| | SWITCHBOARD (탭: Normal SWBD · Special SWBD) | SWITCHBOARD | 게시판 `sub03_01` |
| | MOTOR CONTROL CENTER | 동일 | `sub03_02` |
| | VFD | 동일 | `sub03_03` |
| | DISTRIBUTION BOARD | 동일 | `sub03_04` |
| | JUNCTION BOX | 동일 | `sub03_05` |
| | CONSOLE | 동일 | `sub03_06` |
| | BOOTH (탭: Safe Booth · Telephone Booth) | 동일 | `sub03_07` |
| | NAVIGATION CONTROL | 동일 | `sub03_08` |
| | OTHERS | 동일 | `sub03_09` |
| R&D | 보유기술&인증서 (카테고리 6: 경영시스템·기업인증서·라이센스·제품인증서·단체표준 인증서·표창) | TECHNOLOGY & CERTIFICATE (Q.M System · Company · License · Product · Self-Production · Recognition) | 게시판 `ceri1` lightbox_01 갤러리 스킨, 15개/페이지, 총 5페이지(EN 4) |
| | 시험 및 검사장비 | TEST & INSPECTION | 이미지 1장 (`sub04_02.gif`) |
| PARTNER | PARTNER · 고객사 · DISTRIBUTION | PARTNER · CUSTOMER · DISTRIBUTION | 로고 테이블 |
| 고객지원 / CUSTOMER CENTER | 서비스 범위 · Life-cycle 서비스 · 연락처 | SERVICE RANGE · LIFE CYCLE SERVICE · CONTACT | 이미지 1장씩 |
| | FAQ | FAQ | 게시판 `faq` basic 스킨 (글 1건) |
| ENG / KOR | 언어 전환 | | 각각 `/eng/index.php`, `/index.php` |

주석 처리되어 숨겨진 메뉴: 사업분야>ENERGY·기타사업, R&D>제조설비(`ceri3`), 고객지원>카달로그(`cadal`).
페이지별 URL·콘텐츠·스크린샷 매핑은 `PAGES.md` 참조.

---

## 2. 공통 레이아웃

### 2.1 헤더 / GNB (`.navi` + `.gnb`)
- `header` 전체폭, `.navi` 높이 80px, `position:absolute`(콘텐츠 위에 얹힘), 하단 1px `rgba(255,255,255,.3)` 선. 배경 투명 -> 메인 비주얼/서브 비주얼 위에 겹침
- 로고 `h1 a` 167x69, 좌측 padding 50px, `logo_bg.png`(흰 로고) / 호버 흰 배경 시 `logo_bg02.png`(진한 로고)
- `.gnb` 폭 1200px, `left:50%; margin-left:-350px` (화면 중앙에서 오른쪽으로 치우친 배치). 1뎁스 `li` 각 155px, 가운데 정렬
- 1뎁스 글자: 흰색 15px, weight 600, line-height 78px. 호버 시 상단에 2px `#1f0f67` 언더라인이 0% -> 100% 폭으로 늘어남(`.line` / `.depth1-line-show`)
- 2뎁스: 항상 DOM에 있고 `translateY(100px)`로 숨김. `.gnb`에 마우스 진입 시 전체 메뉴가 한꺼번에 펼쳐지는 "메가 드롭다운" 형태. 12px `#eee`, 항목 간 5px, 상단 padding 18px
- 펼침 상태: `.navi-bg.open` 높이 266px(검정 40% 반투명 `#000/0.4`), `.gnb.open` 높이 400px, `.navi.wh`로 헤더 흰 배경 + 1뎁스 글자 `#333`
- ENG/KOR 항목은 폭 35px, ENG는 padding-left 30px, KOR는 margin-left 10px (우측 끝에 붙음)
- 모션: `.motion` = `all .3s ease-out`
- 스크립트: `/js_cjenc/gnb-main.js` (mouseenter/leave로 클래스 토글만 수행)

### 2.2 푸터 (`footer`)
- 높이 30px, 배경 `#2b2b2b`, 내부 `.foot_wrap` 1000px 중앙, padding-top 8px, 11px
- 좌: `address` `#666` — "부산광역시 강서구 미음산단로 105번길 34 (구랑동)  T . 051.974.9500  F . 051.974.9595"
- 우: `.copy` `#555` — "Copyrught ⓒ 2016 JKE All rights reserved." (오타 원문 그대로)
- EN 주소: "34, Mieumsandan-ro 105beon-gil, Gangseo-gu, Busan, 46748 Korea."

### 2.3 TOP 버튼 (서브페이지)
- `#back-top` fixed, bottom 100px, `left:50%; margin-left:575px`, 1px `#000` 테두리, 글자 "TOP", 스크롤 10px 이상에서 fadeIn, 클릭 시 200ms 스크롤 업

---

## 3. 메인 페이지 짜임 (`/index.php`, `/eng/index.php`)

```
[header/GNB 80px, 투명, absolute]
[#mainSpace.topVisual  높이 = window.innerHeight - 30]
   #spaceSlide (jquery.cycle + TweenMax)
     .slide01~04  .bgImg (배경 이미지 cover) + .visualCont(1000px, 좌정렬)
        p.title_visual img v_t0N.png     (헤드카피, 이미지)
        .btnArea .btn_view img v_t0N02.png (서브카피, 이미지)
   #spaceSlideNav  (우측 32px, 세로 중앙: 12px 원형 도트 4개, 흰 테두리, 활성=흰 채움, 간격 9px)
   #spaceSlideCntrol (우측 35px, 48% 높이: 일시정지 play.png / 재생 play02.png 8x10)
   .f_conten_bg (absolute bottom 40px, z 1000): 1332px 중앙, 하단에 f_bg.png repeat-x 선
      .foot_box x4 (각 333x150, float) : JKE TOUR / PRODUCT / CONTACT / FAMILY + f_allow.png 화살표
[footer 30px]
```

- 슬라이드 배경: `bg01.jpg`, `bg02.jpg`, `bg03.jpg`, `bg04_re.jpg` (1960x966), `background-size:cover`, 표시 opacity 0.8, 슬라이드 컨테이너 배경 `#1e1f29`, 슬라이드 배경 `#000`
- 슬라이드 순서와 카피 이미지 매핑(KR): 1=`v_t01`+`v_t0102`, 2=`v_t02`+`v_t0302`, 3=`v_t03`+`v_t0202`, 4=`v_t04`+`v_t0402` (원본이 2·3번 서브카피를 서로 바꿔 씀). EN도 동일 매핑
- 전환: 커스텀 `topSlide` — 현재 슬라이드가 위로 `-height` 만큼 슬라이드 아웃(`Expo.easeInOut`, 0.95s), 다음 슬라이드 fadeIn. 진입 시 `.bgImg` opacity 0->0.8(0.8s), 헤드카피 left 50px->0 + opacity 0->1(1s, delay .4), 서브카피(delay .6)
- Ken Burns: 슬라이드 진입 후 배경 10초 동안 scale 1->1.1, x/y -5% 이동(`Linear`)
- 자동 재생 7초(`timeout:7000`), 페이지 로드 후 `cycle('resume')`. 스크롤이 1px이라도 내려가면 pause, 0이면 resume
- 퀵박스 호버: `.actionImg4:hover .hoverNN` padding 15px->50px, 2px 흰 테두리, 배경 이미지 `jke.gif`/`product.gif`/`contac.gif`/`family.gif`(330x125), 텍스트는 text-indent로 숨김. 링크: JKE TOUR->`/sub01/sub01_05.php`, PRODUCT->SWITCHBOARD 게시글, CONTACT->`/sub06/sub06_04.php`, FAMILY->`/sub01/sub01_07.php`
- 메인의 header 인라인 스타일 `background:#f9f9f9`가 있으나 `.navi`가 absolute라 시각적으로는 투명

---

## 4. 서브 페이지 공통 짜임

```
.sub_wrap
  .header > .navi (메인과 동일 GNB)
  #sub_containner
    .sub_visual (100% x 310px, 배경 sub_bg01.gif 2000x310 cover, 중앙 상단)
       .s_visual_t p : 1뎁스 이름, 흰색 30px, 가운데, padding-top 160px
    .sub_content (1000px 중앙)
       .sub_leftmenu (200px float:left)
          p.left_bg_t : 180px, 배경 #29166e(보라), 흰 18px bold, padding-top 50px + height 50px
          ul.left_menu : 180px, li 좌/우/하 1px #ddd 테두리, padding 10px, a 12px #666
                         on/hover: #1e0b67 + 우측 sub_l_bg.gif(‘-’ 표시) 
       .sub_layout (800px float:left, margin-top 50px)
          .sitemap : 페이지명 23px #444 letter-spacing -2px, 하단 1px #ddd, padding-bottom 10px
                     .site_home (우측 float, 12px #888): "1뎁스 | **2뎁스**"
          [본문]
  #back-top
  footer
```

- 서브 상단 비주얼 이미지는 모든 1뎁스 공통 1장(`sub_bg01.gif`). CSS에 섹션별 `sub_visual1~5`가 정의되어 있으나 이미지가 서버에 없어 미사용
- 본문 폭 800px 기준으로 콘텐츠 이미지가 거의 다 800px 폭으로 제작됨

### 4.1 본문 패턴별 구조
| 패턴 | 사용 페이지 | 마크업/스타일 |
|---|---|---|
| 이미지 1장 | 인사말, 조직도, BUILDING, 시험장비, 서비스범위, Life-cycle, 연락처 | `<div class="tc"><img src=...></div>` 가운데 정렬 |
| 상단 탭 (`.sub_tab_cate`) | 비전&방침(5탭), FAMILY(2탭) | 탭 159px, 1px `#ddd`, 배경 `#f7f7f7`, 글자 `#888`; 활성 `.sub_tab_cate_on` 테두리 `#29146b` 글자 `#29146b` bold 흰 배경 |
| 방침 페이지(0201~0204) | 기업경영·품질·안전보건·환경 | 문장 1줄(`.top_title` 19px `#4f4f4f`, 강조 `#0b5190`) + 220x220 아이콘 타일 4개(`testNN.png`) 각 아래 220px 타이틀 gif(`tNN.gif`) |
| 사업분야 | OFFSHORE, SHIPBUILDING | top 이미지 -> `.sub02_con_t`(180px 회색 박스 “LV Electrical System”, `#f8f8f8`, 좌 float) + `.sub02_con_text .sub02_link`(500px, 항목 앞 `sub02_icon.gif`, 링크 `#888`, 제품 게시글로 연결) -> bottom 이미지 |
| 파트너 로고 표 | PARTNER/고객사/DISTRIBUTION | `.result_title` 22px "THE BEST BUSINESS PARTNER (주) JKE" + `table.boardType2.topBor` (상단 2px `#0b5190`, th 배경 `#f9f9f9`, td 12px `#555`, 셀 테두리 `#ddd`). 열: [구분] 거래처(로고) / 거래처명 / SITE / ITEM |
| 제품 게시글 (product 스킨) | 제품소개 전체 | 상단 `.result_wrap`(회색 `#f9f9f9` 박스 + 1px `#ccc`) 안 `.tab2` 탭(활성 배경 `#646f75` 흰 글자, 비활성 흰 배경 1px `#aaa`) -> `#slideshow-main ul.pgwSlideshow`(800px 폭, 메인 이미지 + 80x80 썸네일 스트립 배경 `#555`) -> "※ 제목" -> `table.boardType2` 사양표 |
| 인증서 갤러리 (lightbox_01 스킨) | R&D 보유기술&인증서 | `#bo_cate` 카테고리 탭(110px, EN 130px, 활성 1px `#565e60` bold) -> `#bo_gall .gall_li` 155x210 썸네일 float + 캡션, 클릭 시 simple-lightbox 원본 -> 페이지네이션 |
| 연혁 (history 스킨) | 회사연혁 | `.list_year` 연도 2.0em `#00417d` 하단 dashed `#ccc` -> `.mc_con`(margin-left 15%, 위로 -25px 당김) 안 `.list_month` 10% 폭 14px `#079CCD` + `.list_content` 90% 13px `#333` |
| JKE Tour | JKE Tour | `img_00__.jpg`(800x600 전경) + `tourtable.jpg`(평면도) + lightbox-plus-jquery 갤러리 `tour_01~27.jpg`(600x800) |
| 찾아오시는길 | 찾아오시는길 | 문장 2줄 + Daum roughmap (`timestamp 1476624123457`, `key dk6s`, 800x300) |
| FAQ | FAQ | 그누보드 basic 스킨 기본 목록/읽기 (댓글폼·캡차 포함) |

---

## 5. 디자인 토큰

### 색상
| 역할 | 값 |
|---|---|
| 브랜드 보라(좌측메뉴 배경, 포인트, 탭 활성) | `#29166e` / `#29166f` / `#29146b` (거의 동일, 혼용) |
| 보라 진한(메뉴 호버 글자, GNB 언더라인) | `#1e0b67` / `#1f0f67` |
| 보조 블루(표 상단선, 제목 강조 span) | `#0b5190` |
| 연혁 연도 / 월 | `#00417d` / `#079CCD` |
| 제품 탭 활성 | `#646f75` |
| 인증서 탭 활성 테두리 | `#565e60` |
| 본문 텍스트 | `#444`(제목) `#555`(표) `#666`(메뉴) `#888`(보조, 브레드크럼) `#4c4c4c`(기본 링크) |
| 선/테두리 | `#ddd`(기본) `#ccc`(진한) `#eee`(연한) `#aaa`(탭) |
| 회색 배경 | `#f9f9f9` `#f8f8f8` `#f7f7f7` `#fcfcfc` |
| 푸터 | 배경 `#2b2b2b`, 글자 `#666` / `#555` |
| 메인 슬라이드 컨테이너 | `#1e1f29`, 슬라이드 `#000`, 비주얼 fallback `#232629` |
| GNB 드롭 배경 | `#000` opacity .4 |

### 타이포
- 기본 폰트: `"NotoSansCJKkr-Medium", sans-serif` (자체 호스팅 `@font-face`, 실제 파일은 `/noto/NotoSansCJKkr-Medium.otf`, `-Light.otf`; woff/eot는 404). 그누보드 default.css는 `dotum` 12px(0.75em)
- GNB 1뎁스 15px/600, 2뎁스 12px
- 서브 비주얼 제목 30px 흰색, letter-spacing -0.5px
- 좌측메뉴 제목 18px/600 흰색, 항목 12px
- 페이지 제목(`.sitemap`) 23px, letter-spacing -2px; 브레드크럼 12px
- 본문 표/설명 12~13px, `.top_title` 19px/400 line-height 30px, `.result_title` 22px
- 푸터 11px

### 치수
- 콘텐츠 폭 1000px (푸터, 서브 콘텐츠, 메인 비주얼 텍스트 영역). 퀵박스 스트립 1332px. GNB 1200px
- 서브 비주얼 310px, 좌측메뉴 200px(내용 180px), 본문 800px, 헤더 80px, 푸터 30px
- 콘텐츠 이미지 표준 폭 800px, 인증서 썸네일 155x210, 정책 아이콘 220x220, 파트너 로고 높이 40~45px

---

## 6. 동작(JS) 요약
| 기능 | 라이브러리 | 파일 |
|---|---|---|
| GNB 메가드롭 | jQuery 1.11 | `js_cjenc/gnb-main.js` |
| 메인 슬라이더 | jquery.cycle.all + TweenMax(GSAP 1.x) | `js_pana/common.js` (`spaceSlider`, `topSlide` 전환, `onAfter` Ken Burns, `topVisualH`) |
| 제품 이미지 슬라이드쇼 | PgwSlideshow 2.0 | `js/pgwslideshow.min.js`, `css/product.css` |
| 인증서 라이트박스 | simple-lightbox | `skin/board/lightbox_01/js/` |
| JKE Tour 갤러리 | lightbox-plus-jquery (Lightbox2) | `sub01/js/`, `sub01/css/lightbox.css` |
| TOP 버튼 | jQuery | 각 서브페이지 인라인 |
| 지도 | Daum roughmap Lander | `sub01/sub01_06.php` 인라인 |

---

## 7. 게시판(bo_table) 목록
| bo_table | 스킨 | 용도 | 글 수 |
|---|---|---|---|
| `sub01_03` / `_en` | history | 회사연혁 | 연도 2002~2020 |
| `sub03_01`~`sub03_09` / `_en` | product | 제품 9종 (01,07은 2건, 06 "CONTSOLE") | 각 1~2 |
| `sub03_10` / `_en` | product | MAS 4종 | 4 |
| `ceri1` / `_en` | lightbox_01 | 인증서 갤러리 (카테고리 `sca`) | KR 62건, EN 약 55건 |
| `faq` / `_en` | basic | FAQ | 1 (테스트글) |
| 숨김: `ceri3`(제조설비), `cadal`(카달로그) | | GNB 주석 처리 | 미수집 |

---

## 8. 복제 시 참고
- 텍스트 대부분이 이미지에 박혀 있음(인사말, 조직도, 사업분야 설명, 서비스, 연락처 등). 이미지 내 텍스트 전사본은 `content/_image_text.md` 참조
- 게시판 첨부 이미지(`/data/file/<bo_table>/`)가 제품 사진·인증서 원본. `assets/board-uploads/<bo_table>/`에 정리, 원본 URL 매핑은 `assets/_map.json`
- KR/EN 콘텐츠 이미지는 파일명이 같고 경로만 `/img/` vs `/eng/img/` (`assets/kr/`, `assets/en/`)
- 원본 HTML/CSS/JS 전체는 `mirror/` (URL 경로 그대로, 쿼리스트링은 `__key-value` 파일명)
