from libs.flows.windows.wja.base_page import BasePage
from libs.flows.windows.ui_wait import ui_step_wait
from qama_regression_ascendion.config.logger import get_logger

log = get_logger(__name__)


class NavigationPage(BasePage):

    def open_overview_and_groups(self):
        self.main_window.child_window(
            title="Overview", control_type="TreeItem"
        ).select()
        ui_step_wait()

        self.main_window.child_window(
            title="Groups", control_type="TreeItem"
        ).select()
        ui_step_wait()

    def click_create_group(self):
        self.main_window.child_window(
            auto_id="button_create",
            control_type="Button"
        ).click()
        ui_step_wait()

    def create_group(self, group_name):
        dlg = self.app.window(title_re="Create Group.*")
        dlg.wait("exists", timeout=5)

        dlg.child_window(
            auto_id="textBox_newGroupName",
            control_type="Edit"
        ).set_edit_text(group_name)

        dlg.child_window(auto_id="btnNext").click()
        ui_step_wait()
        dlg.child_window(auto_id="btnNext").click()
        ui_step_wait()
        dlg.child_window(auto_id="btnDone").click()
        ui_step_wait()

    # 🔹 RESTORED (tests require this)
    def select_group(self, group_name):
        self.main_window.child_window(
            title=group_name,
            control_type="TreeItem"
        ).select()
        ui_step_wait()

    def delete_group(self):
        self.main_window.child_window(
            auto_id="button_delete",
            control_type="Button"
        ).click()
        ui_step_wait()

        dlg = self.app.window(title_re="Delete Group.*")
        dlg.wait("exists", timeout=5)
        dlg.child_window(auto_id="btnNext").click()
        ui_step_wait()
        dlg.child_window(auto_id="btnDone").click()
        ui_step_wait()
