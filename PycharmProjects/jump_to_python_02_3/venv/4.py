a=[1,2,3]
a.append([4,5])
b=[1,2,3]
b.extend([4,5])
print(f'append >> {a}, extend >> {b}')

# append는 인자가 list일 때, 인자를 그대로 list에 추가하고 extend의 경우에는, list의 + 연산과 결과가 같다.
# append는 하나의 값을 추가하는 함수이며, extend는 기존 리스트에 입력받은 리스트를 더하는 함수이기에 차이가 있다.