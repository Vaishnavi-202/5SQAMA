import allure
from libs.flows.windows.wja.base_page import BasePage
from libs.flows.windows.ui_wait import ui_step_wait
from qama_regression_ascendion.config.logger import get_logger

log = get_logger(__name__)


class MainPage(BasePage):

    _tree = None
    _items = {}
    _current = None

    def __init__(self, app):
        super().__init__(app)

        if not MainPage._tree:
            overview = self.main_window.child_window(
                title="Overview",
                control_type="TreeItem"
            )
            overview.wait("exists", timeout=15)
            MainPage._tree = overview.parent()

            MainPage._items = {
                "Overview": r"\Overview",
                "Groups": r"\Groups",
                "Discovery": r"\Discovery",
                "Configuration": r"\Configuration",
            }

    def _select(self, name):
        with allure.step(f"Navigate to {name}"):
            if MainPage._current == name:
                log.info(f"Skipping reload: {name}")
                return

            log.info(f"Navigating to {name}")
            MainPage._tree.get_item(MainPage._items[name]).select()
            MainPage._current = name
            ui_step_wait()

    def click_overview(self):
        self._select("Overview")

    def click_groups(self):
        self._select("Groups")

    def click_discovery(self):
        self._select("Discovery")

    def click_configuration(self):
        self._select("Configuration")
