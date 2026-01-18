import unittest
from test._test_multiprocessing import install_tests_in_module_dict

install_tests_in_module_dict(globals(), 'spawn', only_type="threads")

# TODO: RUSTPYTHON
import os, sys
class WithThreadsTestPool(WithThreadsTestPool):
    @unittest.skip('TODO: RUSTPYTHON; flaky environment pollution when running rustpython -m test --fail-env-changed due to unknown reason')
    def test_terminate(self): super().test_terminate()
# END RUSTPYTHON;
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
