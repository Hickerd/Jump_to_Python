a="Life is too short, you need python"
if "wife" in a:
    print("wife")
elif "python" in a and 'you' not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

'''
출력결과는 shirt. elif "shirt" not in a 에서 shirt가 없기 때문에 이 문장이 실행된다.
'''