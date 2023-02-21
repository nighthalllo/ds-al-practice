import sys

def sol(x, y) :
    if dp[x][y] != -1 :
        return dp[x][y]
    
    list_ = [[x, a, a+1, y] for a in range(x, y)] # ��� �Ʒ��� ��� ���Ǹ� ���ؼ� 
    value_ = [sol(a, b) + sol(c, d) for a, b, c, d in list_] # ��ȭ�� �󿡼� ���� �� �ִ� ����� ��
    dp[x][y] = min(value_) + sum([input_[i] for i in range(x, y + 1)]) # ��ü ����� ���� �ּ� + ����

    return dp[x][y]
    
if __name__ == "__main__" :
    T = int(input())

    global input_, dp # �Լ��� �ѱ�� �����Ƽ� �׳� global��

    for _ in range(T) :
        K = int(input())
        input_ = [0] + list(map(int, sys.stdin.readline().rstrip().split())) # index�� 1���� ���� ���ؼ�

        dp = [[-1 for _ in range(K + 1)] for _ in range(K + 1)] # �� -1�� �ʱ�ȭ, -1�� ���� ���� ���ٴ� ��

        for i in range(1, K + 1) :
            dp[i][i] = 0 # �ϳ��� �ִ� ���� ����ġ�ϱ�

        print(sol(1, K))