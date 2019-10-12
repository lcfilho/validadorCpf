import unittest
import validacpf_luis

class Testvalidacpf_luis(unittest.TestCase):

    def test_retira_formatacao(self):
        self.assertEqual(validacpf_luis.retira_formatacao('345!333@871*09'),'34533387109')
    def test_retira_formatacao_1(self):
        self.assertEqual(validacpf_luis.retira_formatacao('345.333.871.09'),'34533387109')
    def test_retira_formatacao_2(self):
        self.assertEqual(validacpf_luis.retira_formatacao('345-333+871*09'),'34533387109')
    def test_retira_formatacao_3(self):
        self.assertEqual(validacpf_luis.retira_formatacao('345}333@871*&09'),'34533387109')
        
    def test_valida_cpf(self):
        self.assertFalse(validacpf_luis.valida_cpf('00000000000'),())
    def test_valida_cpf_1(self):
        self.assertFalse(validacpf_luis.valida_cpf('111-111-111-11'),())
    def test_valida_cpf_2(self):
        self.assertTrue(validacpf_luis.valida_cpf('514+749*590-83'),())
    def test_valida_cpf_3(self):
        self.assertTrue(validacpf_luis.valida_cpf('070.588.360-43'),())
    def test_valida_cpf_4(self):
        self.assertTrue(validacpf_luis.valida_cpf('089.247.020-84'),())
    def test_valida_cpf_5(self):
        self.assertFalse(validacpf_luis.valida_cpf('000.588.360-43'),())
    def test_valida_cpf_6(self):
        self.assertFalse(validacpf_luis.valida_cpf('1234567890123'),())


if __name__ == '__main__':
    unittest.main()
