import unittest
from tool import audit
class Tests(unittest.TestCase):
 def test_variables(self): self.assertEqual(audit('Hi {name} {x}',{'name','age'}),{'undeclared':['x'],'unused':['age']})
if __name__=='__main__': unittest.main()
