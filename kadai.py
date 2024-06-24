import math as mt

def main(): 
    num1 = int(input("1つ目の自然数を入力してください: "))
    num2 = int(input("2つ目の自然数を入力してください: "))  

    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    div = num1 / num2
    print(f'2つの自然数の合計は {sum}')
    print(f'1つめの自然数から2つ目の自然数を引くと {diff}')
    print(f'2つの自然数の積は {prod}')
    print(f'1つ目の自然数を2つ目の自然数で割ると {div}')

    gcd = mt.gcd(num1, num2)
    lcm = int(prod / mt.gcd(num1, num2))
    print(f'2つの自然数の最大公約数は {gcd}')
    print(f'2つの自然数の最小公倍数は {lcm}')

    GP_sum = int(sum * (abs(diff) + 1) / 2)
    print(f'小さい方の自然数から大きい方の自然数までのすべての自然数の和は {GP_sum}')

    count = 0
    for n in range(min(num1, num2), max(num1, num2) + 1):
        if n != 1:
            count += 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    count -= 1
                    break
                

    print(f'小さい方の自然数から大きい方の自然数までに存在する素数の個数は {count}')

if __name__=='__main__':
    main()