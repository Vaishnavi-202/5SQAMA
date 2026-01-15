import os
import time
import datetime
import warnings

import pytest
import allure
from PIL import ImageGrab
from allure_commons.types import AttachmentType

from qama_regression_ascendion.config.logger import get_logger

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

# =================================================
# LOGGER
# =================================================
log = get_logger("pytest")


# =================================================
# WARNING HANDLING (CLEAN OUTPUT)
# =================================================
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="pywinauto")
warnings.filterwarnings("ignore", category=UserWarning, module="PIL")


# =================================================
# SESSION APP FIXTURE
# =================================================
'''@pytest.fixture(scope="session")
def app(request):
    log.info("Initializing HP Web Jetadmin session")
    
    # Unpack the app instance and the boolean flag
    # app_instance: the pywinauto Application object
    # was_already_open: True if we connected to an existing app, False if we started it
    app_instance, was_already_open = launch_and_prepare_wja()
    
    yield app_instance
    
    try:
        if was_already_open:
            log.info("App was already open before testing; skipping kill command to preserve state.")
        else:
            log.info("App was launched from EXE; performing teardown and killing process.")
            app_instance.kill()
    except Exception as e:
        log.warning(f"App close failed or was not necessary: {e}")'''

@pytest.fixture(scope="session")
def app(request):
    # If no test uses wja marker → do nothing
    if not any(item.get_closest_marker("wja") for item in request.session.items):
        yield None
        return

    # Import ONLY when needed
    from libs.app_package.wja_win_app import launch_and_prepare_wja

    app_instance, was_already_open = launch_and_prepare_wja()
    yield app_instance

    if not was_already_open:
        try:
            app_instance.kill()
        except Exception:
            pass

# =================================================
# TEST EXECUTION TIMER (START)
# =================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    item._start_time = time.time()
    yield


# =================================================
# TEST REPORT + SCREENSHOT ON FAILURE
# =================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        duration = time.time() - item._start_time

        # Attach execution time to Allure
        allure.attach(
            f"{duration:.2f} seconds",
            name="Test Duration",
            attachment_type=AttachmentType.TEXT
        )

        log.info(f"{item.nodeid} took {duration:.2f}s")

        # Screenshot on FAILURE (File + Allure)
        if rep.failed:
            try:
                os.makedirs("screenshots", exist_ok=True)
                ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

                img = ImageGrab.grab(all_screens=True)

                # Save locally
                img.save(f"screenshots/{item.name}_{ts}.png")

                # Attach to Allure
                allure.attach(
                    img.tobytes(),
                    name="Failure Screenshot",
                    attachment_type=AttachmentType.PNG
                )

                log.error(f"Screenshot captured for {item.name}")

            except Exception as e:
                log.error(f"Screenshot capture failed: {e}")


# =================================================
# TEST TEARDOWN (LOG ATTACHMENT + GAP)
# =================================================
@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
    # Attach execution log to Allure
    log_file = os.path.join("logs", "execution.log")
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
            allure.attach(
                f.read(),
                name="Execution Log",
                attachment_type=AttachmentType.TEXT
            )

    # EXACT 1-second gap between tests
    time.sleep(1)
