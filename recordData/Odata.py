def Odwin(owcount):
    o=str(owcount)
    f=open("Owin.txt","w")
    f.write(o)
    f.close()
    f=open("Owin.txt","r")
    owin=f.read()
    f.close()
    print("Player O wining :",owin)
