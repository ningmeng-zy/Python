import unittest,csv
import os,sys
import time


def createsuite():
    discover=unittest.defaultTestLoader.discover('E:/Pythoncode',pattern='test*.py',top_level_dir=None)
    print (discover)
    return discover
if __name__=="__main__":
    suite=createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)