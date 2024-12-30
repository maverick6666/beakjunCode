
while True:
    try:
        a,b = map(int,input().split())
        print (int(a + b))
    except EOFError:
        break