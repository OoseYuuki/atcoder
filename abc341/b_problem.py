N = int(input())
A_list = list(map(int, input().split()))

S_T_list = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N-1):
    if S_T_list[i][0] == 0:
        C = 1
    else:
        C = A_list[i] // S_T_list[i][0]
    A_list[i] -= C * S_T_list[i][0]
    A_list[i + 1] += C * S_T_list[i][1]

print(A_list[-1])
