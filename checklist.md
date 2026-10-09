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
- [ ] HTTPS 강제 켜기 + aikkul.com 접속 확인
- [ ] 구글 서치 콘솔 등록, 사이트맵 제출
- [ ] 애드센스 신청 → `ADSENSE_CLIENT` 입력 + `public/ads.txt`
