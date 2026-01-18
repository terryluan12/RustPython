import unittest
from test._test_multiprocessing import install_tests_in_module_dict

install_tests_in_module_dict(globals(), 'fork', only_type="threads")

# TODO: RUSTPYTHON
import os, sys
class WithThreadsTestPool(WithThreadsTestPool):
    @unittest.skip('TODO: RUSTPYTHON; flaky environment pollution when running rustpython -m test --fail-env-changed due to unknown reason')
    def test_terminate(self): super().test_terminate()

class WithThreadsTestManagerRestart(WithThreadsTestManagerRestart):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky flaky BrokenPipeError, flaky ConnectionRefusedError, flaky ConnectionResetError, flaky EOFError')
    def test_rapid_restart(self): super().test_rapid_restart()
# END RUSTPYTHON;
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
