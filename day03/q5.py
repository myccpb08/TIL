# 문제 5.
# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
# 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.

# 입력 예시: 300000;20000;10000


# map 이용
prices = input('물품 가격을 입력하세요: ')
a = prices.split(";")
prices = map(int,a)
price = list(prices)
price.sort()
print(price)

# map 안 쓴 거
prices = input('물품 가격을 입력하세요: ')
a = prices.split(";")
b = [int(i) for i in a]
b.sort()
print(b)