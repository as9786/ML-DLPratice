# Enriching Word Vectors with Subword Information

## Abstract
- 기존 model은 단어마다 다른 vector를 할당하여 단어의 형태를 무시
- 위와 같은 문제점을 해결하기 위해 skip-gram을 기반으로 한 model에 각 단어를 n-gram vector의 조합으로 표현
- 기존 model은 parameter를 공유하지 않은 다른 vector로 단어를 표현=> 형태학적(Morphological)으로 복잡한 언어는 잘 표현 못함
- 철자 단위 정보를 사용하여 더 좋은 단어 표현 생성

## Model
- where -> \<where\>. 단어의 양 끝에 <, >를 더하여 접두사와 접미사를 구분할 수 있도록 함
- 
