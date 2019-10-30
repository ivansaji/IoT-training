val = int(input("enter a number"))
f = open('count.txt','w')
for i in range(0,21):
    f.write(str(i) + " * " + str(val) +" =" + str(i*val) + "\n")
f.close()
