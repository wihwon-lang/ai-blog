// 공개된 글(임시저장 아님 + 발행일이 오늘 이전)을 최신순으로 가져오는 헬퍼 (개발 모드에서는 전부 포함)

import { getCollection } from 'astro:content';

// 빌드 시점의 한국 날짜 (YYYY-MM-DD)
function todayInKorea() {
	return new Date().toLocaleDateString('sv-SE', { timeZone: 'Asia/Seoul' });
}

export async function getPublishedPosts() {
	const today = todayInKorea();
	// 로컬 미리보기(npm run dev)에서는 임시저장·예약 글도 보여서 초안을 확인할 수 있다
	const posts = await getCollection(
		'blog',
		({ data }) =>
			import.meta.env.DEV || (!data.draft && data.pubDate.toISOString().slice(0, 10) <= today),
	);
	return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}
