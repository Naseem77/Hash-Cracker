#!/usr/bin/env python3
import hashlib, sys, time
from itertools import product
from tkinter import *
from tkinter import ttk

 
    

def get_algorithm( type ):

    def algorithm( string ):
        h = type()
        h.update(string.encode('utf-8'))
        return h.hexdigest()
    return algorithm


TYPES_DICT = { 32 : get_algorithm( hashlib.md5 ) }



class Control( object ):
    """ Main class """
    
    def __init__( self ):
        self.decrypt_method = None
        self.decrypted_hash = None
        print('start')
        root=Tk()
        button=ttk.Button(root,text='cc')
        button.pack()
    
    
    def main( self ):

        root=Tk()
        self.user_hash = self.get_hash()
        
        
        self.decrypted_hash = self.brute_force()
                
            
        if self.decrypted_hash != None:  
            self.elapsed = (time.time() - self.start)  
            print('Hash cracked in '+str(self.elapsed)+' seconds. The correct word is: '
                      +self.decrypted_hash)
            #sys.exit()
        else:
            print('no matches found')

            
    def get_hash(self):
         
        while True:
            hash_input = input('Please enter the hash: ')
            
            if hash_input.isalnum(): 
                length =32
                if TYPES_DICT.get( length, None ):
                    self.hashtype = TYPES_DICT[length]
                    return hash_input

                else:
                    print('invalid hash')
            
            else:
                print('invalid hash')
                    
    
                
    def brute_force(self):
        charset = 'abcdefghijklmnopqrstuvwxyz'
        minlen=8
        maxlen=16
        #input('Please enter required character set: ')
        #minlen = int(input('Minimum word length: '))
        #maxlen = int(input('Maximum word length: '))
        
        print('Checking...\n\n')
        self.start = time.time()
        for i in range(minlen, maxlen+1):
            for p in product(charset, repeat=i):
                word = ''.join(p)
                if self.hashtype(word) == self.user_hash:
                    return word
                
                    
                    
if __name__ == "__main__":
    run_it = Control()
    run_it.main()
     
   
    input('press enter')
    input('press enter')
