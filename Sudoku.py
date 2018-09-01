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
    
def posar_numero(x1,y1,tor,llista):
    tor.penup()
    tor.goto((x1+30)//60*60-10,(y1+30)//60*60-20)
    text=tl.textinput("Nombre","")
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
    
def sudoku(xr,yr):
    global tor
    global llista
    
    if xr<60*4.5 and xr>-60*4.5 and yr<60*4.5 and yr>-60*4.5:
        posar_numero(xr,yr,tor,llista)
    else:
        for i in range(len(llista)): #per mirar tots els quadrats
            analitzar_llista(llista[i]) #mira cada quadrat
        for k in range(3): #mira 3 files de quadrats
            for i in range(3): #mira 3 nombres d'un mateix quadrat
                fila=[]
                for j in range(3): #mira 3 quadrats consecutius
                    fila[100:100]=llista[j+3*k][0+3*i:3+3*i]
                print(f"fila:{fila}")
                analitzar_llista(fila)
        for k in range(3): #mira 3 columnes de quadrats
            for i in range(3): #mira 3 nombres d'un mateix quadrat
                columna=[]
                for j in range(3): #mira 3 quadrats diferents
                    columna[100:100]=llista[j*3+k][i],llista[j*3+k][i+3],llista[j*3+k][i+6]
                print(f"columna:{columna}")
                analitzar_llista(columna) 
        
    
def analitzar_llista(llista):
    for i in range(len(llista)):
        for j in range(i):
            if i!=j and llista[i-1]!=0  and llista[j-1]!=0:
                if llista[i-1]==llista[j-1]:
                    print(f"Error: el valor en la posició {i} ({llista[i-1]}) és igual al valor en la posició {j} ({llista[j-1]}).")
#                else:
#                    print("Tot correcte")
    
#def analitzar_quadrat(llista):
    

fin=finestra()
tor=punter()
graella(tor,60)

llista=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]  
    
fin.onscreenclick(sudoku)
 
fin.listen()
tl.mainloop()   
#tl.done()    
    
    