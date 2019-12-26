from selenium import webdriver
import config
from datetime import datetime, date
import time
import sys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

def fillForm():
    office = browser.find_element_by_id("officeId")  #
    Select(office).select_by_visible_text(config.location)
    if config.testType == "auto":
        browser.find_element_by_id("DT").click()
    elif config.testType == "motor":
        browser.find_element_by_id("MC").click()
        browser.find_element_by_id("yes").click()
    else:
        print("Correct config.py for testType")
        sys.exit()
    browser.find_element_by_id("firstName").send_keys(config.firstName)
    browser.find_element_by_id("lastName").send_keys(config.lastName)
    browser.find_element_by_id("dl_number").send_keys(config.ID)
    browser.find_element_by_id("birthMonth").send_keys(config.birthMonth)
    browser.find_element_by_id("birthDay").send_keys(config.birthDay)
    browser.find_element_by_id("birthYear").send_keys(config.birthYear)
    browser.find_element_by_id("areaCode").send_keys(config.phonenum1)
    browser.find_element_by_id("telPrefix").send_keys(config.phonenum1)
    browser.find_element_by_id("telSuffix").send_keys(config.phonenum1)
    browser.find_element_by_xpath('//*[@id="findOffice"]/fieldset/div[5]/input[2]').click()


    for number in range(25):
        try:
            browser.find_element_by_xpath('//*[@id="formId_1"]/div/div[2]/table/tbody/tr/td[2]/p[2]/strong')
            print('CAPTCHA passed')
            break
        except NoSuchElementException:
            print(str(100 - (number * 4)) + ' seconds remaining for CAPTCHA!')
            time.sleep(4)
            pass


def determineRepeated(tempDate, date_list):
    if (len(date_list) == 0):
        return False
    else:
        for i in range(len(date_list)):
            if str(tempDate) == str(date_list[i]):
                return True
            else:
                continue
        return False


def convertDateStr(strdate_list):
    date_list = []
    for i in range(len(strdate_list)):
        date = datetime.strptime(strdate_list[i], '%Y-%m-%d').date()
        date_list.append(date)
    return date_list


def register(num):
    browser.find_element_by_xpath('//*[@id="app_content"]/div/a[1]').click()
    if num == 0:
        print("Booking appointment on first run!")
    else:
        print("Booking appointment..")
        browser.find_element_by_xpath('// *[ @ id = "ApptForm"] / button').click()
    try:
        browser.find_element_by_id("telephone_method").click()
    except NoSuchElementException:
        pass
    browser.find_element_by_xpath('//*[@id="ApptForm"]/fieldset/div[11]/button').click()
    browser.find_element_by_xpath('// *[ @ id = "ApptForm"] / fieldset / div[9] / button').click()
    scrollTo = browser.find_element_by_xpath('//*[@id="app_content"]/div/p[1]/strong')
    browser.execute_script("arguments[0].scrollIntoView();", scrollTo)
    browser.save_screenshot('CurrentlyBooked.png')
    print("Done! CHECK CURRENTLYBOOKED.PNG!")


def dateFitsPreferences(tempDate):
    delta = tempDate - today()
    if delta.days <= config.desiredDateRange:
        return True
    else:
        return False


def search(date_list, closest):
    while True:
        try:
            print(date_list)
            strdate_list = [line.strip() for line in open("dateLog.txt", 'r')]
            date_list = convertDateStr(strdate_list)

            if len(date_list) == 0:
                pass
            else:
                closest = min(date_list)

            tempDate = datetime.strptime(
                browser.find_element_by_xpath('//*[@id="formId_1"]/div/div[2]/table/tbody/tr/td[2]/p[2]/strong').text,
                '%b %d, %Y at %I:%M %p').date()
            if dateFitsPreferences(tempDate):
                if determineRepeated(tempDate, date_list):
                    pass
                else:
                    print('New entry found! ////////////////////' + str(tempDate))
                    dateLog = open("dateLog.txt", "a")
                    dateLog.write(str(tempDate) + "\n")
                    dateLog.flush()
                    date_list.append(tempDate)
                    if len(date_list) != 0:
                        newclosest = min(date_list)
                        if len(date_list) == 1:
                            register(0)
                            break
                        else:
                            if closest != newclosest:
                                register(1)
                                break
            else:
                pass
            time.sleep(config.refreshInterval)
            print(date_list)
            print("------------------")
            # "Refresh" Search
            Select(browser.find_element_by_id("requestedTime")).select_by_visible_text('8:00 AM')
            browser.find_element_by_id("checkAvail").click()

        except NoSuchElementException:
            print("Webpage error. Refreshing...")
            time.sleep(config.refreshInterval)
            browser.refresh()


date_list = []
closest = 0
today = date.today

while True:
    browser = webdriver.Chrome()
    browser.set_page_load_timeout(10)
    browser.get("https://www.dmv.ca.gov/wasapp/foa/driveTest.do")
    fillForm()
    search(date_list, closest)
    print("Restarting browser...")
    browser.quit()
    continue
