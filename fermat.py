# フェルマーテスト（参考）

import random

n = int(input("素数判定を行う数を入力："))

a = random.randint(2, n-1)
fermat = 1

if n % a == 0:
    print(f"{n}は素数ではありません")
    
else:
    for _ in range(n-1):
        fermat *= a
        fermat %= n
        
    if fermat == 1:
        print(f"{n}は素数です")
        
    else:
        print(f"{n}は素数ではありません")
