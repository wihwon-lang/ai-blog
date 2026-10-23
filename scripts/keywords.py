# 구글·네이버 자동완성으로 실제 검색어를 모아 글 주제·제목 후보를 찾는 스크립트
"""
사용법
  python3 scripts/keywords.py 나노바나나 "suno"
  python3 scripts/keywords.py --expand 나노바나나   # 씨앗 + 무료/프롬프트/안됨 등 붙여서 한 번 더 조회

출력: 씨앗별로 구글(G)·네이버(N) 자동완성 목록. 양쪽에 다 나오는 검색어 앞에 * 표시.
"""
import json
import sys
import urllib.parse
import urllib.request

SUFFIXES = ['무료', '사용법', '프롬프트', '가격', '안됨', '추천', '비교', '저작권', '한국어', '현실']


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=10).read()


def google(q):
    url = 'https://suggestqueries.google.com/complete/search?' + urllib.parse.urlencode(
        {'client': 'chrome', 'hl': 'ko', 'gl': 'kr', 'q': q})
    return json.loads(fetch(url).decode('utf-8', 'ignore'))[1]


def naver(q):
    url = 'https://ac.search.naver.com/nx/ac?' + urllib.parse.urlencode(
        {'q': q, 'st': 100, 'r_format': 'json', 'q_enc': 'UTF-8', 'r_enc': 'UTF-8', 'frm': 'nv'})
    data = json.loads(fetch(url).decode('utf-8'))
    return [item[0] for item in data['items'][0]] if data.get('items') else []


def safe(fn, q):
    try:
        return fn(q)
    except Exception as e:
        print(f'  ({fn.__name__} 실패: {e})')
        return []


def show(q):
    g, n = safe(google, q), safe(naver, q)
    both = set(g) & set(n)
    mark = lambda xs: ' | '.join(('*' + x if x in both else x) for x in xs[:10])
    print(f'== {q}')
    print('  G:', mark(g))
    print('  N:', mark(n))


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    args = sys.argv[1:]
    expand = '--expand' in args
    seeds = [a for a in args if a != '--expand']
    for seed in seeds:
        show(seed)
        if expand:
            for s in SUFFIXES:
                show(f'{seed} {s}')


if __name__ == '__main__':
    main()
