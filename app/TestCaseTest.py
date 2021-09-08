from app.TestCase import TestCase
from WasRun import WasRun
from app.TestResult import TestResult


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)

    def testResult(self):
        self.test = WasRun("testMethod")
        result = self.test.run()
        assert("1 run, 0 failed" == result.summary())
        assert("1 run, 1 failed" != result.summary())

    def testFailedResult(self):
        self.test = WasRun("testMethod")
        result = self.test.run()
        assert("2 run, 2 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed", result.summary


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
#TestCaseTest("testFailedResult").run()

