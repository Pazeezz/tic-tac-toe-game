def Xdwin(xwcount):
    x=str(xwcount)
    f=open("xwin.txt","w")
    f.write(x)
    f.close()
    f=open("xwin.txt","r")
    xwin=f.read()
    f.close()
    print("Player x wining :", xwin)
