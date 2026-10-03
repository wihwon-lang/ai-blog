// draft를 제외한 발행 글을 최신순으로 가져오는 헬퍼

import { getCollection } from 'astro:content';

export async function getPublishedPosts() {
	const posts = await getCollection('blog', ({ data }) => !data.draft);
	return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}
