import os
os.system("pip install selenium")

#Importação dos componentes necessários ao funcionamento do webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from time import sleep
keep_alive = True

#apenas para limpar a tela
import os
os.system("cls")


#about
about = """     WoS Downloader
A simple downloader for Web of Science bibliographic data
Version 1.10 Beta
Created by Gabriel Gustavo Soares Santos

"""
print(about)



#Descrição de opções de Download
textSaveTo = """Em qual lugar você deseja salvar seu arquivo? Digite a opção correspondente:
    1- Salvar em EndNote online (em implantação)
    2- Salvar no EndNote para desktop (em implantação)
    3- Salvar no ResearcherID - Eu escrevi estas publicações (em implantação)
    4- Salvar em InCites (em implantação)
    5- Salvar em outros formatos de arquivo

"""

textSaveAs = """Em qual lugar você deseja salvar seu arquivo? Digite a opção correspondente:
    1- Autor, Título, Fonte
    2- Autor, Título, Fonte, Resumo
    3- Registro completo
    4- Registro completo e Referências citadas

"""



#Selecão de opções para download:
optionSaveTo = 5
while ((optionSaveTo < 1) or (optionSaveTo > 5)):

    print(textSaveTo)
    optionSaveTo = int(input("Digite a opção desejada: "))

    if ((optionSaveTo < 1) or (optionSaveTo > 5)):
        print("Opção inválida, tente novamente!")

    else:
        if optionSaveTo == 1:
            selectionSaveTo = "enw"
        elif optionSaveTo == 2:
            selectionSaveTo = "endnote"
        elif optionSaveTo == 3:
            selectionSaveTo = "rid"
        elif optionSaveTo == 4:
            selectionSaveTo = "incites"
        elif optionSaveTo == 5:
            selectionSaveTo = "other"

selectionSaveTo = "other"

optionSaveAs = 4
while ((optionSaveAs < 1) or (optionSaveAs > 4)):
    print(textSaveAs)
    optionSaveAs = int(input("Digite a opção desejada: "))
    if ((optionSaveAs < 1) or (optionSaveAs > 4)):
        print("Opção inválida, tente novamente!")

    else:
        if optionSaveAs == 1:
            selectionSaveAs = "PMID AUTHORSIDENTIFIERS ACCESSION_NUM ISSN CONFERENCE_SPONSORS CONFERENCE_INFO SOURCE TITLE AUTHORS  "
        elif optionSaveAs == 2:
            selectionSaveAs = "PMID AUTHORSIDENTIFIERS ACCESSION_NUM ISSN CONFERENCE_SPONSORS ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  "
        elif optionSaveAs == 3:
            selectionSaveAs = "HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  "
        elif optionSaveAs == 4:
            selectionSaveAs = "HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  "


selectionSaveAs = "HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  "

#breakline        
bl = """ 
"""
print(bl)

#Opções para navegação
haveLink = "G"
#igual a "S" para pular esta parte, ainda em implementação
address = "http://isiknowledge.com/"
while ((haveLink != "S") and (haveLink != "N")):
	haveLink = input("Você já possui um link da pesquisa? (s/n) ")
	haveLink = haveLink.upper()

	if haveLink == "N":
		print("Então faça a sua pesquisa, quanto estiver pronto retorne aqui! ")
		nav = webdriver.Chrome()
		nav.get(address)

	elif haveLink == "S":
		address = input("Entre com o link da sua pesquisa ")

	else:
		print("Os dados informados são inválidos, digite apenas 'S' ou 'N'")
	
	
#Confirmação final antes do início do Download
print(bl)
#nav = webdriver.Chrome()
#nav.get(address)
if haveLink == "S":
	nav = webdriver.Chrome()
	nav.get(address)

ready = "N"
while (ready != "OK"):
    total = int(input("Informe o número total de registros "))
    ready = input("Quando você estiver pronto digite 'OK' ")
    ready = ready.upper()



#Parâmetros para o laço de repetição que fará o download
#Ainda em implantação
#total = 100000
#total = total + 500
#eXCLUPI 1977
i = (0*500)+1
z = i
f = i+ 499
cont = int(1)

#Início do Laço
while f <= total:
    print(cont)
    cont = cont + 1
    #nav.implicitly_wait(100)
    #nav.refresh()        
    time.sleep(6)

    #Seleção do destino de salvamento
    if i == z:        
        saveTo = nav.find_element_by_id("exportTypeName")
        saveTo.click()
        saveTo2 = nav.find_element_by_xpath("//ul[@id='saveToMenu']/li[3]/a")
        saveTo2.click()
    else:
        saveTo = nav.find_element_by_xpath("/html/body/div[1]/div[26]/div[2]/div/div/div/div[2]/div[3]/div[3]/div[2]/div[1]/ul/li/button")
        saveTo.click()
    

    #Preenchimento do formulário
    markFrom = nav.find_element_by_id('markFrom')
    markFrom.clear()
    markFrom.send_keys(i)
    #time.sleep(3)
    markTo = nav.find_element_by_id('markTo')
    markTo.clear()
    markTo.send_keys(f)
    #time.sleep(3)
    nav.find_element_by_id('numberOfRecordsRange').click()
    #time.sleep(8)

   
    #Seleção do tipo de Download
    saveAs = Select(nav.find_element_by_id("bib_fields")) 
    saveAs.select_by_value(selectionSaveAs)

    
    #Fazer download e fechar janela
    send =  nav.find_element_by_css_selector('#exportButton')
    send.click()

    time.sleep(2)
    close = nav.find_element_by_xpath('//*[@id="page"]/div[11]/div[2]/form/div[2]/a')
    #close = nav.find_element_by_xpath('/html/body/div[11]/div[2]/form/div[2]/a')
    #close = nav.find_element_by_css_selector('.quickoutput-cancel-action')
    #close = nav.find_element_by_class_name('//*[@id="page"]/div[11]/div[1]/button')
    #close = nav.find_element_by_class_name('//*[@id="page"]/div[11]/div[1]/button/span[1]')
    #close = nav.find_element_by_class_name('flat-button quickoutput-cancel-action')
    close.click()

    #nav.implicitly_wait(20)
    #nav.refresh()        
    #time.sleep(15)
    
    #Controle do laço de repetição!
    i = f + 1
    f = f + 500



print("Fim da operação")


