import boardList2
import aboutGame
import recordData.Xdata
import recordData.Odata
import recordData.Ddata
print(" Tic Tac Toe\n")


board1 = [1,2,3,4,5,6,7,8,9]
board3 = [0,0,0,0,0,0,0,0,0]
total_game_play=0
player_x_win=0
player_O_win=0
drawCount=0
numX=0    
numO=0

def show_board1():
    print  (board1[0]," || ",board1[1]," || ",board1[2]) 
    print  ("=======")
    print  (board1[3]," || ",board1[4]," || ",board1[5])
    print  ("=======")
    print  (board1[6]," || ",board1[7]," || ",board1[8])


def game():
    print("\n-----Starting New Game----- ")
    name1=input("Enter the player X name = ")
    name2=input("Enter the player O name = ")
    
    E=True
    Xdrow=False
    Odrow=False
    global numX
    numX=0
    global numO
    numO=0
    global player_x_win
    player_x_win=0
    global player_O_win
    player_O_win=0
    global drawCount
    drawCount=0
    
 #-- Start Game Again ----------------------
    while E:
        
        boardList2.show_board2()
        
        global total_game_play
        total_game_play+=1
        x=1    
        
   #-- Print board -----------------------------     
        
        while (x<10):
            X=True
            O=True             
            if x % 2==1:
                while X:
                  numX = int(input("Player 1 = "+name1+" Enter Number : "))
                  if numX >=1 and numX <=9:
#--Player-1-Check Repeat and Store in to LIst-----------------------------------
                    
                    
                         if (board3[numX-1]!=numX):
                              board3[numX-1]=numX
                              board1[numX-1]="X"
                              x+=1
                              X=False
                         else:
                             print("Invalide - Number Repeat ")
                             
                              
#----End ---------------------------------------
                  else:
                    print("Invalide - Number Repeat ")
            else:
                while O:
                  numO = int(input("Player 2 = "+name2+" Enter Number : "))

#---Player 2 --Check Repeat and Store in to LIst-----------------------------------
                  if numO>=1 and numO<=9:
                       if (board3[numO-1]!=numO):
                              board3[numO-1]=numO
                              board1[numO-1]="O"
                              x+=1
                              O=False
                       else:
                           print("Invalide - Number Repeat ")
                  else:
                       print("Invalide - Number Repeat ")
                             
#------end -------------------------------------
                      
            if (x>=3):
                
                if board1[0]==board1[1]==board1[2]=="X":
                    print(name1," WON !!!")
                    player_x_win+=1
                    x=11
                elif board1[3]==board1[4]==board1[5]=="X":
                    print(name1," WON !!!")
                    player_x_win+=1
                    x=11
                elif board1[6]==board1[7]==board1[8]=="X":
                    print(name1," WON !!!")
                    player_x_win+=1
                    x=11
                elif board1[0]==board1[3]==board1[6]=="X":
                    print(name1," WON !!!")
                    player_x_win+=1
                    x=11
                elif board1[1]==board1[4]==board1[7]=="X":
                    print(name1," WON !!!")
                    player_x_win+=1
                    x=11
                elif board1[2]==board1[5]==board1[8]=="X":
                    print(name1," WON !!!")
                    player_x_win+=1
                    x=11
                elif board1[0]==board1[4]==board1[8]=="X":
                    print(name1," WON !!!")
                    player_x_win+=1
                    x=11
                elif board1[2]==board1[4]==board1[6]=="X":
                    print(name1," WON !!!")
                    player_x_win+=1
                    x=11
                elif x==10:
                    Xdrow=True
                
            
            if (x>=4):
                if board1[0]==board1[1]==board1[2]=="O":
                    print(name2," WON !!!")
                    player_O_win+=1
                    x=11
                elif board1[3]==board1[4]==board1[5]=="O":
                    print(name2," WON !!!")
                    player_O_win+=1
                    x=11
                elif board1[6]==board1[7]==board1[8]=="O":
                    print(name2," WON !!!")
                    player_O_win+=1
                    x=11
                elif board1[0]==board1[3]==board1[6]=="O":
                    print(name2," WON !!!")
                    player_O_win+=1
                    x=11
                elif board1[1]==board1[4]==board1[7]=="O":
                    print(name2," WON !!!")
                    player_O_win+=1
                    x=11
                elif board1[2]==board1[5]==board1[8]=="O":
                    print(name2," WON !!!")
                    player_O_win+=1
                    x=11
                elif board1[0]==board1[4]==board1[8]=="O":
                    print(name2," WON !!!")
                    player_O_win+=1
                    x=11
                elif board1[2]==board1[4]==board1[6]=="O":
                    print(name2," WON !!!")
                    player_O_win+=1
                    x=11
                elif x==10:
                    Odrow=True
                    
            if Xdrow==True and Odrow== True:
                print(" Game Drow ")
                drawCount+=1
                Xdrow=False
                Odrow=False
            show_board1()
        
#-- Print board - END-----------------------------

        
        print("-----Game Over-----")
        run=input("Do you want to run this Game again ?(Yes/No) = ")
        if run=="Yes" or run=="YES" or run=="yes":
            E=True
            for i in range (0,9):
                board3[i]= 0
            for i in range (0,9):
                board1[i]= i+1
#-- Start Game Again - END ----------------------
                   
        else:
            E=False
            
        for i in range (0,9):
                board3[i]= 0
        for i in range (0,9):
                board1[i]= i+1
#---Call Mene -------------------------
    menu()
            

def menu():
    print(" MENU ")
    print("(1) How to Play Game ")
    print("(2) New Game ")
    print("(3) History of Game ")
    print("(4) Exite ")

    T=True
    while T:
        oparate=int(input("\nEnter the Number [ 1/2/3/4] = "))
        if oparate in [1,2,3,4]:

            if oparate==1:
                aboutGame.About_game()
            if oparate==2:
                game()
            if oparate==4:
                exit()
            if oparate==3:
                print("\nHistory of Game\n ")
                print("Total Game Play : ",total_game_play)
                recordData.Xdata.Xdwin(player_x_win)
                recordData.Odata.Odwin(player_O_win)
                recordData.Ddata.Draw(drawCount)
                
                
    
        else:
            print("Invalid Oparate - Number Repeat  ")
    return oparate
menu()
