# -*- coding: utf-8 -*-
import json, os, re
from urllib.parse import urlparse, parse_qs, unquote
m=json.load(open("crawl_manifest.json",encoding="utf-8"))
idx={i["url"]:i for i in json.load(open("content/_index.json",encoding="utf-8"))}
def key(url):
    p = urlparse(url); q = parse_qs(p.query)
    path = p.path.strip("/").replace("/", "_").replace(".php","") or "index"
    if q: path += "__" + "_".join(f"{k}-{unquote(v[0])}" for k,v in sorted(q.items()))
    return re.sub(r"[^\w\-가-힣.]", "_", path)
shots={f for f in os.listdir("screenshots")}
KR=[("메인","/"),
("기업소개 > 인사말","/sub01/sub01_01.php"),("기업소개 > 비전&방침 > 기업비전","/sub01/sub01_02.php"),
("기업소개 > 비전&방침 > 기업경영방침","/sub01/sub01_0201.php"),("기업소개 > 비전&방침 > 품질경영방침","/sub01/sub01_0202.php"),
("기업소개 > 비전&방침 > 안전보건방침","/sub01/sub01_0203.php"),("기업소개 > 비전&방침 > 환경경영방침","/sub01/sub01_0204.php"),
("기업소개 > 회사연혁 (게시판 history 스킨)","/bbs/board.php?bo_table=sub01_03"),("기업소개 > 조직도","/sub01/sub01_04.php"),
("기업소개 > JKE Tour (lightbox 갤러리)","/sub01/sub01_05.php"),("기업소개 > FAMILY > ㈜JKE 2공장","/sub01/sub01_07.php"),
("기업소개 > FAMILY > ㈜JK RST","/sub01/sub01_0701.php"),("기업소개 > 찾아오시는길 (Daum 지도)","/sub01/sub01_06.php"),
("사업분야 > OFFSHORE","/sub02/sub02_01.php"),("사업분야 > SHIPBUILDING","/sub02/sub02_02.php"),("사업분야 > BUILDING","/sub02/sub02_03.php"),
("제품소개 > 단체표준인증품(MAS) > 고압배전반","/bbs/board.php?bo_table=sub03_10&wr_id=1"),("제품소개 > MAS > 저압배전반","/bbs/board.php?bo_table=sub03_10&wr_id=2"),
("제품소개 > MAS > 전동기제어반","/bbs/board.php?bo_table=sub03_10&wr_id=3"),("제품소개 > MAS > 분전반","/bbs/board.php?bo_table=sub03_10&wr_id=4"),
("제품소개 > SWITCHBOARD > Normal SWBD","/bbs/board.php?bo_table=sub03_01&wr_id=1"),("제품소개 > SWITCHBOARD > (wr_id=2 MB301M)","/bbs/board.php?bo_table=sub03_01&wr_id=2"),
("제품소개 > MOTOR CONTROL CENTER","/bbs/board.php?bo_table=sub03_02&wr_id=1"),("제품소개 > VFD","/bbs/board.php?bo_table=sub03_03&wr_id=1"),
("제품소개 > DISTRIBUTION BOARD","/bbs/board.php?bo_table=sub03_04&wr_id=1"),("제품소개 > JUNCTION BOX","/bbs/board.php?bo_table=sub03_05&wr_id=1"),
("제품소개 > CONSOLE","/bbs/board.php?bo_table=sub03_06&wr_id=1"),("제품소개 > BOOTH > Safe Booth","/bbs/board.php?bo_table=sub03_07&wr_id=1"),
("제품소개 > BOOTH > Telephone Booth","/bbs/board.php?bo_table=sub03_07&wr_id=2"),("제품소개 > NAVIGATION CONTROL","/bbs/board.php?bo_table=sub03_08&wr_id=1"),
("제품소개 > OTHERS","/bbs/board.php?bo_table=sub03_09&wr_id=1"),
("R&D > 보유기술&인증서 (Total, 5페이지)","/bbs/board.php?bo_table=ceri1"),("R&D > 인증서 > 경영시스템","/bbs/board.php?bo_table=ceri1&sca=%EA%B2%BD%EC%98%81%EC%8B%9C%EC%8A%A4%ED%85%9C"),
("R&D > 인증서 > 기업인증서","/bbs/board.php?bo_table=ceri1&sca=%EA%B8%B0%EC%97%85%EC%9D%B8%EC%A6%9D%EC%84%9C"),("R&D > 인증서 > 라이센스 (2페이지)","/bbs/board.php?bo_table=ceri1&sca=%EB%9D%BC%EC%9D%B4%EC%84%BC%EC%8A%A4"),
("R&D > 인증서 > 제품인증서","/bbs/board.php?bo_table=ceri1&sca=%EC%A0%9C%ED%92%88%EC%9D%B8%EC%A6%9D%EC%84%9C"),("R&D > 인증서 > 단체표준 인증서","/bbs/board.php?bo_table=ceri1&sca=%EB%8B%A8%EC%B2%B4%ED%91%9C%EC%A4%80+%EC%9D%B8%EC%A6%9D%EC%84%9C"),
("R&D > 인증서 > 표창","/bbs/board.php?bo_table=ceri1&sca=%ED%91%9C%EC%B0%BD"),("R&D > 시험 및 검사장비","/sub04/sub04_02.php"),
("PARTNER > PARTNER","/sub05/sub05_01.php"),("PARTNER > 고객사","/sub05/sub05_02.php"),("PARTNER > DISTRIBUTION","/sub05/sub05_03.php"),
("고객지원 > 서비스 범위","/sub06/sub06_01.php"),("고객지원 > Life-cycle 서비스","/sub06/sub06_02.php"),("고객지원 > 연락처","/sub06/sub06_04.php"),
("고객지원 > FAQ (목록)","/bbs/board.php?bo_table=faq"),("고객지원 > FAQ > 글보기","/bbs/board.php?bo_table=faq&wr_id=1")]
EN=[("MAIN","/eng/index.php"),
("COMPANY > GREETING","/eng/sub01/sub01_01.php"),("COMPANY > VISION & POLICY","/eng/sub01/sub01_02.php"),("... > Management Policy","/eng/sub01/sub01_0201.php"),
("... > Quality Policy","/eng/sub01/sub01_0202.php"),("... > Safety & Health Policy","/eng/sub01/sub01_0203.php"),("... > Environmental Policy","/eng/sub01/sub01_0204.php"),
("COMPANY > HISTORY","/bbs/board.php?bo_table=sub01_03_en"),("COMPANY > ORGANIZATION","/eng/sub01/sub01_04.php"),("COMPANY > JKE TOUR","/eng/sub01/sub01_05.php"),
("COMPANY > FAMILY > JKE 2nd Factory","/eng/sub01/sub01_07.php"),("COMPANY > FAMILY > JK RST","/eng/sub01/sub01_0701.php"),("COMPANY > LOCATION","/eng/sub01/sub01_06.php"),
("BUSINESS AREAS > OFFSHORE","/eng/sub02/sub02_01.php"),("BUSINESS AREAS > SHIPBUILDING","/eng/sub02/sub02_02.php"),("BUSINESS AREAS > BUILDING","/eng/sub02/sub02_03.php"),
("INTRODUCTION > STANDARDS OF PRIVATE (MAS) 1~4","/bbs/board.php?bo_table=sub03_10_en&wr_id=1"),("INTRODUCTION > SWITCHBOARD","/bbs/board.php?bo_table=sub03_01_en&wr_id=1"),
("INTRODUCTION > SWITCHBOARD (wr_id=2)","/bbs/board.php?bo_table=sub03_01_en&wr_id=2"),("INTRODUCTION > MOTOR CONTROL CENTER","/bbs/board.php?bo_table=sub03_02_en&wr_id=1"),
("INTRODUCTION > MCC (wr_id=2)","/bbs/board.php?bo_table=sub03_02_en&wr_id=2"),("INTRODUCTION > VFD","/bbs/board.php?bo_table=sub03_03_en&wr_id=1"),
("INTRODUCTION > DISTRIBUTION BOARD","/bbs/board.php?bo_table=sub03_04_en&wr_id=1"),("INTRODUCTION > DB (wr_id=2)","/bbs/board.php?bo_table=sub03_04_en&wr_id=2"),
("INTRODUCTION > JUNCTION BOX","/bbs/board.php?bo_table=sub03_05_en&wr_id=1"),("INTRODUCTION > CONSOLE","/bbs/board.php?bo_table=sub03_06_en&wr_id=1"),
("INTRODUCTION > BOOTH > Safe","/bbs/board.php?bo_table=sub03_07_en&wr_id=1"),("INTRODUCTION > BOOTH > Telephone","/bbs/board.php?bo_table=sub03_07_en&wr_id=2"),
("INTRODUCTION > NAVIGATION CONTROL","/bbs/board.php?bo_table=sub03_08_en&wr_id=1"),("INTRODUCTION > OTHERS","/bbs/board.php?bo_table=sub03_09_en&wr_id=1"),
("R&D > TECHNOLOGY & CERTIFICATE (Total, 4 pages)","/bbs/board.php?bo_table=ceri1_en"),("... > Q.M System Certificate","/bbs/board.php?bo_table=ceri1_en&sca=Q.M+System+Certificate"),
("... > Company certificate","/bbs/board.php?bo_table=ceri1_en&sca=Company+certificate"),("... > License (2 pages)","/bbs/board.php?bo_table=ceri1_en&sca=License"),
("... > Product certificate","/bbs/board.php?bo_table=ceri1_en&sca=Product+certificate"),("... > Self-Production (empty)","/bbs/board.php?bo_table=ceri1_en&sca=Self-Production"),
("... > Recognition","/bbs/board.php?bo_table=ceri1_en&sca=Recognition"),("R&D > TEST & INSPECTION","/eng/sub04/sub04_02.php"),
("PARTNER > PARTNER","/eng/sub05/sub05_01.php"),("PARTNER > CUSTOMER","/eng/sub05/sub05_02.php"),("PARTNER > DISTRIBUTION","/eng/sub05/sub05_03.php"),
("CUSTOMER CENTER > SERVICE RANGE","/eng/sub06/sub06_01.php"),("CUSTOMER CENTER > LIFE CYCLE SERVICE","/eng/sub06/sub06_02.php"),("CUSTOMER CENTER > CONTACT","/eng/sub06/sub06_04.php"),
("CUSTOMER CENTER > FAQ","/bbs/board.php?bo_table=faq_en"),("CUSTOMER CENTER > FAQ > view","/bbs/board.php?bo_table=faq_en&wr_id=1")]
out=["# PAGES - 페이지별 인덱스 (메뉴 경로 / URL / 텍스트 콘텐츠 / 스크린샷 / 본문 이미지 수)\n"]
def sect(title, rows):
    out.append(f"\n## {title}\n\n| 메뉴 경로 | URL | 콘텐츠 md | 스크린샷 | 본문 이미지 |\n|---|---|---|---|---|")
    for name,path in rows:
        u="http://jketech.co.kr"+path
        k=key(u); i=idx.get(u,{})
        shot=f"screenshots/{k}.png" if f"{k}.png" in shots else "-"
        out.append(f"| {name} | `{path}` | [{k}.md](content/{k}.md) | {shot} | {i.get('n_img','?')} |")
sect("한국어 (KOR)",KR); sect("영어 (ENG)",EN)
out.append("""
## 상태 캡처 (메인)

- screenshots/index__gnb-hover.png : GNB 마우스오버 (드롭다운 전체 펼침 + 헤더 흰 배경 전환)
- screenshots/index__slide2.png ~ index__slide4.png : 메인 슬라이드 2~4
- screenshots/index__footbox-hover.png : 하단 퀵박스(JKE TOUR) 호버 상태
- screenshots/eng_index__gnb-hover.png : 영문 GNB 호버

## 크롤 시 발견된 깨진 링크 / 빈 항목

- 제품 탭 `Special SWBD` (SWITCHBOARD, CONSOLE) 링크가 `wr_id=` 빈 값 -> 글 없는 목록 페이지로 이동
- ENG GNB 소스에 KR 전용 항목이 주석으로 남아 있음 (ENERGY, 기타사업, 제조설비, 카달로그)
- `/eng/bbs/...` 링크 1건 404 (실제 게시판은 `/bbs/board.php?bo_table=*_en`)
- CSS가 참조하는 `/images/common/*`, `/img/sub/sub_visual0X.gif`, `/noto/*.woff|eot` 는 서버에 없음(404, 템플릿 잔재). 폰트는 `.otf` 2종만 실제 존재
- FAQ 게시판에는 테스트 글 1건("FAQ test")만 존재
- CONSOLE 페이지 제목 오타 "CONTSOLE" 그대로 노출됨
- 푸터 저작권 문구 오타 "Copyrught" 그대로 노출됨
""")
open("PAGES.md","w",encoding="utf-8").write("\n".join(out))
print("PAGES.md", len(out), "lines")
