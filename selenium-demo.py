import time
from selenium import webdriver

# driver_path=""
driver = webdriver.Firefox()
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get('http://localhost/otrs/index.pl')

driver.find_element_by_id('User').send_keys('monitor')
driver.find_element_by_id('Password').send_keys('Xiaoniu@2018')

driver.find_element_by_id('LoginButton').click()

time.sleep(10)
try:
    while 1:
        driver.refresh()
        print('[%s] OTRS Dashboard Refresh Successful!' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        time.sleep(60)
except Exception as e:
    print('Exception Found:', format(e))
    driver.execute_script('window.stop()')
