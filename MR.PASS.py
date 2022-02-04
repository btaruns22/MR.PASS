import simplegui
import random
import time

#hackBCA Team Glen Rock
#MrPass - Password Manager

#Note: Password Retrieval *Incomplete*
#Complications with Codeskulptor prevented us from accomplishing our full task
#The full intent is to set a game in which you solve to retrieve a password
#Enjoy our code!!

passwordA = []
accountA = []

mainmenu = True
face0 = False
face1 = False
face2 = False
face3 = False
face4 = False
face5 = False
face6 = False
face7 = False

i = 0

music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
image = simplegui.load_image("https://images.pexels.com/photos/255379/pexels-photo-255379.jpeg")

WIDTH = 1680
HEIGHT = 1050

IMAGE_WIDTH = WIDTH // 1.9
IMAGE_HEIGHT = HEIGHT // 1.9


#tic tac toe variables
xo=" "
xo2=" "
xo3=" "
xo4=" "
xo5=" "
xo6=" "
xo8=" "
xo7=" "
xo9=" "


canvas_width = 800
canvas_height = 500
grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
turn = True
won = False

alist = [] 
blist = []


clist = []
dlist = []

    
def pword(word):

    global i
    global face1
    global face3
    
    if(i == 0):
    
        passwordA.append(word)

        numpass = len(passwordA)
        print("Numpass: " + str(numpass))

        frame.add_input("What is this password for?", account, 200)
        
        i = 1
        
    else:
        
        face1 = not face1
        face3 = not face3
        
        i = 0
    
def account(type):
    
    global accpass

    accountA.append(type)   	
    
    accpass = len(accountA)
    print("Accpass: " + str(accpass))
    
    toggle_face3()
    
    
numaccount = len(accountA)

#Defines the first of the "toggling" functions (Switching menus)
def toggle_face0():
    
    global mainmenu
    global face0
    
    mainmenu = not mainmenu
    face0 = not face0
    
def toggle_face1():
    
    global face1
    global mainmenu
    
    mainmenu = not mainmenu
    face1 = not face1
    
def toggle_face2():
    
    global mainmenu
    global face2
    
    mainmenu = not mainmenu
    face2 = not face2  
    
def toggle_face3():
    
    global face1
    global face3
    
    face1 = not face1
    face3 = not face3
    
def toggle_face4():
    
    global face3
    global face4
    
    face3 = not face3
    face4 = not face4
    
def toggle_face5():
    
    global face5
    global face0
    
    face5 = not face5
    face0 = not face0
    
def toggle_face6():
    
    global face0
    global face6
    
    face0 = not face0
    face6 = not face6
    
def toggle_face7():
    
    global face0
    global face7
    
    face0 = not face0
    face7 = not face7
       
length = len(accountA)

def menuA():
    
    global face4
    global mainmenu
    
    face4 = not face4
    mainmenu = not mainmenu
    
#Defines the click function
def click(position):
    global won
    global info
    global turn
    global turn
    global xo
    global xo2
    global xo3
    global xo4
    global xo5
    global xo6
    global xo8
    global xo7
    global xo9
    
    #Assigns the x and y values respective to the position parameter
    x = position[0]
    y = position[1]
    

    if(mainmenu == True):
            
        if(x >= 200 and x <= 600 and y >= 250 and y <= 300):
                
            toggle_face0()
           
        else:
           
            pass
               
        if(x >= 200 and x <= 600 and y >= 325 and y <= 375):
            
            toggle_face1()
            
            frame.add_input("Enter Password: ", pword, 150)            
       
        if(x >= 200 and x <= 600 and y >= 400 and y <= 450):
            
            toggle_face2()
    
    if(face1):
        
        if (x>10 and y > 10 and x <300 and y < 70):
            
            toggle_face1()
   
    if(face0):
        
        if(x>=10 and y >= 10 and x <=300 and y <= 70):
            
            toggle_face0()
       
           
        if(x >= 10 and x <= 110 and y >= 100 and y <= 190):
            
            toggle_face5() 
               
        if(x >= 10 and x <= 110 and y >= 200 and y <= 290):
            
            toggle_face6() 
                
        if(x >= 10 and x <= 110 and y >= 300 and y <= 390):
            
            toggle_face7()
            
            
    
    if(face3):
        
        if (x>10 and y > 10 and x <300 and y < 70):
            
            toggle_face3()
            
            toggle_face1()
            
        if(x >= 190 and x <= 650 and y >= 150 and y <= 225):
            
            toggle_face4()
            frame.add_button("DONE", menuA, 70)
          
    if(face2):
        
        if(x>10 and y >10 and x < 300 and y < 70):
            
            toggle_face2()
            
    '''        
    if(face4):
        if(x>10 and y >10 and x < 110 and y < 60):
            toggle_face4()
      ''' 
        #frame.set_mouseclick_handler(clickA)
    if(face4):
            
        if (x>=0 and x<=265 and y>=0 and y<163):
        
            if turn==True:
                alist.append("a")
                xo="X"
                print (alist)
            if turn == False:
                xo="O"
                blist.append("a")
            #print(blist)
            
            turn=not turn


        if (x>=266 and x<=530 and y>=0 and y<163):
        #alist.append("b")
            if turn==True:
                xo2="X"
                alist.append("b")
                print (alist) 
            if turn == False:
                xo2="O"
                blist.append("b")
            #print(blist)
            turn=not turn
        
        if (x>=531 and x<=800 and y>=0 and y<163):
            
            if turn==True:
                xo3="X"
                alist.append("c")
            
                print (alist)
            if turn == False:
                xo3="O"
                blist.append("c")
            #print(blist)
           
            turn=not turn
        
        if (x>=0 and x<=265 and y>=164 and y<330):
        #alist.append("d")
            if turn==True:
                xo4="X"
                alist.append("d")
           
                print (alist)
            if turn == False:
                xo4="O"
                blist.append("d")
            #print(blist)
           
            turn=not turn    

        if (x>=266 and x<=530 and y>=164 and y<330):
        
            if turn==True:
                xo5="X"
                alist.append("e")
          
                print (alist)
            if turn == False:
                xo5="O"
                blist.append("e")
            #print(blist)
            turn=not turn
        
        if (x>=531 and x<=800 and y>=164 and y<330):
            
            if turn==True:
                xo6="X"
                alist.append("f")
            
            print (alist)
            if turn == False:
                xo6="O"
                blist.append("f")
            #print(blist)
    
            turn=not turn
        

        if (x>=0 and x<=265 and y>=330 and y<500):
        
            if turn==True:
                xo7="X"
                alist.append("g")

                print (alist)
            if turn == False:
                xo7="O"
                blist.append("g")
            #print(blist)

            turn=not turn

            if (x>=266 and x<=530 and y>=330 and y<500):
            
                if turn==True:
                    xo8="X"
                    alist.append("h")

                print (alist)
            if turn == False:
                xo8="O"
                blist.append("h")
            #print(blist)

            turn=not turn

        if (x>=531 and x<=800 and y>=330 and y<500):
        
            if turn==True:
                xo9="X"
                alist.append("i")

                print (alist)
            if turn == False:
                xo9="O"
                blist.append("i")
            #print(blist)

            turn=not turn 
           
        
     
def clickA(position):
    global turn
    global xo
    global xo2
    global xo3
    global xo4
    global xo5
    global xo6
    global xo8
    global xo7
    global xo9
    x = position [0]
    y = position [1]
    
    if (x>=0 and x<=265 and y>=0 and y<163):
        
        if turn==True:
            alist.append("a")
            xo="X"
            print (alist)
        if turn == False:
            xo="O"
            blist.append("a")
            #print(blist)
            
        turn=not turn


    if (x>=266 and x<=530 and y>=0 and y<163):
        #alist.append("b")
        if turn==True:
            xo2="X"
            alist.append("b")
            print (alist) 
        if turn == False:
            xo2="O"
            blist.append("b")
            #print(blist)
        turn=not turn
        
    if (x>=531 and x<=800 and y>=0 and y<163):
        
        if turn==True:
            xo3="X"
            alist.append("c")
            
            print (alist)
        if turn == False:
            xo3="O"
            blist.append("c")
            #print(blist)
           
        turn=not turn
        
    if (x>=0 and x<=265 and y>=164 and y<330):
        #alist.append("d")
        if turn==True:
            xo4="X"
            alist.append("d")
           
            print (alist)
        if turn == False:
            xo4="O"
            blist.append("d")
            #print(blist)
           
        turn=not turn    

    if (x>=266 and x<=530 and y>=164 and y<330):
        
        if turn==True:
            xo5="X"
            alist.append("e")
          
            print (alist)
        if turn == False:
            xo5="O"
            blist.append("e")
            #print(blist)
        turn=not turn
        
    if (x>=531 and x<=800 and y>=164 and y<330):
        
        if turn==True:
            xo6="X"
            alist.append("f")
            
            print (alist)
        if turn == False:
            xo6="O"
            blist.append("f")
            #print(blist)

        turn=not turn
        

    if (x>=0 and x<=265 and y>=330 and y<500):
        
        if turn==True:
            xo7="X"
            alist.append("g")

            print (alist)
        if turn == False:
            xo7="O"
            blist.append("g")
            #print(blist)

        turn=not turn

    if (x>=266 and x<=530 and y>=330 and y<500):
        
        if turn==True:
            xo8="X"
            alist.append("h")

            print (alist)
        if turn == False:
            xo8="O"
            blist.append("h")
            #print(blist)

        turn=not turn

    if (x>=531 and x<=800 and y>=330 and y<500):
        
        if turn==True:
            xo9="X"
            alist.append("i")

            print (alist)
        if turn == False:
            xo9="O"
            blist.append("i")
            #print(blist)

        turn=not turn    
    if(face4):
        if(x>10 and y >10 and x < 110 and y < 60):
            
             toggle_face4()
                
                
     
def clickAccess(position):
    global turn
    global xo
    global xo2
    global xo3
    global xo4
    global xo5
    global xo6
    global xo8
    global xo7
    global xo9
    x = position [0]
    y = position [1]
    
    if (x>=0 and x<=265 and y>=0 and y<163):
        
        if turn==True:
            clist.append("a")
            xo="X"
            print (clist)
        if turn == False:
            xo="O"
            dlist.append("a")
            #print(blist)
            
        turn=not turn


    if (x>=266 and x<=530 and y>=0 and y<163):
        #alist.append("b")
        if turn==True:
            xo2="X"
            clist.append("b")
            print (alist) 
        if turn == False:
            xo2="O"
            dlist.append("b")
            #print(blist)
        turn=not turn
        
    if (x>=531 and x<=800 and y>=0 and y<163):
        
        if turn==True:
            xo3="X"
            clist.append("c")
            
            print (alist)
        if turn == False:
            xo3="O"
            dlist.append("c")
            #print(blist)
           
        turn=not turn
        
    if (x>=0 and x<=265 and y>=164 and y<330):
        #alist.append("d")
        if turn==True:
            xo4="X"
            clist.append("d")
           
            print (alist)
        if turn == False:
            xo4="O"
            dlist.append("d")
            #print(blist)
           
        turn=not turn    

    if (x>=266 and x<=530 and y>=164 and y<330):
        
        if turn==True:
            xo5="X"
            clist.append("e")
          
            print (alist)
        if turn == False:
            xo5="O"
            dlist.append("e")
            #print(blist)
        turn=not turn
        
    if (x>=531 and x<=800 and y>=164 and y<330):
        
        if turn==True:
            xo6="X"
            clist.append("f")
            
            print (alist)
        if turn == False:
            xo6="O"
            dlist.append("f")
            #print(blist)

        turn=not turn
        

    if (x>=0 and x<=265 and y>=330 and y<500):
        
        if turn==True:
            xo7="X"
            clist.append("g")

            print (alist)
        if turn == False:
            xo7="O"
            dlist.append("g")
            #print(blist)

        turn=not turn

    if (x>=266 and x<=530 and y>=330 and y<500):
        
        if turn==True:
            xo8="X"
            clist.append("h")

            print (alist)
        if turn == False:
            xo8="O"
            dlist.append("h")
            #print(blist)

        turn=not turn

    if (x>=531 and x<=800 and y>=330 and y<500):
        
        if turn==True:
            xo9="X"
            clist.append("i")

            print (alist)
        if turn == False:
            xo9="O"
            dlist.append("i")
            #print(blist)

        turn=not turn    
    if(face4):
        if(x>10 and y >10 and x < 110 and y < 60):
            
             toggle_face4()
            
            
            
                    
    
def play():
    
    music.play()                   

def draw(canvas): 

    global face0, face1, face2, image, xo, xo2, xo3, xo4, xo5, xo6, xo7, xo8, xo9, c, r, accpass, accountA, passwordA
    
    if(mainmenu):
        
        canvas.draw_image(image, (WIDTH, HEIGHT ), (WIDTH, HEIGHT), (IMAGE_WIDTH , IMAGE_HEIGHT ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_image(image, (WIDTH//2, HEIGHT//2 ), (WIDTH, HEIGHT), (IMAGE_WIDTH//2 , IMAGE_HEIGHT//2 ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_text("Mr. Pass", (230,165), 100, "Blue")
        canvas.draw_text("hackBCA Team Glen Rock", (260, 200), 25, "Blue")
        canvas.draw_polygon([(200, 400), (200, 450), (600, 450), (600, 400)], 1, "Black", "White")
        canvas.draw_polygon([(200, 325), (200, 375), (600, 375), (600, 325)], 1, "Black", "White")
        canvas.draw_polygon([(200, 250), (200, 300), (600, 300), (600, 250)], 1, "Black", "White")
        canvas.draw_text("Access Passwords", (310, 283), 25, "Black")
        canvas.draw_text("Add New Password", (305, 358), 25, "Black")
        canvas.draw_text("Settings", (355, 433), 25, "Black")
    
    if(face0):
        
        maxrange = len(accountA)
        
        canvas.draw_image(image, (WIDTH, HEIGHT ), (WIDTH, HEIGHT), (IMAGE_WIDTH , IMAGE_HEIGHT ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_image(image, (WIDTH//2, HEIGHT//2 ), (WIDTH, HEIGHT), (IMAGE_WIDTH//2 , IMAGE_HEIGHT//2 ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_polygon([(10, 10), (110, 10), (110, 60), (10, 60)], 1, "Black", "White")
        canvas.draw_text("Main Menu",(10,40),20,"Green")
       

        for box in range (0, (maxrange)*100,100):
            canvas.draw_polygon([(10, 100+box), (110, 100+box), (110, 190+box), (10, 190+box)], 1, "Black", "White")
        for text in range(0, maxrange):
            acctext = accountA[text]
            canvas.draw_text((acctext), (10, 150 + text*100), 25, "Black")
                
            
    if(face1):
        
        canvas.draw_image(image, (WIDTH, HEIGHT ), (WIDTH, HEIGHT), (IMAGE_WIDTH , IMAGE_HEIGHT ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_image(image, (WIDTH//2, HEIGHT//2 ), (WIDTH, HEIGHT), (IMAGE_WIDTH//2 , IMAGE_HEIGHT//2 ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_polygon([(10, 10), (110, 10), (110, 60), (10, 60)], 1, "Black", "White")
        canvas.draw_text("Main Menu",(10,40),20,"Green")    
        canvas.draw_text("Enter Your Password: ", (200, 250), 50, "Black")
             
   
    if(face2):        
        
        canvas.draw_polygon([(10, 10), (20, 10), (10, 20), (20, 20)], 1, "Black", "White")
        canvas.draw_text("word",(30,50),20,"red")
        canvas.draw_image(image, (WIDTH, HEIGHT ), (WIDTH, HEIGHT), (IMAGE_WIDTH , IMAGE_HEIGHT ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_image(image, (WIDTH//2, HEIGHT//2 ), (WIDTH, HEIGHT), (IMAGE_WIDTH//2 , IMAGE_HEIGHT//2 ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_polygon([(10, 10), (110, 10), (110, 60), (10, 60)], 1, "Black", "White")
        canvas.draw_text("Under Construction",(200,300),50,"Black")  
        canvas.draw_text("Main Menu",(10,40),20,"Green")
  
    if(face3):
        
        canvas.draw_image(image, (WIDTH, HEIGHT ), (WIDTH, HEIGHT), (IMAGE_WIDTH , IMAGE_HEIGHT ), (IMAGE_WIDTH, IMAGE_HEIGHT))
        canvas.draw_image(image, (WIDTH//2, HEIGHT//2 ), (WIDTH, HEIGHT), (IMAGE_WIDTH//2 , IMAGE_HEIGHT//2 ), (IMAGE_WIDTH, IMAGE_HEIGHT))        
        canvas.draw_polygon([(190, 150), (650, 150), (650, 225), (190, 225)], 1, "Black", "Gray")
        canvas.draw_text("Which game would you like to save this password with?",(100,100),30,"black")
        canvas.draw_text("Game 1: Tic-Tac-Toe",(200,200),50,"White")
        canvas.draw_polygon([(10, 10), (110, 10), (110, 60), (10, 60)], 1, "Black", "White")
        canvas.draw_text("Main Menu",(10,40),20,"Green")
        
    if(face4):

        # Draws the grid lines
        canvas.draw_line([0, canvas_height // 3], [canvas_width, canvas_height // 3], 1, "White")
        canvas.draw_line([0, canvas_height // 3 * 2], [canvas_width, canvas_height // 3 * 2], 1, "White")
        canvas.draw_line([canvas_width // 3, 0], [canvas_width // 3, canvas_height], 1, "White")
        canvas.draw_line([canvas_width // 3 * 2, 0], [canvas_width // 3 * 2, canvas_height], 1, "White")
        canvas.draw_polygon([(10, 10), (330, 10), (330, 60), (10, 60)], 1, "Black", "White")
        canvas.draw_text("Choose 3 spaces for your password",(110,40),15,"black")
        canvas.draw_text(xo,(100,100),100,"red")
        canvas.draw_text(xo2,(350,100),100,"red")
        canvas.draw_text(xo3,(600,100),100,"red")
        canvas.draw_text(xo4,(100,300),100,"red")
        canvas.draw_text(xo5,(350,300),100,"red")
        canvas.draw_text(xo6,(600,300),100,"red")
        canvas.draw_text(xo7,(100,450),100,"red")
        canvas.draw_text(xo8,(350,450),100,"red")
        canvas.draw_text(xo9,(600,450),100,"red")

        # Draws the player choices using loops
        #for r in range(0,3):
            #for c in range(0,3):
                #canvas.draw_text(grid[r][c],[c * canvas_width // 3 + 20, r * canvas_height // 3 + 80], 80, "Red")

    if(face5):
        canvas.draw_line([0, canvas_height // 3], [canvas_width, canvas_height // 3], 1, "White")
        canvas.draw_line([0, canvas_height // 3 * 2], [canvas_width, canvas_height // 3 * 2], 1, "White")
        canvas.draw_line([canvas_width // 3, 0], [canvas_width // 3, canvas_height], 1, "White")
        canvas.draw_line([canvas_width // 3 * 2, 0], [canvas_width // 3 * 2, canvas_height], 1, "White")
        canvas.draw_polygon([(10, 10), (330, 10), (330, 60), (10, 60)], 1, "Black", "White")
        canvas.draw_text("Choose 3 spaces for your password",(110,40),15,"black")
        canvas.draw_text(xo,(100,100),100,"red")
        canvas.draw_text(xo2,(350,100),100,"red")
        canvas.draw_text(xo3,(600,100),100,"red")
        canvas.draw_text(xo4,(100,300),100,"red")
        canvas.draw_text(xo5,(350,300),100,"red")
        canvas.draw_text(xo6,(600,300),100,"red")
        canvas.draw_text(xo7,(100,450),100,"red")
        canvas.draw_text(xo8,(350,450),100,"red")
        canvas.draw_text(xo9,(600,450),100,"red")
        canvas.draw_polygon([(10, 10), (110, 10), (110, 60), (10, 60)], 1, "Black", "White")
        canvas.draw_text("Main Menu",(10,40),20,"Green")
        
    if(face6):
        canvas.draw_text("", (100, 100), 10, "Black")
    if(face7):
        canvas.draw_text("", (100, 100), 10, "Black")
        
        
#Defining the SimpleGUI Canvas
frame = simplegui.create_frame("MrPass", 800, 500)

#Setting Up Control Elements
frame.set_draw_handler(draw)
vol = 7
volume_button = frame.add_label("Volume = " + str(vol))

frame.add_button("play", play,100)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("Gray")

# Loading Sounds
music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")

#Start the Canvas
frame.start()
