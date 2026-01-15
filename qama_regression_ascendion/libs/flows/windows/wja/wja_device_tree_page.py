import allure
from libs.flows.windows.wja.base_page import BasePage
from libs.flows.windows.ui_wait import ui_step_wait
from qama_regression_ascendion.config.logger import get_logger

log = get_logger(__name__)

TREE_PATHS = {
    "all": r"\All Devices",
    "error": r"\Error Devices",
    "warning": r"\Warning Devices",
    "new": r"\New (Last Discovery)",
    "ungrouped": r"\Ungrouped Devices",
}


class WJADeviceTreePage(BasePage):

    _tree = None
    _items = {}

    def __init__(self, app):
        super().__init__(app)

        if not WJADeviceTreePage._tree:
            log.info("Resolving TreeView once")
            overview = self.main_window.child_window(
                title="Overview",
                control_type="TreeItem"
            )
            overview.wait("exists", timeout=15)
            WJADeviceTreePage._tree = overview.parent()

    def _select(self, key):
        with allure.step(f"Select device tree item: {key}"):
            if key not in self._items:
                log.info(f"Caching tree item: {TREE_PATHS[key]}")
                self._items[key] = self._tree.get_item(TREE_PATHS[key])

            log.info(f"Selecting tree item: {key}")
            self._items[key].select()
            ui_step_wait()

    # 🔹 KEEP OLD METHODS (tests rely on these)
    def click_all_devices(self): 
        self._select("all")

    def click_error_devices(self): 
        self._select("error")

    def click_warning_devices(self): 
        self._select("warning")

    def click_new_devices(self): 
        self._select("new")

    def click_ungrouped_devices(self): 
        self._select("ungrouped")
