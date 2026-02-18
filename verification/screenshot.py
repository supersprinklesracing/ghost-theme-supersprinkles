from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 800})

    # Path to the preview file
    cwd = os.getcwd()
    file_path = f"file://{cwd}/preview.html"
    print(f"Navigating to: {file_path}")

    page.goto(file_path)

    # Wait for images and fonts
    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except:
        print("Timeout waiting for network idle, proceeding anyway.")

    # Take screenshot
    screenshot_path = "verification/vibrant_preview.png"
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot saved to {screenshot_path}")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
