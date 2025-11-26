from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

URL = "https://www.todamateria.com.br/segunda-guerra-mundial/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

time.sleep(3)

titulo = driver.find_element(By.TAG_NAME, "h1").text
print("Título da página:", titulo)

paragrafos = driver.find_elements(By.TAG_NAME, "p")

print("\nConteúdo extraído:\n")
for p in paragrafos:
    print(p.text)

driver.quit()
