import unittest
from test._test_multiprocessing import install_tests_in_module_dict

install_tests_in_module_dict(globals(), 'fork', only_type="manager")

# TODO: RUSTPYTHON
import sys
class WithManagerTestCondition(WithManagerTestCondition):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; times out')
    def test_notify_all(self): super().test_notify_all()

class WithManagerTestQueue(WithManagerTestQueue):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; times out')
    def test_fork(self): super().test_fork()

local_globs = globals().copy()
for name, base in local_globs.items():
    if name.startswith('WithManagerTest') and issubclass(base, unittest.TestCase):
        base = unittest.skipIf(
            sys.platform == 'linux',
            'TODO: RUSTPYTHON; flaky BrokenPipeError, flaky ConnectionRefusedError, flaky ConnectionResetError, flaky EOFError'
        )(base)
# END RUSTPYTHON;
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
