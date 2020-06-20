
import hashlib, sys, time
from itertools import product
from tkinter import *
from tkinter import ttk


def getAlgorithm(type):
    def algorithm(string):
        temp = type()
        temp.update(string.encode('utf-8'))
        return temp.hexdigest()
    return algorithm


Dictionary_TYPES = { 32 : getAlgorithm( hashlib.md5 ),40 : getAlgorithm( hashlib.sha1 )}



class Control(object):

    root = Tk(className='Hash Cracker')
    user_input = StringVar(root)
    enterHash = Entry(root,textvariable=user_input);
    myLabel1 = Label(root, text="");
    decryptedHash = None
    inputFile = None

    def __init__(self):

        self.inputFile = None

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
        self.myLabel1.config(text='Checking...')
        self.userHash = self.getHash()
        self.decryptedHash = self.bruteForceAttack()
        self.elapsed = (time.time() - self.start)
        self.myLabel1.config(text='Hash cracked in '+str(self.elapsed)+'\n\nThe correct word is: '+self.decryptedHash)

    def myClick1(self):
        self.myLabel1.place(x=230,y=250)
        self.myLabel1.config(text='Checking...')
        self.userHash = self.getHash()
        self.wordlist = self.readWordlist() # get the wordlist...
        self.decryptedHash = self.dictionaryAttack()
        self.elapsed = (time.time() - self.start)
        self.myLabel1.config(text='Hash cracked in '+str(self.elapsed)+'\n\nThe correct word is: '+self.decryptedHash)




    def getHash(self):
        hashInput=self.user_input.get()

        if hashInput.isalnum():
            length = len(hashInput)
            if Dictionary_TYPES.get(length, None ):
                self.hashtype = Dictionary_TYPES[length]
                return hashInput

            else:
                self.myLabel1.config(text='invalid hash')

        else:
            self.myLabel1.config(text='invalid hash')


    def readWordlist(self):

        while self.inputFile == None:

            try:
                self.inputFile = open("wordlist.txt", "r", encoding="utf8", errors='ignore')

            except FileNotFoundError:
                self.retry('file name '+self.filename+'not found')

        words = self.inputFile.read()
        self.inputFile.close()
        return words.split()

    def dictionaryAttack(self):
        self.start = time.time()
        for word in self.wordlist:
            temp = self.hashtype(word)
            if temp == self.userHash:
                return word


    def bruteForceAttack(self):
        charWord = 'abcedf0123456789'
        minlen = 3
        maxlen = 20
        self.start = time.time()
        for i in range(minlen, maxlen+1):
            for j in product(charWord, repeat=i):
                word = ''.join(j)
                if self.hashtype(word) == self.userHash:
                    return word

if __name__ == "__main__":
    runIt = Control()
