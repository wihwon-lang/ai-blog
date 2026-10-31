---
title: '클링 AI 프롬프트 예시 — 장면별로 바로 쓰는 영상 프롬프트'
description: '클링 AI 프롬프트를 공식 가이드의 공식에 맞춰 장면별 예시로 정리했습니다. 텍스트·이미지 영상, 멀티샷과 대사, 네거티브 프롬프트, 한글 프롬프트 쓰는 법을 표와 함께 설명합니다.'
category: 'ai-video'
pubDate: '2026-11-03'
draft: false
heroImage: '../../assets/blog/kling-ai-prompt-examples/hero.webp'
heroAlt: '노을 속 인물이 재생 중인 노트북 옆에 슬레이트와 세 칸짜리 스토리보드 스케치가 놓인 책상 일러스트'
---

클링 AI 프롬프트를 어떻게 써야 할지 몰라 같은 영상을 여러 번 다시 만드는 경우가 많습니다. 이 글은 2026년 10월 기준 클링 공식 프롬프트 가이드와 VIDEO 3.0 사용 가이드를 바탕으로, 장면별로 복사해서 바로 쓸 수 있는 프롬프트 예시와 고치는 요령을 정리했습니다. 가입과 첫 영상 만들기가 처음이라면 [클링 AI 사용법](../kling-ai-guide/)을 먼저 보시는 것을 추천합니다.

## 결론부터 — 클링 AI 프롬프트 기본 공식

클링 공식 가이드는 만드는 방식에 따라 프롬프트에 넣을 요소를 다르게 안내합니다. 아래 표의 순서대로 칸을 채우면 대부분의 장면을 쓸 수 있습니다.

| 만드는 방식 | 공식 가이드의 기본 공식 | 꼭 넣을 것 | 생략해도 되는 것 |
|---|---|---|---|
| 텍스트 → 영상 | 주체(외모 설명) + 주체의 움직임 + 장면(배경 설명) + (카메라 언어 + 조명 + 분위기) | 주체, 움직임, 장면 | 카메라, 조명, 분위기 |
| 이미지 → 영상 | 주체 + 움직임, 배경 + 움직임 | 누가 어떻게 움직이는지 | 이미지에 이미 보이는 외모·배경 |
| VIDEO 3.0 멀티샷 | 장면·인물·분위기 설정 → 샷 1, 샷 2 … 순서대로 구도와 행동 | 샷 번호, 샷 크기, 행동 | 샷별 길이(자동 모드일 때) |
| 대사가 있는 영상 | 인물 이름 (말투·억양): 대사 | 누가 말하는지 | 목소리를 이미 연결한 경우 말투 |

공식 가이드가 공통으로 강조하는 요령은 세 가지입니다. 쉬운 단어와 짧은 문장을 쓰고, 5~10초 안에 끝날 만큼 단순한 동작을 고르고, 공을 튀기거나 높이 던지는 것 같은 복잡한 물리 동작은 피하는 것입니다.

## 텍스트로 영상 만들 때 — 장면별 프롬프트 예시

텍스트만으로 영상을 만들 때는 주체와 장면을 모두 글로 설명해야 합니다. 공식 가이드는 짧은 문장에서 시작해 외모 설명, 카메라와 조명을 덧붙이는 방식을 예로 듭니다.

| 단계 | 프롬프트 | 더해진 요소 |
|---|---|---|
| 1 | A giant panda is reading a book in a café. | 주체 + 움직임 + 장면 |
| 2 | Shot in medium range, with a blurred background and atmospheric lighting, a giant panda wearing black-framed glasses is reading a book in a café. | 외모 설명 + 카메라 언어 + 조명 |

이 흐름에 맞춰 숏폼에서 자주 쓰는 장면을 프롬프트로 정리하면 다음과 같습니다.

| 장면 | 용도 | 핵심 구성 |
|---|---|---|
| 카페 인물 | 브이로그 오프닝, 감성 숏폼 | 인물 외모 + 커피 마시는 동작 + 창가 + 오후 햇빛 |
| 도시 야경 | 인트로, 전환 컷 | 드론 시점 + 네온 + 비 내린 도로 |
| 제품 회전 | 쇼핑몰 광고, 상세페이지 영상 | 제품 + 천천히 회전 + 단색 배경 + 스튜디오 조명 |

아래는 표의 앞 두 장면을 그대로 옮긴 예시입니다. 영어로 쓰고, 문장마다 한 가지 정보만 담았습니다.

```
A young woman with short brown hair and a beige knit sweater sips coffee by a café window.
Soft afternoon sunlight falls on the table. Medium close-up, shallow depth of field, calm and cozy mood.
```

```
Aerial drone shot of a city at night after rain.
Neon signs reflect on the wet streets, cars leave light trails. Slow forward movement, cinematic atmosphere.
```

카메라 무빙·샷 크기·조명 용어를 더 다양하게 쓰고 싶다면 [AI 영상 프롬프트 작성법](../ai-video-prompt-camera-lighting/)의 용어 표를 함께 참고하면 됩니다.

## 이미지로 영상 만들 때 — 움직임만 적는다

이미지 → 영상에서는 장면이 이미 이미지에 들어 있기 때문에, 공식 가이드는 주체와 그 움직임을 적는 데 집중하라고 안내합니다. 여러 인물이 있으면 각자의 움직임을 순서대로 나열합니다.

| 안 좋은 예 | 좋은 예 | 이유 |
|---|---|---|
| Put on sunglasses | The woman puts on sunglasses with her right hand. | 누가 어떻게 하는지 없으면 정지 화면이나 단순 패닝이 나오기 쉽습니다. |
| A beautiful girl in a red dress in Paris | The girl turns toward the camera and smiles, her hair blown by the wind. | 이미지에 보이는 외모·장소를 다시 쓰기보다 움직임을 적는 편이 낫습니다. |
| The man jumps off the roof and flies into space | The man walks slowly toward the edge of the roof and looks at the city. | 이미지와 크게 다른 내용을 쓰면 장면 전환이나 컷이 생길 수 있습니다. |

사진 한 장으로 영상을 만드는 전체 흐름은 [사진 영상 변환 AI](../image-to-video-guide/)에서 따로 정리했습니다.

## 멀티샷·대사 프롬프트 — VIDEO 3.0 예시

Kling VIDEO 3.0은 한 번에 3~15초 길이를 고를 수 있고, 멀티샷을 켜면 최대 6개 샷으로 장면을 나눌 수 있습니다. 공식 블로그는 먼저 장소·조명·인물·분위기를 정한 뒤, 샷에 번호를 붙여 순서대로 구도와 행동을 적으라고 안내합니다.

| 멀티샷 모드 | 샷 길이 | 프롬프트 쓰는 법 |
|---|---|---|
| 자동 (Multi-Shot 켜기) | AI가 계산 | 장면 전체를 설명하면 모델이 샷 구성을 정합니다. 장면에 따라 한 샷으로 만들 수도 있습니다. |
| 커스텀 (Custom Multi-Shot) | 샷마다 직접 지정 | 샷 개수와 길이를 정하고, 샷마다 구도·시점·내용·카메라 움직임을 적습니다. |

공식 블로그에 나온 형식을 따르면 아래처럼 씁니다. 샷마다 새로운 정보가 하나씩 더해지도록 하는 것이 요령입니다.

```
Night, a quiet rooftop with distant city lights. A woman in a blue striped shirt, calm and thoughtful mood.
[Shot 1: Wide shot] She walks slowly to the railing and looks at the city.
[Shot 2: Medium shot] She takes a deep breath and closes her eyes.
[Shot 3: Close-up shot] A small smile appears on her face. The camera slowly pushes in.
Cinematic lighting, realistic textures.
```

대사는 "인물 이름 (말투·억양): 대사" 형식으로 씁니다. 공식 가이드는 대사마다 말하는 사람을 바로 붙여 써야 세 명 이상이 나오는 장면도 잘 처리된다고 설명합니다. 음성은 중국어, 영어, 일본어, 한국어, 스페인어를 지원하고, 그 밖의 언어 대사는 영어로 번역된다고 안내되어 있습니다.

```
A small Korean restaurant at night, two friends sitting at a table.
Minji (cheerful, in Korean): 오늘 진짜 고생 많았어.
Jiho (tired but smiling, in Korean): 너도. 이제 밥 먹자.
Medium shot, warm lighting.
```

캐릭터 요소에 목소리를 이미 연결해 두었다면, 프롬프트에서 목소리 톤을 다시 지정하지 말라는 것이 공식 안내입니다. 오디오를 넣으면 크레딧이 더 들기 때문에, 크레딧이 넉넉하지 않다면 [클링 AI 무료 크레딧 정리](../kling-ai-free-credits/)를 참고해 오디오 없이 먼저 구도를 확인하는 순서를 추천합니다.

## 클링 AI 네거티브 프롬프트 — 무엇을 넣을까

네거티브 프롬프트는 영상에 나오지 않았으면 하는 것을 적는 칸입니다. 클링 공식 블로그는 팔다리 뒤틀림(warped limbs)이나 낮은 화질(low quality) 같은 흔한 오류를 네거티브 프롬프트로 걸러 내라고 안내합니다. 최신 모델 안내에서는 별도 칸 대신 본문 끝에 "피해야 할 것"을 적는 방식(Constraints)도 예로 듭니다.

| 피하고 싶은 문제 | 네거티브 프롬프트 예시 | 본문에 쓰는 방식 |
|---|---|---|
| 손·팔다리 변형 | warped limbs, extra fingers | Keep hands natural. |
| 화질 저하 | low quality, blurry | Sharp details, realistic textures. |
| 화면에 자막·글자 생김 | subtitles, text, watermark | Add no subtitle or text overlay. |
| 원하지 않는 인물 등장 | extra person, crowd | Add no second person. |
| 제품 라벨 변형 | distorted label | Keep the label clear and unchanged. |
| 원하지 않는 배경음악 | music, soundtrack | SFX only, no music. |

네거티브 프롬프트는 짧게 쓰는 편이 좋습니다. 모델에 따라 네거티브 프롬프트 칸이 보이지 않으면 표의 오른쪽처럼 본문 끝에 한 문장으로 적으면 됩니다.

## 클링 AI 한글 프롬프트 — 한국어로 써도 될까

공식 프롬프트 가이드에는 입력 언어에 대한 별도 안내가 없고, 예시는 모두 영어로 되어 있습니다. 그래서 카메라 용어나 조명 표현처럼 세밀한 연출은 영어로 쓰는 편이 의도대로 반영되기 쉽습니다.

| 프롬프트 부분 | 추천 언어 | 이유 |
|---|---|---|
| 인물·장소 설명 | 한국어 또는 영어 | 단순한 묘사는 어느 쪽이든 무난합니다. |
| 카메라 무빙·샷 크기 | 영어 | dolly in, close-up 같은 용어가 그대로 통합니다. |
| 조명·분위기 | 영어 | golden hour, soft light 같은 표현이 공식 예시와 같습니다. |
| 대사 | 한국어 | VIDEO 3.0이 한국어 음성을 지원하므로 대사는 한국어로 씁니다. |

영어가 어렵다면 한국어로 장면을 먼저 쓰고 ChatGPT나 번역기로 영어로 바꾼 뒤, 대사만 한국어로 남기는 방식이 편합니다. 한국인 인물이 필요하면 "Korean"을 명확히 적는 것을 추천합니다.

## 클링 프롬프트가 안 먹힐 때 — 문제별 고치는 법

결과가 기대와 다르면 아래 표에서 원인을 찾고, 한 번에 한 가지만 바꿔 보세요.

| 증상 | 흔한 원인 | 고치는 법 |
|---|---|---|
| 거의 움직이지 않음 | 동작 설명이 없거나 모호함 | "누가 + 무엇을 + 어떻게"를 한 문장으로 적습니다. |
| 동작이 엉키거나 어색함 | 한 영상에 동작을 너무 많이 넣음 | 5초 영상에는 동작 하나, 10초 이상은 시간 순서대로 나눠 적습니다. |
| 갑자기 다른 장면으로 바뀜 | 이미지와 다른 내용을 프롬프트에 씀 | 이미지에서 일어날 법한 움직임으로 바꿉니다. |
| 카메라가 원하는 대로 안 움직임 | 카메라 무빙을 여러 개 섞음 | 무빙은 하나만 적고, 피사체 동작을 먼저 쓴 뒤 카메라를 씁니다. |
| 인물 얼굴이 샷마다 달라짐 | 인물 고정 없이 멀티샷 사용 | 요소 참조(Element Reference)로 인물을 연결하고 같은 설명을 반복합니다. |
| 사람·사물 개수가 틀림 | 모델이 숫자에 민감하지 않음 | 개수가 중요하면 이미지를 먼저 만들고 이미지 → 영상으로 진행합니다. |

얼굴 변형이나 손가락 오류처럼 프롬프트로 해결하기 어려운 문제는 [AI 영상 오류 해결](../ai-video-common-failures-fix/)에서 따로 정리했습니다.

## 마무리

클링 AI 프롬프트는 "주체 + 움직임 + 장면"을 기본으로 두고, 필요할 때 카메라·조명·분위기를 덧붙이는 공식만 기억하면 대부분의 장면에 쓸 수 있습니다. 이미지로 영상을 만들 때는 움직임만 적고, VIDEO 3.0에서는 샷 번호와 "인물 (말투): 대사" 형식을 쓰면 멀티샷과 대사도 정리된 형태로 넣을 수 있습니다. 결과가 마음에 들지 않으면 동작과 카메라 무빙을 하나씩 줄여 가며 고쳐 보는 방식을 추천합니다.

클링은 모델 업데이트가 잦아 지원 길이, 멀티샷, 음성 언어 같은 기능이 바뀔 수 있습니다. 중요한 작업 전에는 클링 공식 가이드에서 최신 내용을 다시 확인하시기 바랍니다.

## 참고 자료

- [Kling AI Text to Video Prompt Guide](https://kling.ai/quickstart/text-to-video-prompt-guide)
- [Kling AI Image to Video Guide](https://kling.ai/quickstart/image-to-video-guide)
- [Kling VIDEO 3.0 Model User Guide](https://kling.ai/quickstart/klingai-video-3-model-user-guide)
