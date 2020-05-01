# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:24:46 2020

@author: kevin k
"""


class DateNaissance:
    
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee
    
    def ToString(self):
        print("Date de naissance: " +str(self.jour)+"/"+str(self.mois)+"/"+str(self.annee))
        
class Personne:
    
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
    
    def afficher(self):
        print("Nom: " + self.nom)
        print("Prénom: " + self.prenom)
        self.date_naissance.ToString()        
        

K = Personne('Nadeau','Kevin',DateNaissance(18,9,1990))
print(K.afficher())

class Employe(Personne):
    
    def __init__(self, nom, prenom, date_naissance, salaire):
        Personne.__init__(self, nom, prenom, date_naissance)
        self.salaire = salaire
        
    def afficher(self):
        print("Nom: " + self.nom)
        print("Prénom: " + self.prenom)
        self.date_naissance.ToString()
        print("Salaire: " + str(self.salaire))

L = Employe('Nadeau','Kevin',DateNaissance(18,9,1990),1560)
print(L.afficher())

class Chef(Employe):
    
    def __init__(self, nom, prenom, date_naissance, salaire, service):
        Employe.__init__(self, nom, prenom, date_naissance, salaire)
        self.service = service
    
    def afficher(self):
        print("Nom: " + self.nom)
        print("Prénom: " + self.prenom)
        self.date_naissance.ToString()
        print("Salaire: " + str(self.salaire))
        print("Service: " + self.service)
        
M = Chef('Nadeau','Kevin',DateNaissance(18,9,1990),1560, 'Recherche et Developpement')        
print(M.afficher())

