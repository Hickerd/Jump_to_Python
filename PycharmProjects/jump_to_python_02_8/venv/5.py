a=[1,2,3]
b=a[:]
a[1]=4 # a=[1,4,3]
print(b)

'''
print(b)의 결과는 [1,2,3]이다. 4번에서 설명한 바와 동일하다.
a와 b는 다른 공간에 저장된 변수이므로 관련이 없다.
a의 값을 변경하면 a의 값이 변경된 것이지 b에는 아무 영향을 끼치지 않는다.
'''