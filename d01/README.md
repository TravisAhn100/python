### Coding Practices - Day 1
@TravisAhn100
@anto5710

#### Python
* Python은 interpreter형 언어다: *한줄 한줄 내려가면서* 기계어로
  실시간 통역을 하는 언어.
  * <-> C/C++, Java 등은 compiler형 언어. 한번에 전체 코드를 기계어로 변환(compile).
  * 코드량이 많을 경우 interpreter형에 비해 compile하는덴 시간이 좀 더 걸려도
    프로그램 성능은 더 빠를 수 있음
* 메모리 등 내부 디테일은 Python이 알아서 관리

#### Primitive Data Types
기본 데이터 타입들. 어느 프로그래밍 언어든 공통 요소.
|       | 값     | 만드는 법 |  변환 |
| ----: |      :-----: | :----- | :--- |
| **Int 정수** | -2<sup>31</sup> ≤ `v` ≤ (2<sup>31</sup> - 1) | ```v = 31```<br> ```v = int(input())``` | ```v = int("문자열")``` |
| **Double 소수** | 아무 소수값[^dec]


[^dec]: 실제론 소수가 이진수로 저장되기 때문에 (1/2, 1/4, 1/8, ... 등이 합쳐진 형태로 저장됨) 계산할 수록 오류가 날 수 있다.

