import turtle

colors  = ["red","purple","blue","green","yellow","orange"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(5)
t.width(20)
length = 10

while length < 500:
     t.fd(length)
     t.pencolor(colors[length%6])
     t.right(89)
     length += 5;
