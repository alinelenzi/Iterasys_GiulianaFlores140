import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Cadastrar():

    url = "https://www.giulianaflores.com.br"

    def setup_method(self, method):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(20);

    def teardown_method(self, method):
        self.driver.quit();

    def test_cadastrar_usuario(self):
        self.driver.get(self.url);
        self.driver.find_element(By.ID, "perfil-display").click();
        self.driver.find_element(By.ID, "UrlLogin").click();

        #transição de página
        assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "IDENTIFICAÇÃO";
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click();

        #transição de página
        assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "MINHA CONTA";
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Henrique Claudio Yago Barros");
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("849.365.060-95");
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("henrique.claudio.barros@bcconsult.com.br");
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("eg1CCzZx2o");
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("29141675");
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_btnAddressFind").click();
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("841");
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("28998448801");
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click();

        #sair
        self.driver.find_element(By.ID, "perfil-display").click();
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a:nth-child(2)").click()






