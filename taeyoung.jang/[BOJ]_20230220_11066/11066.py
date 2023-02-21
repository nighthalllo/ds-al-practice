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

        for i in range(1, K + 1) :
            dp[i][i] = 0 # 하나만 있는 경우는 안합치니까

        print(sol(1, K))