import g2d
from time import time
from random import choice
from BoardGame import BoardGame, abstract, print_game, console_play, BoardGameGui, gui_play
from BoardLevel import board_level_0, board_level_1, caselle_fisse_level_0, caselle_fisse_level_1

class three_Row(BoardGame):
    def __init__(self, w:int, h:int, l:int):
        self._w, self._h, self._level = w, h, l
        if self._level==0:
            self._board = board_level_0(self._w)
            self._caselle_non_cambiabili=caselle_fisse_level_0(self._h)
            
        elif self._level==1:
                self._board = board_level_1(self._w)
                self._caselle_non_cambiabili=caselle_fisse_level_1(self._h)        
        
    def play_at(self, x:int, y:int):
        n=False
        for i in self._caselle_non_cambiabili:
           if (y,x) == i :
              n=True
        if n==False:      
           if  self._board[y][x] == "-":
               self._board[y][x]= "0" 
           elif self._board[y][x] == "0":
               self._board[y][x]= "1"
           elif self._board[y][x] == "1":
               self._board[y][x]= "-"
            
    def flag_at(self, x,y):
        pass

    def finished(self)-> bool:                        
        for y in range(self._h):
            count_nere_orizzontali=0
            count_bianche_orizzontali=0
            count_nere_verticali=0
            count_bianche_verticali=0
            
            for x in range(self._w):
                #no 3 celle contigue
                if (x<self._w-2 and self._board[y][x]== self._board[y][x+1] and self._board[y][x] == self._board[y][x+2]) or (y<self._h-2 and self._board[y][x] == self._board[y+1][x] and self._board[y][x] == self._board[y+2][x]):
                    return False
                
                #diverso da grigio
                if self._board[y][x]=="-":
                    return False
                
                #3 bianche e 3 nere
                if self._board[y][x]=="0":
                    count_bianche_orizzontali+=1
                if self._board[y][x]=="1":
                    count_nere_orizzontali+=1
                    
                if self._board[x][y]=="0":
                    count_bianche_verticali+=1
                if self._board[x][y]=="1":
                    count_nere_verticali+=1
   
            if count_bianche_verticali!=count_nere_verticali or count_bianche_orizzontali!=count_nere_orizzontali:
                return False
            
        return True
        
    def unsolvable(self)->bool:
        for y in range(self._h):
            count_nere_orizzontali=0
            count_bianche_orizzontali=0
            count_bianche_verticali=0
            count_nere_verticali=0
            for x in range(self._w):
                if self._board[y][x]!="-":
                    #no 3 celle contigue
                    if (x<self._w-2 and self._board[y][x]== self._board[y][x+1] and self._board[y][x] == self._board[y][x+2]) or (y<self._h-2 and self._board[y][x] == self._board[y+1][x] and self._board[y][x] == self._board[y+2][x]):
                        #print("la casella (", x,", ", y,") rende impossibile finire il gioco")
                        return True
                    
                    # bianche = nere
                    if self._board[y][x]=="0":
                        count_bianche_orizzontali+=1
                    elif self._board[y][x]=="1":
                        count_nere_orizzontali+=1
                        
                if  self._board[x][y]!="-" :      
                    if self._board[x][y]=="0":
                        count_bianche_verticali+=1
                    elif self._board[x][y]=="1":
                        count_nere_verticali+=1
                
            if count_bianche_orizzontali > self._h/2 or count_nere_orizzontali > self._h/2:
                #print("la casella (", x,", ", y,") rende impossibile finire il gioco")
                return True
            
            if count_bianche_verticali> self._h/2 or count_nere_verticali > self._h/2 :
                return True
            
        return False
        
    def value_at(self, x,y):
        return self._board[y][x]

    def cols(self):
        return self._w

    def rows(self):
        return self._h

    def message(self):
        return "HAI VINTO!"
      
    def automatismi(self):
        for y in range(self._h):
            count_nere_orizzontali=0
            count_bianche_orizzontali=0
            count_nere_verticali=0
            count_bianche_verticali=0
            for x in range(self._w):
                
                #gestire bilanciamento 3nere3bianche
                if self._board[y][x]=="0":
                    count_bianche_orizzontali+=1
                    
                if self._board[x][y]=="0":
                    count_bianche_verticali+=1

                if self._board[y][x]=="1":
                    count_nere_orizzontali+=1
                    
                if self._board[x][y]=="1":
                    count_nere_verticali+=1
                    
                #gestire terne
                if x<self._w-1:
                    #orizzontali
                    if (self._board[y][x]=="0" and self._board[y][x+1]=="0" ):
                        for i in self._caselle_non_cambiabili:
                            if x==0 and (y,x+2) != i and self._board[y][x+2]=="-":
                                self._board[y][x+2]="1"
                            elif x>=self._w-2 and (y,x-1) != i and self._board[y][x-1]=="-":
                                self._board[y][x-1]="1"
                            elif x>0 and  x<self._w-2 and (y,x-1) != i and (y,x+2) != i :
                                if self._board[y][x-1]=="-":
                                    self._board[y][x-1]="1"
                                if self._board[y][x+2]=="-":
                                    self._board[y][x+2]="1"
                    #verticali
                    if (self._board[x][y]=="0" and self._board[x+1][y]=="0" ):
                        for i in self._caselle_non_cambiabili:
                            if x==0 and (y,x+2) != i and self._board[x+2][y]=="-":
                                self._board[x+2][y]="1"
                            elif x>=self._w-2 and (y,x-1) != i and self._board[x-1][y]=="-":
                                self._board[x-1][y]="1"
                            elif x>0 and  x<self._w-2 and (y,x-1) != i and (y,x+2) != i:
                                if self._board[x-1][y]=="-": 
                                    self._board[x-1][y]="1"
                                if self._board[x+2][y]=="-":
                                    self._board[x+2][y]="1"
                    #orizzontali
                    if (self._board[y][x]=="1" and self._board[y][x+1]=="1"):
                        for i in self._caselle_non_cambiabili:
                            if x==0 and (y,x+2) != i and self._board[y][x+2]=="-":
                                self._board[y][x+2]="0"
                            elif x>=self._w-2 and (y,x-1) != i and self._board[y][x-1]=="-":
                                self._board[y][x-1]="0"
                            elif x>0 and  x<self._w-2 and (y,x-1) != i and (y,x+2) != i :
                                if self._board[y][x-1]=="-":
                                    self._board[y][x-1]="0"
                                if self._board[y][x+2]=="-":
                                    self._board[y][x+2]="0"
                    #verticali
                    if (self._board[x][y]=="1" and self._board[x+1][y]=="1"):
                        for i in self._caselle_non_cambiabili:
                            if x==0 and (y,x+2) != i and self._board[x+2][y]=="-":
                                self._board[x+2][y]="0"
                            elif x>=self._w-2 and (y,x-1) != i and self._board[x-1][y]=="-":
                                self._board[x-1][y]="0"
                            elif x>0 and  x<self._w-2 and (y,x-1) != i and (y,x+2) != i :
                                if self._board[x-1][y]=="-": 
                                    self._board[x-1][y]="0"
                                if self._board[x+2][y]=="-":
                                    self._board[x+2][y]="0"
                                
                    if x<self._w-2:
                        if (self._board[y][x]== "0" and self._board[y][x+2]=="0"):
                            for i in self._caselle_non_cambiabili:
                                if (y,x+1) != i and self._board[y][x+1]=="-":
                                    self._board[y][x+1]="1"
                        elif (self._board[x][y]== "0" and self._board[x+2][y]=="0"):
                            for i in self._caselle_non_cambiabili:
                                if (y,x+1) != i and self._board[x+1][y]=="-":
                                    self._board[x+1][y]="1"
                        elif (self._board[y][x]== "1" and self._board[y][x+2]=="1"):
                            for i in self._caselle_non_cambiabili:
                                if (y,x+1) != i and self._board[y][x+1]=="-":    
                                    self._board[y][x+1]="0"
                        elif (self._board[x][y]== "1" and self._board[x+2][y]=="1"):
                             for i in self._caselle_non_cambiabili:
                                if (y,x+1) != i and self._board[x+1][y]=="-":
                                    self._board[x+1][y]="0"
                        #fine gestione terne

            #gestione bilanciamento                       
            if count_bianche_verticali==(self._w/2):
                for x in range(self._w):
                    for i in self._caselle_non_cambiabili:
                        if (y,x) != i and self._board[x][y]!="0":
                            self._board[x][y]="1"
                                
            if count_bianche_orizzontali==(self._w/2):
                for x in range(self._w):
                    for i in self._caselle_non_cambiabili:
                        if (y,x) != i and self._board[y][x]!="0":
                            self._board[y][x]="1"
                            
            if count_nere_verticali==(self._w/2):
                for x in range(self._w):
                    for i in self._caselle_non_cambiabili:
                        if (y,x) != i and self._board[x][y]!="1":
                            self._board[x][y]="0"
                            
            if count_nere_orizzontali==(self._w/2):
                for x in range(self._w):
                    for i in self._caselle_non_cambiabili:
                        if (y,x) != i and self._board[y][x]!="1":
                            self._board[y][x]="0"



    def ricerca_grigie(self)->bool: #funzione per i test
        for y1 in range (self._w):
            for x1 in range (self._h):
                if self._board[y1][x1] == "-" :
                    return True
        return False
    
    def deepcopy(self,A): #funzione per copiare la lista self._board impedendole di modificarsi con suggerimenti
       rt = []
       for elem in A:
           if isinstance(elem,list):
               rt.append(self.deepcopy(elem))
           else:
               rt.append(elem)
       return rt
    
    def suggerimenti(self):
        saved=self.deepcopy(self._board)
        for y in range (self._w):
            for x in range (self._h):
                if self._board[y][x] == "-" :
                    self._board=self.deepcopy(saved)
                    self._board[y][x] = "1"
                    self.automatismi()
                        
                    if self.unsolvable(): #ovvero vicolo cieco    
                        self._board=self.deepcopy(saved)
                        self._board[y][x]="0"
                        return 
                                  
                    else: #ovvero risolvibile
                        self._board=self.deepcopy(saved)
                        self._board[y][x] = "0"
                        self.automatismi()
                        if self.unsolvable():
                            self._board=self.deepcopy(saved)
                            self._board[y][x]="1"
                            return

                        else:
                            self._board=self.deepcopy(saved)
                            self._board[y][x] = "-"
            

    def solved(self)->bool:
        self.automatismi()
        if self.unsolvable():
            return False
        if self.ricerca_grigie():
            self.suggerimenti()
            self.solved()
        else:
            return self.finished()

    #la soluzione istantanea viene data dalla funzione solved
        
    '''    
    def backtracking(self,x1, y1) -> bool:
       self.automatismi()
       if self.unsolvable():
           return False
       for y in range (self._w):
            while x1 < self._h and self._board[y][x1] != "-":
                x1 += 1
            if x1 < self._h :
                saved = self.deepcopy(self._board)  # save current status
                for color in ("1", "0"):
                    self._board[y][x1] = color
                    if self.backtracking(x1+1,y):
                        return True
                    self._board = self.deepcopy(saved) # backtracking
                    
            return self.finished()'''
