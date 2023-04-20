import os

import allure
import pytest
from selenium import webdriver


# @pytest.mark.hookwrapper(hookwrapper=True)(旧写法)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param call:
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            with allure.step("添加失败截图。。。"):
                allure.attach(driver.get_screenshot_as_png(),
                              "失败截图", allure.attachment_type.PNG)


def capture_screenshots(case_path):
    """
        配置用例失败截图路径，以用例nodeid保存图片
    :param case_path: nodeid
    :return:
    """
    # 使用全局变量driver
    global driver
    # 需要处理case_path，不能有/，以/为分隔符，保留最后一段
    file_name = case_path.split("/")[-1]
    # 声明图片保存路径
    image_dir = os.path.join("../report", "image", file_name)
    # 浏览器驱动，在用例前置里实例化
    driver.save_screenshot(image_dir)


@pytest.fixture(scope="session", autouse=True)
def browser():
    """
        全局定义浏览器启动
    """
    global driver
    options = webdriver.ChromeOptions()
    # 去掉密码管理弹窗
    prefs = dict()
    prefs["credentials_enable_services"] = False
    prefs["profiles.password_manager_enabled"] = False
    options.add_experimental_option('prefs', prefs)
    # 最大化
    options.add_argument("start-maximized")
    # 无头模式：
    options.add_argument('--headless')
    # 去掉浏览器提示自动化黄条
    options.add_experimental_option('useAutomationExtension', False)
    # 禁用浏览器正在被自动化程序控制的提示
    options.add_argument('--disable-infobars')
    # 配置忽略HTTPS安全证书提示
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    print("test end!")
    # return driver
