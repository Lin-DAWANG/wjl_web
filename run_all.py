import unittest
from common import HTMLTestRunner_cn

casePath = "D:\PycharmProjects\web_auto\case"
rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir = casePath, pattern = rule)
print(discover)

reportPath = "D:\\PycharmProjects\\web_auto\\report\\"+"result.html"
fp = open(reportPath,"wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title="报告名称",
                                       description="描述")
runner.run(discover)
fp.close()