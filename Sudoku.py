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
    global llista
    
    tor.penup()
    tor.goto((x1+30)//60*60-10,(y1+30)//60*60-20)
    text=tl.textinput("Nombre","")
    if text=="exit": #Per quan vulgui parar de posar números i que ho resolgui l'ordi
        return
    else:
        tor.write(text,False,"left",("Arial",30))
        posx=int((x1+90)//180)
        posy=int((y1+90)//180)
        if posy==1:
            posy=0
        elif posy==0:
            posy=3
        elif posy==-1:
            posy=6
        posxx=int((x1+30)//60)
        posyy=int((y1+30)//60)
        if posxx<-1:
            posxx=posxx+3
        elif posxx>1:
            posxx=posxx-3
        if posyy<-1:
            posyy=posyy+3
        elif posyy>1:
            posyy=posyy-3
        if posyy==1:
            posyy=0
        elif posyy==0:
            posyy=3
        elif posyy==-1:
            posyy=6
        llista[1+posx+posy][1+posxx+posyy]=text
        
#def analitzar_columna(llista):
    
#def analitzar_fila(llista):
    
#def analitzar_quadrat(llista):
    

fin=finestra()
tor=punter()
graella(tor,60)

llista=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]  
    
fin.onscreenclick(posar_numero)
#sudoku()
 
fin.listen()
tl.mainloop()   
#tl.done()    
    
    