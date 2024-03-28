import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Login():

    url = "https://www.giulianaflores.com.br"

    def setup_method(self, method):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(10);

    def teardown_method(self, method):
        self.driver.quit();

    def test_login_positivo(self):
        self.driver.get(self.url);
        self.driver.find_element(By.ID, "perfil-display").click();
        self.driver.find_element(By.ID, "UrlLogin").click();

        #transição de página
        assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept"). text == "IDENTIFICAÇÃO";
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("82644237360");
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("egEXGj413P");
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click();

        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("egEXGj413P");
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click();

        #transição de página
        self.driver.find_element(By.ID, "perfil-hidden").click();
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="javascript:Logout();void 0;"]').click()
        



        

