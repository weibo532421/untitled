import requests
import json
import unittest

class Mytest(unittest.TestCase):
    """百度请求"""

    def setUp(self):
        print("Test start")


    def tearDown(self):
        print("Test stop")



class test_baidu_get(Mytest):

    def test_baidu_get(self):
        self.url='https://www.baidu.com'
        self.header={"content-Type":"application/json"}
        r=requests.get(url=self.url)

        print (r.text)
        print(r.status_code)

if __name__=='__main__':
    unittest.main()
