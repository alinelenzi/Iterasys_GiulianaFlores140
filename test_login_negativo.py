import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Login_Negativo():

    url = "https://www.giulianaflores.com.br/";

    def setup_method(self, method):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(10);

    def teardown_method(self, method):
        self.driver.quit();


    def test_login_negativo(self):
        self.driver.get(self.url);
        self.driver.find_element(By.ID, "perfil-hidden").click();
        self.driver.find_element(By.ID, "UrlLogin").click();

        #transição de página
        assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "IDENTIFICAÇÃO";
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("elaine-baptista72@br.ibn.com");
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("errado");
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click();

        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("errado");
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click();
        self.driver.find_element(By.ID, "ContentSite_divMessages").text == "e-mail ou senha inválidos!";



