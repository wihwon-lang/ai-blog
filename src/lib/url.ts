// 사이트 내부 링크에 base 경로를 붙이고, 페이지 경로 끝에 /를 붙여 GitHub Pages의 301 리디렉션을 피하는 헬퍼.

export function url(path: string) {
	const withSlash = /\.[a-z0-9]+$/i.test(path) || path.endsWith('/') ? path : path + '/';
	return import.meta.env.BASE_URL.replace(/\/$/, '') + withSlash;
}
