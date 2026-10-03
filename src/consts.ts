// 사이트 이름·설명·카테고리·애드센스 ID 등 전역 설정값

export const SITE_TITLE = 'AI 작업실';
export const SITE_DESCRIPTION =
	'AI 영상, 이미지, 음악, 업무 자동화까지 생성형 AI를 실무에 쓰는 방법을 직접 써보고 정리합니다.';

// 문의 페이지·개인정보처리방침에 노출되는 연락처. 비어 있으면 "준비 중"으로 표시된다.
export const CONTACT_EMAIL = '';

// 애드센스 승인 신청 시 'ca-pub-XXXXXXXXXXXXXXXX' 입력. 비어 있으면 광고 스크립트를 넣지 않는다.
export const ADSENSE_CLIENT = '';

export const CATEGORIES = [
	{ slug: 'ai-video', name: 'AI 영상', description: '클링, Seedance, 런웨이 등 AI 영상 생성 도구 사용법과 비교' },
	{ slug: 'ai-image', name: 'AI 이미지', description: '나노바나나, 미드저니 등 AI 이미지 생성과 편집' },
	{ slug: 'ai-audio', name: 'AI 음악·음성', description: 'AI 작곡, TTS, 더빙과 보이스오버' },
	{ slug: 'ai-automation', name: 'AI 업무 자동화', description: 'ChatGPT, Claude로 문서·마케팅 업무 줄이기' },
	{ slug: 'ai-side-income', name: 'AI 부업·수익화', description: '숏폼, 광고 소재, 외주 등 AI로 돈 버는 방법' },
] as const;

export type CategorySlug = (typeof CATEGORIES)[number]['slug'];

export function getCategory(slug: CategorySlug) {
	return CATEGORIES.find((c) => c.slug === slug)!;
}
