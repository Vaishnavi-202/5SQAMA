from libs.flows.windows.wja.group_management_page import NavigationPage


def test_create_and_delete_group(app):
    nav = NavigationPage(app)

    nav.open_overview_and_groups()
    nav.click_create_group()
    nav.create_group("WJA")
    nav.select_group("WJA")
    nav.delete_group()
