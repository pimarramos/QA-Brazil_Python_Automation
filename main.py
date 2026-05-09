import time
import data
import helpers

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        options = ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = Chrome(options=options)
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
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO

    def test_select_plan(self):
        self.page.select_comfort_plan()
        assert self.page.is_comfort_plan_selected()

    def test_fill_phone_number(self):
        self.page.fill_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        phone_code = helpers.retrieve_phone_code(self.driver)
        self.page.fill_phone_code(phone_code)
        assert data.PHONE_NUMBER in self.page.get_phone_number()

    def test_fill_card(self):
        self.page.select_comfort_plan()
        self.page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)

    def test_comment_for_driver(self):
        self.page.write_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        assert self.page.get_comment_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.page.select_comfort_plan()
        self.page.order_blanket_and_handkerchiefs()
        assert self.page.is_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        self.page.select_comfort_plan()
        self.page.order_ice_creams(2)
        assert self.page.get_ice_cream_count() == 2

    def test_car_search_model_appears(self):
        self.page.select_comfort_plan()

        self.page.fill_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        phone_code = helpers.retrieve_phone_code(self.driver)
        self.page.fill_phone_code(phone_code)

        self.page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        self.page.write_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        self.page.order_blanket_and_handkerchiefs()
        self.page.order_ice_creams(2)

        self.page.order_taxi()
        assert self.page.is_car_search_modal_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
