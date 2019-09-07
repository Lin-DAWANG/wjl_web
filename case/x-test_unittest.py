# coding = utf-8
from selenium import webdriver
import time
import unittest

class FirstTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("前置操作，只执行一次")
    @classmethod
    def tearDownClass(cls):
        print("后置操作，只执行一次")

    # def setUp(self):
    #     print("前置操作,所有用例都要执行") # 每个用例执行之前执行
    #
    # def tearDown(self):
    #     print("后置操作，所有用例都要执行") # 每个用例执行之后调用

    def test_1(self):
        print("-------1-------")
        # self.assertEqual((1 + 2), 3)
        a = 1 + 2
        b = 3
        self.assertEqual(a, b)

    def test_2(self):
        print("-------2-------")
        self.assertEqual((0 * 2), 0)
        self.assertEqual((5 * 2), 10)

    def test_3(self):#截图
         print("-------3-------")
         a = "admin"
         b = "12345"
         self.assertTrue(a != b)
         self.assertIn(a, b)
    def test_4(self):
         print("-------4-------")
         a = "admin"
         b = "admin1"
         self.assertIn(a, b)




