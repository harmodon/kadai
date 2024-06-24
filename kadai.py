def main():
    number_1 = int(input("1つ目の自然数を入力してください: "))
    number_2 = int(input("2つ目の自然数を入力してください: "))  
    sum = number_1 + number_2
    diff = number_1 - number_2
    prod = number_1 * number_2
    div = number_1 / number_2
    print(f'2つの自然数の合計は {sum}')
    print(f'1つめの自然数から2つ目の自然数を引くと {diff}')
    print(f'2つの自然数の積は {prod}')
    print(f'1つ目の自然数を2つ目の自然数で割ると {div}')


if __name__=='__main__':
    main()