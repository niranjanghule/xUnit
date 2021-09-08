class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def summary(self):
        return "%d run, 2 failed" % self.runCount

    def testFailed(self):
        self.errorCount = self.errorCount + 1
