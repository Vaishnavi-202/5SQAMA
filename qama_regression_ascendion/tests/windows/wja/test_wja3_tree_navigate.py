import pytest
from libs.flows.windows.wja.wja_device_tree_page import WJADeviceTreePage
import pytest

pytestmark = pytest.mark.wja

# @pytest.mark.desktop
def test_device_navigation_tree_items(app):
    device_tree = WJADeviceTreePage(app)

    device_tree.click_all_devices()
    device_tree.click_error_devices()
    device_tree.click_warning_devices()
    device_tree.click_new_devices()
    device_tree.click_ungrouped_devices()
