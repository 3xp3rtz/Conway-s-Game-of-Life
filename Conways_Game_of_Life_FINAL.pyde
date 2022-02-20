                            
                    #Conway's Game of Life
                    
                    #Made by: 3xp3rtz
                    #Made in: Processing 3.5.4 (Python)
                    #Date: April 30th, 2021
                    
                    #Settings: Change speed in the code to whatever speed you would like
                            #The program will run at a certain number of frames per second
                            #Default is 50
                    
                    #Controls: Space to play, click a square to change it's state
                    
                    #Notes: 
                    # - I made this with edges, unlike the original

                    #SETTING UP

from copy import deepcopy
                #used to copy a 2D array later

Array = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
                #Example Array (changeable)
                
#Array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
                #Testing Array (Stable shapes, shapes with loops, etc.)

time = 0            #declaring the counter for whether to draw or not
bool = 1            #declaring the counter for setting the case
speed = 10          #declaring the speed at which to draw

                            #DRIVER CODE

def setup():        #starting the program
    
    size(1300,1300) #set size of display
    frameRate(speed);
    drawArray(Array)#draw first board
    
                            #ACTIVE CODE

def draw():         #to always run

    global time     #to keep
    global Array    #track of
    global case     #important
    global bool     #variables
        # <-  nice
    
    if mousePressed == True:
                    #if the mouse is pressed
                    
        mousePress()#check the case
        
        mX = mouseX/(height/len(Array[0]))
                    #mX is the column the square you're clicking on is in
                    #sets it by dividing the X coordinate of the mouse by the height of the squares,
                    #which is the height of the display divided by the number of columns in the array
        
        mY = mouseY/(width/len(Array))
                    #mY is the row the square you're clicking on is in
                    #sets it by dividing the Y coordinate of the mouse by the width of the squares,
                    #which is the width of the display divided by the numer of rows in the array
        
        Array[mY%len(Array)][mX%len(Array[0])] = case
                    #set the square you're mouse is on to 'case'
        
        drawArray(Array)
                    #draw the new array

    else:           #otherwise
        bool = 0    #change bool to 0 for the next time you need 'case'
    
    if time%2 == 1: #if the counter to draw is 1
        newArray(Array)
                    #make the new array
        drawArray(Array)
                    #and draw the new one

                            #KEY PRESSED

def keyReleased():  #used to check when a key is pressed
    global time
    if key == " ":  #if the spacebar is pressed
        time += 1   #change the counter by 1
    return

                            #MOUSE PRESSED

def mousePress():   #to set what the squares you change will be
                    #e.g. you press on a black square, you will light it up and anything you drag your mouse onto will also become lit
                    #and if you press on a white square, you will darken it and anything you drag your mouse onto will also become dark
    global case
    global Array
    global bool
    bool += 1       #keep track using a variable
    
    if bool == 1:   #if it's the first time clicking down, keep the value of the square you just clicked on
        
        if Array[mouseY/(width/len(Array))][mouseX/(height/len(Array[0]))] == 1:
                    #if the square you're clicking is lit
            
            case = 0#change the case to 0, meaning you turn any subsequent squares you click on OFF
        
        else:       #otherwise (the square is dark)
            case = 1#change the case to 1, meaning you turn any subsequent squares you click on ON

    return

                            #DRAWING THE ARRAY

def drawArray(grid):
    strokeWeight(0)         #no outline
    background(255,255,255) #white blank background

    for i in range(len(grid)):
                            #for each row
        
        for j in range(len(grid[0])):
                            #for each column
            
            if grid[i][j] == 0:     #if square is unlit
                fill(0,0,0)         #fill with black
            
            else:                   #else (if square is lit)
                fill(255,255,255)   #fill with white
            
            rect((((width/(len(grid)))*j) + 3), (((height/(len(grid[0])))*i) + 3), (((width/(len(grid)))-6)), (((height/(len(grid[0])))-6)))
                            #draw a grid with squares taking up the whole screen, using the height and width of the display and the size of the grid we declare
    return


                            #COMPUTING THE NEXT ARRAY

def newArray(grid):
    #computing the next state of the array

    new = deepcopy(grid)    #copy grid

    count = 0       #keep count of the number of 1s around grid[i][j]

    for i in range(len(grid)):
        #for each row
        
        for j in range(len(grid[0])):
            #for each column
            
            if j == 0:
                                #if along the left edge
                if i == 0:
                                    #if top left
                                    
                    if grid[i][j+1] == 1:
                        count += 1
                                    #if the square right of the cell is on then add 1 to count
                    if grid[i+1][j] == 1:
                        count += 1
                                    #if the square under the cell is on then add 1 to count
                    if grid[i+1][j+1] == 1:
                        count += 1
                                    #if the square to the bottom right is on then add 1 to count
                                    
                                    # + - -
                                    # | X 0
                                    # | 0 0
            
                elif i == len(grid)-1:
                                    #if bottom left
                                    
                    if grid[i][j+1] == 1:
                        count += 1
                                    #if the square right of the cell is on then add 1 to count
                    if grid[i-1][j] == 1:
                        count += 1
                                    #if the square above the cell is on then add 1 to count
                    if grid[i-1][j+1] == 1:
                        count += 1
                                    #if the square to the top right is on then add 1 to count
                        
                                    # | 0 0 
                                    # | X 0 
                                    # + - -
            
                else:
                                    #along left edge
                                    
                    if grid[i-1][j] == 1:
                        count += 1
                                    #if the square above the cell is on then add 1 to count
                    if grid[i-1][j+1] == 1:
                        count += 1
                                    #if the square to the top right is on then add 1 to count
                    if grid[i][j+1] == 1:
                        count += 1
                                    #if the square right of the cell is on then add 1 to count
                    if grid[i+1][j] == 1:
                        count += 1
                                    #if the square under the cell is on then add 1 to count
                    if grid[i+1][j+1] == 1:
                        count += 1
                                    #if the square to the bottom right is on then add 1 to count
            
                                    # | 0 0
                                    # | X 0
                                    # | 0 0
        
            elif j == len(grid[0])-1:
                                #if along the right edge
                if i == 0:
                                    #if top right
                                    
                    if grid[i][j-1] == 1:
                        count += 1
                                    #if the square left of the cell is on then add 1 to count
                    if grid[i+1][j] == 1:
                        count += 1
                                    #if the square under the cell is on then add 1 to count
                    if grid[i+1][j-1] == 1:
                        count += 1
                                    #if the square to the bottom left is on then add 1 to count
                                    
                                    # - - +
                                    # 0 X |
                                    # 0 0 |
            
                elif i == len(grid)-1:
                                    #if bottom right
                                    
                    if grid[i][j-1] == 1:
                        count += 1
                                    #if the square left of the cell is on then add 1 to count
                    if grid[i-1][j] == 1:
                        count += 1
                                    #if the square above the cell is on then add 1 to count
                    if grid[i-1][j-1] == 1:
                        count += 1
                                    #if the square to the top left is on then add 1 to count
                                    
                                    # 0 0 |
                                    # 0 X |
                                    # - - +
            
                else:
                                    #along right edge
                                    
                    if grid[i-1][j] == 1:
                        count += 1
                                    #if the square above the cell is on then add 1 to count
                    if grid[i-1][j-1] == 1:
                        count += 1
                                    #if the square to the top left is on then add 1 to count
                    if grid[i][j-1] == 1:
                        count += 1
                                    #if the square left of the cell is on then add 1 to count
                    if grid[i+1][j] == 1:
                        count += 1
                                    #if the square under the cell is on then add 1 to count
                    if grid[i+1][j-1] == 1:
                        count += 1
                                    #if the square to the bottom left is on then add 1 to count
            
                                    # 0 0 |
                                    # 0 X |
                                    # 0 0 |
            
            else:
                                    #not along left/right edges
                if i == 0:
                                    #if along top edge
                                    
                    if grid[i][j-1] == 1:
                        count += 1
                                    #if the square left of the cell is on then add 1 to count
                    if grid[i][j+1] == 1:
                        count += 1
                                    #if the square right of the cell is on then add 1 to count
                    if grid[i+1][j-1] == 1:
                        count += 1
                                    #if the square to the bottom left is on then add 1 to count
                    if grid[i+1][j] == 1:
                        count += 1
                                    #if the square under the cell is on then add 1 to count
                    if grid[i+1][j+1] == 1:
                        count += 1
                                    #if the square to the bottom right is on then add 1 to count
                    
                                    # - - -
                                    # 0 X 0
                                    # 0 0 0
            
                elif i == len(grid)-1:
                                    #if along bottom edge
                                    
                    if grid[i-1][j-1] == 1:
                        count += 1
                                    #if the square to the top left is on then add 1 to count
                    if grid[i-1][j] == 1:
                        count += 1
                                    #if the square above the cell is on then add 1 to count
                    if grid[i-1][j+1] == 1:
                        count += 1
                                    #if the square to the top right is on then add 1 to count
                    if grid[i][j-1] == 1:
                        count += 1
                                    #if the square left of the cell is on then add 1 to count
                    if grid[i][j+1] == 1:
                        count += 1
                                    #if the square right of the cell is on then add 1 to count
                        
                                    # 0 0 0
                                    # 0 X 0
                                    # - - -
                                    
                else:
                                    #if in middle
                    if grid[i-1][j-1] == 1:
                        count += 1
                                    #if the square to the top left is on then add 1 to count
                    if grid[i][j-1] == 1:
                        count += 1
                                    #if the square left of the cell is on then add 1 to count
                    if grid[i+1][j-1] == 1:
                        count += 1
                                    #if the square to the bottom left is on then add 1 to count
                    if grid[i-1][j] == 1:
                        count += 1
                                    #if the square above the cell is on then add 1 to count
                    if grid[i+1][j] == 1:
                        count += 1
                                    #if the square under the cell is on then add 1 to count
                    if grid[i-1][j+1] == 1:
                        count += 1
                                    #if the square to the top right is on then add 1 to count
                    if grid[i][j+1] == 1:
                        count += 1
                                    #if the square right of the cell is on then add 1 to count
                    if grid[i+1][j+1] == 1:
                        count += 1
                                    #if the square to the bottom right is on then add 1 to count
                                    
                                    # 0 0 0
                                    # 0 X 0
                                    # 0 0 0
        
        
            if grid[i][j] == 0:
                    #if the current cell is off
                
                if count == 3:
                    new[i][j] = 1
                    #if the number of lit squares around is equal to 3 then it lights up
                
                else:
                    new[i][j] = 0
                    #otherwise it stays off
            
            else:   #otherwise (if the current cell is on)
    
                if count > 1 and count < 4:
                    new[i][j] = 1
                    #if the lit cell has 2 or 3 other lit squares around it it will stay lit
                
                else:
                    new[i][j] = 0
                    #otherwise it dies and turns off
            
            count = 0
                    #reset count for next cell
    global Array
    Array = new
                    #set Array to the result
    return Array
                    #return the result
