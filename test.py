# -*- coding: utf-8 -*-
#Resolvendo o problema do Ano Bissexto - http://dojopuzzles.com/problemas/exibe/ano-bissexto/

import unittest
class TestAnoBissexto(unittest.TestCase):
    def test_passa_multiplo_4(self):
        self.assertTrue(bissexto(400))
        
if __name__ == "__main__":
    unittest.main()