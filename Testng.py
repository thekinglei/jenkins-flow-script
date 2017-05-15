#!/usr/local/bin/python
#coding:utf-8
# __author__ = 'Administrator'
import jenkins
import unittest
class TestJenkins(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_jenkins_compile(self):
        jenkins.jenkins_compile()

    def test_jenkins_package_store(self):
        jenkins.package_store()

    def test_jenkins_package_info(self):
        jenkins.package_info()

    def test_jenkins_deploy(self):
        jenkins.deploy()

    def test_jenkins_main(self):
        jenkins.sid_main()


