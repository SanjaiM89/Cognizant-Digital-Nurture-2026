"""
24. In a comment block at the top of setup_test.py, describe the three main Selenium components: WebDriver, what it is and how it communicates with the browser, Selenium Grid, what problem it solves, parallel execution on multiple machines/browsers, and Selenium IDE, what it is used for, record and playback, code generation.
"""

"""
SELENIUM COMPONENTS OVERVIEW

1. WebDriver:
   WebDriver is a library/API that allows a test script to control a real browser
   by sending it commands, such as opening a page, clicking an element, or typing
   text. It communicates with the browser through a browser-specific driver, such
   as chromedriver for Chrome or geckodriver for Firefox, which acts as a bridge
   between the test script and the browser. This communication follows the W3C
   WebDriver protocol, a standardized set of HTTP-based commands, so there is no
   separate intermediary server required. The script talks to the driver, and the
   driver talks directly to the browser.

2. Selenium Grid:
   Selenium Grid solves the problem of running tests one at a time on a single
   machine and browser, which becomes very slow as the number of test cases and
   supported browsers grows. Grid allows tests to be distributed and run in
   parallel across multiple machines and multiple browser and OS combinations at
   the same time, for example running the Course Management login tests on
   Chrome, Firefox, and Edge simultaneously across different nodes, drastically
   reducing total execution time for large test suites.

3. Selenium IDE:
   Selenium IDE is a browser extension used mainly for quickly recording user
   actions, such as clicks, typing, and navigation, and playing them back as an
   automated test without writing any code manually. It is commonly used for
   rapid prototyping of test cases or by non-technical users, and it can also
   export or generate code in languages such as Python or Java from the recorded
   steps, which can then be used as a starting point in a full automation
   framework.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Implicit wait applies globally to EVERY element lookup for the entire
# driver session, not just the ones that actually need it. This means:
# 1. Fast lookups still carry the same wait ceiling in the background,
#    which can silently slow down the whole test suite as it scales.
# 2. It can't wait for a SPECIFIC condition (e.g. "element is clickable"
#    or "text has loaded") — it only checks if the element exists in the
#    DOM, so a test can still fail even after the wait if the element is
#    present but not yet interactable.
# 3. Mixing implicit and explicit waits in the same test can cause
#    unpredictable, inconsistent wait times, since the two mechanisms
#    don't coordinate with each other.
driver.implicitly_wait(10)
driver.get("https://www.lambdatest.com/selenium-playground/")

print(driver.title)
driver.quit()
