import time
from selenium.webdriver.common.by import By

def test_titulo_pagina_principal(browser):
    browser.get("https://demoqa.com/")
    time.sleep(1)
    assert "DEMOQA" in browser.title

def test_botao_elements_existe(browser):
    browser.get("https://demoqa.com/")
    time.sleep(1)
    botao = browser.find_element(By.XPATH, "//h5[text()='Elements']")
    assert botao.is_displayed()

def test_navegar_para_elements(browser):
    browser.get("https://demoqa.com/")
    time.sleep(1)
    browser.find_element(By.XPATH, "//h5[text()='Elements']").click()
    time.sleep(1)
    assert "elements" in browser.current_url

def test_preencher_form(browser):
    browser.get("https://demoqa.com/text-box")
    time.sleep(1)
    browser.find_element(By.ID, "userName").send_keys("Gui da Silva")
    browser.find_element(By.ID, "userEmail").send_keys("gui@gmail.com")
    browser.find_element(By.ID, "currentAddress").send_keys("Rua Y, 123")
    browser.find_element(By.ID, "permanentAddress").send_keys("Rua Z, 523")
    browser.find_element(By.ID, "submit").click()
    time.sleep(1)
    output = browser.find_element(By.ID, "output")
    assert "Gui da Silva" in output.text
    assert "gui@gmail.com" in output.text
    assert "Rua Y, 123" in output.text
    assert "Rua Z, 523" in output.text