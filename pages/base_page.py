class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url=None):
        target = url or getattr(self, 'url', None)
        if target:
            self.page.goto(target)
            self.page.wait_for_load_state("networkidle")

    def wait_for_element(self, selector, timeout=10000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def click(self, selector):
        self.page.locator(selector).first.click()

    def fill(self, selector, value):
        self.page.locator(selector).first.fill(value)

    def get_text(self, selector):
        return self.page.locator(selector).first.inner_text()

    def is_visible(self, selector):
        try:
            return self.page.locator(selector).first.is_visible()
        except Exception:
            return False

    def is_element_present(self, selector):
        return self.page.locator(selector).count() > 0

    def get_current_url(self):
        return self.page.url

    def take_screenshot(self, path="screenshot.png"):
        self.page.screenshot(path=path)
