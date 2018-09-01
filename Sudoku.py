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
    tor.write(int(text),False,"left",("Arial",30))
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
        '''for i in range(len(llista)): #per mirar tots els quadrats
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
                analitzar_llista(columna)'''
        resoldre(llista,tor)
        
    
def analitzar_llista(llista):
    suma=0
    for i in range(len(llista)):
        for j in range(i):
            if i!=j and llista[i]!=0  and llista[j]!=0:
                if llista[i]==llista[j]:
                    print(f"Error: el valor en la posició {i} ({llista[i]}) és igual al valor en la posició {j} ({llista[j]}).")
                    suma+=1
                else:
                    print("Tot correcte")
    if suma!=0:
        print(suma)
        error=True
        return error
    else:
        print(suma)
        error=False
        return error
#            elif llista[i]==0  or llista[j]==0:
#                error=False
#                return error


def resoldre(llista,tor):
    nombres=['1','2','3','4','5','6','7','8','9']
    error=True
    for i in range(9): #quadrat
        for j in range(9): #cel·la
            if llista[i][j]==0:
                cont=0
                while error==True and cont<9:
                    llista[i][j]=nombres[cont]
    #                    for n in range(3): #mira 3 nombres d'un mateix quadrat
                    fila=[]
                    for m in range(3): #mira 3 quadrats consecutius
                        if i<3:
                            k=0
                        elif i>5:
                            k=6
                        else:
                            k=3
                        if j<3:
                            n=0
                        elif j>5:
                            n=6
                        else:
                            n=3
                        fila[100:100]=llista[k+m][0+n:3+n]
                    print(f"fila:{fila},{i},{j}")
                    error1=analitzar_llista(fila)
    #                    for n in range(3): #mira 3 nombres d'un mateix quadrat
                    columna=[]
                    for m in range(3): #mira 3 quadrats diferents
                        if i==0 or i==3 or i==6:
                            k=0
                        if i==1 or i==4 or i==7:
                            k=1
                        if i==2 or i==5 or i==8:
                            k=2
                        if j==0 or j==3 or j==6:
                            n=0
                        if j==1 or j==4 or j==7:
                            n=1
                        if j==2 or j==5 or j==8:
                            n=2
                        columna[100:100]=llista[m*3+k][n],llista[m*3+k][n+3],llista[m*3+k][n+6]
                    print(f"columna:{columna},{i},{j}")
                    error2=analitzar_llista(columna)
                    print(f"quadrat:{llista[i]},{i},{j}")
                    error3=analitzar_llista(llista[i])
                    if error1==False and error2==False and error3==False:
                        error=False
                        tor.penup()
                        tor.home()
                        if i==0:
                            tor.setheading(135)
                            tor.forward(180*math.sqrt(2))
                        if i==1:
                            tor.setheading(90)
                            tor.forward(60*3)
                        if i==2:
                            tor.setheading(45)
                            tor.forward(180*math.sqrt(2))
                        if i==3:
                            tor.setheading(180)
                            tor.forward(60*3)
                        if i==5:
                            tor.forward(60*3)
                        if i==6:
                            tor.setheading(225)
                            tor.forward(180*math.sqrt(2))
                        if i==7:
                            tor.setheading(270)
                            tor.forward(60*3)
                        if i==8:
                            tor.setheading(315)
                            tor.forward(180*math.sqrt(2))
                        
                        if j==0:
                            tor.setheading(135)
                            tor.forward(60*math.sqrt(2))
                        if j==1:
                            tor.setheading(90)
                            tor.forward(60)
                        if j==2:
                            tor.setheading(45)
                            tor.forward(60*math.sqrt(2))
                        if j==3:
                            tor.setheading(180)
                            tor.forward(60)
                        if j==5:
                            tor.setheading(0)
                            tor.forward(60)
                        if j==6:
                            tor.setheading(225)
                            tor.forward(60*math.sqrt(2))
                        if j==7:
                            tor.setheading(270)
                            tor.forward(60)
                        if j==8:
                            tor.setheading(315)
                            tor.forward(60*math.sqrt(2))
                        tor.setheading(180+63.435)
                        tor.forward(10*math.sqrt(5))
                        tor.write(nombres[cont],False,"left",("Arial",30))
                    cont+=1
    

fin=finestra()
tor=punter()
graella(tor,60)

llista=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]  
    
fin.onscreenclick(sudoku)
 
fin.listen()
tl.mainloop()   
#tl.done()    
    
    