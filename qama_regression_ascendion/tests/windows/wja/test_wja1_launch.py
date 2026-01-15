from libs.flows.windows.wja.wja_main_page import WJAMainPage
import pytest

pytestmark = pytest.mark.wja

def test_wja_launch(app):
    main = WJAMainPage(app)
    assert main.is_launched(), "WJA did not launch"
