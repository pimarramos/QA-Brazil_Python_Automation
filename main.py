import numbers
import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print(
                "Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução."
            )

    def test_set_route(self):
        # adicionar em S8
        print("Função criada para definir a rota")
        pass

    def test_select_plan(self):
        # adicionar em S8
        print("Função criada para selecionar o plano")
        pass

    def test_fill_phone_number(self):
        # adicionar em S8
        print("Função criada para preencher o número de telefone")
        pass

    def test_fill_card(self):
        # adicionar em S8
        print("Função criada para preencher os dados do cartão")
        pass

    def test_comment_for_driver(self):
        # adicionar em S8
        print("Função criada para adicionar comentário para o motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # adicionar em S8
        print("Função criada para solicitar cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        numbers_of_ice_creams = 2
        for count in range(numbers_of_ice_creams):
            # adicionar em S8
            print(f"Função criada para adicionar o {count + 1}º sorvete ao pedido")
        pass

    def test_car_search_model_appears(self):
        # adicionar em S8
        print("Função criada para verificar se o modelo de carro aparece na busca")
        pass