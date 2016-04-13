import unittest
import highscore

class TestHighScore(unittest.TestCase):
    
    def setUp(self):
        self.shelf = r'.\testscores.shlf'
        self.player1 = "Pinky"
        self.score1 = 320000
        self.player2 = "The Brain, Jr."
        self.score2 = 1000
        highscore.newScore(self.player1, self.score1)

    def testAddPlayer(self):
        win = highscore.newScore(self.player2, self.score2, self.shelf)
        self.assertEqual(win, self.score2, "{0}'s high score should be {1}".format(self.player2, self.score2))
    
    def testStoreHighScore(self):
        HighScore = highscore.newScore  # <--- synchronized with your namespace i.e. names your object HighScore for limited scope
        self.assertEqual(-100, HighScore('joe', -100, self.shelf))
        self.assertGreater(-99, HighScore('joe', -100, self.shelf))
        self.assertEqual(0, HighScore('joe', 0, self.shelf))
        self.assertLess(0, HighScore('chris', 100, self.shelf))
        self.assertEqual(1000, HighScore('chris', 1000, self.shelf))
        self.assertLess(100, HighScore('chris', 1000, self.shelf))
        self.assertEqual(0, HighScore('joe', -1, self.shelf))
       
    def testManyScores(self):
        HighScore = highscore.newScore
        self.assertEqual(50, HighScore('Kirby', 50, self.shelf))
        self.assertEqual(150, HighScore('Kirby', 150, self.shelf))
        self.assertEqual(150, HighScore('Kirby', 40, self.shelf))
        self.assertEqual(150, HighScore('Kirby', 95, self.shelf))
        self.assertTrue(HighScore('Kirby', 180, self.shelf) == 180, 'Kirby should have 180 as a top score')
    
    def tearDown(self):
        highscore.dumpSB(self.shelf)
        
if __name__ == "__main__":
    unittest.main()