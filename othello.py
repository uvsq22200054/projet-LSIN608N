import tkinter as tk 
import numpy as np

player=0
cases={}
pions=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
noms_j={0:'black',1:'white'}


class Othellier:
    def __init__(self,player):
        self.joueurs={1:'white',0:'black'}
        self.matrice=np.zeros((8,8),dtype=object)
        self.matrice[4,4]=Pion(0,(4,4))
        self.matrice[4,5]=Pion(1,(4,5))
        self.matrice[5,4]=Pion(1,(5,4))
        self.matrice[5,5]=Pion(0,(5,5))
        self.player=player

class Pion():
    def __init__(self,couleur,coord):
        self.couleur=couleur
        self.coordonnee=coord
    def get_couleur(self):
        return self.couleur
    def change_couleur(self,nv_couleur):
        self.couleur=nv_couleur
    def get_coordonnee(self):
        return self.coordonnee
    
othellier=Othellier(0)

for i in range(0,800,100):
    for j in range(0,800,100):
        if pions[i//100][j//100]==0:
            cases[(i,j)]='false'
        elif pions[i//100][j//100]==1:
            cases[(i,j)]='black'
        else:
            cases[(i,j)]='white'

def jeu(matrice,player):
    if player==0:
        actual='black'
        oppose='white'
    else:
        actual='white'
        oppose='black'
    global cases
    pions_atraiter=[]
    possibilite={}
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j]==player+1:
                pions_atraiter.append((i,j))
    for elem in pions_atraiter:
        possibilite[elem]=[]
        x,y=elem
        encercler=[]
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if (i>=0  and i<=7) and ( j>=0 and  j<=7) and cases[(i*100,j*100)]==oppose:
                    encercler.append((i,j))
        for pb in encercler:
            w,z=pb
            # sur la meme ligne
            if x==w:
                k=z
                #si pion opposé est a gauche du pion du joueur
                if y>z:
                    while k>=0:
                        if cases[(w*100,k*100)]=='false':
                            if (w,k) not in list(possibilite.values()):
                                possibilite[elem].append((w,k))
                            break
                        if cases[(w*100,k*100)]==actual:
                            break
                        k-=1
                #si pion opposé est a droite du pion du joueur   
                if y<z:
                    while k<8:
                        if cases[(w*100,k*100)]=='false':
                            if (w,k) not in list(possibilite.values()):
                                possibilite[elem].append((w,k))
                            break
                        if cases[(w*100,k*100)]==actual:
                            break
                        k+=1 
            
            # sur la meme colonne
            if y==z:
                #pion oppose en dessous du pion du joueur
                if x>w:
                    k=w
                    while k>=0:
                        if cases[(k*100,z*100)]=='false':
                            if (k,z) not in list(possibilite.values()):
                                possibilite[elem].append((k,z))
                            break
                        if cases[(k*100,z*100)]==actual:
                            break
                        k-=1
                #pion oppose au dessus du pion du joueur  
                if x<w:
                    k=w
                    while k<8:
                        if cases[(k*100,z*100)]=='false':
                            if (k,z) not in list(possibilite.values()):
                                possibilite[elem].append((k,z) )
                            break
                        if cases[(k*100,z*100)]==actual:
                            break
                        k+=1 
            # sur la diagonale
            #diagonale en haut a gauche  
            if x==w+1 and y==z+1:
                k=w
                l=z
                while k>=0 and k<8 and l>=0 and l<8:
                    if cases[(k*100,l*100)]=='false':
                        if (k,l) not in list(possibilite.values()):
                            possibilite[elem].append((k,l))
                            print('A','pos:',(k,l))
                        break
                    if cases[(k*100,l*100)]==actual:
                            break
                    
                    k-=1
                    l-=1
                
            #digonale en bas a droite
            if x==w-1 and y==z-1:
                k=w
                l=z
                while k>=0 and k<8 and l>=0 and l<8:
                    if cases[(k*100,l*100)]=='false':
                        if (k,l) not in list(possibilite.values()):
                            possibilite[elem].append((k,l))
                            print('B','pos:',(k,l))
                        break
                    if cases[(k*100,l*100)]==actual:
                            break
                    
                    k+=1
                    l+=1
                
            #en bas a gauche
            if x==w-1 and y==z+1:
                k=w
                l=z
                while k>=0 and k<8 and l>=0 and l<8:
                    if cases[(k*100,l*100)]=='false':
                        if (k,l) not in list( possibilite.values()):
                            possibilite[elem].append((k,l))
                            print('C','pos:',(k,l))
                        break
                    
                    k+=1
                    l-=1
            #en haut a droite
            if x==w+1 and y==z-1:
                k=w
                l=z
                while k>=0 and k<8 and l>=0 and l<8:
                    if matrice[k][l]==0:
                        if (k,l) not in list(possibilite.values()):
                            possibilite[elem].append((k,l))
                            print('D','pos:',(k,l))
                        break
                    if matrice[k][l]==player+1:
                        break
                   
                    k-=1
                    l+=1
    return possibilite

     
def changement_couleur(plateau,cases,player,coord1,coord2):
    global noms_j,pions
    
    x,y=coord1[0]//100,coord1[1]//100  #coord du pion que l'on vient de placer
    w,z=coord2 #coord du deuxieme point encadrant
    #meme ligne ou meme colonne
    if (x==w and y!=z) or (x!=w and y==z):
        for i in range(min(x, w), max(x, w)+1):
            for j in range(min(z, y), max(z, y)+1):
                pions[i][j]=player+1
                cases[i*100,j*100]=noms_j[player]
                plateau.create_oval(j*100+35,i*100+35,j*100+65,i*100+65,fill=noms_j[player])
    #diagonale
    if x!=w and y!=z:
        if w<x and z<y:
            #diagonale en bas a droite
            i=w
            j=z
            while i>0 and i<x and j<y:
                pions[i][j]=player+1
                cases[i*100,j*100]=noms_j[player]
                plateau.create_oval(j*100+35,i*100+35,j*100+65,i*100+65,fill=noms_j[player])
                j+=1
                i+=1
        # en haut a gauche
        if w>x and z>y:
            i=w
            j=z
            
            while i>x and j>y:
                pions[i][j]=player+1
                cases[i*100,j*100]=noms_j[player]
                plateau.create_oval(j*100+35,i*100+35,j*100+65,i*100+65,fill=noms_j[player])
                j-=1
                i-=1
        # en haut a droite
        if w>x and z<y:
            i=x
            j=y
            while i>0 and i<w and j>z:
                pions[i][j]=player+1
                cases[i*100,j*100]=noms_j[player]
                plateau.create_oval(j*100+35,i*100+35,j*100+65,i*100+65,fill=noms_j[player])
                j-=1
                i+=1
        #en bas a gauche
        if x>w and y<z:
            i=w
            j=z
            while i>0 and i<x and j>y:
                pions[i][j]=player+1
                cases[i*100,j*100]=noms_j[player]
                plateau.create_oval(j*100+35,i*100+35,j*100+65,i*100+65,fill=noms_j[player])
                j-=1
                i+=1
                        
        
            
    
def get_coord(event,canvas):
    dessine_pion(canvas,(event.x,event.y))
def dessine_pion(plateau,couple,yellow_circles,canvas_pions):
    global player
    global cases
    global pions
    x_non_arrondis,y_non_arrondis=couple
    x=x_non_arrondis-x_non_arrondis%100
    y=y_non_arrondis-y_non_arrondis%100
    couleur=noms_j[player]
    poss=jeu(pions,player)
    temp=[]
    for key,val in poss.items():   
        if (y//100,x//100) in val and cases[(y,x)]=='false':
            temp.append(key)
    for elem in temp:
        print(player)
        plateau.create_oval(x+35,y+35,x+65,y+65,fill=couleur)
        if player==0:
            pions[y//100][x//100]=1
            cases[(y,x)]='black'
        else:
            pions[y//100][x//100]=2
            cases[(y,x)]='white'
        print(temp)
        changement_couleur(plateau,cases,player,(y,x),elem)
    player=(player+ 1)%2
        
    for circle in yellow_circles:
        plateau.delete(circle)
        
    # definir les cercles de possibilites
    yellow_circles.clear()
    futur_poss=jeu(pions,player)
    for liste in futur_poss.values():
        for pion in liste:
            px, py = pion
            circle = plateau.create_oval(py * 100 + 35, px * 100 + 35, py * 100 + 65, px * 100 + 65, outline='yellow', width=3)
            yellow_circles.append(circle)
    
    
   
def interface():
    global cases,player
    root=tk.Tk()
    root.title('Othello')
    yellow_circles=[]
    canvas_pions={}
    
    
    plateau=tk.Canvas(root,width=800,height=800,background='green')
    # plateau.bind("<Button-1>", lambda event: dessine_pion(plateau, (event.x, event.y), yellow_circles,canvas_pions))
    # possib=jeu(pions,player)
    # for liste in possib.values():
    #     for pion in liste:
    #         px, py = pion
    #         circle = plateau.create_oval(py * 100 + 35, px * 100 + 35, py * 100 + 65, px * 100 + 65, outline='yellow', width=3)
    #         yellow_circles.append(circle)

    plateau.create_line(100,0,100,800,width=3,fill='black')
    plateau.create_line(200,0,200,800,width=3,fill='black')
    plateau.create_line(300,0,300,800,width=3,fill='black')
    plateau.create_line(400,0,400,800,width=3,fill='black')
    plateau.create_line(500,0,500,800,width=3,fill='black')
    plateau.create_line(600,0,600,800,width=3,fill='black')
    plateau.create_line(700,0,700,800,width=3,fill='black')

    plateau.create_line(0,100,800,100,width=3,fill='black')
    plateau.create_line(0,200,800,200,width=3,fill='black')
    plateau.create_line(0,300,800,300,width=3,fill='black')
    plateau.create_line(0,400,800,400,width=3,fill='black')
    plateau.create_line(0,500,800,500,width=3,fill='black')
    plateau.create_line(0,600,800,600,width=3,fill='black')
    plateau.create_line(0,700,800,700,width=3,fill='black')


    for ligne in othellier.matrice:
        for elem in ligne:
            if elem != 0:
                y,x=elem.get_coordonnee()
                y-=1
                x-=1
                plateau.create_oval(x*100+35,y*100+35,x*100+65,y*100+65,fill=joueurs[elem.get_couleur()])

            
    plateau.grid(row=1,column=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.mainloop()

interface()  


