import matplotlib.pyplot as plt
from pylab import *
from scipy.stats import linregress
from math import *
#Salut Romain
#Moyenne des températures d'une année à Paris
def moyenne_paris(annee):
    fichier = open('TM_PARIS.csv','r')
    somme=0
    j=0
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")
        if ligne[0]==str(annee) :
            for i in range(1,13):
                if ligne[i]!='':
                    somme=somme+float(ligne[i])
                    j=j+1
    if j!=0:
        return somme/j
    else:
        return 0

#Moyenne des températures d'une année en Angleterre
def moyenne_angleterre(annee):
    fichier = open('TM_ANGLETERRE.csv','r')
    somme=0
    j=0
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")
        if ligne[0]==str(annee) :
            for i in range(1,13):
                if ligne[i]!='':
                    somme=somme+float(ligne[i])
                    j=j+1
    if j!=0:
        return somme/j
    else:
        return 0


# savoir quelle est la température maximale d'un mois choisi
def max_mois(m,lieu):
    if lieu==1:
        fichier = open('TM_PARIS.csv','r')
    if lieu==2:
        fichier = open('TM_ANGLETERRE.csv','r')
    T=0
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")

        if ligne[0]!='' and ligne[int(float(m))]!='':
            #print(ligne[0])
            a=ligne[0]
            test=float(ligne[int(float(m))])
            #print(test)
            if test>T:
                T=test
                annee=ligne[0]
    fichier.close()
    return T

# savoir quelle est la température maximale d'un mois choisi
def min_mois(m,lieu):
    if lieu==1:
        fichier = open('TM_PARIS.csv','r')
    if lieu==2:
        fichier = open('TM_ANGLETERRE.csv','r')
    T=1000
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")

        if ligne[0]!='' and ligne[int(float(m))]!='':
            #print(ligne[0])
            a=ligne[0]
            test=float(ligne[int(float(m))])
            #print(test)
            if test<T:
                T=test
                annee=ligne[0]
    fichier.close()
    return T


# connaitre la température moyenne d'un mois choisi
def moyenne_mois(m,lieu):
    if lieu==1:
        fichier = open('TM_PARIS.csv','r')
    if lieu==2:
        fichier = open('TM_ANGLETERRE.csv','r')
    moyenne= -m
    nbr_annee=0
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")
        if ligne[m]!='':
            moyenne=moyenne+float(ligne[m])
            nbr_annee=nbr_annee+1
    fichier.close()
    return moyenne/nbr_annee

#Moyenne d'une année
def moyenne_annee(annee,lieu):
    if lieu==1:
        fichier = open('TM_PARIS.csv','r')
    else :
        fichier = open('TM_ANGLETERRE.csv','r')
    somme=0
    test=0
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")

        if ligne[0]==str(annee) :                       # test si le premier élément de la ligne est 'annee'
            somme=0                                     # Initialise la somme des température à 0
            for i in range(1,13):                       # Pour i variant de 1 (janvier) à 12 (décembre)
                if ligne[i]=='':                        # Test s'il y a bien une valeur de température
                    somme=somme+0
                    test=test+1
                else:
                    temperature=float(ligne[i])         # La température est égale au nombre entre guillemets
                    somme=somme+temperature

    fichier.close()
    return somme/(12-test)

#Moyenne d'une ville sur 1 an
def moyenne_ville(lieu):
    somme=0
    if lieu==1:
        for i in range(1676,2019):
            somme=somme+moyenne_annee(i,1)
        moyenne=somme/(305)
    if lieu==2:
        for i in range(1659,2018):
            somme=somme+moyenne_annee(i,2)
        moyenne=somme/(359)


    return moyenne

#Fonction pour l'écart-type
def ecart_type(lieu):
    somme=0
    n=0

    if lieu==1:
        fichier = open('TM_PARIS.csv','r')
        moyenneville=moyenne_ville(1)
        for i in range(1676,2019):
            for ligne in fichier:
                ligne=ligne.rstrip('\n')
                ligne=ligne.split(";")
                if ligne[0]==str(i):
                    somme=somme+(moyenne_annee(i,1)-moyenneville)**2
                    n=n+1
        ecart_type=sqrt(somme/n)

    if lieu==2:
        fichier = open('TM_ANGLETERRE.csv','r')
        moyenneville=moyenne_ville(2)
        for i in range(1659,2018):
            for ligne in fichier:
                ligne=ligne.rstrip('\n')
                ligne=ligne.split(";")
                if ligne[0]==str(i):
                    somme=somme+(moyenne_annee(i,2)-moyenneville)**2
                    n=n+1
        ecart_type=sqrt(somme/n)
    fichier.close()
    return ecart_type


#Fonction de tri de liste
def partitionnement(L):
    Li,Ls=[],[]
    e=L[0]

    if len(L)+1>1:
        for j in range (len(L)):
            if L[j]<e:
                Li.append(L[j])
            elif L[j]>e:
                Ls.append(L[j])
    return Li,Ls

def tri_rapide(L):
    if len(L)>1:
        Li,Ls=partitionnement(L)
        Li=tri_rapide(Li)
        Ls=tri_rapide(Ls)
        L=Li+[L[0]]+Ls
    return L

#Fonction graphique
def graphique(n,lieu):
    #tracé d'une première figure
    MaFigure1=plt.figure()      #crée une figure et la sélectionne
    plt.grid(True)              #fait apparaitre un quadrillage

    min=15
    max=15
    for k in range(n):
        if lieu==1:
            annee=int(input("Entrez la valeur d'une annee entre 1676 et 2018 "))
        else :
            annee=int(input("Entrez la valeur d'une annee entre 1659 et 2017 "))

        while ((lieu==1 and (annee>2018 or annee<1676)) or (lieu==2 and (annee>2017 or annee<1659))):
            annee=int(input("L'année saisie est incorrecte, entrez une autre année "))

        print(moyenne_annee(annee,lieu))

        if lieu==1:
            fichier = open('TM_PARIS.csv','r')
        if lieu==2:
            fichier = open('TM_ANGLETERRE.csv','r')

        Abs=[]
        Ord=[]
        for ligne in fichier:
            ligne=ligne.rstrip('\n')
            ligne=ligne.split(";")

            if ligne[0]==str(annee) :
                for i in range(1,13):
                    if ligne[i]!='':
                        x=i
                        y=float(ligne[i])
                        Abs.append(x)
                        Ord.append(y)

                plt.plot(Abs,Ord,label=annee)
    fichier.close()

    # COURBE MOYENNE, MIN, MAX
    if lieu==1:
        fichier = open('TM_PARIS.csv','r')
    if lieu==2:
        fichier = open('TM_ANGLETERRE.csv','r')
    X=[1,2,3,4,5,6,7,8,9,10,11,12]
    Y3=[]
    Y2=[]
    Y1=[]
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")

    for i in range(1,13):
        Y1.append(moyenne_mois(i,lieu))
        Y2.append(max_mois(i,lieu))
        Y3.append(min_mois(i,lieu))

    x = array(X)
    y1 = array(Y1)
    y2 = array(Y2)
    y3 = array(Y3)
    plot(x, y1, "y--", label="temperatures moyennes")
    plot(x, y2, "ro", label="temperatures maximales")
    plot(x, y3, "bo", label="températures minimales")


    plt.title("Températures en fonction du mois de l'année ")
    plt.xlabel("Mois de l'année")
    plt.ylabel("Température en °C")
    plt.legend()
    plt.axis([1,12,-8,26])
    plt.show()
    fichier.close()

#Histogramme de Paris
def histogramme1():
    #tracé d'une première figure
    MaFigure2=plt.figure()      #crée une figure et la sélectionne
    plt.grid(True)              #fait apparaitre un quadrillage

    Abs=[]
    Ord=[]
    moyenne=[]
    mediane=0
    for i in range (1676,2019):
        fichier = open('TM_PARIS.csv','r')
        for ligne in fichier:
            ligne=ligne.rstrip('\n')
            ligne=ligne.split(";")
            if ligne[0]==str(i) :
                moyenne.append(moyenne_annee(i,1))

    moyenneb=tri_rapide(moyenne)

    if len(moyenneb)%2==0:
        mediane=((moyenneb[int(len(moyenneb)/2)]+moyenneb[int(len(moyenneb)/2)+1])/2)

    else :
        mediane=moyenneb[int(len(moyenneb)/2)]

    moyenneville=moyenne_ville(1)
    ecarttype=ecart_type(1)

    axvline(x=mediane, color='g',linewidth=2,label="Médiane")
    axvline(x=mediane-2*ecarttype, color='g', linewidth=2, label="1er quartile")
    axvline(x=mediane+2*ecarttype, color='g', linewidth=2, label="3eme quartile")
    fichier.close()

    for i in range(1676,2019):
        fichier = open('TM_PARIS.csv','r')
        for ligne in fichier:
            ligne=ligne.rstrip('\n')
            ligne=ligne.split(";")
            if ligne[0]==str(i):
                point=(1/(ecarttype*sqrt(2*pi)))*exp(-0.5*((moyenne_annee(i,1)-moyenneville)/ecarttype)**2)
                y=point
                x=moyenne_annee(i,1)
                if x!=0 and y!=0 :
                    Abs.append(x)
                    Ord.append(y)
    plt.plot(Abs,Ord, ".", label = "Courbe Gaussienne")

    plt.hist(moyenne, bins=100, range=(5,15), normed=1, color="red", label ="Paris", alpha = 0.3)
    plt.title("Histogramme des températures à Paris")
    plt.xlabel("Températures en °C (Largeur d'un baton = 0.1°C)")
    plt.ylabel("Nombre d'années")
    plt.legend()
    plt.show()
    fichier.close()

#Histogramme de l'Angleterre
def histogramme2():
    #tracé d'une première figure
    MaFigure4=plt.figure()      #crée une figure et la sélectionne
    plt.grid(True)              #fait apparaitre un quadrillage

    Abs=[]
    Ord=[]
    moyenne2=[]
    mediane=0
    for i in range (1659,2018):
        fichier = open('TM_ANGLETERRE.csv','r')
        for ligne in fichier:
            ligne=ligne.rstrip('\n')
            ligne=ligne.split(";")
            if ligne[0]==str(i) :
                moyenne2.append(moyenne_annee(i,2))

    moyenne2b=tri_rapide(moyenne2)
    if len(moyenne2b)%2==0:
        mediane=((moyenne2b[int(len(moyenne2b)/2)]+moyenne2b[int(len(moyenne2b)/2)+1])/2)
    else :
        mediane=moyenne2b[int(len(moyenne2b)/2)]

    moyenneville=moyenne_ville(2)
    ecarttype=ecart_type(2)

    axvline(x=mediane, color='g',linewidth=2,label="Médiane")
    axvline(x=mediane-2*ecarttype, color='g',linewidth=2, label="1er quartile")
    axvline(x=mediane+2*ecarttype, color='g',linewidth=2, label="3eme quartile")
    fichier.close()

    for i in range(1659,2018):
        point=(1/(ecarttype*sqrt(2*pi)))*exp(-0.5*((moyenne_annee(i,2)-moyenneville)/ecarttype)**2)
        y=point
        x=moyenne_annee(i,2)
        if x!=0 and y!=0 :
            Abs.append(x)
            Ord.append(y)
    plt.plot(Abs,Ord,"r.", label ="Courbe Gaussienne")

    plt.hist(moyenne2, bins=100, range=(5,15), normed=1, color="blue", label ="Angleterre", alpha = 0.3)
    plt.title("Histogramme des températures en Angleterre")
    plt.xlabel("Températures en °C (Largeur d'un baton = 0.1°C)")
    plt.ylabel("Nombre d'années")
    plt.legend()
    plt.show()
    fichier.close()


#courbe des températures moyennes en fonction de l'année et du lieu
def courbe_annee():
    #tracé d'une troisième figure
    MaFigure3=plt.figure()      #crée une figure et la sélectionne
    plt.grid(True)              #fait apparaitre un quadrillage

    X1=[]
    fichier=open('TM_PARIS.csv','r')
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")
        if ligne[0]!='':
            X1.append(float(ligne[0]))
    fichier.close()

    X2=[]
    fichier=open('TM_ANGLETERRE.csv','r')
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")
        if ligne[0]!='':
            X2.append(float(ligne[0]))
    fichier.close()

    Y1=[]
    Y2=[]
    fichier=open('TM_ANGLETERRE.csv','r')
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")
        if ligne[0]!='':
            Y2.append(moyenne_annee(ligne[0],2))
    fichier.close()

    fichier=open('TM_PARIS.csv','r')
    for ligne in fichier:
        ligne=ligne.rstrip('\n')
        ligne=ligne.split(";")
        if ligne[0]!='':
            Y1.append(moyenne_annee(ligne[0],1))
    fichier.close()

    #nuage de points
    x1 = array(X1)
    x2=array(X2)
    y1 = array(Y1)
    y2 = array(Y2)
    plot(x1, y1, "r.", label="Températures moyennes, Paris")
    plot(x2, y2, "b.", label="Températures moyennes, Angleterre")
    xlim(1659,2018)
    ylim(6,15.5)
    title("Températures au fil des années")
    xlabel("Années")
    ylabel("Températures en °C")

    #regression lineaire
    (a,b,rho,_,_) = linregress(x1,y1)
    A = []
    for k in x1 :
        A.append(k*a+b)
    plot(x1,A,c = 'r', label = a)

    (a2,b2,rho2,_,_) = linregress(x2,y2)
    A2 = []
    for k in x2 :
        A2.append(k*a2+b2)
    plot(x2,A2,c = 'b', label = a2)

    legend()
    show()

# Courbe paramétrée
def courbe_parametree():
    MaFigure5=plt.figure()
    plt.grid(True)

    x1=[]
    y1=[]
    x2=[]
    y2=[]
    x3=[]
    y3=[]
    x4=[]
    y4=[]
    X=[]
    Y=[]
    for i in range(1659,1950):
        if (moyenne_paris(i))!=0 and (moyenne_angleterre(i)!=0):
            x1.append(moyenne_paris(i))
            y1.append(moyenne_angleterre(i))
    plt.plot(x1,y1, "b.",label="avant 1950")


    for i in range(1950,2007):
        if (moyenne_paris(i))!=0 and (moyenne_angleterre(i)!=0):
            x3.append(moyenne_paris(i))
            y3.append(moyenne_angleterre(i))
    plt.plot(x3,y3, "r.", label="entre 1950 et 2007")

    for i in range(2007,2050):
        if (moyenne_paris(i))!=0 and (moyenne_angleterre(i)!=0):
            x4.append(moyenne_paris(i))
            y4.append(moyenne_angleterre(i))
    plt.plot(x4,y4, "ro", label="10 dernières années")

    for i in range(1659,2019):
        if (moyenne_paris(i))!=0 and (moyenne_angleterre(i)!=0):
            X.append(moyenne_paris(i))
            Y.append(moyenne_angleterre(i))

    (a,b,rho,_,_) = linregress(X,Y)
    A = []
    for k in X :
        A.append(k*a+b)
    plot(X,A,c = 'k', alpha=0.5)

    xlabel("Moyenne des températures anuelles à Paris")
    ylabel("Moyenne des températures anuelles en Angleterre")
    plt.legend()
    plt.show()

#_________________________Programme principal_______________________
type=int(input("\nEntrez: \n1 pour calculer la moyenne d'une année, \n2 pour afficher le graphique, \n3 pour afficher l'histogramme, \n4 pour afficher la régression linéaire  \n5 pour la courbe paramétrée \n"))

# Si l'utilisateur veut juste calculer des moyennes
if type==1:
    lieu=int(input("Entrez 1 pour Paris et 2 pour Angleterre "))
    while lieu!=2 and lieu!=1:
        lieu=int(input("Entrez 1 pour Paris et 2 pour Angleterre "))
    n=int(input("Combien de moyenne(s) voulez-vous calculer ? "))
    compteur=0
    while compteur<n:
        if lieu==1:
            annee=int(input("Entrez la valeur d'une annee entre 1676 et 2018 "))
        else :
            annee=int(input("Entrez la valeur d'une annee entre 1659 et 2017 "))

        while ((lieu==1 and (annee>2018 or annee<1676)) or (lieu==2 and (annee>2018 or annee<1659))):
            annee=int(input("L'année saisie est incorrecte, entrez une autre année "))
        print("la moyenne de l'année", annee, "est de ",moyenne_annee(annee,lieu), "°C")
        compteur+=1

# Si l'utilisateur veut voir le graphique
if type==2:
    lieu=int(input("Entrez 1 pour Paris et 2 pour Angleterre "))
    while lieu!=2 and lieu!=1:
        lieu=int(input("Entrez 1 pour Paris et 2 pour Angleterre "))
    n=int(input("Combien voulez vous voir d'année(s) sur le graphique ? "))

    supp1=int(input("Avec histogramme (1 oui, 2 non)? "))
    supp2=int(input("Avec régression linéaire (1 oui, 2 non)? "))
    supp3=int(input("Avec la courbe paramétrée (1 oui, 2 non)? "))

    print(graphique(n,lieu))
    if supp1==1:
        print(histogramme1())
        print(histogramme2())
    if supp2==1:
        print(courbe_annee())
    if supp3==1:
        print(courbe_parametree())

# Si l'utilisateur veut voir l'histogramme
if type==3:
    print(histogramme1())
    print(histogramme2())

# Si l'utilisateur veut voir la régression linéaire
if type==4:
    print(courbe_annee())

# Si l'utilisateur veut voir la courbe paramétrée
if type == 5 :
    print(courbe_parametree())
