# jketech-clone — jketech.co.kr 복제용 자료 모음

수집일 2026-09-07. ㈜JKE (http://jketech.co.kr) KOR/ENG 전체.

## 어디부터 보면 되나
1. `STRUCTURE.md` — 사이트맵, 공통 레이아웃(GNB/푸터), 메인·서브 페이지 짜임, 디자인 토큰(색/폰트/치수), 동작(JS), 게시판 목록. **복제 스펙 본체**
2. `PAGES.md` — 페이지 1장당 1행: 메뉴 경로 / URL / 텍스트 md / 스크린샷 / 이미지 수. 깨진 링크 목록 포함
3. `screenshots/` — 전 페이지 풀페이지 캡처 121장 (1400px 폭). 메인은 슬라이드 2~4, GNB 호버, 퀵박스 호버 상태 추가
4. `content/` — 페이지별 텍스트 콘텐츠 (좌측메뉴, 브레드크럼, 본문, 표는 마크다운 표, 본문 이미지 목록)
   - `content/_image_text.md` — **이미지에 박힌 텍스트 전사본** 128장 (인사말, 조직도, 사업분야, 방침 타일, 메인 카피, 파트너 로고 등)
5. `assets/` — 이미지·폰트 원본을 용도별로 분류
   - `kr/`, `en/` : `main-visual`(슬라이드 배경 4 + 카피 8), `content`(서브 본문 이미지), `tour-gallery`(JKE Tour 27장)
   - `common-ui/` : 로고 2종, 화살표, 재생/정지, 퀵박스 호버 이미지 4종, lightbox 아이콘
   - `partner-logos/` : 파트너·고객사 로고 19종
   - `board-uploads/<bo_table>/` : 게시판 첨부 원본 (제품 사진, 인증서 스캔 + 155x210 썸네일)
   - `fonts/` : NotoSansCJKkr Light/Medium .otf
   - `_map.json` : 정리 파일 → 원본 URL → 참조 페이지 매핑
6. `mirror/` — 원본 HTML/CSS/JS 그대로 (참고용, 중점 아님). URL 경로 유지, 쿼리는 `board__bo_table-xxx_wr_id-1.php` 식 파일명
7. `crawl_manifest.json`, `asset_dims.json` — 크롤 결과 원장 (페이지별 링크/에셋, 이미지 크기)
8. `tools/` — 재수집 스크립트 (`crawl.py` 미러링 → `extract.py` 텍스트 추출 → `gen_pages.py` 인덱스 → `shot*.py` 스크린샷)

## 숫자
| 항목 | 수 |
|---|---|
| HTML 페이지 | 123 (KR 62 / EN 61, 페이지네이션 포함) |
| 이미지 | 582 (jpg 255 / gif 206 / png 121) |
| 게시판 첨부 | 363 |
| 폰트 | 2 (.otf, 각 16MB) |
| 총 용량 | mirror 96MB, assets 92MB, screenshots 117MB |
