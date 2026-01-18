import unittest
from test._test_multiprocessing import install_tests_in_module_dict

install_tests_in_module_dict(globals(), 'fork', exclude_types=True)

# TODO: RUSTPYTHON
import sys
class TestManagerExceptions(TestManagerExceptions):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky')
    def test_queue_get(self): super().test_queue_get()

@unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky')
class TestInitializers(TestInitializers): pass

class TestStartMethod(TestStartMethod):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky')
    def test_nested_startmethod(self): super().test_nested_startmethod()

@unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky')
class TestSyncManagerTypes(TestSyncManagerTypes): pass

class MiscTestCase(MiscTestCase):
    @unittest.skipIf(sys.platform == 'linux', 'TODO: RUSTPYTHON; flaky')
    def test_forked_thread_not_started(self): super().test_forked_thread_not_started()
# END RUSTPYTHON;
# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
