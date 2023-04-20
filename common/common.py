from selenium import webdriver
from conftest import browser
import allure
import logging.config

# 拿到配置文件
logging.config.fileConfig('log.ini')
# 拿到日志器
log = logging.getLogger()


class basepage():
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    with allure.step('访问网址'):
        def visit(self, url):
            log.info('访问网址{}'.format(url))
            self.driver.get(url)

    with allure.step('查找元素'):
        def loc(self, loc):
            return self.driver.find_element(*loc)

    with allure.step('输入框输入'):
        def input(self, loc, txt):
            self.loc(loc).send_keys(txt)

    with allure.step('点击'):
        def click(self, loc):
            self.loc(loc).click()
    with allure.step('断言'):
        def get_title(self):
            text = self.driver.title
            return text
