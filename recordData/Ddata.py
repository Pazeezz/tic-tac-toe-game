def Draw(dcount):
    d=str(dcount)
    f=open("draw.txt","w")
    f.write(d)
    f.close()
    f=open("draw.txt","r")
    drawt=f.read()
    f.close()
    print("Game Draw times :",drawt)
