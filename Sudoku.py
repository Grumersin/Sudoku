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
    if llista[1+posx+posy][1+posxx+posyy]!=0:
        tor.color("white")
        tor.write(llista[1+posx+posy][1+posxx+posyy],False,"left",("Arial",30))
        tor.color("black")
    llista[1+posx+posy][1+posxx+posyy]=text
    if text==0:
        tor.color("white")
        tor.write(int(text),False,"left",("Arial",30))
        tor.color("black")
    else:
        tor.write(int(text),False,"left",("Arial",30))
    
def dibuixar(q,c,nom):    
    tor.penup()
    tor.home()
    if q==0:
        tor.setheading(135)
        tor.forward(180*math.sqrt(2))
    if q==1:
        tor.setheading(90)
        tor.forward(60*3)
    if q==2:
        tor.setheading(45)
        tor.forward(180*math.sqrt(2))
    if q==3:
        tor.setheading(180)
        tor.forward(60*3)
    if q==5:
        tor.forward(60*3)
    if q==6:
        tor.setheading(225)
        tor.forward(180*math.sqrt(2))
    if q==7:
        tor.setheading(270)
        tor.forward(60*3)
    if q==8:
        tor.setheading(315)
        tor.forward(180*math.sqrt(2))
    
    if c==0:
        tor.setheading(135)
        tor.forward(60*math.sqrt(2))
    if c==1:
        tor.setheading(90)
        tor.forward(60)
    if c==2:
        tor.setheading(45)
        tor.forward(60*math.sqrt(2))
    if c==3:
        tor.setheading(180)
        tor.forward(60)
    if c==5:
        tor.setheading(0)
        tor.forward(60)
    if c==6:
        tor.setheading(225)
        tor.forward(60*math.sqrt(2))
    if c==7:
        tor.setheading(270)
        tor.forward(60)
    if c==8:
        tor.setheading(315)
        tor.forward(60*math.sqrt(2))
    tor.setheading(180+63.435)
    tor.forward(10*math.sqrt(5))
    tor.color("grey")
    tor.write(nom,False,"left",("Arial",30))
    tor.color("black")
    llista[q][c]=nom
    
    
def eliminar_possib(possib,i,j,n):
    for m in range(9): #quadrat
        x=(n in possib[i][m])
        if x==True:
            possib[i][m].remove(n)        
    fila=[]
    for m in range(3): #fila
        if i<3:
            k=0
        elif i>5:
            k=6
        else:
            k=3
        if j<3:
            l=0
        elif j>5:
            l=6
        else:
            l=3
        fila.append([k+m,0+l])
        fila.append([k+m,1+l])
        fila.append([k+m,2+l])
#    print(fila)
    for m in range(len(fila)):
        x=(n in possib[fila[m][0]][fila[m][1]])
        if x==True:
            possib[fila[m][0]][fila[m][1]].remove(n)
    columna=[]
    for m in range(3): #columna
        if i==0 or i==3 or i==6:
            k=0
        if i==1 or i==4 or i==7:
            k=1
        if i==2 or i==5 or i==8:
            k=2
        if j==0 or j==3 or j==6:
            l=0
        if j==1 or j==4 or j==7:
            l=1
        if j==2 or j==5 or j==8:
            l=2
        columna.append([m*3+k,l])
        columna.append([m*3+k,l+3])
        columna.append([m*3+k,l+6])
#    print(columna)
    for m in range(len(columna)):
        x=(n in possib[columna[m][0]][columna[m][1]])
        if x==True:
            possib[columna[m][0]][columna[m][1]].remove(n)
    
    
def sudoku(xr,yr):
    global tor
    global llista
    
    if xr<60*4.5 and xr>-60*4.5 and yr<60*4.5 and yr>-60*4.5:
        posar_numero(xr,yr,tor,llista)
    else:
        resoldre(llista,tor)
        
    
def analitzar_llista(llista):
    suma=0
    for i in range(len(llista)):
        for j in range(i):
            if i!=j and llista[i]!=0  and llista[j]!=0:
                if llista[i]==llista[j]:
#                    print(f"Error: el valor en la posició {i} ({llista[i]}) és igual al valor en la posició {j} ({llista[j]}).")
                    suma+=1
    if suma!=0:
        error=True
        return error
    else:
        error=False
        return error


def resoldre(llista,tor):
    nombres=['1','2','3','4','5','6','7','8','9']
    possib=[[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]]
    for i in range(9): #quadrat
        for j in range(9): #cel·la
            if llista[i][j]==0:
                cont=0
                while cont<9:
                    llista[i][j]=nombres[cont]
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
#                    print(f"fila:{fila},{i},{j}")
                    error1=analitzar_llista(fila)
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
#                    print(f"columna:{columna},{i},{j}")
                    error2=analitzar_llista(columna)
#                    print(f"quadrat:{llista[i]},{i},{j}")
                    error3=analitzar_llista(llista[i])
                    llista[i][j]=0
                    if error1==False and error2==False and error3==False:
                        possib[i][j].append(nombres[cont])                       
                    cont+=1
#                print(f"possib:{possib[i][j]},{i},{j}")
                if len(possib[i][j])==1 and cont==9:
                    dibuixar(i,j,possib[i][j][0])
                    eliminar_possib(possib,i,j,possib[i][j][0])
                    
    for n in range(9): #quadrat
        for i in range(9): #els 9 nombres
            sumx=0
            sumy=0
            sumz=0
            nomx=0
            nomy=0
            nomz=0
            for j in range(9): #cel.la
                x=(nombres[i] in possib[n][j]) #mira en el quadrat
                if x==True:
                    sumx+=1
                    qx=n
                    cx=j
                    nomx=nombres[i]
                fila=[]
                for my1 in range(3): #fila
                    if n<3:
                        kx=0
                    elif n>5:
                        kx=6
                    else:
                        kx=3
                    if j<3:
                        l=0
                    elif j>5:
                        l=6
                    else:
                        l=3
                    fila.append([kx+my1,0+l])
                    fila.append([kx+my1,1+l])
                    fila.append([kx+my1,2+l])
            #    print(fila)
                for my2 in range(len(fila)):
                    y=(nombres[i] in possib[fila[my2][0]][fila[my2][1]])
                    if y==True:
                        sumy+=1
                        qy=n
                        cy=j
                        nomy=nombres[i]
                columna=[]
                for mz1 in range(3): #columna
                    if n==0 or n==3 or n==6:
                        ky=0
                    if n==1 or i==4 or n==7:
                        ky=1
                    if n==2 or n==5 or n==8:
                        ky=2
                    if j==0 or j==3 or j==6:
                        l=0
                    if j==1 or j==4 or j==7:
                        l=1
                    if j==2 or j==5 or j==8:
                        l=2
                    columna.append([mz1*3+ky,l])
                    columna.append([mz1*3+ky,l+3])
                    columna.append([mz1*3+ky,l+6])
#                print(mz1,ky,mz1*3+k)
            #    print(columna)
                for mz2 in range(len(columna)):
#                    print("mz2",mz2)
#                    print("columna",columna)
#                    print("columna[mz2]",columna[mz2])
#                    print("possib[columna[mz2][0]]",possib[columna[mz2][0]])
#                    print("len(possib[columna[mz2][0]])",len(possib[columna[mz2][0]]))
                    z=(nombres[i] in possib[columna[mz2][0]][columna[mz2][1]])
                    if z==True:
                        sumz+=1
                        qz=n
                        cz=j
                        nomz=nombres[i]               
#            print(f"possibilitats en el quadrat {n}: {possib[n]}")
#            print(nomx,sumx)
            if sumx==1:
#                print(nomx,"únic", (qx,cx))
                dibuixar(qx,cx,nomx)
                eliminar_possib(possib,qx,cx,nomx)
#            print(f"possibilitats en el quadrat {n}: {possib[n]}")
            if sumy==1:
#                print(nomy,"únic", (qy,cy))
                dibuixar(qy,cy,nomy)
                eliminar_possib(possib,qy,cy,nomy)
#            print(f"possibilitats en el quadrat {n}: {possib[n]}")
            if sumz==1:
#                print(nomz,"únic", (qz,cz))
                dibuixar(qz,cz,nomz)
                eliminar_possib(possib,qz,cz,nomz)
#            print(f"possibilitats en el quadrat {n}: {possib[n]}")

fin=finestra()
tor=punter()
graella(tor,60)

llista=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]  
    
fin.onscreenclick(sudoku)
 
fin.listen()
tl.mainloop()   
#tl.done()    
    