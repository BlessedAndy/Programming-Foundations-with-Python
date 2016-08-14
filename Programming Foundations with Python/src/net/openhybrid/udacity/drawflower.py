'''
Created on Aug 12, 2016

@author: Andy Zhang
'''
import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
    
draw_square

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    #draw square
    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2000)

    for i in range(1,31):
        draw_square(brad)
        brad.right(12)
        
    brad.right(90)
    brad.forward(250)

    window.exitonclick()
      
draw_flower()