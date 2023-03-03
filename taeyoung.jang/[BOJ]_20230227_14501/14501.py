import sys

if __name__ == "__main__" :
    N = int(sys.stdin.readline())
    dp = [0 for _ in range(N)]
    tp = []
    for _ in range(N) :
        tp.append(list(map(int, sys.stdin.readline().split())))

    if tp[-1][0] == 1 :
        dp[-1] = tp[-1][1]

    for i in range(N-2, -1, -1) :
        if i + tp[i][0] <= N :
            dp[i] = tp[i][1]
            if i + tp[i][0] == N :
                dp[i] = max(dp[i + 1], dp[i])
            else :
                dp[i] = max(dp[i + 1], dp[i] + dp[i + tp[i][0]])
        else :
            dp[i] = dp[i + 1]

    print(dp[0])