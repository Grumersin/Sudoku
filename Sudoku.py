import turtle as tl
import math

def finestra():
    fin=tl.Screen()
    fin.setup(600,600)
    fin.title("Sudoku")
    return fin
    
def punter():
    tor=tl.Turtle()
    tor.speed(0)
    return tor

def graella(tor,mida):
    tor.penup()
    tor.setheading(225)
    tor.forward(mida*4.5*math.sqrt(2))
    tor.pendown()
    tor.pensize("3")
    tor.setheading(0)
    for i in range(4):
        tor.forward(mida*9)
        tor.left(90)
    tor.pensize("1") 
    for i in range(5):
        tor.setheading(90)
        tor.forward(mida*9)
        tor.right(90)
        tor.forward(mida)
        tor.right(90)
        tor.forward(mida*9)
        tor.left(90)
        tor.forward(mida)
    tor.color("white")
    tor.backward(mida)
    tor.color("black")
    for i in range(5):
        tor.setheading(180)
        tor.forward(mida*9)
        tor.right(90)
        tor.forward(mida)
        tor.right(90)
        tor.forward(mida*9)
        tor.left(90)
        tor.forward(mida)
    tor.color("white")
    tor.backward(mida)
    tor.color("black")
    tor.penup()
    tor.pensize("3")
    tor.left(90)
    tor.pendown()
    tor.forward(mida*3)
    tor.left(90)
    tor.forward(mida*9)
    tor.right(90)
    tor.forward(mida*3)
    tor.right(90)
    tor.forward(mida*9)
    tor.penup()
    tor.left(90)
    tor.forward(mida*3)
    tor.left(90)
    tor.pendown()
    tor.forward(mida*3)
    tor.left(90)
    tor.forward(mida*9)
    tor.right(90)
    tor.forward(mida*3)
    tor.right(90)
    tor.forward(mida*9)
    tor.penup()
    
def posar_numero(x1,y1):
    global tor
    
    tor.penup()
    tor.goto((x1+250)//50,(y1+250)//50)
    text=tl.textinput("Nombre","")
    tor.write(text,False,"center",("Arial",30))
    print(text)
    

fin=finestra()
tor=punter()
graella(tor,60)
#posar_numero(xr,yr,punt)   
    
fin.onscreenclick(posar_numero)
#sudoku()
 
fin.listen()
tl.mainloop()   
#tl.done()    
    
    