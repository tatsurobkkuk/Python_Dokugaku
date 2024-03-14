### 関数型プログラミング：グローバルステートに依存せず、その動作は関数に渡された引数によってのみ
### 変わる。
## 利点：グローバルステートによって生じるエラーを全て排除できること。
## 欠点：例えばユーザーインターフェースなどは扱い難い。
# 例
def increment(a):
    return a + 1

increment(3)
