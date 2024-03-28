import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Comprar_Banner():

    url = "https://www.giulianaflores.com.br/";

    def setup_method(self, method):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(15);

    def teardown_method(self, method):
        self.driver.quit();

    def test_comprar(self):
        self.driver.get(self.url);
        self.driver.find_element(By.ID, "perfil-hidden").click();
        self.driver.find_element(By.ID, "UrlLogin").click();

        #transição de página
        assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "IDENTIFICAÇÃO";
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("elaine-baptista72@br.ibn.com");
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("egEXGj413P");
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click();
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("egEXGj413P");
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click();

        self.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active .img_banner").click();

        self.driver.find_element(By.ID, "inputSearchAddress").send_keys("41195650");
        self.driver.find_element(By.CSS_SELECTOR, ".apply-button").click();
        self.driver.find_element(By.CSS_SELECTOR, ".close-button").click();
        
        assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "PRESENTE DE PÁSCOA";
        self.driver.find_element(By.ID, "txtDsKeyWord").click();
        self.driver.find_element(By.ID, "txtDsKeyWord").send_keys("Ovo com Caneca Azul Chase Patrulha Canina 180g");
        self.driver.find_element(By.ID, "btnSearch").click();
        self.driver.find_element(By.CSS_SELECTOR, ".close-button").click();
        self.driver.find_element(By.CSS_SELECTOR, ".image-content > img").click()

        assert self.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == "OVO COM CANECA AZUL CHASE PATRULHA CANINA 180G";
        assert self.driver.find_element(By.CSS_SELECTOR, ".precoPor_prod:nth-child(2) ").text == "R$ 65,30";
        self.driver.find_element(By.ID, "ContentSite_txtZip").send_keys("41195650");
        self.driver.find_element(By.CSS_SELECTOR, ".jOpenShippingPopup").click();
        
        self.driver.find_element(By.LINK_TEXT, "30").click();
        assert self.driver.find_element(By.CSS_SELECTOR, ".vlPriceCalendar").text == "R$ 15,90";
        self.driver.find_element(By.ID, "btConfirmShippingData").click();
        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click();

        assert self.driver.find_element(By.CSS_SELECTOR, ".prodBasket_nome").text == "Ovo com Caneca Azul Chase Patrulha Canina 180g";
        assert self.driver.find_element(By.CSS_SELECTOR, ".precoPor_basket").text == "R$ 65,30";
        self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click();

        self.driver.find_element(By.ID, "txtDsDestinationName").send_keys("Dionisio Sauro");
        self.driver.find_element(By.ID, 'ContentSite_rptDeliveryAddress_rbtFgPersonalAddress_0_0_0').click();
        self.driver.find_element(By.ID, "txtDsNumber").send_keys("441");
        self.driver.find_element(By.ID, "btnContinue").click();
        self.driver.find_element(By.ID, "ContentSite_spanPix").click();
        self.driver.find_element(By.ID, "ContentSite_ibtFinalizeOrderWithPix").click();
        self.driver.find_element(By.CSS_SELECTOR, "titulo-dept title-defaut-checkout").text == "PEDIDO REALIZADO COM SUCESSO!";
