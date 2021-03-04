import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
from email.mime.text import MIMEText
import smtplib
import schedule

s = smtplib.SMTP('smtp.gmail.com', 587)


def send_email(f):
    s.starttls()
    s.login('kjs65623799@gmail.com', 'dflqwptbkvmlbrxn')
    msg = MIMEText(f)
    msg['Subject'] = '자가진단'
    msg['To'] = "kdskds96242337@gmail.com"
    s.sendmail("kjs65623799@gmail.com",
               "kdskds96242337@gmail.com", msg.as_string())
    s.quit()


def main():
    try:
        driver = webdriver.Chrome('.//chromedriver.exe')
        ac = ActionChains(driver)
        url = 'https://hcs.eduro.go.kr/#/relogin'
        driver.get(url)
        driver.set_window_position(50, 50)
        driver.find_element_by_id('btnConfirm2').click()
        driver.find_element_by_class_name('searchBtn').click()
        driver.find_element_by_xpath('//*[@id="sidolabel"]/option[6]').click()
        driver.find_element_by_xpath('//*[@id="crseScCode"]/option[4]').click()
        driver.find_element_by_xpath('//*[@id="orgname"]').send_keys("장덕중학교")
        driver.find_element_by_xpath(
            '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
        driver.implicitly_wait(1)
        school = driver.find_element_by_xpath(
            '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li')
        ac.move_to_element(school).click().perform()
        driver.find_element_by_xpath(
            '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
        driver.find_element_by_xpath(
            '//*[@id="user_name_input"]').send_keys('김준서')
        driver.find_element_by_xpath(
            '//*[@id="birthday_input"]').send_keys('060504')
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys("0605")
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#container > div:nth-child(1) > section.memberWrap > div:nth-child(2) > ul > li > a > em").click()
        time.sleep(2)
        for i in range(1, 4):
            time.sleep(0.5)
            driver.find_element_by_css_selector(
                f"#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child({i}) > dd > ul > li:nth-child(1) > label"
            ).click()
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        send_email('''자가진단에 성공하였습니다''')
    except:
        send_email('''자가진단에 실패하였습니다''')


schedule.every().days.at("07:30").do(main)
if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
