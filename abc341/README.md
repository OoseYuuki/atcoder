## ABC341問題の練習

### A問題(`print 341`)
- 問題
[![Image from Gyazo](https://i.gyazo.com/445847e35c6c85c3bd90e6f672b32f4e.png)](https://gyazo.com/445847e35c6c85c3bd90e6f672b32f4e)

文字列`01`をN回繋げて最後に`1`を追加するというロジックで`AC`だった。

```python
N = int(input())
char = '10' * N + '1'
print(char)
```
### B問題（`Foreign Exchange`）
- 問題
[![Image from Gyazo](https://i.gyazo.com/73066ff57b6528cd842b90ea32d15a02.png)](https://gyazo.com/73066ff57b6528cd842b90ea32d15a02)


愚直に全パターン検証するとTLEになるので、計算量を抑える工夫が必要。<br />
ループを回すのではなく、取引できる回数を算出して一気に差し替えている。

```python
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
```