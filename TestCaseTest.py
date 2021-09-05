from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetup(self):
        self.test.run()
        assert self.test.wasSetup


TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()
