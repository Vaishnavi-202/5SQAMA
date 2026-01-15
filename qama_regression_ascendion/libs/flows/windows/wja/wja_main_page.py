from pywinauto.keyboard import send_keys
from libs.flows.windows.wja.base_page import BasePage
from qama_regression_ascendion.config.logger import get_logger
from libs.flows.windows.ui_wait import ui_step_wait

log = get_logger(__name__)


class WJAMainPage(BasePage):

    def is_launched(self):
        self.main_window.wait("visible", timeout=30)
        log.info("WJA main window is visible")
        return True

    def open_about(self):
        self.focus_window()
        send_keys("%H")
        ui_step_wait()
        send_keys("A")
        ui_step_wait()
        log.info("Opened About dialog")

    def close_about(self):
        send_keys("{ENTER}")
        ui_step_wait()
        log.info("Closed About dialog")

    def open_about_details_and_close(self):
        self.open_about()
        send_keys("{TAB}{ENTER}")
        ui_step_wait()
        send_keys("{ENTER}{TAB}{TAB}{ENTER}")
        ui_step_wait()
        log.info("Opened About details and closed")
