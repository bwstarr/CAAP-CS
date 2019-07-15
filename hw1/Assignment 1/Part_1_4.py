def slope():
    itr=eval(input("Enter the amount of nums to be summed"))
    ans=0
    for num in range(itr):
        ans=ans+eval(input("Enter a number"))
    print(ans);
    
slope()