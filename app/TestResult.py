class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def summary(self):
        print("%d run, %d failed" % (self.runCount, self.errorCount))
        return "%d run, %d failed" % (self.runCount, self.errorCount)

    def testFailed(self):
        self.errorCount = self.errorCount + 1
