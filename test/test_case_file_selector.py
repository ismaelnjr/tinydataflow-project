import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from tinyflow import TinyFlow
from tinyflow import StrToCSVTransformer
from tinyflow import FileSelector

class FileSelTest(unittest.TestCase):

    def test_file_selector(self):
        
        fileReader = FileSelector('.', '*.txt')
        str_to_csv = StrToCSVTransformer()
        # Escreve o resultado dos arquivos selecionados no arquivo CSV
        try:
            app = TinyFlow(fileReader, [str_to_csv])
            app.setup()
            app.run()    
            print(f"Resultados: {app.outputs}")
            
            self.assertEqual(app.outputs, 'output.csv')
        except TypeError as e:
            print(f"Erro de compatibilidade: {e}")
               
if __name__ == '__main__':
    unittest.main()