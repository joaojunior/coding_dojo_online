# -*- coding: utf-8 -*-
#Resolvendo o problema do Ano Bissexto - http://dojopuzzles.com/problemas/exibe/ano-bissexto/

import unittest

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    return False

class TestAnoBissexto(unittest.TestCase):
    def test_passa_multiplo_4_return_True(self):
        self.assertTrue(bissexto(1732))
        
    def test_ano_nao_bissexto_return_False(self):
        self.assertFalse(bissexto(1742))
        
    def test_ano_100_return_False(self):
        self.assertFalse(bissexto(100))
        
    def test_ano_1600_return_True(self):
        self.assertTrue(bissexto(1600))
        
    def test_ano_0_return_True(self):
        self.assertTrue(bissexto(0))
        
if __name__ == "__main__":
    unittest.main()