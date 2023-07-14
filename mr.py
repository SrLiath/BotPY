from selenium import webdriver
import time as timo
from datetime import datetime
from selenium.webdriver.common.keys import Keys
usuario = input("bot iniciado, digite seu usuario: ")
senha = input ("\nDigite sua senha: ")
ticket = input("\nDigite seu ticket: #")
driver = webdriver.Chrome()
#driver=webdriver.firefox()
#driver=webdriver.ie()
#abre a janela
driver.maximize_window()
#navigate to the url
driver.get("Censurado")
#nome e id
user=driver.find_element("id", "name")
user.send_keys(usuario)
passa=driver.find_element("id", "pass")
passa.send_keys(senha)
button = driver.find_element("name","submit")
button.click()
timo.sleep(2)
tticket = driver.find_element("name", "query")
tticket.send_keys(ticket)
driver.find_element("xpath", "//*[@id='basic_search']/form/div/button").click()
timo.sleep(1)
driver.find_element("link text", ticket).click()
timo.sleep(1)
driver.find_element("xpath", "//*[@id='resp_sec']/tr[3]/td/div[1]/div[1]/div/a[1]").click()
timo.sleep(1)
clientee = driver.find_elements("xpath", "//*[@id='content']/table[1]/tbody/tr/td[2]/table/tbody/tr[1]/td/a[1]")
cliente = clientee[0].text
driver.find_element("xpath", "//*[@id='response']").clear()
time = datetime.now()
TIME = time.strftime('%H')
if (TIME <= "11"):
    tempo = "Bom dia"
elif (TIME <= "17" ):
    tempo = "Boa tarde"
elif (TIME >= "18"):
    tempo = "Boa noite"
driver.find_element("xpath", "//*[@id='response']").send_keys("""<p> """ + tempo + """, """ + cliente +""" <br>
<br> Gostaria de confirmar se o problema deste chamado foi resolvido?
<br> Posso ajudar em mais alguma coisa?<br>
<br> Caso precise, pode responder esse e-mail que o chamado será reaberto.
<br> Segue o link para a avaliação do meu atendimento para este chamado """ + ticket + """<br>
<br><a href="https://forms.gle/HCJuMjRUfgLALEGV8">Formulário de avaliação</a><br><br> Atenciosamente;<br>""" + usuario + """ - Tips Tecnologia<br></p>
""")
driver.find_element("name", "reply_status_id").click()
timo.sleep(0.5)
driver.find_element("name", "reply_status_id").send_keys("R")
driver.find_element("name", "reply_status_id").send_keys(Keys.ENTER)
driver.find_element("xpath", "//*[@id='reply']/p/input[1]").click()
#fecha browser
driver.close()
print("postado")