import unittest
from test._test_multiprocessing import install_tests_in_module_dict

install_tests_in_module_dict(globals(), 'spawn', only_type="processes")

# TODO: RUSTPYTHON
import os, sys
class WithProcessesTestCondition(WithProcessesTestCondition):
    @unittest.skipIf(sys.platform == 'darwin', 'TODO: RUSTPYTHON; flaky timeout')
    def test_notify(self): super().test_notify()

class WithProcessesTestLock(WithProcessesTestLock):
    @unittest.skipIf(
        sys.platform in ('darwin', 'linux') and 'RUSTPYTHON_SKIP_ENV_POLLUTERS' in os.environ,
        'TODO: RUSTPYTHON; environment pollution when running rustpython -m test --fail-env-changed due to unknown reason'
    )
    def test_repr_lock(self): super().test_repr_lock()
    @unittest.skipIf(
        sys.platform == 'linux',
        'TODO: RUSTPYTHON; flaky BrokenPipeError, flaky ConnectionRefusedError, flaky ConnectionResetError, flaky EOFError'
    )
    def test_repr_rlock(self): super().test_repr_rlock()

class WithProcessesTestPool(WithProcessesTestPool):
    @unittest.skipIf(
        sys.platform in ('darwin', 'linux') and 'RUSTPYTHON_SKIP_ENV_POLLUTERS' in os.environ,
        'TODO: RUSTPYTHON; environment pollution when running rustpython -m test --fail-env-changed due to unknown reason'
    )
    def test_async_timeout(self): super().test_async_timeout()
    @unittest.skipIf(
        sys.platform in ('darwin', 'linux') and 'RUSTPYTHON_SKIP_ENV_POLLUTERS' in os.environ,
        'TODO: RUSTPYTHON; environment pollution when running rustpython -m test --fail-env-changed due to unknown reason'
    )
    def test_terminate(self): super().test_terminate()
    @unittest.skipIf(
        sys.platform in ('darwin', 'linux') and 'RUSTPYTHON_SKIP_ENV_POLLUTERS' in os.environ,
        'TODO: RUSTPYTHON; environment pollution when running rustpython -m test --fail-env-changed due to unknown reason'
    )
    def test_traceback(self): super().test_traceback()
# END RUSTPYTHON;
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
