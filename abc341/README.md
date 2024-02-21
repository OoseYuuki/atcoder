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
