
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

    root = Tk(className='Hash Cracker')
    user_input = StringVar(root)
    enterHash = Entry(root,textvariable=user_input);
    myLabel1 = Label(root, text="");
    decrypt_method = None
    decrypted_hash = None
    
    def __init__( self ):

        
        # set window size
        self.root.geometry("400x400")
        labelTitle = Label(self.root,text= "Hash Cracker",relief ="solid",
                                   width=20,font=("arial",19,"bold"))
        labelTitle.place(x=50,y=0)

        labelEntry = Label(self.root,text= "Enter A Hash:",width=15,
                           font=("arial",10,"bold"))
        labelEntry.place(x=0,y=70)

        self.enterHash.pack();
        self.enterHash.place(x=155,y=73);

        labelEntry = Label(self.root,text= "Brute-force-attack",width=15,
                           font=("arial",10,"bold"))
        labelEntry.place(x=60,y=200)
        myButton = Button(self.root,width=12 ,text="Enter", command=self.myClick);
        myButton.pack();
        myButton.place(x=70,y=220)

        labelEntry = Label(self.root,text= "Dictionary attack",width=15,
                           font=("arial",10,"bold"))
        labelEntry.place(x=220,y=200)
        myButton = Button(self.root,width=12, text="Enter", command=self.myClick1);
        myButton.pack();
        myButton.place(x=230,y=220)

        self.myLabel1.pack();
        
        self.root.mainloop();

        
    
    
    def myClick(self):
        
        self.myLabel1.place(x=70,y=250)
        self.user_hash = self.get_hash()
        self.decrypted_hash = self.brute_force()
        self.myLabel1.config(text='Checking...')
        self.elapsed = (time.time() - self.start)  
     
        self.myLabel1.config(text='Hash cracked in '+str(self.elapsed)+'\n\nThe correct word is: '+self.decrypted_hash)
        
    def myClick1(self):
        
        
         self.myLabel1.place(x=230,y=250)

    def main( self ):

       
        self.user_hash = self.get_hash()
        decrypted_hash = self.brute_force()
                
        if decrypted_hash != None:  
            self.elapsed = (time.time() - self.start)  
            self.myLabel1.config(text='Hash cracked in '+str(self.elapsed)+' seconds. The correct word is: '
                      +decrypted_hash)
        else:
            self.myLabel1.config(text='no matches found')

            
    def get_hash(self):
         
        hash_input=self.user_input.get()
        if hash_input.isalnum(): 
            length =32
            if TYPES_DICT.get( length, None ):
                self.hashtype = TYPES_DICT[length]
                return hash_input

            else:
                self.myLabel1.config(text='invalid hash')
            
        else:
            self.myLabel1.config(text='invalid hash')
                    
       
    def brute_force(self):
        charset = 'helo'
        minlen=4
        maxlen=10
        self.start = time.time()
        for i in range(minlen, maxlen+1):
            for p in product(charset, repeat=i):
                word = ''.join(p)
                if self.hashtype(word) == self.user_hash:
                    return word
                           
if __name__ == "__main__":
    run_it = Control()
     
