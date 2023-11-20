from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import unicodedata
import time
import re


def nome_do_mes(numero):
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }

    return meses.get(numero, "Número inválido")


def remover_acentos(txt):
    # Normaliza o texto para a forma NFD e remove marcas diacríticas (acentos)
    txt = unicodedata.normalize("NFD", txt)
    txt = txt.encode("ascii", "ignore")
    txt = txt.decode("utf-8")
    return txt


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
    CHROMEDRIVER_PATH = r"/usr/bin/chromedriver"
    # CHROMEDRIVER_PATH = r'C:\Users\vitor\Desktop\chromedriver-win64\chromedriver.exe'
    webdriver.Chrome.driver_path = CHROMEDRIVER_PATH
    driver = webdriver.Chrome()

    # Acesse o site
    driver.get("https://www.localiza.com/brasil/pt-br")
    data_ida = str(year_arrive) + "-" + str(month_arrive) + "-" + str(day_arrive)
    data_ida = re.sub(r'[()."-]', "", data_ida).strip()
    data_ida = data_ida[0:4] + "-" + data_ida[5:7] + "-" + data_ida[8:10]
    data_volta = (
        str(year_departure) + "-" + str(month_departure) + "-" + str(day_departure)
    )
    data_volta = re.sub(r'[()."-]', "", data_volta).strip()
    data_volta = data_volta[0:4] + "-" + data_volta[5:7] + "-" + data_volta[8:10]
    cidade_destino = city
    # Converter as strings de data em objetos datetime
    data_ida_obj = datetime.strptime(data_ida, "%Y-%m-%d")
    print(data_ida_obj)
    data_volta_obj = datetime.strptime(data_volta, "%Y-%m-%d")

    # Extrair ano, mês (nome) e dia
    ano_chegada, mes_chegada, dia_chegada = (
        data_ida_obj.year,
        data_ida_obj.month,
        data_ida_obj.day,
    )
    ano_saida, mes_saida, dia_saida = (
        data_volta_obj.year,
        data_volta_obj.month,
        data_volta_obj.day,
    )
    ano_chegada = str(ano_chegada)
    mes_chegada = nome_do_mes(mes_chegada)
    dia_chegada = str(dia_chegada)
    print(mes_chegada)
    ano_saida = str(ano_saida)
    mes_saida = nome_do_mes(mes_saida)
    dia_saida = str(dia_saida)
    # Converter o nome da cidade para minúsculas e remover acentos
    cidade = remover_acentos(cidade_destino).lower()

    # função caixa alta
    def capitalize(s):
        return " ".join(word.capitalize() for word in s.split())

    cidade = capitalize(cidade)

    # Localize o elemento input e digite "rio de janeiro"
    input_element = driver.find_element(By.ID, "mat-input-1")
    input_element.send_keys(cidade)
    input_element.send_keys(Keys.RETURN)

    # Aguarda até que o elemento dropdown esteja visível
    wait = WebDriverWait(driver, 10)
    dropdown = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "places-list"))
    )

    # Clique no item desejado
    desired_item = driver.find_element(
        By.XPATH, "//span[contains(text(), '" + cidade + "')]"
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
                + ano_chegada
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
                + mes_chegada
                + " de "
                + ano_chegada
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
                + dia_chegada
                + " de "
                + mes_chegada
                + " de "
                + ano_chegada
                + "']",
            )
        )
    )
    dia_selecao.click()

    time_option = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(), '10:00')]")
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
                "td[role='gridcell'][data-mat-col='0'][aria-label='" + ano_saida + "']",
            )
        )
    )
    ano_selecao.click()

    mes_selecao = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "td[role='gridcell'][aria-label='"
                + mes_saida
                + " de "
                + ano_saida
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
                + dia_saida
                + " de "
                + mes_saida
                + " de "
                + ano_saida
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
    # Definição de coleção de hoteis
    carros = []
    carros.append = {"modelo": modelo_carro, "valor": preco_carro}

    # Quando terminar, você pode fechar o navegador:
    driver.close()

    return carros


def capitalize(s):
    return " ".join(word.capitalize() for word in s.split())
