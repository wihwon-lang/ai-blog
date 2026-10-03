// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	// 배포 후 실제 주소로 변경 (GitHub Pages 주소 → 나중에 개인 도메인)
	site: 'https://example.com',
	integrations: [mdx(), sitemap()],
});
