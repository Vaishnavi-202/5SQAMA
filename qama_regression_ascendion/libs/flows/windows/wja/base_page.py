from pywinauto.timings import wait_until_passes
from pywinauto.findwindows import ElementNotFoundError
from qama_regression_ascendion.config.logger import get_logger

log = get_logger(__name__)


class BasePage:
    _main_window = None

    def __init__(self, app):
        self.app = app
        if not BasePage._main_window:
            BasePage._main_window = self._resolve_main_window()
        self.main_window = BasePage._main_window

    def _resolve_main_window(self):
        log.info("Resolving HP Web Jetadmin main window")
        return wait_until_passes(
            timeout=40,
            retry_interval=1,
            func=lambda: self.app.window(title_re=".*HP Web Jetadmin.*"),
            exceptions=(ElementNotFoundError,)
        )

    def focus_window(self):
        self.main_window.set_focus()
