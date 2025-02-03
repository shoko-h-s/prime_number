# √nまでのループにするパターン
# simple.py よりも計算量が減る

# 平方根を用いるためにmathモジュールが必要
import math

n = int(input("素数判定を行う数を入力："))

# 1以下の整数は、素数ではない
if n <= 1:
    print(f"{n}は素数ではありません")

# 2は素数、それ以外の偶数は素数ではない
elif n == 2:
    print(f"{n}は素数です")
elif n % 2 == 0:
    print(f"{n}は素数ではありません")

# 3以降の奇数のみを調べれば良い
else:
    # nの平方根をint型に修正する必要あり
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            print(f"{n}は素数ではありません")
            break
        
    else:
        print(f"{n}は素数です")
