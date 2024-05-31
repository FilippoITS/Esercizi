import unittest
from bo import Calculation 

class TestCalculation(unittest.TestCase):
    
    def test_sum(self):
        calc_1 = Calculation(a=2,b=2)
        self.assertEqual(calc_1.get_Sum(), 4 , msg= "Hai sbagliato")

if __name__ == "__main__":
    
    unittest.main()
