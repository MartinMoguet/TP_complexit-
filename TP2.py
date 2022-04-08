

def paires(tabPlaque):
    tabPaire = []
    for i in range (0,6):
        for j in range (0,6):
            if i != j and i <j :
                tabPaire.append((tabPlaque[i],tabPlaque[j]))
    return tabPaire


def ensemble(tabPlaque, a ,b):
    tabEnsembles =[[],[],[],[]]
    tabEnsembles[0].append(a+b)
    if a < b :
        tabEnsembles[1].append(b-a)
    else:
        tabEnsembles[1].append(a-b)
    if b % a == 0 and b!=0:
        tabEnsembles[2].append(b//a)
    elif a % b == 0 and b!=0:
        tabEnsembles[2].append(a//b)
    else :
        tabEnsembles[2].append(a)
        tabEnsembles[2].append(b)
    tabEnsembles[3].append(a*b)

    for i in range (0,len(tabPlaque)):
        if tabPlaque[i] != a and tabPlaque[i] !=b :
            tabEnsembles[0].append(tabPlaque[i])
            tabEnsembles[1].append(tabPlaque[i])
            tabEnsembles[2].append(tabPlaque[i])
            tabEnsembles[3].append(tabPlaque[i])

    return tabEnsembles

    #def recherche(R)

tabPlaque = [50,25,10,7,3,2]
paires(tabPlaque)
#ensemble(tabPlaque, 4,5)