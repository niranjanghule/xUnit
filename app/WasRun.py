from app.TestCase import TestCase
from app.TestResult import TestResult

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def setUp(self):
        self.wasRun = None
        self.wasSetup =1
        self.log = "setUp "

    def testBrokenMethod(self):
        raise Exception

    def testBrokenSetup(self):
        raise Exception

    def tearDown(self):
        self.log = self.log + "tearDown "
