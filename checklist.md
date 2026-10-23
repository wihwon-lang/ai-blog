# AI 작업실 블로그 체크리스트

목표: 생성형 AI 활용 블로그를 만들어 애드센스 승인받기.

## 1단계 사이트 뼈대
- [x] Astro 블로그 템플릿 설치
- [x] 한국어화 (lang, 날짜 형식, 폰트)
- [x] 카테고리 5개 (frontmatter `category`) + 카테고리별 목록 페이지
- [x] 홈 / 전체 글 / 글 상세 레이아웃 정리
- [x] 필수 페이지: 소개, 개인정보처리방침, 문의
- [x] 애드센스 스크립트 자리 (`ADSENSE_CLIENT` 비어 있으면 미출력)
- [x] 템플릿 샘플 글·이미지 삭제
- [x] `npm run build` 통과
- [x] git init + 첫 커밋
- [x] 문의 이메일 (`CONTACT_EMAIL`) 확정

## 2단계 배포
- [x] GitHub 저장소 생성 (사용자) — wihwon-lang/ai-blog, Public
- [x] GitHub Actions 배포 워크플로
- [x] `astro.config.mjs`의 `site`/`base`를 GitHub Pages 주소로 변경
- [x] 문의 페이지 이메일 확정
- [x] 저장소 Settings → Pages → Source를 "GitHub Actions"로 (사용자)
- [x] 첫 배포 성공 확인 (https://wihwon-lang.github.io/ai-blog/)
- [x] Pages CMS 설정 (`.pages.yml`)
- [ ] Pages CMS에 ai-blog 저장소 접근 허용 + 편집 화면 확인 (사용자)

## 3단계 글 쌓기
- [x] 첫 글 10개 초안 (사용자 경험 추가 자리 표시)
  - [x] 1. 클링 AI 사용법 총정리 (`kling-ai-guide.md`, draft)
  - [x] 2. 클링 vs Seedance 2.0 비교
  - [x] 3. 나노바나나 캐릭터 일관성
  - [x] 4. Image to Video 실전 가이드
  - [x] 5. CapCut 편집·자막·보이스오버
  - [x] 6. AI 영상 프롬프트 카메라·조명 용어
  - [x] 7. AI 영상 도구 요금제 비교
  - [x] 8. ChatGPT로 숏폼 대본·콘티
  - [x] 9. AI로 분양 홍보 영상 만든 후기
  - [x] 10. AI 영상 상업적 이용·저작권
- [ ] 사용자 경험·캡처 추가
- [ ] 글 20~30개 달성

## 4단계 도메인·승인
- [x] 도메인 구매 (사용자) — aikkul.com, 가비아, 2026-10-09
- [x] `astro.config.mjs` site를 aikkul.com으로, base 제거, `public/CNAME` 추가
- [x] 가비아 DNS 설정 (사용자)
- [x] 저장소 Settings → Pages → Custom domain 입력 (사용자) 후 push — 2026-10-09 aikkul.com 접속 확인
- [x] HTTPS 강제 켜기 + aikkul.com 접속 확인
- [x] 구글 서치 콘솔 등록(도메인 속성, 가비아 TXT 인증), 사이트맵 제출 — 2026-10-09
- [x] `ADSENSE_CLIENT` 입력 + `public/ads.txt` (2026-10-15)
- [x] 애드센스 사이트 추가 + 검토 요청 (2026-10-15, 상태 "준비 중")
- [ ] 애드센스 승인 결과 확인

## 5단계 애드센스 거절 후 개편 (2026-10-23 거절: 가치가 별로 없는 콘텐츠)
- [x] `scripts/keywords.py` 구글·네이버 자동완성 검색어 수집
- [x] `scripts/find_image.py` 무료 이미지(Openverse, 상업 이용 가능) 검색·다운로드·출처 기록
- [x] `scripts/gen_image.py` 무료 이미지 없을 때 OpenAI로 생성
- [x] WRITING_GUIDE: 목표 검색어·제목 규칙·이미지 1~2장 규칙
- [x] topics.md 미작성 28개를 검색어 기반 25개로 교체
- [x] 메뉴 링크 끝 `/` 누락(301) 수정
- [x] 기존 글 제목·설명 38개 검색어 기준으로 변경 (2026-10-23, 주소 유지)
- [x] 기존 글 38개에 대표 이미지 (무료 8장 + 생성 30장, 2026-10-23)
- [x] OpenAI 키를 클라우드 네트워크 시크릿으로 등록(사용자) + 네트워크 액세스 전체 + 루틴 프롬프트 갱신 + 클라우드 이미지 생성 확인 (2026-10-23)
- [ ] 서치 콘솔 노출 증가 확인 후 애드센스 재신청 (3~4주 뒤)
