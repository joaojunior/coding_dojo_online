# -*- coding: utf-8 -*-
#Resolvendo o problema do Ano Bissexto - http://dojopuzzles.com/problemas/exibe/ano-bissexto/

import sys
#import unittest
#class TestAnoBissexto(unittest.TestCase):
    
def bissexto(ano):
    # verifica se o ano é multiplo de 4 e não divisível por 100
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    # verifica se divisivel por 400
    elif ano % 400 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    ano = int(sys.argv[1])
    bissexto(ano)