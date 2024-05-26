#ADAM FOUTIH; CHADI AL KERDI; BOUENDJA KEVEEN;

import math
import pygame
from random import*
from pygame import*
from pygame.gfxdraw import*

##CHEMIN_RESSOURCE = "ressources"
##def ressources\(ressource):
##    try:
##        base_path = sys._MEIPASS
##    except Exception:
##        base_path = os.path.abspath(".")
##    return os.path.join(base_path, CHEMIN_RESSOURCE) + "/" + ressource
class Porte:
    def __init__(self, nom, ouverture,xmin,ymin):
        self.nom = nom
        self.ouverture = bool(ouverture)
        self.xmin = xmin
        self.ymin = ymin
    def ouvrir(self):
        if self.ouverture == False:
            fenetre.blit(image.load(self.nom[0]).convert(), (self.xmin,self.ymin))
            display.flip()
            time.wait(500)
            self.ouverture = True
        elif self.ouverture == True:
            fenetre.blit(image.load(self.nom[1]).convert(),( self.xmin,self.ymin ))
            display.flip()
            time.wait(500)
            self.ouverture = False

class Fenetre:
    def __init__(self, nom, volet, ouverture):
        self.nom = str(nom)
        self.volet = int(volet)
        self.ouverture = bool(ouverture)


class Passage:
    def __init__(self, xmin,xmax,ymin,ymax,ancienfond,fond):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.ancienfond = ancienfond
        self.fond = fond
    def passer(self):
        self.ancienfond[1] = False
        fenetre.blit(image.load(self.fond[0]).convert(),(0,0))
        self.fond[1]= True
        display.flip()

class Domaine:
    def __init__(self, porte, FENETRE, passage, fond):
        self.porte = porte
        self.FENETRE = FENETRE
        self.fond = fond
        self.passage = passage
    def afficher(self):
        fenetre.blit(image.load(self.fond[0]).convert(),(0,0))
        self.fond[1]= True
        if self.porte.ouverture == True:
            fenetre.blit(image.load(self.porte.nom[0]).convert(),(self.porte.xmin,self.porte.ymin))
        display.flip()

#initialisation
pygame.init()
largeur = 1000
hauteur = 600
fenetre = display.set_mode((largeur, hauteur))
display.set_caption("Escape Christmas")

#fond
fond1= ["ressources\salon.png",False]
fond2= ["ressources\cuisine.jpg",False]
fond3= ["ressources\chambre-enfant.jpg",False]
chambre_enfant2 = image.load("ressources\chambre-enfant2.jpg").convert_alpha()
chambre_enfant3 = image.load("ressources\chambre-enfant3.jpg").convert_alpha()
fond4 = ["ressources\chambre.jpg",False]
chambre2 = image.load("ressources\chambre2.jpg").convert_alpha()
chambre3 = image.load("ressources\chambre3.jpg").convert_alpha()

fenetre2= Fenetre('hk',0,False)

#porte
porte1=Porte(["ressources\porteouverte.png","ressources\porteferme.png"],False,760,160)
porte2= Porte(["ressources\cuisine.jpg","ressources\cuisine.jpg"],False,0,0)
porte3= Porte(["ressources\longueporteouverte.png","ressources\longueportefermee.png"],False,798,133)
porte4= Porte(["ressources\grandeporteouverte.png","ressources\grandeportefermee.png"],False,0,48)

#passage
passage1 = [Passage(0,60,140,486,fond1,fond2), Passage(122,268,35,130,fond1,fond3),Passage(760,860,160,410,fond1,fond4)]
passage2=  Passage(950,1000,0,600,fond2,fond1)
passage3 = Passage(798,979,133,476,fond3,fond1)
passage4 = Passage(0,95,48,536,fond4,fond1)

#salle
salle1 = Domaine(porte1,"e",passage1,fond1)
salle2= Domaine(porte2,fenetre2,passage2,fond2)
salle3= Domaine(porte3,'e',passage3, fond3)
salle4 = Domaine(porte4,'e',passage4,fond4)

image_p="ressources\pere.png"
papanoel=[[0,360],image.load(image_p).convert_alpha()]

#dialogue perenoel
dialogue=image.load("ressources\dialogue.png").convert_alpha()
dialogue2=image.load("ressources\dialogue2.png").convert_alpha()
noir=(0,0,0)
police=font.Font(None,30)
bonjour=police.render("Bonjour, je suis le père noel",1,noir)
aide=police.render("Peux tu m'aider à sortir d'ici ?!",1,noir)

e_chambre=police.render("La porte est ouverte entrons !",1,noir)
e_chambre_enfant=police.render("Montons à l'étage !",1,noir)
e_cuisine= police.render("Je vois une salle ici !",1,noir)

cadena= police.render("Il y a un cadena sur la fenêtre !",1,noir)
cadena2= police.render("Essayons de trouver la clé ",1,noir)
cadena3=police.render("Ouvrons la fenêtre!",1,noir)

no_escape=police.render("Il n'y a pas de sortie ici ",1,noir)
recherche=police.render("Trouvons un indice ou une clé ",1,noir)

lettre= police.render("Oh il y a une lettre !",1,noir)

cle= police.render("Oh voilà une clé !",1,noir)
prise_cle= police.render("Je vais prendre cette clé ",1,noir)

etroit= police.render("La fenêtre est trop étroite" ,1,noir)
etroite= police.render("je ne peux pas sortir par là" ,1,noir)
air1=police.render("Un courant d'air a fait tomber ",1,noir)
air2=police.render("  quelque chose ailleurs !!",1,noir)
vent= image.load('ressources\ent.png').convert_alpha()

#menu du debut
menu = image.load("ressources\menu.png").convert_alpha()
fin = image.load("ressources\in.png").convert_alpha()
fenetre.blit(menu,(0,0))
display.flip()
musique=mixer.music.load("ressources\musique.mp3" )
mixer.music.play( )



debut=1
a=1
x=0
quitter = 1
d=1
scenar=0
final=0
print("debut")
while quitter:
    for  event in pygame.event.get():


            #commencer
        if event.type == MOUSEBUTTONDOWN and debut==1:
            pointclic = mouse.get_pos()
            if 690 >= pointclic[0] >= 305 and 205 <= pointclic[1] <= 320:
                salle1.afficher()
                debut=0
                x=1
        #mouvement du perenoel dans salle1
        if salle1.fond[1] == True:
            #le pere noel revient de la cuisine
            if x==1 or x==2:
                x=0
                papanoel[0]=[-50,360]
                while papanoel[0][0]<800 :
                    for i in range(1,4):
                        if papanoel[0][0]<800:
                            salle1.afficher()
                            fenetre.blit(papanoel[1],(papanoel[0]))
                            display.flip()
                            papanoel[0][0]=papanoel[0][0]+50
                            time.wait(50)
                            papanoel[1]=pygame.transform.rotate(papanoel[1], 90*i)
                    if papanoel[0][0]>=800 :
                        salle1.afficher()
                        papanoel[1]=image.load(image_p).convert_alpha()
                        fenetre.blit(papanoel[1],(papanoel[0]))
                        fenetre.blit(dialogue,(papanoel[0][0]-350,papanoel[0][1]+40))
                        fenetre.blit(bonjour,(papanoel[0][0]-300,papanoel[0][1]+60))
                        fenetre.blit(aide,(papanoel[0][0]-310,papanoel[0][1]+85))
                        display.flip()
            if x==3:
                #le pere noel revient de la chambre pour enfant
                x=0
                papanoel[0]=[100,100]
                papanoel[1]=image.load(image_p).convert_alpha()
                while papanoel[0]<[800,360]:
                    while papanoel[0][1]<360:
                        salle1.afficher()
                        fenetre.blit(papanoel[1],(papanoel[0]))
                        display.flip()
                        time.wait(20)
                        papanoel[0][1]=papanoel[0][1]+20
                    while papanoel[0][0]<800:
                        for i in range(1,4):
                            if papanoel[0][0]<800:
                                salle1.afficher()
                                fenetre.blit(papanoel[1],(papanoel[0]))
                                display.flip()
                                papanoel[0][0]=papanoel[0][0]+50
                                time.wait(50)
                                papanoel[1]=pygame.transform.rotate(papanoel[1], 90*i)
                        salle1.afficher()
                        papanoel[1]=image.load(image_p).convert_alpha()
                        fenetre.blit(papanoel[1],(papanoel[0]))
                        display.flip()
            if x==4:
                #le pere noel revient de la chambre parentale
                x=0
                papanoel[0]=[680,200]
                for i in range(8):
                                salle1.afficher()
                                papanoel[1] =image.load(image_p).convert_alpha()
                                papanoel[1]=pygame.transform.rotate(papanoel[1],5*(-1)**i)
                                fenetre.blit(papanoel[1],(papanoel[0]))
                                display.flip()
                                time.wait(50)
                                papanoel[0]=[papanoel[0][0]+15,papanoel[0][1]+20]
                salle1.afficher()
                papanoel[1] =image.load(image_p).convert_alpha()
                fenetre.blit(papanoel[1],(papanoel[0]))
                display.flip()

            if event.type == MOUSEBUTTONDOWN  :
                pointclic = mouse.get_pos()
                print(pointclic)
                #entre dans la cuisine
                if salle1.passage[0].xmin <= pointclic[0] <= salle1.passage[0].xmax  and salle1.passage[0].ymin <= pointclic[1] <= salle1.passage[0].ymax:
                    fenetre.blit(dialogue,(papanoel[0][0]-350,papanoel[0][1]+40))
                    fenetre.blit(e_cuisine,(papanoel[0][0]-250,papanoel[0][1]+80))
                    display.flip()
                    time.wait(500)
                    while papanoel[0][0]>(-200) :
                        for i in range(1,4):
                                salle1.afficher()
                                fenetre.blit(papanoel[1],(papanoel[0]))
                                display.flip()
                                papanoel[0][0]=papanoel[0][0]-50
                                time.wait(50)
                                papanoel[1]=pygame.transform.rotate(papanoel[1], 90*i)
                    papanoel[0][0]= 800
                    papanoel[1]=image.load(image_p).convert_alpha()
                    salle1.passage[0].passer()

                #entre dans la chambre enfant
                elif salle1.passage[1].xmin <= pointclic[0] <= salle1.passage[1].xmax  and salle1.passage[1].ymin <= pointclic[1] <= salle1.passage[1].ymax:
                    fenetre.blit(dialogue,(papanoel[0][0]-350,papanoel[0][1]+40))
                    fenetre.blit(e_chambre_enfant,(papanoel[0][0]-250,papanoel[0][1]+80))
                    display.flip()
                    time.wait(500)
                    while papanoel[0][0]>150 :
                        for i in range(1,4):
                            salle1.afficher()
                            fenetre.blit(papanoel[1],(papanoel[0]))
                            display.flip()
                            papanoel[0][0]=papanoel[0][0]-50
                            time.wait(50)
                            papanoel[1]=pygame.transform.rotate(papanoel[1], 90*i)
                    while papanoel[0][1]>100 :
                        salle1.afficher()
                        papanoel[1] =image.load(image_p).convert_alpha()
                        fenetre.blit(papanoel[1],(papanoel[0]))
                        display.flip()
                        time.wait(50)
                        papanoel[0][1]=papanoel[0][1]-20
                    papanoel[0]= [800,360]
                    salle1.passage[1].passer()
                #entre dans la chambre parent
                elif salle1.passage[2].xmin <=pointclic[0] <= salle1.passage[2].xmax and salle1.passage[2].ymin <= pointclic[1] <= salle1.passage[2].ymax:
                    if salle1.porte.ouverture == True:
                        for i in range(8):
                                salle1.afficher()
                                papanoel[1] =image.load(image_p).convert_alpha()
                                papanoel[1]=pygame.transform.rotate(papanoel[1],5*(-1)**i)
                                fenetre.blit(papanoel[1],(papanoel[0]))
                                display.flip()
                                time.wait(50)
                                papanoel[0]=[papanoel[0][0]-15,papanoel[0][1]-20]
                        salle1.porte.ouverture = False
                        salle1.passage[2].passer()
                        papanoel[0]=[0,360]
                        papanoel[1]=image.load(image_p).convert_alpha()


                    else:
                        salle1.porte.ouvrir()
                        fenetre.blit(papanoel[1],(papanoel[0]))
                        fenetre.blit(dialogue,(papanoel[0][0]-350,papanoel[0][1]+40))
                        fenetre.blit(e_chambre,(papanoel[0][0]-320,papanoel[0][1]+80))
                        display.flip()
                        time.wait(500)



            #dans la cuisine
        if salle2.fond[1]==True :
            while papanoel[0][0]>100 :
                for i in range(1,4):
                    if papanoel[0][0]>100:
                        salle2.afficher()
                        fenetre.blit(papanoel[1],(papanoel[0]))
                        display.flip()
                        papanoel[0][0]=papanoel[0][0]-50
                        time.wait(50)
                        papanoel[1]=pygame.transform.rotate(papanoel[1], 90*i)
            if papanoel[0][0]<=100 :
                salle2.afficher()
                papanoel[1]=image.load(image_p).convert_alpha()
                fenetre.blit(papanoel[1],(papanoel[0]))

            if scenar<2:
                fenetre.blit(dialogue2,(papanoel[0][0]+200,papanoel[0][1]+40))
                fenetre.blit(cadena,(papanoel[0][0]+263,papanoel[0][1]+65))
                fenetre.blit(cadena2,(papanoel[0][0]+265,papanoel[0][1]+90))
               # display.flip()

            if scenar== 2:
                fenetre.blit(dialogue2,(papanoel[0][0]+300,papanoel[0][1]+40))
                fenetre.blit(cadena,(papanoel[0][0]+363,papanoel[0][1]+65))
                fenetre.blit(cadena3,(papanoel[0][0]+365,papanoel[0][1]+90))
               # display.flip()

            if scenar ==3 :
                if d==1:
                    fenetre.blit(dialogue2,(papanoel[0][0]+250,papanoel[0][1]+40))
                    fenetre.blit(etroit,(papanoel[0][0]+313,papanoel[0][1]+65))
                    fenetre.blit(etroite,(papanoel[0][0]+313,papanoel[0][1]+90))
                    fenetre.blit(vent,(75,210))
                    display.flip()
                    time.wait(3000)
                    d=d-1
                fenetre.blit(papanoel[1],(papanoel[0]))
                fenetre.blit(dialogue2,(papanoel[0][0]+250,papanoel[0][1]+40))
                fenetre.blit(air1,(papanoel[0][0]+320,papanoel[0][1]+60))
                fenetre.blit(air2,(papanoel[0][0]+320,papanoel[0][1]+90))

            display.flip()






            if  event.type == MOUSEBUTTONDOWN  :
                pointclic = mouse.get_pos()
                print(pointclic)
                #clique sur la fenetre
                if final==1 and 27<= pointclic[0] <= 210  and 90<= pointclic[1] <= 380:
                    salle2.fond[1] = False
                    fenetre.blit(fin,(0,0))
                    display.flip()
                    mixer.music.stop( )
                if scenar==2 and 27<= pointclic[0] <= 49  and 206<= pointclic[1] <= 258:
                    salle2.fond[0]="ressources\cuisine2.jpg"
                    salle2.afficher()
                    fenetre.blit(papanoel[1],(papanoel[0]))
                    display.flip()
                    scenar=3
                    d=1
                #######
                if scenar==3 and 825<=pointclic[0]<=860 and 250<=pointclic[1]<=350:
                    salle2.fond[0]="ressources\cuisine2.jpg"
                    salle2.afficher()
                    image_p= "ressources\pere2.png"
                    papanoel[1]=image.load(image_p).convert_alpha()
                    final=1
                    fenetre.blit(papanoel[1],(papanoel[0]))
                    display.flip()
                # retourne dans le salon
                if salle2.passage.xmin <= pointclic[0] <= salle2.passage.xmax  and salle2.passage.ymin <= pointclic[1] <= salle2.passage.ymax:
                    while papanoel[0][0]<800 :
                        for i in range(1,4):
                            if papanoel[0][0]<800:
                                salle2.afficher()
                                fenetre.blit(papanoel[1],(papanoel[0]))
                                display.flip()
                                papanoel[0][0]=papanoel[0][0]+50
                                time.wait(50)
                                papanoel[1]=pygame.transform.rotate(papanoel[1], 90*i)
                    salle2.passage.passer()
                    x=2
        #dans le chambre enfant
        if salle3.fond[1]==True:
                        while papanoel[0][0]>100 :
                            for i in range(1,3):
                                papanoel[0][0]=papanoel[0][0]-50
                                papanoel[0][1]= papanoel[0][1]-10*(-1)**i
                                time.wait(50)
                                salle3.afficher()
                                fenetre.blit(papanoel[1],(papanoel[0]))
                                display.flip()
                        if scenar==0 and salle3.porte.ouverture==False:
                            fenetre.blit(dialogue2,(papanoel[0][0]+270,papanoel[0][1]+40))
                            fenetre.blit(no_escape,(papanoel[0][0]+355,papanoel[0][1]+65))
                            fenetre.blit(recherche,(papanoel[0][0]+335,papanoel[0][1]+90))
                            display.flip()
                        if event.type == MOUSEBUTTONDOWN :
                            pointclic = mouse.get_pos()

                            if scenar==1 and 348>=pointclic[1] >=306  and 210 <=pointclic[0] <= 248:
                                salle3.fond[0]="ressources\chambre-enfant2.jpg"
                                salle3.afficher()
                                fenetre.blit(papanoel[1],(papanoel[0]))
                                fenetre.blit(dialogue2,(papanoel[0][0]+200,papanoel[0][1]+40))
                                fenetre.blit(cle,(papanoel[0][0]+270,papanoel[0][1]+80))
                                display.flip()
                                time.wait(2000)
                                fenetre.blit(dialogue2,(papanoel[0][0]+200,papanoel[0][1]+40))
                                fenetre.blit(prise_cle,(papanoel[0][0]+270,papanoel[0][1]+80))
                                display.flip()
                                time.wait(2000)
                                scenar=2

                            if scenar==2 and pointclic[1] >=306 and pointclic[1] <= 348 and pointclic[0] >= 210 and pointclic[0] <= 248:
                                salle3.fond[0]="ressources\chambre-enfant3.jpg"
                                image_p = "ressources\pere_cle.png"
                                papanoel[1]=image.load(image_p).convert_alpha()
                                salle3.afficher()
                                fenetre.blit(papanoel[1],(papanoel[0]))
                                display.flip()



                            if salle3.passage.xmin <= pointclic[0] <= salle3.passage.xmax  and salle3.passage.ymin <= pointclic[1] <= salle3.passage.ymax:
                                if salle3.porte.ouverture == True:
                                    salle3.passage.passer()
                                    x=3
                                    salle3.porte.ouverture = False
                                else:
                                    salle3.afficher()
                                    fenetre.blit(papanoel[1],(papanoel[0]))
                                    fenetre.blit(dialogue2,(papanoel[0][0]+200,papanoel[0][1]+40))
                                    fenetre.blit(e_chambre,(papanoel[0][0]+270,papanoel[0][1]+80))
                                    salle3.porte.ouvrir()
                                    display.flip()
                                    time.wait(500)

        #dans la chambre parent
        if salle4.fond[1]==True:
            while papanoel[0][0]<800 :
                for i in range(1,4):
                    if papanoel[0][0]<800:
                        salle4.afficher()
                        fenetre.blit(papanoel[1],(papanoel[0]))
                        display.flip()
                        papanoel[0][0]=papanoel[0][0]+50
                        time.wait(50)
                        papanoel[1]=pygame.transform.rotate(papanoel[1], 90*i)
                papanoel[1]=image.load(image_p).convert_alpha()
            if scenar==0 and salle4.porte.ouverture==False:
                fenetre.blit(dialogue,(papanoel[0][0]-350,papanoel[0][1]+40))
                fenetre.blit(no_escape,(papanoel[0][0]-310,papanoel[0][1]+65))
                fenetre.blit(recherche,(papanoel[0][0]-320,papanoel[0][1]+90))
                display.flip()
            if scenar==3:
                salle4.fond[0]="ressources\chambre_cle.jpg"
                salle4.afficher()
                fenetre.blit(papanoel[1],(papanoel[0]))
                display.flip()

            if event.type == MOUSEBUTTONDOWN  :
                pointclic = mouse.get_pos()
                print(pointclic)


                if pointclic[1] >=350 and pointclic[1] <= 387 and pointclic[0] >= 248 and pointclic[0] <= 325 and scenar==0:
                    salle4.fond[0]="ressources\chambre2.jpg"
                    salle4.afficher()
                    fenetre.blit(papanoel[1],(papanoel[0]))
                    fenetre.blit(dialogue,(papanoel[0][0]-350,papanoel[0][1]+40))
                    fenetre.blit(lettre,(papanoel[0][0]-290,papanoel[0][1]+80))
                    display.flip()
                    time.wait(1000)
                    salle4.fond[0]="ressources\chambre3.jpg"
                    salle4.afficher()
                    scenar=1.1
                    if salle4.porte.ouverture == True:
                        fenetre.blit(image.load(salle4.porte.nom[0]).convert(), (salle4.porte.xmin,salle4.porte.ymin))
                    else:
                         fenetre.blit(image.load(salle4.porte.nom[1]).convert(), (salle4.porte.xmin,salle4.porte.ymin))
                    display.flip()
                if 137 <= pointclic[1] <= 197 and 744 <= pointclic[0] <= 804 and scenar==1.1:
                    salle4.fond[0]="ressources\chambre2.jpg"
                    salle4.afficher()
                    fenetre.blit(papanoel[1],(papanoel[0]))
                    display.flip()
                    scenar=1
                if 220 <= pointclic[1] <= 265 and 550 <= pointclic[0] <= 600 and scenar==3:
                    salle4.fond[0]="ressources\chambre4.jpg"
                    salle4.afficher()
                    fenetre.blit(papanoel[1],(papanoel[0]))
                    display.flip()
                    scenar=3.5
                    time.wait(500)
                if scenar==3.5:
                    salle4.fond[0]="ressources\chambre_cle.jpg"
                    salle4.afficher()
                    fenetre.blit(papanoel[1],(papanoel[0]))
                    display.flip()
                    scenar=3

                if salle4.passage.xmin <= pointclic[0] <= salle4.passage.xmax  and salle4.passage.ymin <= pointclic[1] <= salle4.passage.ymax and scenar!=1.1:
                    if salle4.porte.ouverture == True:
                        while papanoel[0][0]>(-200) :
                                for i in range(1,4):
                                    salle4.afficher()
                                    fenetre.blit(papanoel[1],(papanoel[0]))
                                    display.flip()
                                    papanoel[0][0]=papanoel[0][0]-50
                                    time.wait(50)
                                    papanoel[1]=pygame.transform.rotate(papanoel[1], 90*i)
                        salle4.porte.ouverture = False
                        salle4.passage.passer()
                        x=4
                    else:
                        salle4.porte.ouvrir()
                        fenetre.blit(dialogue,(papanoel[0][0]-350,papanoel[0][1]+40))
                        fenetre.blit(e_chambre,(papanoel[0][0]-320,papanoel[0][1]+80))
                        display.flip()
                        time.wait(500)
        print("milieu")
        if event.type in (QUIT,):
            print("fin")
            pygame.quit()
            quitter = 0