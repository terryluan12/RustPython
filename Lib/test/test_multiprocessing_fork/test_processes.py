import unittest
from test._test_multiprocessing import install_tests_in_module_dict

install_tests_in_module_dict(globals(), 'fork', only_type="processes")

# TODO: RUSTPYTHON
import os, sys
class WithProcessesTestCondition(WithProcessesTestCondition):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky timeout')
    def test_notify_all(self): super().test_notify_all()

class WithProcessesTestLock(WithProcessesTestLock):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky BrokenPipeError, flaky ConnectionRefusedError, flaky ConnectionResetError, flaky EOFError')
    def test_repr_lock(self): super().test_repr_lock()

class WithProcessesTestManagerRestart(WithProcessesTestManagerRestart):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky BrokenPipeError, flaky ConnectionRefusedError, flaky ConnectionResetError, flaky EOFError')
    def test_rapid_restart(self): super().test_rapid_restart()

class WithProcessesTestProcess(WithProcessesTestProcess):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky timeout')
    def test_args_argument(self): super().test_args_argument()
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky timeout')
    def test_process(self): super().test_process()

class WithProcessesTestPool(WithProcessesTestPool):
    @unittest.skipIf(
        sys.platform == 'linux' and 'RUSTPYTHON_SKIP_ENV_POLLUTERS' in os.environ,
        'TODO: RUSTPYTHON; environment pollution when running rustpython -m test --fail-env-changed due to unknown reason'
    )
    def test_async_timeout(self): super().test_async_timeout()
    @unittest.skipIf(
        sys.platform == 'linux' and 'RUSTPYTHON_SKIP_ENV_POLLUTERS' in os.environ,
        'TODO: RUSTPYTHON; environment pollution when running rustpython -m test --fail-env-changed due to unknown reason'
    )
    def test_terminate(self): super().test_terminate()
    @unittest.skipIf(
        sys.platform == 'linux' and 'RUSTPYTHON_SKIP_ENV_POLLUTERS' in os.environ,
        'TODO: RUSTPYTHON; environment pollution when running rustpython -m test --fail-env-changed due to unknown reason'
    )
    def test_traceback(self): super().test_traceback()

class WithProcessesTestPoolWorkerLifetime(WithProcessesTestPoolWorkerLifetime):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky timeout')
    def test_pool_worker_lifetime(self): super().test_pool_worker_lifetime()
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky timeout')
    def test_pool_worker_lifetime_early_close(self): super().test_pool_worker_lifetime_early_close()

class WithProcessesTestQueue(WithProcessesTestQueue):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky timeout')
    def test_fork(self): super().test_fork()
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky timeout')
    def test_get(self): super().test_get()

class WithProcessesTestSharedMemory(WithProcessesTestSharedMemory):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky BrokenPipeError, flaky ConnectionRefusedError, flaky ConnectionResetError, flaky EOFError')
    def test_shared_memory_SharedMemoryManager_basics(self): super().test_shared_memory_SharedMemoryManager_basics()
# END RUSTPYTHON;
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
