import sys

def solution(last_, max_) :
    if last_ == N :
        return max_

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

        dp = [[-1 for _ in range(101)] for _ in range(N + 1)]

        answer = solution(0, 0)

        print(answer if answer > 0 else -1)