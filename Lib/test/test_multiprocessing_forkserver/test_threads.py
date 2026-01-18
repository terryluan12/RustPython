import unittest
from test._test_multiprocessing import install_tests_in_module_dict

install_tests_in_module_dict(globals(), 'forkserver', only_type="threads")

# TODO: RUSTPYTHON
import os
class WithThreadsTestPool(WithThreadsTestPool):
    @unittest.skipIf(
        'RUSTPYTHON_SKIP_ENV_POLLUTERS' in os.environ,
        'TODO: RUSTPYTHON; environment pollution when running rustpython -m test --fail-env-changed due to unknown reason'
    )
    def test_terminate(self): super().test_terminate()
# END RUSTPYTHON;
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
