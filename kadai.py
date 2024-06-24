def main():
    number_1 = int(input("1つ目の自然数を入力してください: "))
    number_2 = int(input("2つ目の自然数を入力してください: "))  
    sum = number_1 + number_2
    diff_1 = number_1 - number_2
    print(f'自然数の合計は {sum}')
    print(f'1つめの自然数から2つ目の自然数を引くと {diff_1}')

if __name__=='__main__':
    main()