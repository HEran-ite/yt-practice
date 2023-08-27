def watermelon():
    w=input('input:' )
    for w in range(1,100):
        if w==2:return False
        elif (w-2)%2==0:return True
        else:return False
    return watermelon(w-2)
print(watermelon())   