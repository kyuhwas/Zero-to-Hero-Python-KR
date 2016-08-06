# -*- coding: utf8 -*-

"""
01. 문자열을 다뤄봅시다. (20분)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4
- 참고: 점프 투 파이썬 (02-2 문자열 자료형) https://wikidocs.net/13
- 아래 설명은 Compact version을 기준으로 합니다.
"""

"""
코멘트를 꼭 작성하는 습관을 가집시다.
- 프로그램이 무엇을 하는지
- 특정 라인이나 섹션이 무엇을 하는지
- 특별이 무엇을 하기 위해 선택한 방법이 있다면 "왜" 썼는지?
- 나중에 코드를 다시 볼때 이해하기 쉽게 도움이 될만한 내용은 뭐든 씁시다.
"""

# 이건 코멘트입니다.
# 첫 파이썬 프로그램입니다.
# 특정 구문이 색상이 다르게 표현되기 때문에 함수와 문자열, 변수등을 쉽게 구분할 수 있습니다.
print('Hi world')

# 문자열 작성
# ' 작은 따옴표 ('), 큰 따옴표 (")를 이용하여 문자열을 표현 할 수 있습니다.

print('문자열 표현 - 작은 따옴표')
print("문자열 표현 - 큰 따옴표")
print("한줄로 작성하면서 이스케이프 코드를 넣어서\n 두줄로 출력할 수 있습니다.")
print("""혹은 여러줄을 작성하기 위해
따옴표를 3개씩 써서
여러줄로 표현 가능합니다.""")

print('작은 따옴표 안에서 큰 따옴표 (")를 쓰면 그대로 출력합니다.')
print("마찬가지로 큰 따옴표 안에서 작은 따옴표 (') 를 쓰면 그대로 출력합니다.")
print("아니면 이스케이프 코드 (\")를 통해 큰따옴표를 작성할수도 있습니다.")

print("그럼 슬래쉬 \ 를 쓰고 싶으면 어떻게 하나요?")


# 무엇이 더 좋을까요?
# 1번
print('한줄씩 써봅시다.')
print('두번째 내용은 둘번째 줄에 써봅시다.')
# 2번
print('한줄에 다 써봅시다. \n두번째 내용도 같은 줄에 써봅시다.')
# 3번
print('''한줄씩 또 써봅시다.
두번째 줄은 이렇게도 쓸 수 있죠.''')

print("그럼 화면에 \를 출력하기 위해선 어떻게 할까요?")
print("그리고 \news를 출력하고 싶다면..??")

