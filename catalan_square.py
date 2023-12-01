import sys

n = int(sys.stdin.readline())
c = [1 for i in range(n + 2)]

for k in range(2, n + 2):
    # 2*k because its pairs of people
    # *2 because the sum mirrors
    c[k] = c[k - 1] * (2 * k - 1) * 2 / (k + 1)

    # calclculates the catalan number for n+1
    print(int(c[n + 1]))