class TestCase:

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self):
        test_method = getattr(self, self.test_method_name)
        test_method()
        self.set_up()
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass
