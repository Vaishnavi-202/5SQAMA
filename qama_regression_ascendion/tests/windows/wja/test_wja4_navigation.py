from libs.flows.windows.wja.wja_navigation_page import MainPage

def test_quick_device_discovery(app):
    main_page = MainPage(app)

    main_page.click_overview()
    main_page.click_groups()
    main_page.click_discovery()
    main_page.click_configuration()
