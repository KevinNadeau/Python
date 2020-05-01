# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:49:49 2020

@author: kevin k
"""

class Envoi:
    
    def __init__(self, expedition, expedition_adresse, destination_adresse, poids):
        self.expedition=expedition
        self.expedition_adresse= expedition_adresse        
        self.destination_adresse=destination_adresse
        self.poids=poids
    
    def calculTimbre(self):
        return 'WHATEVER'
        
    def ToString(self):
        print("WHATEVER")

class Lettre(Envoi):
    
    def __init__(self, expedition, expedition_adresse, destination_adresse, poids, format):
        Envoi.__init__(self, poids, expedition, destination_adresse, expedition_adresse)
        self.format=format
     
    def calculTimbre(self):
        count = self.poids/1000
        if format == 'A4':
            montant = 2.50*count
        else:
            montant = 3.50*count
        if self.expedition == 'expresse':
            return montant*2
        else: 
            return montant
    
    def ToString(self):
        print("Mode:" + self.expedition)
        print("Adresse d'expedition: " + self.expedition_adresse)
        print("Adresse de destination: " + self.destination_adresse)
        print("Poids: " + str(self.poids) + " grammes")
        print("Format : " + self.format)
        print("Prix du timbre : " + str(self.calculTimbre()))
        
#L1 = Lettre("expresse", "Denver", "Paris", 80, 'A4')
#L1.ToString()
        