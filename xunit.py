class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1


TestCaseTest("testRunning").run()
