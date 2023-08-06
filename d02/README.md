### Coding Practices - Day 2
@TravisAhn100
@anto5710

#### Today's Goals
* Projer Euler - Problem 1 숙제 리뷰
  * Edge Case에 대하여
* 스트링 리뷰 - 카이사르 암호 상위호환, 1:1대응 암호 변환기 만들기
* 반복문 사용하여 간단한 주크박스 만들기

#### Project Euler - Problem 1

> If we list all the natural numbers below $10$ that are multiples of $3$ or $5$
> , we get $3, 5, 6$ and $9$. The sum of these multiples is $23$. Find the sum
> of all the multiples of $3$ or $5$ below $1000$.

##### Student's Response
```python
x=[]
for i in range(0,1000):
    if i%3==0:
        x+=[i]
    if i%5==0:
        x+=[i]
    if i%3==0 and i%5==0:
        x.pop()
print(sum(x))
```
##### Problem 1 - Edge Case
만약 현재 숫자(`i`)가 $3$과 $5$의 공배수일 경우, 위 코드 상에선 `i`가 정답 리스트에
두 번 (중복되어) 추가돼버린다. 이를 만회하기 위해, 공배수의 경우 `i`를 다시 한 번
빼주는 해결책을 추가했다.

#### What is an Edge Case?
**Edge Case:** 프로그램 작성 시 버그는 필연적으로 발생한다.
그 중에서도 예외적인 값 (엄청 크거나, 음수이거나, 0이거나)
버그가 발생하기 쉬운 부분이 흔히 있는데 이를 Edge Case라고 한다.

* 알고리즘을 짜기 전, 가능한 입력의 *종류*를 생각해보자. 예를 들어, 입력이
  숫자일 경우, $0$, 양수, 음수 등이 있고, 리스트일 경우 빈 리스트, 한 개짜리 리스트
  (singleton list), 2개 이상 리스트로 크게 나눌 수 있다.
* 알고리즘을 대강 구상하였다면, 간단한 입력으로 (머릿속이나 종이에 그려가며)
 시뮬레이션을 해 본 뒤, 바로 *Edge Case*, 예외의 경우를 생각해 봐야 한다!!!

대표적으로:
##### Example 1 - Out of Index Range
```python
list = [0, 1, 2, 3]
for i in range(0, 5):
        print(list[i]) ## 오류 발생! 인덱스가 0 ~ 3까지 가야하는데, 4가 포함돼버렸다
```
리스트 등 '인덱스,' 즉 숫자 위치로 값을 찾아오는 식의 자료구조는 인덱스 끝값을
조심해야 한다. 프로그래밍에서 $n$칸 짜리 리스트를 찾아볼 때, 인덱스는 $0$에서
$\textbf{n - 1}$까지 이므로, $n$까지 가면 한 칸밖으로 나가 버리게 된다!

##### Example 2 - Zero Division
프로그래밍에선, 애매한 것을 최대한 배제하려하므로, '$0$으로 나누기' 같은 애매한
연산은 아예 *금지*시켜 버린다.
```python
print(0 / 0) ### Division by Zero는 금지돼었다 뜨며 프로그램이 튕긴다
```
따라서, 사측연산 프로그램 등의 경우, 항상 *분모* (denominator)가 0이 되는 경우가
있는지 확인 할 것. **베스트 전략은 프로그램이 최대한 안 튕기도록 자연스레 넘어갈 수
있도록 해주는 것이다.**
* 예를 들어, `if` 조건으로 감싸, 분모가 $0$일 경우 아무것도
   안 하고 스킵해버리는 수가 있다.

#### In-Class Work: Caesar Cipher++
##### Caesar Cipher
카이사르 암호(Caesar Cipher)는 가장 널리 알려진 암호화 방식 중 하나로,
텍스트에서 알파벳 `'a'` ~ `'z'`를 각각 n칸 뒤의 알파벳으로 바꾸어 암호화한다.
여기서 $n$ ($0 \leq |n| < 26$)이 곧 암호화 키가 된다.

| From  | a | b | c | d | e |... | z |
| ---- | -- | --| --| --| --|---| -- |
| To    | `x` | `y` | `z` | `a` | `b` |... | `w` |

* `'a'`(0번째 알파벳)을 `'x'`(23번째 알파벳)으로 바꾼다. 즉 $n=23$칸 만큼 오른쪽으로
  알파벳표를 민 것이다.
* `'z'` (25번째 알파벳)의 경우 $23$칸 오른쪽으로 돌리면 $25+23=48$로 알파벳 범위를 넘어가므로
  $26$을 빼주면, 한 바퀴 돌아 $22$(`'w'`)가 된다.


##### Caesar Cipher++
위 방식의 상위 호환인, 카이사르 암호 2.0을 만들어 보자.


