import unittest

import ClassToTest as my

class TestStack(unittest.TestCase):

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.stack = my.Stack(10)
        print("setUp is called")
        
    def tearDown(self):
        """
        tearDown is called after each test function execution.
        """
        print("tearDown is called")
        
    def testPush(self):
        self.stack.push(30)
        self.assertEqual(len(self.stack), 1)
        self.assertFalse(self.stack.isEmpty())
        
    def testStackFull(self):
        for e in range(10):
            self.stack.push(e)
            
        self.assertRaises(Exception, self.stack.push, 19) 
         
    def testPop(self):
        if len(self.stack) < self.stack.maxSize():
            val=23
        self.stack.push(val)
        self.assertEqual(self.stack.pop(), val)
        self.assertEqual(len(self.stack), 1)
        self.assertTrue(self.stack.isEmpty())
        
    def testStackEmptyException(self):
        self.assertRaises(my.StackEmptyError, self.stack.pop)
#         
if __name__ == '__main__':
    unittest.main(verbosity=2) # can be 0, 1 or 2
    
    
    