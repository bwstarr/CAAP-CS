def fib():
    num=eval(input("Enter the index of the Fibonacci Term desired"))
    n,m=1,1
    ans=0;
    if num <= 2:
        print(n)
    for ind in range(num-2):
        ans=n+m
        n=m
        m=ans
    print(ans)
    
fib()
        