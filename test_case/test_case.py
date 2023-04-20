import os
import pytest
import yaml
import allure
from common.common import basepage
from common.file_read import read_yalm


# def test_01(browser):
#     driver = browser
#     driver.get('https://www.baidu.com')
#     driver.find_element(By.ID, 'kw').send_keys('你好')
#     driver.find_element(By.ID, 'su').click()
#     assert driver.title == '你好_百度搜索'
@pytest.mark.parametrize('data', read_yalm("111.yaml"))
def test_01(data):
    print('开始测试')
    print(str(data))


@allure.story('百度首页1111111111')
@allure.feature('搜索模块111111111')
@allure.title('百度搜索')
@pytest.mark.parametrize('data', read_yalm('111.yaml'))
def test_03(browser, data):
    """
        百度搜索
        :param browser:
        :param data:
        :return:
    """
    print(data)
    driver = basepage(browser)
    driver.visit(data['url'])
    driver.input(data['loc'], data['txt'])
    driver.click(data['commit_idvalue'])
    assert driver.get_title() == data['expected']


if __name__ == '__main__':
    # 不要加-s参数，allure将stdout输出到allure报告，加了只会输出到consloe里
    # 用例执行步骤中会有一个stdout附件记录单个用例执行过程中的stdout
    pytest.main(["test_case.py", "--alluredir", "./result", "--clean-alluredir"])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
    os.system('allure serve result')
