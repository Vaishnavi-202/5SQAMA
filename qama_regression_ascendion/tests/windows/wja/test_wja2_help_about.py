from libs.flows.windows.wja.wja_main_page import WJAMainPage

def test_help_about_flow(app):
    main = WJAMainPage(app)

    main.open_about()
    main.close_about()


def test_help_about_details_flow(app):
    main = WJAMainPage(app)

    main.open_about_details_and_close()
