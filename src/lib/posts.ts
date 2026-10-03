// draft를 제외한 발행 글을 최신순으로 가져오는 헬퍼 (개발 모드에서는 draft 포함)

import { getCollection } from 'astro:content';

export async function getPublishedPosts() {
	// 로컬 미리보기(npm run dev)에서는 draft도 보여서 초안을 확인할 수 있다
	const posts = await getCollection('blog', ({ data }) => import.meta.env.DEV || !data.draft);
	return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}
