from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def crawler_carros(
    city,
    year_arrive,
    month_arrive,
    day_arrive,
    year_departure,
    month_departure,
    day_departure,
):
    # Inicie o webdriver (você deve ter o driver correspondente ao navegador instalado)
    # CHROMEDRIVER_PATH = r"/usr/bin/chromedriver"
    CHROMEDRIVER_PATH = r"C:\Users\vitor\Desktop\chromedriver-win64\chromedriver.exe"
    webdriver.Chrome.driver_path = CHROMEDRIVER_PATH
    driver = webdriver.Chrome()

    # Acesse o site
    driver.get("https://www.localiza.com/brasil/pt-br")

    city = capitalize(city)

    # Localize o elemento input e digita o nome da cidade
    input_element = driver.find_element(By.ID, "mat-input-1")
    input_element.send_keys(city)
    input_element.send_keys(Keys.RETURN)

    # Aguarda até que o elemento dropdown esteja visível
    wait = WebDriverWait(driver, 10)
    dropdown = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "places-list"))
    )

    # Clique no item desejado
    desired_item = driver.find_element(
        By.XPATH, "//span[contains(text(), '" + city + "')]"
    )
    desired_item.click()

    wait = WebDriverWait(driver, 10)
    # Esperar até que o botão do datepicker esteja visível e clicar nele
    date_selector = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "mat-calendar-header button.mat-calendar-period-button")
        )
    )
    date_selector.click()

    ano_selecao = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "td[role='gridcell'][data-mat-col='0'][aria-label='"
                + year_arrive
                + "']",
            )
        )
    )
    ano_selecao.click()

    mes_selecao = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "td[role='gridcell'][aria-label='"
                + month_arrive
                + " de "
                + year_arrive
                + "']",
            )
        )
    )
    mes_selecao.click()

    dia_selecao = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "td[role='gridcell'][aria-label='"
                + day_arrive
                + " de "
                + month_arrive
                + " de "
                + year_arrive
                + "']",
            )
        )
    )
    dia_selecao.click()

    time_option = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(), '12:00')]")
        )
    )
    time_option.click()

    # Esperar até que o botão do datepicker esteja visível e clicar nele
    date_selector = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "mat-calendar-header button.mat-calendar-period-button")
        )
    )
    date_selector.click()

    ano_selecao = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "td[role='gridcell'][data-mat-col='0'][aria-label='"
                + year_departure
                + "']",
            )
        )
    )
    ano_selecao.click()

    mes_selecao = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "td[role='gridcell'][aria-label='"
                + month_departure
                + " de "
                + year_departure
                + "']",
            )
        )
    )
    mes_selecao.click()

    dia_selecao = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "td[role='gridcell'][aria-label='"
                + day_departure
                + " de "
                + month_departure
                + " de "
                + year_departure
                + "']",
            )
        )
    )
    dia_selecao.click()
    time.sleep(1)

    # Localize e clique no botão:
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        "/html/body/loc-root/app-header/header/div/app-topbar-first-step/div/div/div/div[2]/div[5]",
    ).click()

    result_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/loc-root/main/app-fluxo-reserva/app-selecao-grupo/section/div[4]/div[1]/ds-new-group-car/article/div/ds-new-button/button",
            )
        )
    )
    result_element.click()

    result_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="main-content"]/app-fluxo-reserva/app-selecao-ofertas-opcionais/section/div[2]/div/div[3]/app-tipo-retirada/section/div/div/ul/li[2]/button/div/header/span',
            )
        )
    )
    result_element.click()

    # Localizando o elemento que contém o modelo do carro
    elemento_modelo_carro = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="main-content"]/app-fluxo-reserva/app-selecao-ofertas-opcionais/section/div[2]/div/div[2]/app-resumo-reserva/ds-reservation-resume/section/div[2]/ds-reservation-resume-item[3]/div/div[1]/div[2]/p',
            )
        )
    )
    # Localizando o elemento que contém o modelo do carro
    elemento_preco_carro = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/loc-root/main/app-fluxo-reserva/app-selecao-ofertas-opcionais/section/div[2]/div/div[2]/app-resumo-reserva/ds-reservation-resume/section/div[3]/div/span[1]",
            )
        )
    )

    # Armazenando o texto do elemento na variável
    modelo_carro = elemento_modelo_carro.text
    preco_carro = elemento_preco_carro.text

    print(modelo_carro)
    print(preco_carro)

    time.sleep(5)

    # Quando terminar, você pode fechar o navegador:
    driver.close()


def capitalize(s):
    return " ".join(word.capitalize() for word in s.split())