# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:48:13 2020

@author: kevin k
"""

class CompteBancaire:
    def __init__(self, nom = "Dupont", solde = 1000):
        self.nom = nom
        self.solde = solde
    
    def setNom(self, nom):
        self.nom = nom
    def setSolde (self, solde):
        self.solde = solde
    def getNom(self):
        return self.nom
    def getSolde(self):
        return self.solde

    def depot(self,somme):
        depot_comte = self.getSolde()+somme
        self.setSolde(depot_comte)
        #---retrait---#
    def retrait(self,somme):
        retrait_compte = self.getSolde()-somme
        self.setSolde(retrait_compte)
        #---affichage---#
    def affiche(self):
        print("Le solde du compte bancaire de",self.getNom(),"est de",self.getSolde(),'euros')


compte1 = CompteBancaire("Eric", 10000)
compte1.depot(400)
compte1.retrait(150)
compte1.affiche()
#Le solde du compte bancaire de Eric est de 10250 euros



# test voila comment faire une cellule
# In[2]:
a = {}
a["nom"] = "engel"
a["prenom"] = "olivier"
print(a)
