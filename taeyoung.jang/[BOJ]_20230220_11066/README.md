# [BOJ]11066번: 파일 합치기

[11066번: 파일 합치기](https://www.acmicpc.net/problem/11066)

문제의 조건이 두 파일을 계속 합쳐서 최종적으로 하나의 파일을 만드는 것이므로, 반대로 생각하면 최종결과물은 두 개의 파일로 만들어진다. 그렇다면, 두 개의 파일을 어떻게 선택하더라도 최종결과물을 만드는데 드는 비용은 다 같고(input의 총합이므로), 그 이전의 결과들이 최솟값이면 전체로 봐도 최소가 될 수 있다.

이 로직을 점화식으로 세우면 다음과 같다.

DP[i][k]의 값을 i ~ k의 파일을 합치는데 드는 비용의 최소값이라고 정의하자.

예를 들어, 입력이 [40, 30, 30, 50]이고, DP[1][3]이라고 하면 1번, 2번, 3번 (40, 30, 30)을 합쳤을 때의 최소값을 의미하며, 이 값은 100이 될 것이다.

$DP[i][k] = Min(DP[i][i] + DP[i+1][k], DP[i][i+1] + DP[i+2][k], … , DP[i][k-1] + DP[k][k]) + Sum(Input[i] + Input[i+1] + … + Input[k])$


이 점화식을 바탕으로, 문제의 답을 구하기 위해선 DP[1][K]를 구하면 되고, Top-Down 방식으로 로직을 설계하면 된다.

```python
import sys

def sol(x, y) :
    if dp[x][y] != -1 :
        return dp[x][y]
    
    list_ = [[x, a, a+1, y] for a in range(x, y)] # 얘는 아래의 계산 편의를 위해서 
    value_ = [sol(a, b) + sol(c, d) for a, b, c, d in list_] # 점화식 상에서 나올 수 있는 경우의 수
    dp[x][y] = min(value_) + sum([input_[i] for i in range(x, y + 1)]) # 전체 경우의 수의 최소 + 원가

    return dp[x][y]
    
if __name__ == "__main__" :
    T = int(input())

    global input_, dp # 함수에 넘기기 귀찮아서 그냥 global로

    for _ in range(T) :
        K = int(input())
        input_ = [0] + list(map(int, sys.stdin.readline().rstrip().split())) # index를 1부터 쓰기 위해서

        dp = [[-1 for _ in range(K + 1)] for _ in range(K + 1)] # 다 -1로 초기화, -1은 아직 값이 없다는 뜻
																																# input이 다 양의 정수니깐
        for i in range(1, K + 1) :
            dp[i][i] = 0 # 하나만 있는 경우는 안합치니까 0으로

        print(sol(1, K))
```
