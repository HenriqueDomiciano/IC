for i in range(1,101):
    a=(i%3==0)
    b=(i%5==0)
    if a and b:
        print('FizzBuzz')
        continue
    elif a:
        print('fizz')
        continue
    elif b:
        print('buzz')
        continue
    else:
        print(i)
