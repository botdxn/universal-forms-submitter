from bs4 import BeautifulSoup
import requests, random, time
from selenium import webdriver

form_types = ['freebirdFormviewerViewNumberedItemContainer']

class getForm:
    def __init__(self, url):
        self.url = url
    
    def getSource(self):
        #request = requests.get(self.url)
        #soup = BeautifulSoup(request.text, 'html.parser')
        driver = webdriver.Firefox()
        driver.get(self.url)
        questionsContainer = driver.find_element_by_class_name("freebirdFormviewerViewItemList")
        #questionsContainer = soup.find("div", {"class": "freebirdFormviewerViewItemList"})
        #questions = questionsContainer.find_all("div", {"class": "freebirdFormviewerViewNumberedItemContainer"})
        questions = questionsContainer.find_elements_by_class_name("freebirdFormviewerViewNumberedItemContainer")
        print(f"Found {len(questions)} questions")


        for question in questions:
            buttons = question.find_elements_by_class_name("appsMaterialWizToggleRadiogroupRadioButtonContainer")
            buttons2 = question.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
            print(len(buttons), len(buttons2))
            if len(buttons) == 0 and len(buttons2) == 0:
                pass
            elif len(buttons) != 0 and len(buttons2) == 0:
                rnd = random.choice(buttons)
                driver.execute_script("arguments[0].scrollIntoView()", rnd)
                try:
                    rnd.click()
                except:
                    pass
            elif len(buttons) == 0 and len(buttons2) != 0:
                rnd = random.choice(buttons2)
                driver.execute_script("arguments[0].scrollIntoView()", rnd)
                try:
                    rnd.click()
                except:
                    pass
            else:
                pass
        

        # WIP - not working
        driver.find_element_by_xpath("//span[@class = 'appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']").click()
        
        time.sleep(25)

