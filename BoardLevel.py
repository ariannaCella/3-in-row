def board_level_0(self_w):
   
        with open("3roweasy.txt","r") as file:
           
                board = []
                if self_w == 6:
                   #leggere riga per riga il file fino alla 6 riga e
                    #inserirlo all'interno della matrice con append
                     for n in range(6):
                        f = file.readline()
                        g = f.strip()
                        board.append(list(g))
                    
                elif self_w == 8:
                    #leggere 6 righe(quelle della matrice precedente +1 vuota) e poi inserire
                    #fino al'ottava riga le liste con append
                    for i in range(7):
                        f = file.readline()

                    for n in range(8):
                        g = file.readline()
                        h = g.strip()
                        board.append(list(h))
                
                elif self_w == 10:
                    #leggere 14 (+2 di righe vuote) righe(quelle delle matrici precedenti) e poi inserire
                    #fino alla fine del txt le liste con append
                    for i in range(16):
                        f = file.readline()

                    for n in range(10):
                        g = file.readline()
                        h = g.strip()
                        board.append(list(h))

                elif self_w == 12:
                    for i in range(27):
                        f= file.readline()

                    for n in range(12):
                        g = file.readline()
                        h = g.strip()
                        board.append(list(h))
                        
                elif self_w == 14:
                    for n in range(40):
                        f= file.readline()

                    for n in range(14):
                        g = file.readline()
                        h = g.strip()
                        board.append(list(h))
                        
                return board

               
def board_level_1(self_w):
   
   with open("3row_medium.txt","r") as file:
                board = []
                if self_w == 6:
                   #leggere riga per riga il file fino alla 6 riga e
                    #inserirlo all'interno della matrice con append
                     for n in range(6):
                        f = file.readline()
                        g = f.strip()
                        board.append(list(g))
                    
                elif self_w == 8:
                    #leggere 6 righe(quelle della matrice precedente +1 vuota) e poi inserire
                    #fino al'ottava riga le liste con append
                    for i in range(7):
                        f = file.readline()

                    for n in range(8):
                        g = file.readline()
                        h = g.strip()
                        board.append(list(h))
                    
                elif self_w == 10:
                    #leggere 14 (+2 di righe vuote) righe(quelle delle matrici precedenti) e poi inserire
                    #fino alla fine del txt le liste con append
                    for i in range(16):
                        f = file.readline()

                    for n in range(10):
                        g = file.readline()
                        h = g.strip()
                        board.append(list(h))

                elif self_w == 12:
                    for i in range(27):
                        f= file.readline()

                    for n in range(12):
                        g = file.readline()
                        h = g.strip()
                        board.append(list(h))

                elif self_w == 14:
                    for n in range(40):
                        f= file.readline()

                    for n in range(14):
                        g = file.readline()
                        h = g.strip()
                        board.append(list(h))
                        
                return board        

            
def caselle_fisse_level_0(self_h):
   
            if self_h == 6:
                caselle_non_cambiabili=[(1,1),(2,2),(2,5),(3,3),(4,4),(4,1),(5,0),(5,1),(5,3)]

            elif self_h == 8:
                caselle_non_cambiabili=[(0,0),(0,4),(0,5),(1,0),(1,1),(1,3),(1,7),(3,0),(3,2),(3,5),(3,7),(5,1),(5,4),(5,7),(6,5),(7,2)]

            elif self_h == 10:
                caselle_non_cambiabili=[(0,9),(1,0),(1,5),(2,3),(2,6),(2,8),(2,9),(3,0),(3,3),(3,6),(5,5),(6,2),(6,3),(6,8),(6,9),(7,0),(7,5),(7,6),(8,2),(8,5),(9,2),(9,4),(9,9)]

            elif self_h ==12:
                caselle_non_cambiabili=[(0,3),(0,6),(0,7),(0,10),(0,11),(1,2),(1,8),(2,3),(2,6),(2,10),(3,4),(3,8),(3,10),(4,0),(4,2),(4,11),(5,3),(5,4),(5,10),(6,1),(6,4),(7,5),(7,8),(8,2),(8,10),(8,11),(9,0),(9,2),(9,4),(9,7),(9,9),(10,0),(10,6),(10,7),(11,1),(11,3),(11,6)]

            elif self_h ==14:
                caselle_non_cambiabili= [(0,2),(0,10),(1,0),(1,1),(1,3),(1,6),(1,8),(1,13),(2,10),(2,13),(3,0),(3,4),(3,6),(3,8),(3,12),(4,7),(4,9),(4,10),(5,2),(5,5), (6,0),(6,2),(6,13),(7,5),(7,8),(7,9),(7,12),(8,0),(9,5),(9,6),(9,12),(10,0),(10,1),(10,8),(10,10),(10,11),(11,2),(11,4),(11,8),(11,13),(12,0),(12,3),(12,5),(12,9),(13,1),(13,10),(13,13)]

            return caselle_non_cambiabili

   
def caselle_fisse_level_1(self_h):
   
                if self_h == 6:
                    caselle_non_cambiabili =[(0,4),(1,0),(1,1),(2,1),(2,4),(3,4),(4,0),(5,2),(5,5)]

                elif self_h==8:
                    caselle_non_cambiabili =[(0,0),(0,3),(1,2),(1,6),(2,2),(2,7),(3,4),(3,7),(4,1),(4,3),(5,5),(5,6),(6,1),(6,3),(6,5)]
        
                elif self_h==10:
                    caselle_non_cambiabili =[(0,7),(1,0),(1,4),(1,7),(2,3),(2,4),(2,9),(3,2),(3,3),(3,7),(4,0),(4,5),(4,6),(6,1),(6,3),(7,0),(7,1),(7,6),(7,7),(8,4),(8,6),(9,9)]
            
                elif self_h ==12:
                    caselle_non_cambiabili=[(0,3),(0,7),(0,10),(1,0),(1,5),(1,11),(2,2),(2,9),(3,1),(3,4),(3,7),(3,10),(4,4),(4,5),(4,11),(5,0),(5,5),(5,9),(5,10),(6,2),(6,7),(7,1),(7,4),(8,0),(8,6),(8,11),(9,2),(9,4),(9,5),(9,7),(9,10),(10,0),(10,2),(10,4),(11,1),(11,7),(11,10),(11,11)]

                elif self_h == 14:
                    caselle_non_cambiabili=[(0,4),(0,5),(0,8),(0,13),(1,1),(1,6),(1,11),(2,1),(2,3),(2,4),(2,10),(2,12),(3,7),(3,9),(4,2),(4,11),(4,12),(5,1),(5,7),(5,9),(7,0),(7,3),(7,7,),(7,10),(7,12),(8,1),(8,4),(9,0),(9,2),(9,5),(9,9),(10,6),(10,11),(11,1),(11,8),(11,12),(12,0),(12,2),(12,3),(12,10),(13,0),(13,6),(13,7),(13,10),(13,11)]

                return caselle_non_cambiabili 

   
