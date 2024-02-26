import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

http = 'http://127.0.0.1:8000/'


class Test(unittest.TestCase):

    def test_conexion(self):
        response = requests.get(http)
        self.assertEqual(response.status_code, 200, "no se conecto")

class LoginTest(unittest.TestCase):

    def index(self):
        self.user = {"username":"usertest", "password":"passtest"}
    
    def test_login_correct(self):
        response = requests.get(http)
        self.user = {"username":"usertest", "password":"passtest"}
        csrf_token = response.cookies['csrftoken']
        respons = requests.post(http,json=self.user, headers={'X-CSRFToken': csrf_token})
        name = self.user["username"]
        self.assertEqual(respons.status_code, 302, "No funciono el login")

        ruta = r"c:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta

        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/homeUser")

        titulo = WebDriverWait(driver, 10).until(EC.element_to_be_selected((By.XPATH, "/html/body/div[1]/h3[text()]")))
        self.assertEqual(titulo, f"BIENVENIDO USER{name}", "salio como el culo")

if __name__ == '__main__':
    unittest.main()

