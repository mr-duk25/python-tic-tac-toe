# Sam Version

# Create board array
# Variable assignment without types 

boardarray = [                    #Created and assigned 2-D Array
              ["_","_","_"],      # (lines 3-7 Array init with string literals)
              ["_","_","_"],
              ["_","_","_"]
              ]
# Create Renderboard fxn     (   renderboard('X')  )
def renderboard(boardarray):      # fxn def with one parameter
    # Can be modified to exactly how we want
    outerlength = len(boardarray) #len(boardarray) = 9

    #Problem 1: how to print without a new line
    #Prob 2: how to print create a new line everytime you hit the end of a row (check row variable, see last time when it's going to access the row OR
    # )
    for i in range(outerlength):
        innerlength = len(boardarray[i])
        for j in range(innerlength):
            print(boardarray[i][j], end="")  #print 
            if(j == 0 or j == 1):
               print("|", end="")
            if(j == 2):
               print(" ")  # print a new line
            
    # Another way of doing the top for nested loop () CANNOT be modified -> Assumes to go to full size of object
    # for i in boardarray:
    #     for j in boardarray[i]:
    
    # for(let i = 0; i < boardarray.length; i++)         #this iterates thru the columns
    #   for(let j = 0; j < boardarray[i].length;j++)    #this iterates thru the rows
       
            
            
            
    # print(f'{boardarray[0][0]}|{boardarray[0][1]}|{boardarray[0][2]}')    # Logging printing with f-string type (Dereferencing/Accessing 2-d array values instead of string literals)
    # print(f'{boardarray[1][0]}|{boardarray[1][1]}|{boardarray[1][2]}')
    # print(f'{boardarray[2][0]}|{boardarray[2][1]}|{boardarray[2][2]}')

PLAYER = ['X', 'O']
OFF_SWITCH = 1  #Flag; we want to set OFF_SWITCH to false or O





# Create PlayerMove fxn (indicate whether it's X or O)
def playermove(row,col):             # fxn def with multiple parameters
       #validate player move 
   if(row < 0 or row > 3 or col < 0 or col > 3):     
       print("Invalid move")
   boardarray[row][col] = PLAYER[0]       # 2D array s[ecific indices assignment]
    
    
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
        
       
        

        
       



# Create Player    
# Single responsibility principle (watch video on it) 
#-> Classes fxns variables etc. in programming (building blocks of programming that we define) even if they dont exist in a class should only


# game loop function
def game_loop():
   
    
    while OFF_SWITCH:  
       
        #Infinite while loop implementation
        #render board
        renderboard(boardarray)          
   #player prompt
        
        row,col = input(f"{PLAYER[0]} make move:").split()        # input/cleaning and player(user input) decisions using split method
        row = int(row)
        col = int(col)
        if(boardarray[row][col] == 'X' or boardarray[row][col] == 'O'):
            print('Invalid move: space already taken' )
            game_loop() # using a form of recursion, loops back to top of function
        
        
   #add player move to board
        playermove(row,col)
    #   renderboard(boardarray)
        PLAYER.reverse() # The reverse() method reverses the elements of the list.
  
   #check win conditions
        pvar = check_win_function(PLAYER, boardarray, row, col,OFF_SWITCH)
        # paolo = check_win_function(PLAYER, boardarray, row, col,OFF_SWITCH)
      
        if(pvar == 0):
            break

game_loop()