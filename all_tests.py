from test_case_test import TestCaseTest
from test_loader import TestLoader
from test_loader_test import TestLoaderTest
from test_runner import TestRunner
from test_suite import TestSuite
from test_suite_test import TestSuiteTest


loader = TestLoader()
test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_loader_suite = loader.make_suite(TestLoaderTest)

suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_loader_suite)

runner = TestRunner()
runner.run(suite)
