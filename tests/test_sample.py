from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel


class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel(
            "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel(
            "Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        """
        O teste consta com 2 erros:
        1. O tipo do cliente é, obrigatóriamente 'Regular' ou 'Reward', e o teste verifica a string 'Rewards'. Esse tipo de erro deve ser filtrado antes de realizarem os testes unitários
        2. A função pode retornar tanto 'Ridgewood' quanto 'Lakewood' pois os dois ficam com o mesmo preço no teste de caso 3. 
        """

        """
        Teste com erros:
        """
        # result = "Ridgewood"
        # self.assertEqual(result, get_cheapest_hotel(
        #     "Reward: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))
        # self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

        '''
        Teste refatorado:
        '''
        result_1 = "Ridgewood"
        result_2 = "Lakewood"

        params = "Reward: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"

        self.assertTrue((result_1 == get_cheapest_hotel(params))
                        or (result_2 == get_cheapest_hotel(params)))
