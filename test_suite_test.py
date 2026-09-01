from test_case import TestCase
from test_case_test import TestCaseTest, TestStub
from test_result import TestResult
from test_suite import TestSuite


class TestSuiteTest(TestCase):

    def test_suite_size(self):
        suite = TestSuite()

        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))

        assert len(suite.tests) == 3

    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))

        suite.run(result)

        assert result.summary() == '1 run, 0 failed, 0 error'

    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))

        suite.run(result)

        assert result.summary() == '3 run, 1 failed, 1 error'


if __name__ == '__main__':
    result = TestResult()
    suite = TestSuite()

    test_case_test_names = [
        'test_result_success_run',
        'test_result_failure_run',
        'test_result_error_run',
        'test_result_multiple_run',
        'test_was_set_up',
        'test_was_run',
        'test_was_tear_down',
        'test_template_method',
    ]

    for test_name in test_case_test_names:
        suite.add_test(TestCaseTest(test_name))

    test_suite_test_names = [
        'test_suite_size',
        'test_suite_success_run',
        'test_suite_multiple_run',
    ]

    for test_name in test_suite_test_names:
        suite.add_test(TestSuiteTest(test_name))

    suite.run(result)
    print(result.summary())
