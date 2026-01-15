import pywinauto
from pywinauto import Desktop

def check_wja_visibility():
    target_title = "HP Web Jetadmin - localhost"
    print(f"--- Debugging Connection to: {target_title} ---")
    
    # 1. Check with UIA Backend
    print("\n[Step 1] Checking 'uia' backend...")
    try:
        app_uia = pywinauto.Application(backend="uia").connect(title_re=".*HP Web Jetadmin.*", timeout=2)
        print("SUCCESS: Found window using 'uia' backend!")
        app_uia.window(title_re=".*HP Web Jetadmin.*").set_focus()
    except Exception as e:
        print(f"FAILED: 'uia' could not find the window. Error: {e}")

    # 2. Check with Win32 Backend (Legacy)
    print("\n[Step 2] Checking 'win32' backend...")
    try:
        app_win32 = pywinauto.Application(backend="win32").connect(title_re=".*HP Web Jetadmin.*", timeout=2)
        print("SUCCESS: Found window using 'win32' backend!")
        app_win32.window(title_re=".*HP Web Jetadmin.*").set_focus()
    except Exception as e:
        print(f"FAILED: 'win32' could not find the window. Error: {e}")

    # 3. List ALL open window titles
    print("\n[Step 3] Listing all visible window titles on your system:")
    print("-" * 50)
    windows = Desktop(backend="uia").windows()
    found_any = False
    for win in windows:
        title = win.window_text()
        if title:
            print(f"Visible Title: {title}")
            if "Jetadmin" in title or "HP" in title:
                print(f"  >>> POTENTIAL MATCH FOUND: '{title}'")
                found_any = True
    print("-" * 50)

    if not found_any:
        print("\nRESULT: No window containing 'HP' or 'Jetadmin' was detected.")
        print("SUGGESTION: Ensure you are running this script as ADMINISTRATOR.")

if __name__ == "__main__":
    check_wja_visibility()