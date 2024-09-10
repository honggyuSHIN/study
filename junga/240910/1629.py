a, b, c = map(int, input().split())

'''
[수학, 분할정복]
1. 거듭제곱 분할정복해 계산하기 : a를 b번 거듭제곱하는 시간복잡도 줄이기!
    1.1. ex. 2^32 = (2^16)^2 = ((2^8)^2)^2 = (((2^4)^2)^2)^2 = ((((2^2)^2)^2)^2)^2
        계산  32번    17번        10번          7번                5번
2. 모들러 연산(나머지 분배 법칙) 활용 : (X*Y)%Z = (X%Z * Y%Z) % Z
==> 거듭제곱을 분할정복해가면서, 모들러 연산을 활용해 재귀 계산
'''


def divide_conquer(a, b, c): # a : 거듭제곱할 수, b : 거듭제곱할 횟수, c : 계산된 값을 나눠 나머지를 구할 수
    if b == 1: # 거듭제곱을 한 번만 해도 될 만큼 나눴으면
        return a % c # = (a ** 1) % c 를 리턴
    
    x = divide_conquer(a, b//2, c) # 거듭제곱을 2번 이상 해야 하면 거듭제곱 횟수//2 해서 분할정복
    # x : a ** b//2 % c
    
    if b % 2 == 0: # 거듭제곱할 횟수가 짝수이면
        return x ** 2 % c # = ((a ** b//2 % c) ** 2) % c
                          # = ((a ** b//2 % c) * (a ** b//2 % c)) % c
                          # = (a ** b) % c
    else: # 거듭제곱할 횟수가 홀수이면 == b//2 * 2 = b-1이면
        return a * x ** 2 % c # = (a * (a ** b//2 % c) ** 2) % c
                              # = (a * (a ** b//2 % c) * (a ** b//2 % c)) % c
                              # = (a * (a ** (b-1))) % c
                              # = (a ** b) % c

print(divide_conquer(a, b, c)) 