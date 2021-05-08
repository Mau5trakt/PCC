temp = 1001
for temp in range(0,1001,10): #The third value is the step (in this case
    conv = (temp -32)* 5/9    #this gonna be from 0 - 1000 in 10 in 10)

    print(temp, "ºF","------", conv, "ºC")