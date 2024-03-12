H, W, N = list(map(int, input().split()))
T_list = list(input())
S_list = [list(input()) for _ in range(H)]


def search(x, y, S, T):
    for t in T:
        if t == 'L':
            x -= 1
        elif t == 'R':
            x += 1
        elif t == 'U':
            y -= 1
        elif t == 'D':
            y += 1

        if S[y][x] == '#':
            return 0
    return 1


answer = 0
for y in range(H):
    for x in range(W):
        if S_list[y][x] == '.':
            answer += search(x, y, S_list, T_list)

print(answer)
