# √nまでのループにするパターン
# simple.py よりも計算量が減る

# 平方根を用いるためにmathモジュールが必要
import math

n = int(input())

if n <= 1:
    print("NO")

else:
    # nの平方根をint型に修正する必要あり
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            print("NO")
            break
        
    else:
        print("YES")
