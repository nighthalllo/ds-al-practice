# [BOJ]10564번: 팔굽혀펴기

[10564번: 팔굽혀펴기](https://www.acmicpc.net/problem/10564)

득점 할 때마다 현재 점수만큼 팔굽혀 펴기를 하고, 팔굽혀 펴기를 N번 한다고 했을 때 최대 점수가 되게 구하는 것이다. 처음에는 득점 경로 (ex, 2-3-7, 7-3-2)를 모두 계산해봐야 했는데 그렇게 하면 당연히 메모리가 터질 것 같다는 생각이 들었고, 또 생각해보면 결국 중요한거는 마지막에 그래서 팔굽혀 펴기를 N번 했는지? 그리고 득점 누적이 얼마인지만 알면 될 것 같았다. 결국 10점까지 가는데, 2점씩 5번해서 갔는지 5점씩 2번만에 갔는지는 중요하지 않다라는 이야기.

이러한 생각을 토대로 dp array의 x, y값을 다음과 같이 정의했다.

x = 팔굽혀 펴기의 총 횟수

y = 누적 횟수

최초의 정답 풀이

```python
import sys

def solution(last_, max_) :
    if last_ == N :
        dp[last_][max_] = max(dp[last_][max_], max_)
        return dp[last_][max_]

    if last_ > N :
        return 0

    if dp[last_][max_] != -1 :
        return dp[last_][max_]

    for score in scores :
        add_ = max_ + score
        dp[last_][max_] = max(dp[last_][max_], solution(last_ + add_, add_))
        
    return dp[last_][max_]

if __name__ == "__main__" :
    TC = int(sys.stdin.readline())

    for _ in range(TC) :
        global dp, N, M, scores
        N, M = map(int, sys.stdin.readline().split())
        scores = list(map(int, sys.stdin.readline().split()))

        dp = [[-1 for _ in range(451)] for _ in range(N + 1)]

        answer = solution(0, 0)

        print(max(dp[N]))
```

조금 더 memory에 접근을 덜 하는 풀이(큰 의미는 사실 없음)

```python
import sys

def solution(last_, max_) :
		# N번의 팔굽혀펴기를 했다면 지금까지의 득점 누적이 얼마인지 return
    if last_ == N :
        return max_

		# 점수가 넘어가면 이 길은 아니다. 라고 표시하기 위해 0
    if last_ > N :
        return 0

		# 이미 계산된 경로라면 계산된 값 사용
    if dp[last_][max_] != -1 :
        return dp[last_][max_]

		# 모든 득점 경우의 수에 대해 dp array를 채움
    for score in scores :
        add_ = max_ + score # 이번에 하게 될 푸쉬업의 횟수
        dp[last_][max_] = max(dp[last_][max_], solution(last_ + add_, add_))
        
    return dp[last_][max_]

if __name__ == "__main__" :
    TC = int(sys.stdin.readline())

    for _ in range(TC) :
        global dp, N, M, scores
        N, M = map(int, sys.stdin.readline().split())
        scores = list(map(int, sys.stdin.readline().split()))

        dp = [[-1 for _ in range(451)] for _ in range(N + 1)]

        answer = solution(0, 0)

        print(answer if answer > 0 else -1)
```