import unittest

from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail(file_new):

    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header('自动化测试报告','utf-8')

    smtp=smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("503483264@qq.com", "zkvhuhzxuvyobgdf")
    smtp.sendmail("503483264@qq.com", "3044721565@qq.com", msg.as_string())
    smtp.quit()
    print('邮件已发出')

def new_report(test_report):

    lists=os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getatime(test_report+'\\'+fn))
    file_new=os.path.join(test_report,lists[-1])
    print(file_new)
    return file_new

if __name__=='__main__':
    test_dir="./test_case"
    test_report="./report"

    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    now=time.strftime("%Y-%m-%d_%H-%M-%S-")

    filename=test_report+"\\"+now+'result.html'

    fp=open(filename,'wb')

    runner=HTMLTestRunner(stream=fp,
                          title='自动化测试报告',
                          description="测试执行情况")

    runner.run(discover)
    fp.close()

    new_report=new_report(test_report)
    send_mail(new_report)
