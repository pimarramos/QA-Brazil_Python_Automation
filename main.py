import numbers
import data
import helpers
import time

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print(
                "Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução."
            )

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()


    def test_set_route(self):
        assert self.page._get_from_location() == data.ADDRESS_FROM
        assert self.page._get_to_location() == data.ADDRESS_TO
        time.sleep(10)


    def test_select_plan(self):
        self.page.click_taxi_option()
        self.page.click_icon_comfort_selected()
        assert self.page.is_comfort_icon_active()
        time.sleep(10)

    def test_fill_phone_number(self):

        print("função criada para definir o cartão para pagamento")
        pass

    def test_fill_card(self):

        print ("função criada para definir o cartão para pagamento")
        pass

    def test_comment_for_driver(self):

       print ("função criada para bla")
       pass

    def test_order_blanket_and_handkerchiefs(self):

        print("função criada para bla bla")
        pass

    def test_order_2_ice_creams(self):
        numbers_of_ice_creams = 2
        for count in range(numbers_of_ice_creams):
            # adicionar em S8
            print(f"Função criada para adicionar o {count + 1}º sorvete ao pedido")
        pass

    def test_car_search_model_appears(self):

        print("função criada para bla bla bla")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()