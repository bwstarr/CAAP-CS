def change():
    print("Hello! I will tell you the least amount of cranks neccesary to dish out change. All I need YOU to do is enter the amount of each coin you have on hand")
    cn1_amo=eval((input("Coin 1 amount you have")))
    cn2_amo=eval((input("Coin 5 amount you have")))
    cn3_amo=eval((input("Coin 10 amount you have")))
    cn4_amo=eval((input("Coin 25 amount you have")))
    chng=eval((input("Change due to customer")))
    chng=chng*100
    num=0
    while chng>0:
        if chng>=25 and cn4_amo>0:
            cn4_amo=cn4_amo-1
            chng=chng-25
            num=num+1
        elif chng>=10 and cn3_amo>0:
            cn3_amo=cn3_amo-1
            chng=chng-10
            num=num+1
        elif chng>=5 and cn2_amo>0:
            cn2_amo=cn2_amo-1
            chng=chng-5
            num=num+1
        elif chng>=1 and cn1_amo>0:
            cn1_amo=cn1_amo-1
            chng=chng-1
            num=num+1
        else:
            print("Not enough Coins")
            chng=0
            num=0
            
    
    print("Cranks",num)
    print("Pennies Leftover:" ,cn1_amo)
    print("Nickels Leftover:" ,cn2_amo)
    print("Dimes Leftover:" ,cn3_amo)
    print("Quarters Leftover:" ,cn4_amo)
    
    
change()