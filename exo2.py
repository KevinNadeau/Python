# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:40:30 2020

@author: kevin k
"""

class Point:
    
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z
    
    def ToString(self):
        if self.z == 0:
            print(" P=( "+str(self.get_x())+","+str(self.get_y())+" )")
        else:
            print(" P=( "+str(self.get_x())+","+str(self.get_y())+","+str(self.get_z())+" )")
            
P1 = Point(5, 6) 
P1.ToString()           