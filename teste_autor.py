import unittest

import coletando_autores

from bs import beauty


class ReqTest(unittest.TestCase):

    def teste_autores(self):
        esperado = 'Albert Einstein'
        atual = coletando_autores.coletando_primeiro_autor()

        self.assertEqual(esperado, atual)
        
    def extrair_autores(self):
        esperado = ['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 
'Eleanor Roosevelt', 'Steve Martin']
        atual = beauty.extrair_autores()
        
        self.assertEqual(esperado, atual)
        
    
        

