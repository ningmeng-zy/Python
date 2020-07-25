import unittest,csv
import os,sys
import time
import test1
import test2

#手工添加案例到套件
def createsuite():
    suite = unittest.TestSuite()
    suite.addTest(test1.Baidu1("test_baidusearch"))
    suite.addTest(test1.Baidu1("test_hao"))
    suite.addTest(test2.Baidu2("test_baidusearch"))
    return suite

if __name__=="__main__":
    suite = createsuite()
    ret = unittest.TextTestRunner(verbosity=2)
    ret.run(suite)