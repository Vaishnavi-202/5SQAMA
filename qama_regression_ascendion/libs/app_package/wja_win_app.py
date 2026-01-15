from pywinauto import Application, Desktop
from pywinauto.keyboard import send_keys
import time

WJA_EXE_PATH = r"C:\Program Files\HP Inc\Web Jetadmin 10\bin\LaunchWJA.exe"
WJA_TITLE = "HP Web Jetadmin - localhost"

def launch_and_prepare_wja():
    app = Application(backend="uia")

    try:
        main_win = Desktop(backend="uia").window(
            title_re=f".*{WJA_TITLE}.*",
            control_type="Window",
            visible_only=True
        )

        main_win.wait("exists visible", timeout=90)
        app.connect(handle=main_win.handle)
        main_win.set_focus()

        print("Connected to existing instance. It will NOT be killed after tests.")
        return app, True

    except Exception:
        print("No instance found. Launching fresh...")

    app.start(WJA_EXE_PATH)
    desktop = Desktop(backend="uia")

    # --- Handle In-Secure Connection ---
    for _ in range(30):
        dlg = desktop.window(title_re=".*In-Secure Connection.*")
        if dlg.exists():
            dlg.set_focus()
            time.sleep(1)
            send_keys("{ENTER}")
            break
        time.sleep(1)

    # --- Handle Run Discovery ---
    for _ in range(40):
        dlg = desktop.window(title_re=".*Run Discovery.*")
        if dlg.exists():
            dlg.set_focus()
            time.sleep(1)
            send_keys("{ENTER}")
            break
        time.sleep(1)

    # --- Final attach ---
    main_win = Desktop(backend="uia").window(
        title_re=f".*{WJA_TITLE}.*",
        control_type="Window",
        visible_only=True
    )

    main_win.wait("exists visible", timeout=120)
    time.sleep(3)
    main_win.set_focus()

    app.connect(handle=main_win.handle)
    print("Launched from path. It WILL be killed after tests.")
    return app, False
