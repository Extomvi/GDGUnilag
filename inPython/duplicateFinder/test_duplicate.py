import unittest
import duplicate_finder

class TestDuplicate(unittest.TestCase):

    def test_findduplicate1(self):
        '''
        result = duplicate_finder.findduplicate1([2,5,1,3,2,5])
        self.assertEqual(result, 3)
        '''
        self.assertEqual(duplicate_finder.findduplicate1([2,4,3,2,1,5]), 2)
        self.assertEqual(duplicate_finder.findduplicate1([2,5,3,6,1,5]), 5)
        self.assertEqual(duplicate_finder.findduplicate1([1,4,3,2,1,5]), 1)

    def test_findduplicate2(self):
        '''
        result = duplicate_finder.findduplicate2([2,5,1,3,2,5])
        self.assertEqual(result, 3)
        '''
        self.assertEqual(duplicate_finder.findduplicate2([2,4,3,2,1,5]), 2)
        self.assertEqual(duplicate_finder.findduplicate2([2,5,3,6,1,5]), 5)
        self.assertEqual(duplicate_finder.findduplicate2([1,4,3,2,1,5]), 1)

    def test_findduplicate3(self):
        '''
        result = duplicate_finder.findduplicate3([2,5,1,3,2,5])
        self.assertEqual(result, 3)
        '''
        self.assertEqual(duplicate_finder.findduplicate3([2,4,2,1,5]), 2)
       #self.assertEqual(duplicate_finder.findduplicate3([2,5,3,6,1]), 5)
       #self.assertEqual(duplicate_finder.findduplicate3([1,4,3,2,1]), 1)




'''
To run in the shell, you use python3 -m unittest test_duplicate.py
'''

if __name__ == '__main__':
    unittest.main()