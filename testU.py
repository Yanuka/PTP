import unittest


# ma fonction dans le code chesscore.py line 14

def draw(self):
    print("        1     2     3     4     5     6     7     8")

# le test unitaire
class MyTest(unittest.TestCase):
    def test_draw(self):
        self.assert(draw)

# lancement test (pas touche)
if __name__ == '__main__':
    unittest.main()