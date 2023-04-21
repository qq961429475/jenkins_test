import os
import shutil
import pytest


if __name__ == '__main__':
    # 不要加-s参数，allure将stdout输出到allure报告，加了只会输出到console里
    # 用例执行步骤中会有一个stdout附件记录单个用例执行过程中的stdout
    pytest.main(["-v", "./test_case/", "--alluredir", "./allure-results", "--clean-alluredir"])
    shutil.copy("environment.properties", "./allure-results")
    os.system('allure generate ./allure-results/ -o ./report_allure/ --clean')
    # os.system('allure serve result')
