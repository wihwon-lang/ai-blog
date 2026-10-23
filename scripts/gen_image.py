# 무료 이미지가 없을 때 OpenAI 이미지 API로 글 이미지를 생성해 저장하는 스크립트
"""
사용법
  python3 scripts/gen_image.py src/assets/blog/<slug>/hero "영어 프롬프트"
  키: OPENAI_API_KEY 환경변수, 없으면 클라우드 환경의 네트워크 시크릿(api.openai.com)이 인증 헤더를 붙여 준다고 보고 키 없이 요청
  → <경로>.webp 로 저장 (1536x1024, 가로형)

프롬프트 규칙: 영어로, 글 내용을 보여주는 장면·도식. 글자·로고·실제 브랜드 화면은 넣지 않는다.
스크립트가 프롬프트 끝에 "글자 없음" 지시를 자동으로 붙인다.
"""
import base64
import json
import os
import re
import sys
import time
import urllib.request

NO_TEXT = ' No text, no letters, no words, no logos, no watermarks, no brand UI.'


def call(path, key, body=None):
    headers = {'Content-Type': 'application/json'}
    if key:  # 키가 없으면 네트워크 시크릿 프록시가 Authorization을 붙인다
        headers['Authorization'] = f'Bearer {key}'
    req = urllib.request.Request('https://api.openai.com/v1/' + path, headers=headers,
                                 data=json.dumps(body).encode() if body else None)
    for attempt in range(3):  # 일시적인 오류(429·5xx)는 잠시 뒤 다시 시도
        try:
            return json.loads(urllib.request.urlopen(req, timeout=300).read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 2:
                time.sleep(20)
                continue
            sys.exit(f'API 오류 {e.code}: {e.read()[:500].decode("utf-8", "ignore")}')


def pick_model(key):
    # 계정에서 쓸 수 있는 gpt-image 모델 중 가장 최신(mini 아닌 것 우선)
    ids = [m['id'] for m in call('models', key)['data'] if m['id'].startswith('gpt-image')]
    if not ids:
        sys.exit('이 계정에서 쓸 수 있는 gpt-image 모델이 없습니다.')
    ver = lambda i: [int(n) for n in re.findall(r'\d+', i)] or [0]
    ids.sort(key=lambda i: (ver(i), 'mini' not in i))
    return ids[-1]


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    dest, prompt = sys.argv[1], sys.argv[2]
    key = os.environ.get('OPENAI_API_KEY')
    model = pick_model(key)
    res = call('images/generations', key, {
        'model': model, 'prompt': prompt + NO_TEXT, 'size': '1536x1024', 'quality': 'medium',
        'output_format': 'webp', 'output_compression': 80, 'n': 1,
    })
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    path = dest + '.webp'
    with open(path, 'wb') as f:
        f.write(base64.b64decode(res['data'][0]['b64_json']))
    print(f'모델: {model}')
    print('저장:', path)


if __name__ == '__main__':
    main()
