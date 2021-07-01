import random
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def fill_form(driver, url):
    driver.get(url)
    questionsContainer = driver.find_element_by_class_name("freebirdFormviewerViewItemList")
    questions = questionsContainer.find_elements_by_class_name("freebirdFormviewerViewNumberedItemContainer")

    for question in questions:
        buttons = question.find_elements_by_class_name("appsMaterialWizToggleRadiogroupRadioButtonContainer")
        buttons2 = question.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
        try:
            textfields = question.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
        except Exception as e:
            print(f"Pola tekstowe nie znalezione.\n{e}")
            pass
        if len(buttons) == 0 and len(buttons2) == 0:
            for textfield in textfields:
                print(textfield)
                textfield.send_keys("lol spam")

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

    submit = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div/div/div/span/span")
    submit.click()
    return True


def main():
    threads = 2
    per_thread = 20
    done = 0
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1420,1080")
    options.add_argument("--disable-gpu")
    drivers = [webdriver.Firefox(options=options) for _ in range(threads)]

    link = 'https://docs.google.com/forms/d/1TBbCXTwmdT6FMYx8FAYDkwOGfkUZ1LkKu6uKq9bwjDM/edit'

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        for x in range(per_thread):
            futures = [executor.submit(fill_form, driver, link) for driver in drivers]
            for future in futures:
                if future.result():
                    done += 1
                    print(done)

    # close all active drivers after the process completed
    if done == threads * per_thread:
        for drv in drivers:
            drv.quit()
    print(done)


if __name__ == '__main__':
    main()
