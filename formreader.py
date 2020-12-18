from bs4 import BeautifulSoup
import requests, random, time
from selenium import webdriver

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

        i_quest = 1

        for question in questions:
            buttons = question.find_elements_by_class_name("appsMaterialWizToggleRadiogroupRadioButtonContainer")
            buttons2 = question.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
            try:
                textfield = question.find_element_by_class_name("quantumWizTextinputPaperinputContentArea")
            except:
                try:
                    textfield = question.find_element_by_class_name("quantumWizTextinputPaperinputMainContent")
                except:
                    try:
                        textfield = question.find_element_by_class_name("quantumWizTextinputPaperinputInput")
                    except:
                        textfield = []
                        pass
            
            #textfield = question.find_elements_by_xpath("//input[@class = 'quantumWizTextinputPaperinputInput exportInput']")
            print(f"{i_quest}) {len(buttons), len(buttons2)}")
            i_quest += 1
            if len(buttons) == 0 and len(buttons2) == 0:
                driver.execute_script("arguments[0].scrollIntoView()", textfield)
                print(textfield)    
                textfield.click()
                textfield.send_keys("lol spam")
            #elif type(textfield) == 'FirefoxWebElement':
                
            elif len(buttons) != 0 and len(buttons2) == 0:
                rnd = random.choice(buttons[:-1])
                driver.execute_script("arguments[0].scrollIntoView()", rnd)
                try:
                    rnd.click()
                except:
                    pass
            elif len(buttons) == 0 and len(buttons2) != 0:
                rnd = random.choice(buttons2[:-1])
                driver.execute_script("arguments[0].scrollIntoView()", rnd)
                try:
                    rnd.click()
                except:
                    pass
            else:
                pass


        # WIP - not working
        driver.find_element_by_xpath("//span[@class = 'appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']").click()
        time.sleep(60)
#test = getForm('https://docs.google.com/forms/d/e/1FAIpQLScwMpN6oucYUIz7V31IiDGzJEOKjFO5Rh-iuRHKoCqenea7hQ/viewform?fbclid=IwAR0-flg2mSJiD2xNEwABwHIVj6sU00wpz6LmUN_rIhyySKEzTxuuanZzGs4')
test = getForm('https://docs.google.com/forms/d/e/1FAIpQLSf7bMgAlHULriA6npZ3jkmERiVfxUtk6gDyrBLGIgsEKOAg3w/viewform?fbclid=IwAR1DGGvwLAQHCB-nRE0Kf635saU_VQMJ25CIEHYuXidpdXxLnOwBCvMF3S0')
test.getSource()
