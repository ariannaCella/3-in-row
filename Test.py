import unittest
import BoardGame 
import RowGame as game

class RowTest(unittest.TestCase):

    def test_play_at_6(self):
        t6=game.three_Row(6,6,0)
        
        t6.play_at(2,0)
        self.assertTrue(t6.value_at(2,0) == "0")
        
        t6.play_at(2,0)
        self.assertTrue(t6.value_at(2,0) == "1")
        
        t6.play_at(2,0)
        self.assertTrue(t6.value_at(2,0) == "-")

        t6.play_at(1,1)
        self.assertTrue(t6.value_at(1,1) == "1")

        t6.play_at(2,2)
        self.assertTrue(t6.value_at(2,2) == "0")

        
    def test_play_at_8(self):
        t8=game.three_Row(8,8,0)

        t8.play_at(1,0)
        self.assertTrue(t8.value_at(1,0) == "0")
        
        t8.play_at(1,0)
        self.assertTrue(t8.value_at(1,0) == "1")
        
        t8.play_at(1,0)
        self.assertTrue(t8.value_at(1,0) == "-")

        t8.play_at(0,0)
        self.assertTrue(t8.value_at(0,0) == "1")

        t8.play_at(3,1)
        self.assertTrue(t8.value_at(3,1) == "0")


    def test_play_at_10(self):
        t10=game.three_Row(10,10,0)

        t10.play_at(0,0)
        self.assertTrue(t10.value_at(0,0) == "0")
        
        t10.play_at(0,0)
        self.assertTrue(t10.value_at(0,0) == "1")
        
        t10.play_at(0,0)
        self.assertTrue(t10.value_at(0,0) == "-")

        t10.play_at(3,2)
        self.assertTrue(t10.value_at(3,2) == "1")

        t10.play_at(0,1)
        self.assertTrue(t10.value_at(0,1) == "0")
    
    def test_finished_6(self):
        t6=game.three_Row(6,6,0)
        count=0
        ancora_grigie=True
        
        while t6.ricerca_grigie() and count<10:
            count+=1
            t6.automatismi()
            t6.ricerca_grigie()
        
        for y in range (6):
            for x in range (6):
                val=t6.value_at(x,y)
                if val=="-":
                    ancora_grigie=True
                    break
                else:
                    ancora_grigie=False

        if ancora_grigie:
            self.assertTrue(t6.finished()==False)
        else:
            self.assertTrue(t6.finished()==True)
            
    def test_unsolvable_6(self):
        t6=game.three_Row(6,6,0)
        t6.play_at(0,1)=="1"
        t6.play_at(0,2)=="1"
        t6.play_at(0,3)=="1"
        self.assertTrue(t6.unsolvable()==True)
        
        t6.play_at(0,0)=="1"
        t6.play_at(1,0)=="1"
        t6.play_at(2,0)=="1"
        self.assertTrue(t6.unsolvable()==True)
        
        t6.play_at(0,0)=="1"
        t6.play_at(1,0)=="1"
        t6.play_at(2,0)=="0"
        t6.play_at(3,0)=="0"
        t6.play_at(4,0)=="1"
        t6.play_at(5,0)=="1"
        self.assertTrue(t6.unsolvable()==True)

        t6.play_at(0,0)=="1"
        t6.play_at(0,1)=="1"
        t6.play_at(0,2)=="0"
        t6.play_at(0,3)=="0"
        t6.play_at(0,4)=="1"
        t6.play_at(0,5)=="1"
        self.assertTrue(t6.unsolvable()==True)

    def test_finished_8(self):
        t8=game.three_Row(8,8,1)
        count=0
        ancora_grigie=True
        
        while t8.ricerca_grigie() and count<10:
            count+=1
            t8.automatismi()
            t8.ricerca_grigie()
        
        for y in range (8):
            for x in range (8):
                val=t8.value_at(x,y)
                if val=="-":
                    ancora_grigie=True
                    break
                else:
                    ancora_grigie=False
                   
        if ancora_grigie:
            self.assertTrue(t8.finished()==False)
        else:
            self.assertTrue(t8.finished()==True)
            
    def test_unsolvable_8(self):
        t8=game.three_Row(8,8,1)
        t8.play_at(0,1)=="1"
        t8.play_at(0,2)=="1"
        t8.play_at(0,3)=="1"
        self.assertTrue(t8.unsolvable()==True)
        
        t8.play_at(0,0)=="1"
        t8.play_at(1,0)=="1"
        t8.play_at(2,0)=="1"
        self.assertTrue(t8.unsolvable()==True)
        
        t8.play_at(0,0)=="0"
        t8.play_at(1,0)=="1"
        t8.play_at(2,0)=="0"
        t8.play_at(3,0)=="0"
        t8.play_at(4,0)=="1"
        t8.play_at(5,0)=="0"
        t8.play_at(6,0)=="1"
        t8.play_at(7,0)=="0"
        self.assertTrue(t8.unsolvable()==True)

        t8.play_at(0,0)=="0"
        t8.play_at(0,1)=="1"
        t8.play_at(0,2)=="0"
        t8.play_at(0,3)=="0"
        t8.play_at(0,4)=="1"
        t8.play_at(0,5)=="0"
        t8.play_at(0,6)=="1"
        t8.play_at(0,7)=="0"
        self.assertTrue(t8.unsolvable()==True)
        
    def test_automatismi(self):
        t14=game.three_Row(14,14,1)
        t14.play_at(0,1)=="0"
        t14.play_at(0,3)=="0"
        t14.automatismi()
        self.assertTrue(t14.value_at(0,2)=="1")

        t14.play_at(0,0)=="1"
        t14.play_at(0,2)=="1"
        t14.automatismi()
        self.assertTrue(t14.value_at(0,1)=="0")
    
        t14.play_at(4,4)=="0"
        t14.play_at(4,5)=="0"
        t14.automatismi()
        self.assertTrue(t14.value_at(4,3)=="1")
        self.assertTrue(t14.value_at(4,6)=="1")

          
if __name__ == '__main__':
    unittest.main()
