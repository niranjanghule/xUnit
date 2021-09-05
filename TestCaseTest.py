from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert test.wasRun

    def testSetup(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetup)


TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()
