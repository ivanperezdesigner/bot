from selenium import webdriver
from time import sleep

# url = 'https://www.youtube.com'
url = 'https://chaturbate.com/oksanafedorova/'
sleep_time = 3
new_tabs = 5

def bot_scraper(url, time, tabs):
    global driver
    driver=webdriver.Chrome()
    driver.get(url)
    sleep(time)
    driver.find_element_by_xpath('//*[@id="close_entrance_terms"]').click()
    for i in range (tabs):
        driver.execute_script("window.open()")
        # print(f'windows number {i}')
        driver.switch_to.window(driver.window_handles[i + 1])
        driver.get(url)
        sleep(time)
    # driver.quit()
# print(browser.window_handles)
# print(len(browser.window_handles))
# browser.switch_to_window(browser.window_handles[0])
# browser.get("https://python.org")

bot_scraper(url, sleep_time, new_tabs)