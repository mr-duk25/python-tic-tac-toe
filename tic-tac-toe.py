# Sam Version

boardarray = [                   
              ["_","_","_"],     
              ["_","_","_"],
              ["_","_","_"]
              ]
# Create Renderboard fxn    
def renderboard(boardarray):     
    outerlength = len(boardarray) 
    for i in range(outerlength):
        innerlength = len(boardarray[i])
        for j in range(innerlength):
            print(boardarray[i][j], end="")  #print 
            if(j == 0 or j == 1):
               print("|", end="")
            if(j == 2):
               print(" ") 
            

PLAYER = ['X', 'O']
OFF_SWITCH = 1  #Flag; we want to set OFF_SWITCH to false or O





# Create PlayerMove fxn (indicate whether it's X or O)
def playermove(row,col):           
       #validate player move 
   if(row < 0 or row > 3 or col < 0 or col > 3):     
       print("Invalid move")
   boardarray[row][col] = PLAYER[0]      
    
    
def check_win_function(PLAYER, boardarray, row, col, OFF_SWITCH):
    
    if(boardarray[0][0] == 'X' and boardarray[0][1] == 'X' and boardarray[0][2] == 'X' ) or (boardarray[0][0] == 'O' and boardarray[0][1] == 'O' and boardarray[0][2] == 'O' ):
        print(f'tic-tac-toe top row! {PLAYER[1]} wins!')
        renderboard(boardarray)
        OFF_SWITCH = 0
        return OFF_SWITCH
    elif(boardarray[1][0] == 'X' and boardarray[1][1] == 'X' and boardarray[1][2] == 'X') or (boardarray[1][0] == 'O' and boardarray[1][1] == 'O' and boardarray[1][2] == 'O'):
        print(f'tic-tac-toe middle row! {PLAYER[1]} wins!')
        renderboard(boardarray)
        OFF_SWITCH = 0
        return OFF_SWITCH
    elif(boardarray[2][0] == 'X' and boardarray[2][1] == 'X' and boardarray[2][2] == 'X') or (boardarray[2][0] == 'O' and boardarray[2][1] == 'O' and boardarray[2][2] == 'O'):
        print(f'tic-tac-toe bottom row! {PLAYER[1]} wins!')
        renderboard(boardarray)
        OFF_SWITCH = 0
        return OFF_SWITCH
    elif(boardarray[0][0] == 'X' and boardarray[1][0] == 'X' and boardarray[2][0] == 'X') or (boardarray[0][0] == 'O' and boardarray[1][0] == 'O' and boardarray[2][0] == 'O'):
        print(f'tic-tac-toe left row! {PLAYER[1]} wins!')
        renderboard(boardarray)
        OFF_SWITCH = 0
        return OFF_SWITCH
    elif(boardarray[0][1] == 'X' and boardarray[1][1] == 'X' and boardarray[2][1] == 'X') or (boardarray[0][1] == 'O' and boardarray[1][1] == 'O' and boardarray[2][1] == 'O'):
        print(f'tic-tac-toe middle row! {PLAYER[1]} wins!')
        renderboard(boardarray)
        OFF_SWITCH = 0
        return OFF_SWITCH
    elif(boardarray[0][2] == 'X' and boardarray[1][2] == 'X' and boardarray[2][2] == 'X') or (boardarray[0][2] == 'O' and boardarray[1][2] == 'O' and boardarray[2][2] == 'O'):
        print(f'tic-tac-toe right row! {PLAYER[1]} wins!')
        renderboard(boardarray)
        OFF_SWITCH = 0
        return OFF_SWITCH
    elif(boardarray[0][0] == 'X' and boardarray[1][1] == 'X' and boardarray[2][2] == 'X') or (boardarray[0][0] == 'O' and boardarray[1][1] == 'O' and boardarray[2][2] == 'O'):
        print(f'tic-tac-toe diagonal left! {PLAYER[1]} wins!')
        renderboard(boardarray)
        OFF_SWITCH = 0
        return OFF_SWITCH
    elif(boardarray[0][2] == 'X' and boardarray[1][1] == 'X' and boardarray[2][0] == 'X') or (boardarray[0][2] == 'O' and boardarray[1][1] == 'O' and boardarray[2][0] == 'O'):
        print(f'tic-tac-toe diagonal right! {PLAYER[1]} wins!')
        renderboard(boardarray)
        OFF_SWITCH = 0
        return OFF_SWITCH
        
       

# game loop function
def game_loop():
   
    
    while OFF_SWITCH:  
        renderboard(boardarray)          
   #player prompt
        row,col = input(f"{PLAYER[0]} make move:").split()        # input/cleaning and player(user input) decisions using split method
        row = int(row)
        col = int(col)
        if(boardarray[row][col] == 'X' or boardarray[row][col] == 'O'):
            print('Invalid move: space already taken' )
            game_loop() 
        
        playermove(row,col)
        PLAYER.reverse() 
  
   #check win conditions
        pvar = check_win_function(PLAYER, boardarray, row, col,OFF_SWITCH)
        if(pvar == 0):
            break
       
game_loop()
      
