# Openverse에서 상업적 이용 가능한 무료 이미지를 찾아 내려받고 출처 표기 문구를 만드는 스크립트
"""
사용법
  1) 후보 찾기 (영어 검색어가 결과가 많다)
     python3 scripts/find_image.py search "robot painting"
     → 번호, 라이선스, 크기, 제목, 미리보기 URL 목록. 미리보기를 열어 글 내용과 맞는지 직접 확인한다.
  2) 고른 후보 내려받기
     python3 scripts/find_image.py get "robot painting" 2 src/assets/blog/<slug>/hero
     → 확장자를 붙여 저장하고, 본문 아래에 붙일 출처 문구(마크다운)를 출력한다.

조건: 상업적 이용 가능 + 변경 금지(ND) 제외 + 가로 800px 이상.
"""
import json
import os
import sys
import urllib.parse
import urllib.request

API = 'https://api.openverse.org/v1/images/'
LICENSE_NAMES = {'cc0': 'CC0', 'pdm': '퍼블릭 도메인', 'by': 'CC BY', 'by-sa': 'CC BY-SA'}


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'aikkul-blog/1.0 (https://aikkul.com)'})
    return urllib.request.urlopen(req, timeout=60).read()


def search(query):
    params = {'q': query, 'license_type': 'commercial', 'page_size': 12, 'mature': 'false'}
    data = json.loads(fetch(API + '?' + urllib.parse.urlencode(params)))
    results = []
    for r in data.get('results', []):
        if r.get('license') not in LICENSE_NAMES:  # ND·NC 등 제외
            continue
        if (r.get('width') or 0) < 800:
            continue
        results.append(r)
    return results


def credit(r):
    version = f" {r['license_version']}" if r.get('license_version') else ''
    creator = r.get('creator') or '작성자 미상'
    title = r.get('title') or '이미지'
    source = r.get('foreign_landing_url') or r['url']
    license_url = r.get('license_url') or ''
    lic = f"[{LICENSE_NAMES[r['license']]}{version}]({license_url})" if license_url else LICENSE_NAMES[r['license']] + version
    return f"*이미지 출처: [{title}]({source}), {creator}, {lic}*"


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 3 or sys.argv[1] not in ('search', 'get'):
        print(__doc__)
        sys.exit(1)
    cmd, query = sys.argv[1], sys.argv[2]
    results = search(query)
    if cmd == 'search':
        if not results:
            print('조건에 맞는 무료 이미지가 없습니다.')
        for i, r in enumerate(results):
            print(f"[{i}] {r['license']} {r['width']}x{r['height']} {r.get('title', '')[:60]}")
            print(f"     미리보기 {r.get('thumbnail') or r['url']}")
        return
    index, dest = int(sys.argv[3]), sys.argv[4]
    r = results[index]
    ext = os.path.splitext(urllib.parse.urlparse(r['url']).path)[1].lower() or '.jpg'
    if ext not in ('.jpg', '.jpeg', '.png', '.webp'):
        ext = '.jpg'
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    path = dest + ext
    with open(path, 'wb') as f:
        f.write(fetch(r['url']))
    print('저장:', path)
    print('출처 문구:', credit(r))


if __name__ == '__main__':
    main()
