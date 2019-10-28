from turtle import Screen, Turtle

radio = 300

pantalla = Screen()
pantalla.setup(620, 420)
pantalla.screensize(600, 400)
pantalla.setworldcoordinates (-50, -150, 350, 250)

tortuga = Turtle()
tortuga.pensize(6)
tortuga.pencolor("green")

"""
tortuga.left(180)
tortuga.forward(130)
tortuga.right(90)
tortuga.forward(20)
tortuga.right(90)
tortuga.circle(15)
tortuga.forward(40)
tortuga.left(90)
tortuga.forward(70)
tortuga.right(90)
tortuga.forward(55)
tortuga.right(90)
tortuga.forward(70)
tortuga.left(90)
tortuga.forward(40)
tortuga.right(90)
tortuga.forward(20)
tortuga.write("pitooperrooo")
"""
tortuga.dot(180)
tortuga.forward(130)
tortuga.dot(90)
tortuga.forward(20)
tortuga.dot(90)

tortuga.forward(40)
tortuga.dot(90)

pantalla.exitonclick()

