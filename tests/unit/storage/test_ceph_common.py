import os

from hotsos.core.config import HotSOSConfig

from .. import utils


CEPH_MON_DATA_ROOT = os.path.join(utils.TESTS_DIR,
                                  'fake_data_root/storage/ceph-mon')


class CephCommonTestsBase(utils.BaseTestCase):

    def setUp(self):
        super().setUp()
        HotSOSConfig.data_root = CEPH_MON_DATA_ROOT
        HotSOSConfig.plugin_name = 'storage'


@utils.load_templated_tests('scenarios/storage/ceph/common')
class TestCephCommonScenarios(CephCommonTestsBase):
    """
    Scenario tests can be written using YAML templates that are auto-loaded
    into this test runner. This is the recommended way to write tests for
    scenarios. It is however still possible to write the tests in Python if
    required. See defs/tests/README.md for more info.
    """
