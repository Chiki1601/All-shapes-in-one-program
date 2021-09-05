#All shapes in one program
import turtle     
import time    
screen=turtle.Screen()     
screen.setup(620,470)
t =turtle.Turtle()
t.pencolor('red')     
t.pensize(5)     
t.speed(1)     
num=3    
Shape_Name=['Triangle','Square','Pentagon','Hexagon'
        ,'Heptagon','Octagon','Nonagon','Decagon']
while num<11: 
        for i in range(num):     
            t.pencolor('red')
            t.forward(100)     
            t.right(360/num)    
        t.penup()
        t.setpos(-80,180)    
        t.pendown()
        t.pencolor('blue')
        t.write(' This is a '+Shape_Name[num-3],
                   font=("Arial", 16, "bold"))    
        num=num+1
        time.sleep(1)

        t.penup()
        t.setpos(-num*8,num*14)
        t.pendown()
        t.clear()
