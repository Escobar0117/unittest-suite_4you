import os
import pytest
from datetime import datetime
from pathlib import Path

SCREENSHOTS_DIR = Path("screenshots")

def _ensure_screenshot_dir() -> None:
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


def _build_screenshot_name(test_name: str, status: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_test_name = "".join(c if c.isalnum() or c in ("_", "-") else "_" for c in test_name)
    return SCREENSHOTS_DIR / f"{safe_test_name}_{status}_{timestamp}.png"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    #Sricript de pytest, sirve para:
    #1.tomar screenshot cuando la prueba PASA o FALLA
    #2.imprimir mensaje de resultado en consola
    
    outcome = yield
    rep = outcome.get_result()

    # Solo evaluar el resultado final del test
    if rep.when != "call":
        return

    page = item.funcargs.get("page", None)
    _ensure_screenshot_dir()

    if rep.passed:
        print(f"\n✅ PRUEBA EXITOSA: {item.name}")

        if page:
            screenshot_path = _build_screenshot_name(item.name, "PASS")
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"📸 Screenshot PASS guardado en: {screenshot_path}")

    elif rep.failed:
        print(f"\n❌ PRUEBA FALLIDA: {item.name}")

        if page:
            screenshot_path = _build_screenshot_name(item.name, "FAIL")
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"📸 Screenshot FAIL guardado en: {screenshot_path}")