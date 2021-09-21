from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get("https://cliente.americanas.com.br/simple-login/?next=https%3A%2F%2Fwww.americanas.com.br%2F%3Fepar%3Dbp_br_00_go_sch_brand_americanas_202002%26utm_medium%3Dbuscappc%26utm_source%3Dgoogle%26utm_campaign%3Dmarca%3Aacom%253bmidia%3Abuscappc%253bformato%3Abranding%253bsubformato%3A00%253bidcampanha%3Asch_brand_americanas_202002%26opn%3DYZMEZP%26WT.srch%3D1%26gclid%3DCjwKCAjwhaaKBhBcEiwA8acsHBhsjD3Stq8X4DDVwn3z94KdVK-DuSwafADWltozJTJ_ctRNp4zUvhoCCBYQAvD_BwE")
time.sleep(10)
username = browser.find_element_by_id("email-input")
password = browser.find_element_by_id("password-input")
username.send_keys("exemplo@exemplo.com") #Colocar um e-mail valido autenticado do e-commerce americanas.com.br
password.send_keys("senha1234") #Colocar a senha de acordo com o e-mail valido autenticado do e-commerce americanas.com.br
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()