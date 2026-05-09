from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    # Endereços
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Chamada de táxi
    taxi_option = (By.XPATH, '//button[contains(text(), "Chamar")]')
    comfort_plan = (
        By.XPATH,
        '//div[contains(@class, "tcard")][.//div[contains(@class, "tcard-title") and text()="Comfort"]]'
    )

    # Telefone
    phone_button = (By.CLASS_NAME, 'np-button')
    phone_input = (By.ID, 'phone')
    phone_submit_button = (
        By.XPATH,
        '//div[contains(@class, "number-picker") and contains(@class, "open")]'
        '//div[contains(@class, "section") and contains(@class, "active")]'
        '//button[contains(@class, "button") and contains(@class, "full")]'
    )
    phone_code_input = (
        By.XPATH,
        '//div[contains(@class, "number-picker") and contains(@class, "open")]'
        '//div[contains(@class, "section") and contains(@class, "active")]'
        '//input[@id="code"]'
    )

    # Cartão
    payment_method_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (
        By.XPATH,
        '//div[contains(@class, "payment-picker") and contains(@class, "open")]'
        '//div[contains(@class, "pp-row")][.//div[text()="Adicionar cartão"]]'
    )
    card_number_input = (
        By.XPATH,
        '//div[contains(@class, "payment-picker") and contains(@class, "open")]//input[@id="number"]'
    )
    card_code_input = (
        By.XPATH,
        '//div[contains(@class, "payment-picker") and contains(@class, "open")]'
        '//div[contains(@class, "card-code")]//input[@id="code"]'
    )
    add_card_submit_button = (
        By.XPATH,
        '//div[contains(@class, "payment-picker") and contains(@class, "open")]'
        '//button[normalize-space()="Adicionar"]'
    )
    close_payment_modal_button = (
        By.XPATH,
        '//div[contains(@class, "payment-picker") and contains(@class, "open")]'
        '//div[contains(@class, "section") and contains(@class, "active")]'
        '//button[contains(@class, "close-button")]'
    )

    # Comentário
    comment_input = (By.ID, 'comment')

    # Cobertor e lençóis
    blanket_slider = (
        By.XPATH,
        '//div[contains(@class, "r-sw-container")][.//div[contains(text(), "Cobertor")]]'
        '//span[contains(@class, "slider")]'
    )
    blanket_checkbox = (
        By.XPATH,
        '//div[contains(@class, "r-sw-container")][.//div[contains(text(), "Cobertor")]]'
        '//input[contains(@class, "switch-input")]'
    )

    # Sorvetes
    ice_cream_plus_button = (
        By.XPATH,
        '//div[contains(@class, "r-counter-container")][.//div[contains(text(), "Sorvete")]]'
        '//div[contains(@class, "counter-plus")]'
    )
    ice_cream_counter = (
        By.XPATH,
        '//div[contains(@class, "r-counter-container")][.//div[contains(text(), "Sorvete")]]'
        '//div[contains(@class, "counter-value")]'
    )

    # Pedido
    order_button = (
        By.XPATH,
        '//button[contains(@class, "smart-button")]'
    )
    car_search_modal = (
        By.XPATH,
        '//div[contains(@class, "order") and contains(@class, "shown")]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_value(self, locator):
        return self._find(locator).get_attribute('value')

    def enter_locations(self, from_text, to_text):
        self._type(self.from_field, from_text)
        self._type(self.to_field, to_text)

    def get_from_location(self):
        return self._get_value(self.from_field)

    def get_to_location(self):
        return self._get_value(self.to_field)

    def click_taxi_option(self):
        self._click(self.taxi_option)

    def select_comfort_plan(self):
        comfort = self._find(self.comfort_plan)
        if "active" not in comfort.get_attribute("class"):
            self.driver.execute_script("arguments[0].click();", comfort)

    def is_comfort_plan_selected(self):
        return "active" in self._find(self.comfort_plan).get_attribute("class")

    def fill_phone_number(self, phone_number):
        self._click(self.phone_button)
        self._type(self.phone_input, phone_number)
        self._click(self.phone_submit_button)
        self._find(self.phone_code_input)

    def fill_phone_code(self, code):
        self._type(self.phone_code_input, code)
        self._click(self.phone_submit_button)

    def get_phone_number(self):
        return self._find(self.phone_button).text

    def add_credit_card(self, card_number, card_code):
        self._click(self.payment_method_button)
        self._click(self.add_card_button)
        self._type(self.card_number_input, card_number)

        code_field = self._find(self.card_code_input)
        code_field.send_keys(card_code)
        code_field.send_keys(Keys.TAB)

        self._click(self.add_card_submit_button)

        try:
            self._click(self.close_payment_modal_button)
        except TimeoutException:
            pass

    def write_comment_for_driver(self, message):
        self._type(self.comment_input, message)

    def get_comment_for_driver(self):
        return self._get_value(self.comment_input)

    def order_blanket_and_handkerchiefs(self):
        checkbox = self._present(self.blanket_checkbox)
        if not checkbox.is_selected():
            self._click(self.blanket_slider)

    def is_blanket_and_handkerchiefs_selected(self):
        return self._present(self.blanket_checkbox).is_selected()

    def order_ice_creams(self, amount):
        for _ in range(amount):
            self._click(self.ice_cream_plus_button)

    def get_ice_cream_count(self):
        return int(self._find(self.ice_cream_counter).text)

    def order_taxi(self):
        self._click(self.order_button)

    def is_car_search_modal_visible(self):
        return self._find(self.car_search_modal).is_displayed()
