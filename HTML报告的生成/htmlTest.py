import unittest,csv
import os,sys
import time
import HTMLTestRunner


def createsuite():
    discover=unittest.defaultTestLoader.discover('E:/Pythoncode',pattern='test*.py',top_level_dir=None)
    print (discover)
    return discover
if __name__=="__main__":
    curpath=sys.path[0]
    #sys.path是一个list
    #取当前时间
    #对时间格式化time.strftime("格式化的形式"，time.localtime本地时间，time.time()获取时间戳)
    #为了生成的HTML报告名字不重复，引入时间戳   时间戳time.time()
    #将时间戳转换为本地的一个时间time.localtime(time.time())
    #再将本地时间以"%Y-%m-%d-%H %M：%S"的形式输出
    now=time.strftime("%Y-%m-%d-%H %M %S",time.localtime(time.time()))
    if not os.path.exists(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')
        #经过上述步骤，已经得到了HTML报告的名称
        filename=curpath+'/resultreport/'+now+'resultreport.html'
        #打开HTML文件，wb以写的方式
        with open(filename,'wb') as fp:
        #出html报告
        # 括号里的参数是HTML报告里面的参数
            runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况',verbosity=2)
            suite=createsuite()
            runner.run(suite)