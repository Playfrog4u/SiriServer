#!/usr/bin/python
# -*- coding: utf-8 -*-

# catfacts.py
#by Casey "Nurfballs" Mullineaux

from random import randint
from plugin import *
import os, random



class catfacts(Plugin):

    @register("en-US",".*cat fact.*")
    def st_catfact(self, speech, language):
        if language == 'en-US':
            filename = "./plugins/catfacts.txt"
            file = open(filename, 'r')

            #Get the total file size
            file_size = os.stat(filename)[6]

            #Seek to a place int he file which is a random distance away
            #Mod by the file size so that it wraps around to the beginning
            file.seek((file.tell()+random.randint(0, file_size-1))%file_size)
    
            #Dont use the first readline since it may fall in the middle of a line
            file.readline()

            #this will return the next (complete) line from the file
            line = file.readline()
    
            #here is the random line
            self.say(line) 
             
        self.complete_request()


