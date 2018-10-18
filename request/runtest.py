import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from test_case import test_request_mmmoney

suite=unittest.TestSuite()
suite.addTest(test_request_mmmoney.test_baidu_get("test_baidu_get"))
test_dir='D:\\untitled\\request\\report'
if __name__=='__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(suite)
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename='./report'+'./'+now+'test_result.html'
    fp=open(filename,'wb')

    runner=HTMLTestRunner(stream=fp,
                          title='接口测试报告',
                          description="测试执行情况")

    runner.run(testunit)
    fp.close()