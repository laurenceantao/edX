# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:30:41 2016

@author: lantao
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff): 
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)