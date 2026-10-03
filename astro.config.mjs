// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	// 개인 도메인 연결 시: site를 도메인으로 바꾸고 base 줄을 지운다 (public/CNAME도 추가)
	site: 'https://wihwon-lang.github.io',
	base: '/ai-blog',
	integrations: [mdx(), sitemap()],
});
