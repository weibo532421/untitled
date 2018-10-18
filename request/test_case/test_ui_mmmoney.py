import unittest
import csv
import scripts.h5firefox
import scripts.h5chrome
import scripts.pcfirefox
import csv
import unittest
import scripts.pcchrome
import scripts.appAndriod

from scripts.h5firefox import Test_mmmoney


class MyTest(unittest.TestCase):


    def setUp(self):
        print('test start')

    def tearDown(self):
        pass


# class Test_Firefox_login(MyTest):
#     """钱包H5火狐请求"""
#
#
#     def test_login(self):
#         date=csv.reader(open('D:\\untitled\\request\\date\\01.csv','r'))
#         for user in date:
#             phone=user[1]
#             password=user[2]
#             a=scripts.h5firefox.Test_mmmoney()
#             a.login(phone,password)
#             a.loginout( )
#
# class Test_Chrome_login(MyTest):
#     """钱包H5谷歌请求"""
#
#     def test_login(self):
#         date=csv.reader(open('D:\\untitled\\request\\date\\01.csv','r'))
#         for user in date:
#             phone=user[1]
#             password=user[2]
#             a=scripts.h5chrome.Test_mmmoney()
#             a.login(phone,password)
#             a.loginout( )
#
# class Test_Chrome_pc(MyTest):
#     """钱包pc谷歌请求"""
#
#     def test_login(self):
#         date = csv.reader(open('D:\\untitled\\request\\date\\01.csv', 'r'))
#         for user in date:
#             phone = user[1]
#             password = user[2]
#             a = scripts.pcchrome.Pc_mmmoney()
#             a.login_in(phone,password)
#             a.login_out()
#
# class Test_Firefox_pc(MyTest):
#     """钱包火狐请求"""
#
#     def test_login(self):
#         date = csv.reader(open('D:\\untitled\\request\\date\\01.csv', 'r'))
#         for user in date:
#             phone = user[1]
#             password = user[2]
#             a = scripts.pcfirefox.Pc_mmmoney()
#             a.login_in(phone, password)
#             a.login_out()

class Test_huawei(MyTest):

    def test_login(self):
        date=csv.reader(open('D:\\untitled\\request\\date\\01.csv','r'))
        for user in date:
            phone=user[1]
            pasword=user[2]
            a=scripts.appAndriod.Test_app()
            a.test(phone,pasword)






if __name__=='__main__':
    unittest.main()