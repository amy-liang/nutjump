###################################################################################

###   ### ###    ### ###########    ########### ###    ### ####       #### ####### 
#  #  # # # #    # # #         #    #         # # #    # # #   #     #   # #      #
#   # # # # #    # # ##### #####    ##### ##### # #    # # # #  #   #  # # #  ###  #
# #  ## # # #    # #     # #            # #     # #    # # # ##  # #  ## # #      #
# ##  # # # #    # #     # #            # #     # #    # # # # #  #  # # # # #####
# # #   # # ###### #     # #       ###  # #     # ###### # # #  #   #  # # # #
# #  #  # #        #     # #       # ###  #     #        # # #   ###   # # # #
###   ###  ########      ###        #######      ########  ###         ### ### 

########################################################################  By Amy L. 

from tkinter import *
from time import *
from random import *
from math import *

root = Tk()
s = Canvas(root, width=600,height=700, background="#98cffe")
s.pack()


#=============== SETTING UP ===============#
def importImages():
    global brownNut, greenNut, yellowNut, bronzeNut, silverNut, goldNut, flamingNut, rainbowNut, creepyNut, happyNut, pinkNut, timeNut
    global squirrelR, squirrelL, squirrelAir, sadEnding, goodEnding, greatEnding, startScreen, instructionScreen
    
    #Import nut images
    brownNut = PhotoImage(file="img/brown.gif")
    greenNut = PhotoImage(file="img/green.gif")
    yellowNut = PhotoImage(file="img/yellow.gif")
    bronzeNut = PhotoImage(file="img/bronze.gif")
    silverNut = PhotoImage(file="img/silver.gif")
    goldNut = PhotoImage(file="img/gold.gif")
    flamingNut = PhotoImage(file="img/flaming.gif")
    rainbowNut = PhotoImage(file="img/rainbow.gif")
    creepyNut = PhotoImage(file="img/creepy.gif")
    happyNut = PhotoImage(file="img/happy.gif")
    pinkNut = PhotoImage(file="img/pink.gif")
    timeNut = PhotoImage(file="img/time.gif")

    #Import squirrel images
    squirrelR = PhotoImage(file="img/squirrelRight.gif")
    squirrelL = PhotoImage(file="img/squirrelLeft.gif")
    squirrelAir = PhotoImage(file="img/squirrelair.gif")

    #Start & End screen images
    startScreen = PhotoImage(file="img/startScreen.gif")
    instructionScreen = PhotoImage(file="img/instructions.gif")
    sadEnding = PhotoImage(file="img/sadEnd.gif")
    goodEnding = PhotoImage(file="img/goodEnd.gif")
    greatEnding = PhotoImage(file="img/greatEnd.gif")
    

def startingValues():
    global score, gameTime, timeBonus, popUpText, popUpTimes
    global nuts, nutSpeeds, xPos, yPos, nutType
    global xSpeed, ySpeed, xSquirrelA, ySquirrelA, xSquirrelB, ySquirrelB, moveSpeed, jumpSpeed
    global squirrelSelect, squirrelPicA, squirrelPicB, falling, jumping, directionA, directionB

    #General game variables
    score = 0
    gameTime = 60
    timeBonus = 0
    popUpText = []
    popUpTimes = []

    #Nut arrays
    nuts = []
    nutSpeeds = []
    xPos = []
    yPos = []
    nutType = []

    #Main squirrel variables
    xSpeed = 0
    ySpeed = 0
    xSquirrelA = 100
    ySquirrelA = 110
    xSquirrelB = 500
    ySquirrelB = 560
    moveSpeed = 5.5
    jumpSpeed = 4.5

    #Secondary squirrel variables
    squirrelSelect = "A"
    squirrelPicA = squirrelR
    squirrelPicB = squirrelL
    falling = False
    jumping = False
    directionA = "R"
    directionB = "L"

    
def keyDownHandler( event ):
    global xSpeed, ySpeed, moveSpeed, jumpSpeed, falling, jumping

    #Move to the left
    if event.keysym == "Left":
        xSpeed = -moveSpeed

    #Move to the right
    elif event.keysym == "Right":
        xSpeed = moveSpeed

    #If "J" key pressed, jump but not if the squirrel is already jumping or falling
    if event.keysym == "j":
        if falling == False and jumping == False:
            ySpeed = jumpSpeed
            falling = True
        
    
def keyUp(event):
    global xSpeed

    #Stop moving if an arrow key is released
    xSpeed = 0


#=============== STARTING SCREEN ===============#
#Opening screen
def startingScreen():

    importImages()
    
    s.create_image(300,350, image = startScreen)
    root.bind("<Button-1>", startScreenClick)


#Detects clicks for opening screen
def startScreenClick(event):
    xMouse = event.x
    yMouse = event.y

    if 402 <= xMouse <= 578 and 517 <= yMouse <= 586:
        runGame()
    elif 402 <= xMouse <= 578 and 604 <= yMouse <= 674:
        instructions()


#Instruction screen
def instructions():
    s.create_image(300,350, image = instructionScreen)
    root.bind("<Button-1>", instructionsClick)


#Detects clicks for instructions screen
def instructionsClick(event):
    xMouse = event.x
    yMouse = event.y

    if 22 <= xMouse <= 198 and 22 <= yMouse <= 90:
        startingScreen()

    
#=============== BACKGROUND ===============#
def background():
    global score, scoreText, gameTime, timeText, timeBonus, timeBonusText, squirrelA, squirrelB, indicator

    #Creates a rectangle over everything to make sure nothing from starting & end screens appear
    s.create_rectangle(0,0,600,700, fill = "#98cffe", outline = "#98cffe")

    #Clouds
    for r in range(0,30):
        x = randint(0,600)
        y = randint(-20,100)
        width = randint(60,90)
        height = randint(20,50)

        for i in range(0,20):
            x1 = x - randint(1, width)
            y1 = y - randint(1, height)
            x2 = x + randint(1, width)
            y2 = y + randint(1, height)
            s.create_oval( x1,y1, x2,y2, fill = "white", outline = "white" )

    #Trees
    for r in range(0,40):
        treeWidth = randint(50,75)
        x1 = randint(0,600)
        x3 = x1 + treeWidth
        x2 = (x1 + x3)/2
        y1 = 450
        y2 = y1 - randint(50,100)
        treeColour = choice(["#658b3f","#516d32","#5b7c38"])
        s.create_polygon( x1,y1,x2,y2,x3,y1, fill = treeColour, outline = treeColour )

    #Ground
    s.create_rectangle( 0,450,600,700, fill = "#497a49", outline = "#497a49" )
    s.create_oval( -50,510,650,800,fill = "#3a623a", outline = "#3a623a" )

    #Foreground Trees
    s.create_rectangle( 0,0,75,500, fill = "#7b5839", outline = "#7b5839" ) #Left tree
    s.create_polygon( 75,450, 130,520, 35,500, fill = "#7b5839", outline = "#7b5839" )

    s.create_rectangle( 525,0,600,500, fill = "#7b5839", outline = "#7b5839" ) #Right tree
    s.create_polygon( 525,450, 470,520, 565,500, fill = "#7b5839", outline = "#7b5839" )

    #Tree Bark Texture
    for r in range(0,40):
        x1 = choice([randint(0,65),randint(535,600)])
        y2 = randint(0,500)
        y1 = y2 - randint(50,100)
        s.create_line( x1,y1, x1,y2, fill = "#473322", width = "1.35" )

    #Trampoline
    s.create_rectangle(20,660,60,710, fill = "#737373", outline = "#595959", width = "2")
    s.create_rectangle(540,660,580,710, fill = "#737373", outline = "#595959", width = "2")
    s.create_oval( -20,555,620,705, fill = "#002266", outline = "#001133", width = "2")
    s.create_oval( 25,570,585,675,fill = "#1a1a1a", outline = "#0d0d0d", width = "2" )

    #Branch
    s.create_rectangle( 0,150, 600,200, fill = "#7b5839", outline = "#473322", width = "2" )
    for r in range(0,30):
        x1 = randint(0,600)
        y1 = randint(155,195)
        x2 = x1 + randint(50,100)
        s.create_line( x1,y1, x2,y1, fill = "#473322", width = "1.35" )

    #Time Remaining Box
    s.create_rectangle( 100,10, 200,80, fill = "#ffbc00", outline = "#ffbc00" )
    s.create_text( 150,28, text = "TIME LEFT", font = "Helvetica 10 bold italic", fill = "white" )
    timeText = s.create_text( 150,55, text = gameTime, font = "Helvetica 24 bold italic", fill = "white" )

    #Score Box
    s.create_rectangle( 225,10, 375,125, fill = "#ffbc00", outline = "#ffbc00" )
    s.create_text( 300,42, text = "SCORE", font = "Helvetica 16 bold italic", fill = "white" )
    scoreText = s.create_text( 300,85, text = score, font = "Helvetica 42 bold italic", fill = "white" )
    
    #Times Bonus Box
    s.create_rectangle( 400,10, 500,80, fill = "#ffbc00", outline = "#ffbc00" )
    s.create_text( 450,28, text = "TIME BONUS", font = "Helvetica 10 bold italic", fill = "white" )
    timeBonusText = s.create_text( 445,55, text = timeBonus, font = "Helvetica 24 bold italic", fill = "white" )
    s.create_text( 462,60, text = "/3", font = "Helvetica 12 bold italic", fill = "white" )

    #Squirrels
    squirrelA = s.create_image( 100,110, image = squirrelR )
    squirrelB = s.create_image( 500,560, image = squirrelL )
    indicator = s.create_polygon( xSquirrelA-10,ySquirrelA-70,xSquirrelA+10,ySquirrelA-70,xSquirrelA,ySquirrelA-50, fill = "#cc0000", outline = "#990000" )


#=============== SQUIRREL PROCEDURES ===============#
def moveSquirrels():
    global squirrelA, squirrelB, xSpeed, ySpeed, xSquirrelA, ySquirrelA, xSquirrelB, ySquirrelB
    global squirrelSelect, squirrelPicA, squirrelPicB, falling, jumping, directionA, directionB, indicator

    ground = 560

    #If Squirrel A is in control
    if squirrelSelect == "A":

        #Add speeds to update position
        xSquirrelA += xSpeed  
        ySquirrelA += ySpeed

        #Adds gravity if the squirrel is in the air
        if falling == True and ySquirrelA < ground or jumping == True and ySquirrelA > 115:
            ySpeed += 0.5
        else: #If the squirrel is on the ground, set ySpeed to 0 and variables to false
            ySpeed = 0
            falling = False
            jumping = False

        #Delete previous squirrel
        s.delete(squirrelA)

        #Determines which .gif file to draw
        if falling == True or jumping == True: #Falling squirrel
            squirrelPicA = squirrelAir
        elif xSpeed > 0: #Squirrel facing right
            squirrelPicA = squirrelR
            directionA = "R"
        elif xSpeed < 0 or directionA == "L": #Squirrel facing left
            squirrelPicA = squirrelL
            directionA = "L" #Need direction to keep squirrel facing the same way after the user lets go
        else: #When the squirrel lands
            squirrelPicA = squirrelR 

        #Draw new squirrel
        squirrelA = s.create_image( xSquirrelA,ySquirrelA, image = squirrelPicA )

        #Draw indicator
        s.delete(indicator)
        indicator = s.create_polygon( xSquirrelA-10,ySquirrelA-70,xSquirrelA+10,ySquirrelA-70,xSquirrelA,ySquirrelA-50, fill = "#cc0000", outline = "#990000" )

        #If the squirrel landed, switch the control to the other squirrel
        if ySquirrelA > ground and ySquirrelB > 110:
            squirrelSelect = "B"
            jumping = True
            ySpeed = -22.5
            

    #Same code for Squirrel B
    else:
            
        xSquirrelB += xSpeed
        ySquirrelB += ySpeed

        if falling == True and ySquirrelB < ground or jumping == True and ySquirrelB > 115:
            ySpeed += 0.5
        else:
            ySpeed = 0
            falling = False
            jumping = False

        s.delete(squirrelB)

        if falling == True or jumping == True:
            squirrelPicB = squirrelAir
        elif xSpeed < 0:
            squirrelPicB = squirrelL
            directionB = "L"
        elif xSpeed > 0 or directionB == "R":
            squirrelPicB = squirrelR
            directionB = "R"
        else:
            squirrelPicB = squirrelL

        s.delete(indicator)
        squirrelB = s.create_image( xSquirrelB,ySquirrelB, image = squirrelPicB )
        indicator = s.create_polygon( xSquirrelB-10,ySquirrelB-70,xSquirrelB+10,ySquirrelB-70,xSquirrelB,ySquirrelB-50, fill = "#0066ff", outline = "#0047b3" )

        if ySquirrelB > ground and ySquirrelA > 110:
            
            jumping = True
            ySpeed = -22.5
            squirrelSelect = "A"


#=============== NUT PROCEDURES ===============#
def spawnNut():
    global nuts, nutSpeeds, xPos, yPos, nutType

    xPos.append(choice([-10,610])) #Spawns at the left or right side of the screen
    yPos.append(randint(220,500)) #Spawns at a random y-value
    
    if xPos[len(xPos)-1] == -10:
        nutSpeeds.append(randint(5,9)) #If spawned at left side, give random positive speed
    else:
        nutSpeeds.append(randint(-9,-5)) #If spawned at right side, give random negative speed

    nuts.append(0) #First append a value of 0, draws the nut in moveNuts()

    #Based on the random number, spawn a nut
    #Spawns higher value nuts less often
    randomNum = randint(0,1000) #Random number
    chance = [400,530,655,755,835,885,925,955,975,985,995,1000]
    types = [brownNut,timeNut,greenNut,yellowNut,bronzeNut,silverNut,goldNut,
               rainbowNut,flamingNut,creepyNut,happyNut,pinkNut]

    for num in chance: #Searches through array to match number to nut
        if randomNum <= num:
            nutDrawn = types[chance.index(num)]
            break

    nutType.append(nutDrawn) #Append the type of nut to nutType array       


def checkForCollision():
    global xSquirrelA, ySquirrelA, xSquirrelB, ySquirrelB
    global nuts, nutSpeeds, xPos, yPos, nutType

    #Goes through nut array and checks the distance to find collisions
    for i in range(0,len(nuts)):
        distanceA = sqrt( (xSquirrelA-xPos[i])**2 + (ySquirrelA-yPos[i])**2 )
        distanceB = sqrt( (xSquirrelB-xPos[i])**2 + (ySquirrelB-yPos[i])**2 )

        #If a nut was hit
        if distanceA <= 45 or distanceB <= 45:
            
            updateScore(nutType[i],xPos[i],yPos[i]) #Update score

            #Delete that nut
            s.delete(nuts[i])
            nuts.remove(nuts[i])
            nutSpeeds.remove(nutSpeeds[i])
            xPos.remove(xPos[i])
            yPos.remove(yPos[i])
            nutType.remove(nutType[i])
            break


def moveNuts():
    global nuts, nutSpeeds, xPos, yPos, nutType

    #Moves all nuts in the array
    for i in range(0,len(nuts)):
        xPos[i] += nutSpeeds[i]
        nuts[i] = s.create_image(xPos[i],yPos[i], image = nutType[i])


def removeNuts():
    global nuts, nutSpeeds, xPos, yPos, nutType

    #Checks through nuts and deletes one that is off the screen
    for i in range(0,len(nuts)): 
        if xPos[i] < -20 or xPos[i] > 620:
            s.delete(nuts[i])
            nuts.remove(nuts[i])
            nutSpeeds.remove(nutSpeeds[i])
            xPos.remove(xPos[i])
            yPos.remove(yPos[i])
            nutType.remove(nutType[i])
            break

    #Updates screen, sleeps and deletes nuts
    s.update()
    sleep(0.045)
    for i in range(0,len(nuts)):
         s.delete(nuts[i])


#=============== OTHER GAME PROCEDURES ===============#
def timeUpdate():
    global gameTime, timeText, timeStart

    #Updates the timer
    timeNow = time()
    timeElapsed = timeNow - timeStart

    #If one second has passed, update the timer
    if timeElapsed >= 1:
        gameTime -= 1
        s.delete( timeText )
        timeText = s.create_text( 150,55, text = gameTime, font = "Helvetica 24 bold italic", fill = "white" )
        timeStart = time()
        
        if randint(1,30) <= 11: #11/30 chance of spawning nut each second
            spawnNut()
        

def updateScore(nutType,x,y):
    global score, scoreText

    #Arrays with the nut type and the corresponding points given
    types = [brownNut,timeNut,greenNut,yellowNut,bronzeNut,silverNut,goldNut,
               rainbowNut,flamingNut,creepyNut,happyNut,pinkNut]
    scores = [1,2,2,3,4,5,10,15,25,30,30,50]

    #Time nut adding time bonus
    if nutType == timeNut:
        addTimeBonus()

    #Get the corresponding points
    for i in types:
        if nutType == i:
            scoreNum = scores[types.index(i)]
            score += scoreNum
            addPopUp("+" + str(scoreNum),x+40,y) #Make the score pop up
            break
    
    #Update total score display
    s.delete(scoreText)
    scoreText = s.create_text( 300,85, text = score, font = "Helvetica 42 bold italic", fill = "white" )


def addTimeBonus():
    global gameTime, timeText, timeBonusText, timeBonus

    timeBonus += 1

    #If the user has collected three time nuts, give a 10 second bonus and reset the counter
    if timeBonus == 3:
        timeBonus = 0
        timeBonusAmount = 10
    else:
        #If bonus counter below 3, just add 3 seconds
        timeBonusAmount = 3    
    gameTime += timeBonusAmount

    #Add a pop-up
    addPopUp("+" + str(timeBonusAmount) + " seconds!",300,275)

    #Update game timer
    s.delete( timeText )
    timeText = s.create_text( 150,55, text = gameTime, font = "Helvetica 24 bold italic", fill = "white" )

    #Update time bonus text
    s.delete(timeBonusText)
    timeBonusText = s.create_text( 445,55, text = timeBonus, font = "Helvetica 24 bold italic", fill = "white" )


def addPopUp(message,x,y):
    global popUpText, popUpTimes
    
    #Draw the pop up
    popUp = s.create_text( x,y, text = message, font = "Helvetica 24 bold", fill = "white" )

    #Add graphic to array
    popUpText.append(popUp)

    #Add time it appears to array
    popUpTimes.append(time())


def popUpTimeCounter():
    global popUpText, popUpTimes

    for i in range(0,len(popUpTimes)):
        #For each pop up, get the time elapsed since it appeared
        timeNow = time()
        timeElapsed = timeNow - popUpTimes[i]

        #Delete & remove from arrays if 1 second (or more) has passed
        if timeElapsed >= 1:
            s.delete(popUpText[i])
            popUpText.remove(popUpText[i])
            popUpTimes.remove(popUpTimes[i])
            break


def countdown():
    
    #3, 2, 1 countdown before beginning the game
    for i in range(3,-1,-1):
        if i == 0:
            countdown = s.create_text( 300,275, text = "Go!", font = "Helvetica 64 bold", fill = "white" )
        else:
            countdown = s.create_text( 300,275, text = i, font = "Helvetica 64 bold", fill = "white" )
        s.update()
        sleep(1)
        s.delete(countdown)
        

#=============== ENDING SCREEN ===============#
def endGame():
    global score
    
    #End game message
    endMessage = s.create_text( 300,250, text = "Game Over!", font = "Helvetica 48 bold", fill = "white" )
    s.update()
    sleep(1.25)
    s.delete(endMessage)

    #Depending on the score, display a different ending screen
    if score < 50:
        s.create_image(300,350, image = sadEnding)
    elif score < 100:
        s.create_image(300,350, image = goodEnding)
    else:
        s.create_image(300,350, image = greatEnding)
        
    #Display final score
    s.create_text(300,100, text = "Final Score:", font = "Helvetica 18", fill = "white" )
    s.create_text(300,150, text = score, font = "Helvetica 64 bold", fill = "white" )

    root.bind("<Button-1>", endGameClick)


#Detects clicks for end game screen
def endGameClick(event):
    xMouse = event.x
    yMouse = event.y

    if 89 <= xMouse <= 279 and 603 <= yMouse <= 676:
        runGame()
    elif 320 <= xMouse <= 509 and 603 <= yMouse <= 676:
        root.destroy()


#=============== MAIN GAME LOOP ===============#
def runGame():
    global gameTime, timeStart

    startingValues()
    background()
    countdown()

    timeStart = time()
    
    while gameTime > 0: #Runs until the timer reaches 0

        timeUpdate()
        popUpTimeCounter()
        moveSquirrels()
        moveNuts()
        checkForCollision()
        removeNuts()
  
    endGame()


#=============== KEY BINDINGS + START PROGRAM ===============#
#Binds key down
root.bind("<Key>", keyDownHandler)
#Binds key release
root.bind("<KeyRelease>", keyUp)

#Starts game
root.after(0, startingScreen())

root.focus_set() 
root.mainloop()
