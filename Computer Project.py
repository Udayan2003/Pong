"""
PONG
"""


#Importing modules
import turtle
import random
import tkinter
import tkinter.font as font
import mysql.connector as mc
from tkinter import ttk


def play():
    
    #We check if the table to store the game log exists
    def check(): 
        cur.execute("Create table if not exists Game_log(Serial int(16) auto_increment,Player1 Varchar(10),Player2 varchar(10),Score varchar(5),primary key(Serial));")

    #To accept the player names
    def submit():
        global plyr1
        global plyr2

        check()
        plyr1=e1.get()
        plyr2=e2.get()

        #Checking if the username enterred is alphanumeric
        if plyr1.isalnum() and plyr2.isalnum():

            #Making sure the length of username is not greater than 8 characters
            if len(plyr1)<=8 and len(plyr2)<=8:
                e1.delete(0,"end")
                e2.delete(0,"end")
                root3.destroy()
                
                #DIFFICULTY LEVELS
                
                #Easiest level with less ball speed
                def VeryEasy():
                    global ballspeed
                    ballspeed=7.5
                    play1()
                    cur.execute("insert into Game_log(Player1,Player2,Score) values(%s,%s,%s)",(plyr1,plyr2,winner))
                    con.commit()
                    root4.destroy()
                    
                #Easy level with relatively slower ball speed  
                def Easy():
                    global ballspeed
                    ballspeed=10
                    play1()
                    cur.execute("insert into Game_log(Player1,Player2,Score) values(%s,%s,%s)",(plyr1,plyr2,winner))
                    con.commit()
                    root4.destroy()
                    
                #Medium level with moderate ball speed
                def Medium():
                    global ballspeed
                    ballspeed=15
                    play1()
                    cur.execute("insert into Game_log(Player1,Player2,Score) values(%s,%s,%s)",(plyr1,plyr2,winner))
                    con.commit()
                    root4.destroy()
                    
                #Tough level with high ball speed
                def Hard():
                    global ballspeed
                    ballspeed=20
                    play1()
                    cur.execute("insert into Game_log(Player1,Player2,Score) values(%s,%s,%s)",(plyr1,plyr2,winner))
                    con.commit()
                    root4.destroy()

                #Hardest level with fastest ball speed
                def VeryHard():
                    global ballspeed
                    ballspeed=25
                    play1()
                    cur.execute("insert into Game_log(Player1,Player2,Score) values(%s,%s,%s)",(plyr1,plyr2,winner))
                    con.commit()
                    root4.destroy()

                    
                #Make a window to set Difficulty level
                root4=tkinter.Tk()
                root4.geometry("400x450")
                root4.title("Difficulty")

                Lab=tkinter.Label(root4,height=3,width=15,text="Choose Difficulty",fg="Red")

                #Creating buttons for various difficulty levels
                but1=tkinter.Button(root4,text="Very Easy",command=VeryEasy,height=2,width=8,)
                but2=tkinter.Button(root4,text="Easy",command=Easy,height=2,width=7,)
                but3=tkinter.Button(root4,text="Medium",command=Medium,height=2,width=8) 
                but4=tkinter.Button(root4,text="Hard",command=Hard,height=2, width=7)
                but5=tkinter.Button(root4,text="Very Hard",command=VeryHard,height=2,width=8)

                but1.config(font=("Helvetica",18))
                but2.config(font=("Helvetica",18))
                but3.config(font=("Helvetica",18))
                but4.config(font=("Helvetica",18))
                but5.config(font=("Helvetica",18))
                Lab.config(font=("Helvetica",24))
                
                Lab.pack()
                but1.pack(pady=10)
                but2.pack()
                but3.pack(pady=10)
                but4.pack()
                but5.pack(pady=10)

             #Names having more than 8 characters will not be accepted
            else:
                print("Values containing only upto 8 characters can be accepted")
        else:
            print("Names of players can contain only alpha numeric values")


    #To make a window asking for the usernames
    root3=tkinter.Tk()
    root3.geometry("400x200")
    root3.title("Login")
    
    #Setting the font type an font size
    myfont=font.Font(family="Helvetica",size=15)
    
    e1=tkinter.Entry(root3)
    e2=tkinter.Entry(root3)

    e1.place(x=135,y=30)
    e2.place(x=135,y=80)

    lbl1=tkinter.Label(root3,text="Player1:")
    lbl2=tkinter.Label(root3,text="Player2:")

    lbl1.config(font=("Helvetica",16))
    lbl2.config(font=("Helvetica",16))

    sub=tkinter.Button(root3,text="Enter",height=2,width=5,command=submit)
    sub["font"]=myfont

    sub.place(x=180,y=125)

    lbl1.place(x=70,y=30)
    lbl2.place(x=70,y=80)

def play1():

    #To setup the PONG window.
    global wn
    wn = turtle.Screen()
    wn.title("PONG")
    wn.bgcolor("black")
    wn.setup(width = 1.0, height = 1.0)

    #Border
    border = turtle.Turtle()
    border.penup()
    border.color("white")
    border.pensize(3)

    #To hide the turtle
    border.ht()
    border.setposition(-500, 300)
    border.speed(0)

    #To create the border on top and bottom
    def border1():
        border.pendown()
        border.fd(1000)
        border.right(90)
        border.fd(600)
        border.right(90)
        border.fd(1000)
        border.right(90)
        border.fd(600)
        border.penup()

    #To draw the dotted line in the centre
    def dotted_line():
        border.pensize(1)
        border.setposition(0, -300)
        border.pendown()
        border.setheading(90)
        for i in range (12):
            border.fd(26)
            border.penup()
            border.fd(26)
            border.pendown()

    #Pong_Ball
    def ball_object():
        global ball
        ball = turtle.Turtle()
        ball.shape("turtle")
        ball.color("white")
        ballheading = random.randint(1,360)
        ball.penup()
        ball.setheading(ballheading)
        ball.speed("fastest")

    #Player1
    def play1():
        global player1
        global playerspeed
        player1 = turtle.Turtle()
        player1.speed(8)
        player1.shape("square")
        player1.turtlesize(4,1)
        player1.color("blue")
        player1.penup()
        player1.setposition(-499, 0)
        playerspeed = 50

    #Player2
    def play2():
        global player2
        global playerspeed
        player2 = turtle.Turtle()
        player2.speed(8)
        player2.shape("square")
        player2.shapesize(4,1)
        player2.color("red")
        player2.penup()
        player2.setposition(499, 0)
       
        
    border1()
    dotted_line()
    ball_object()
    play1()
    play2()
    
    #Player 1 movement

    #For upward movement of player1
    def up():
        y = player1.ycor()
        y += playerspeed
        if y < 270:
                player1.sety(y)
                
    #For downward movement of player1          
    def down():
        y = player1.ycor()
        y -= playerspeed
        if y > -270:
                player1.sety(y)               

    #Player 2 movement

    #For upward movement of player2           
    def up1():
            y = player2.ycor()
            y += playerspeed
            if y < 280:
                    player2.sety(y)
                    
    #For downward movement of player2
    def down1():
        y = player2.ycor()
        y -= playerspeed
        if y > -280:
                player2.sety(y)

    #To set the ball's position in the centre.
    def start():
        ballheading = random.randint(1,360)
        ball.setposition(0, 0)
        ball.setheading(ballheading)

    #Condition to bounce
    def distance(t1,t2):
        dist=t1.distance(t2)
        if dist<40:
            t2.setheading(180-t2.heading())                

    #We assign w/s to move the player 1
    turtle.listen()
    turtle.onkey(up, "w")
    turtle.onkey(down,"s")

    #We assign up and down arrow to move the player 2
    turtle.onkey(up1, "Up")
    turtle.onkey(down1,"Down")

    #Restart
    turtle.onkey(start,"p")

    
    #Player1 score
    Score1 = 0
    s1 = turtle.Turtle()
    s1.speed(0)
    s1.ht()
    s1.color("white")
    s1.penup()
    s1.setposition(-190, 250)
    s1.pd()
    s1.write(Score1, font=("Arial", 30, "normal"))

    s3=turtle.Turtle()
    s3.ht()
    s3.color("white")
    s3.pu()
    s3.setposition(-310,250)
    s3.pd()
    s3.write(plyr1+":",font=("Arial", 30, "normal"))


    #Player 2 score's
    Score2= 0
    s2 = turtle.Turtle()
    s2.speed(0)
    s2.ht()
    s2.color("white")
    s2.penup()
    s2.setposition(300, 250)
    s2.write(Score1, font=("Arial", 30, "normal"))

    s3.pu()
    s3.setpos(180,250)
    s3.pd()
    s3.write(plyr2+":",font=("Arial", 30, "normal"))

    Run=True
    
    #Mainloop
    while Run:
        ball.forward(ballspeed)
        y = ball.ycor()
        x = ball.xcor()
        

        #We define the border colision 
        if y > 279 or y<-279:
            degree=ball.heading()
            ball.setheading(-degree)

        if x > 520:
            Score1 += 1
            s1.clear()
            s1.write(Score1, font=("Arial", 30, "normal"))
            start()
            
        if x < -520:
            Score2 += 1
            s2.clear()
            s2.write(Score2, font=("Arial", 30, "normal"))
            start()

        #Colision between player and ball                
        distance(player1,ball)
        distance(player2,ball)

        if Score1==10 or Score2==10:
            Run=False
            
    if Run==False:
        root2=tkinter.Tk()
        root2.title("Dialog")
        root2.geometry("300x100")
        root2.configure(bg="black")
        if Score1==10:
            label5=tkinter.Label(root2,fg="white",text= plyr1+" WINS",bg="black")
            label5.config(font=("Helvetica",23))
            label5.pack(pady=20)
            global winner
            winner="1-0"
        else:
            label5=tkinter.Label(root2,fg="white",text= plyr2+" WINS",bg="black")
            label5.config(font=("Helvetica",23))
            label5.pack(pady=20)
            winner="0-1"
          
#Highscore window
def Highscore():
    root4=tkinter.Tk()
    root4.title("GAME_LOG")
    root4.geometry("550x525")
    cur.execute("select Player1,Player2,Score from Game_log order by Serial desc limit 10;")
    
    
    Lb1=tkinter.Label(root4,text="Player1",font=("Calibri",18),fg="Red")
    Lb2=tkinter.Label(root4,text="Player2",font=("Calibri",18),fg="Red")
    Lb3=tkinter.Label(root4,text="Winner",font=("Calibri",18),fg="Red")

    Lb1.grid(row=0,column=0)
    Lb2.grid(row=0,column=1)
    Lb3.grid(row=0,column=2)

    i=1
    for playr in cur:
        for j in range(len(playr)):
            e = tkinter.Entry(root4, font=("Calibri",18),width=14, fg='black',highlightthickness=1) 
            e.grid(row=i, column=j,ipady=10) 
            e.insert("end",playr[j])
        i=i+1   

#To make the Help window
def Help():
    root1=tkinter.Tk()
    root1.geometry("600x275")
    root1.title("Help")

    #Instructions regarding the game
    label1=tkinter.Label(root1,fg="Red",text="INSTRUCTIONS")
    label2=tkinter.Label(root1,text="1) Player1 uses the keys W and S to move up and down respectively.")
    label3=tkinter.Label(root1,text="2) Player2 uses the arrow keys 'up' and 'down' to do the same.")
    label4=tkinter.Label(root1,text="3) The key 'P', can be used to reset ball's position")
    label5=tkinter.Label(root1,text="4)The player to score 10 points first wins the game.")
    label6=tkinter.Label(root1,text="5)While logging in to play the game names containing \n only 8 alphanumeric characters are allowed.")
                         
    label1.config(font=("Helvetica",20))
    label2.config(font=("Helvetica",18))
    label3.config(font=("Helvetica",18))
    label4.config(font=("Helvetica",18))
    label5.config(font=("Helvetica",18))
    label6.config(font=("Helvetica",18))
    
    label1.pack(pady=18)
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    label6.pack()
    
def Exit():
    root.destroy()
    
#Main window
root=tkinter.Tk()
button1=tkinter.Button(root,text="Play",fg="black",height=2,width=5, command=play)
button2=tkinter.Button(root,text="Game Log",fg="black",height=2,width=10, command=Highscore)
button3=tkinter.Button(root,text="Help",fg="black",height=2,width=5, command=Help)
button4=tkinter.Button(root,text="Exit",fg="black",height=2,width=5,command=Exit)

myfont=font.Font(family="Helvetica",size=22)

button1["font"]=myfont
button2["font"]=myfont
button3["font"]=myfont
button4["font"]=myfont

root.title("Pong")
root.geometry("800x700")
root.configure(bg="#124FC1")

#Connecting to MySql database.
con=mc.connect(host="localhost",user="root",database="sample",passwd="123456789")
cur=con.cursor()

#To insert the Pong image 
# C=tkinter.Canvas(root,height=0,width=0)
# filename = tkinter.PhotoImage(file = "PongImg1.png")
# img_label = tkinter.Label(root, image=filename)
# img_label.pack(pady=15)
# C.pack()

button1.pack(pady=15)
button2.pack()
button3.pack(pady=15)
button4.pack()

root.mainloop()