import numpy as np
from datetime import datetime, date,timedelta
import calendar
from dateutil.relativedelta import relativedelta
TO=np.array(["date.....","mode d'Operation","Montant"])
def Ajout_lst(L,dop,ch,montant):
    L.append(dop)
    L.append(ch)
    L.append(montant)
print("Bonjour dans la suiveur de votre compte d'epargne\nles régles:\n<1> L'interet est mensuelle\n<2>il ne faut pas mettre les dates des operations a la fin d mois ou au debut de mois et il faut les mets d'une maniere ascendantes\n<3>le tableau sera rempli automatiquement et sera terminer au dernier jour de mois de la dernier operation\n<4>le Mode d'operation: Retrait en especes ou Versement en especes (écrivant en tout lettere 'e' au lieu de'é').  ")
nbop=int(input("nombre d'operation="))
l=[]
for i in range (nbop):
    yra=int(input("annee d'op="))
    mnt=int(input("mois d'op="))
    jr=int(input("jours d'op="))
    dop=date(yra,mnt,jr)
    while True:
        ch=input("Mode d'operation(Retrait en espèces ou Versement en espèces ):")
        if ch=="Retrait en especes" or ch=="Versement en especes":
            break
    montanto=float(input("Montant="))
    Ajout_lst(l,str(dop),ch,str(montanto))
    TO=np.vstack([TO,np.array(l)])
    l.clear()
print(TO)
TF=np.array(["Date opér","Date valeur","Opér","Int.m","Solde","Nbj","TRE","Intbrut"])
montant=float(input("Montant initial="))
yro=int(input("annee de ep:"))
mnto=int(input("mois de ep:"))
jro=int(input("jours de ep:"))
dateep=date(yro,mnto,jro)
intervalle=timedelta(days=7)
dvop=dateep+intervalle
LF=[str(dateep),str(dvop),str(montant),"0.000",str(montant),"0","##","0.000"]
TF=np.vstack([TF,np.array(LF)])
def dernier_jour_du_mois(date):
    annee, mois = date.year, date.month
    dernier_jour = calendar.monthrange(annee, mois)[1]
    return dernier_jour
def calculnbj(date1,date2):
    delta = date1 - date2
    return abs(delta.days)
def supprimer_ligne(matrix, row_index):
    if row_index < 0 or row_index >= matrix.shape[0]:
        print("Indice de ligne invalide.")
        return matrix
    lignes_avant = matrix[:row_index, :]
    lignes_apres = matrix[row_index + 1:, :]
    nouveau_matrix = np.concatenate((lignes_avant, lignes_apres), axis=0)
    return nouveau_matrix
LF1=[]
TRE=2.5
while(TO.shape[0]!=1):
    while ((dvop.month)!=int(TO[1][0][5:7])):
        aux=dvop
        dvop=date(int(dvop.year),int(dvop.month),dernier_jour_du_mois(date(int(dvop.year),int(dvop.month),1)))
        nbj=calculnbj(dvop,aux)
        intb=(montant*nbj*TRE)/36000
        intert=intb*0.8
        montant=montant+intert
        LF1.append("##########")
        LF1.append(str(dvop))
        dvop=dvop+timedelta(days=1)
        LF1.append("0.000")
        LF1.append(str(intert)[:4])
        LF1.append(str(montant)[:6])
        LF1.append(str(nbj))
        LF1.append("2.5%")
        LF1.append(str(intb)[:4])
        TF=np.vstack([TF,np.array(LF1)])
        LF1.clear()
        
    if (dvop.month==int(TO[1][0][5:7])):
        if TO[1][1]=="Retrait en especes":
            LF1.append(TO[1][0])
            aux1=dvop-timedelta(days=1)
            dvop=date(int(TO[1][0][:4]),int(TO[1][0][5:7]),int(TO[1][0][8:]))-intervalle
            nbj=calculnbj(dvop,aux1)
            montant-=float(TO[1][2])
            intb=(montant*nbj*TRE)/36000
            intert=intb*0.8
            montant=montant+intert
            LF1.append(str(dvop))
            LF1.append("-"+TO[1][2])
            LF1.append(str(intert)[:4])
            LF1.append(str(montant)[:6])
            LF1.append(str(nbj))
            LF1.append("2.5%")
            LF1.append(str(intb)[:4])
            TF=np.vstack([TF,np.array(LF1)])
            LF1.clear()
            TO=supprimer_ligne(TO, 1)
        else:
            LF1.append(TO[1][0])
            aux1=dvop-timedelta(days=1)
            dvop=date(int(TO[1][0][:4]),int(TO[1][0][5:7]),int(TO[1][0][8:]))+intervalle
            nbj=calculnbj(dvop,aux1)
            montant+=float(TO[1][2])
            intb=(montant*nbj*TRE)/36000
            intert=intb*0.8
            montant=montant+intert
            LF1.append(str(dvop))
            LF1.append(TO[1][2])
            LF1.append(str(intert)[:4])
            LF1.append(str(montant)[:6])
            LF1.append(str(nbj))
            LF1.append("2.5%")
            LF1.append(str(intb)[:4])
            TF=np.vstack([TF,np.array(LF1)])
            LF1.clear()
            TO=supprimer_ligne(TO, 1)
aux=dvop
dvop=date(int(dvop.year),int(dvop.month),dernier_jour_du_mois(date(dvop.year,dvop.month,1)))
nbj=calculnbj(dvop,aux)
intb=(montant*nbj*TRE)/36000
intert=intb*0.8
montant=montant+intert
LF1.append("##########")
LF1.append(str(dvop))
LF1.append("0.000")
LF1.append(str(intert)[:4])
LF1.append(str(montant)[:6])
LF1.append(str(nbj))
LF1.append("2.5%")
LF1.append(str(intb)[:4])
TF=np.vstack([TF,np.array(LF1)])
LF1.clear()
print(TF)
print("le montant recupere=",montant)