// 사이트 내부 링크에 base 경로(/ai-blog)를 붙여 주는 헬퍼. 도메인 연결 후 base가 '/'가 되면 그대로 동작한다.

export function url(path: string) {
	return import.meta.env.BASE_URL.replace(/\/$/, '') + path;
}
