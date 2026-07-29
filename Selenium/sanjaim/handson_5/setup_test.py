
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
assert "simple-form-demo" in driver.current_url
print("True")
print(driver.title)

using_id = driver.find_element(By.ID, "user-message")
print("Found using ID", using_id)

using_name = driver.find_element(By.NAME, "message")
print("Found using name", using_name)

using_class_name = driver.find_element(By.CLASS_NAME, "rounded")
print("Found using class name", using_class_name)

using_tag_name = driver.find_element(By.TAG_NAME, "input")
print("Found using tag name", using_tag_name)

using_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input")
print("Found using xpath", using_xpath)

using_xpath_relative = driver.find_element(By.XPATH, "//input[@id='user-message']")
print("Found using relative xpath", using_xpath_relative)


element1_by_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
print("CSS by ID: ",element1_by_id)

element2_attribute = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)
print("CSS by Attribute: ",element2_attribute)

element3_parent_child = driver.find_element(
    By.CSS_SELECTOR,
    "div > input"
)
print("CSS Parent-Child",element3_parent_child)

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
label = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)
print("First Label:", label.text)
labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)
print("\nAll Option Labels:")
for l in labels:
    print(l.text)

"""
Locator Preference Ranking (Most Preferred → Least Preferred)

1. By.ID
   - Usually unique.
   - Fast.
   - Easy to read.
   - Least likely to break.

2. By.NAME
   - Often unique.
   - Easy to understand.
   - Stable if developers keep the name.

3. By.CSS_SELECTOR
   - Very flexible.
   - Shorter than XPath.
   - Can locate elements using id, class, attributes, etc.

4. By.XPATH
   - Extremely powerful.
   - Can locate almost any element.
   - Relative XPath is preferred over absolute XPath.

5. By.CLASS_NAME
   - Good only if the class is unique.
   - Many elements often share the same class.

6. By.TAG_NAME
   - Least preferred.
   - Usually matches many elements.
   - Not unique, so rarely suitable by itself.
"""


driver.get("https://www.testmuai.com/selenium-playground/bootstrap-alert-messages-demo/")
driver.find_element(By.XPATH,"//button[text()='Normal Success Message']").click()

success = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[contains(.,'Normal Success Message')]"))
)

print("Success Message Shown: ",success.text)
assert("Normal Success Message" in success.text)
print("Test Case Passes on Successfully Message")

driver.get("https://www.testmuai.com/selenium-playground/bootstrap-alert-messages-demo/")
start_sleep = time.time()

driver.find_element(By.XPATH, "//button[text()='Normal Success Message']").click()
time.sleep(3)
msg_sleep = driver.find_element(By.XPATH, "//div[contains(.,'Normal success message')]")
print("Sleep version text:", msg_sleep.text)

end_sleep = time.time()
print(f"time.sleep version took: {end_sleep - start_sleep:.2f} seconds")

driver.get("https://www.testmuai.com/selenium-playground/bootstrap-alert-messages-demo/")
start_wait = time.time()

driver.find_element(By.XPATH, "//button[text()='Normal Success Message']").click()
msg_wait = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(.,'Normal success message')]"))
)
print("Explicit wait version text:", msg_wait.text)

end_wait = time.time()
print(f"Explicit wait version took: {end_wait - start_wait:.2f} seconds")

"""
Comment:
- time.sleep(3) ALWAYS waits the full 3 seconds, even if the element
  appeared in 200ms. This wastes time on fast machines/networks.
- On slow machines or slow-loading pages, 3 seconds might not be enough,
  causing a NoSuchElementException even though the element would have
  appeared if we'd waited a bit longer. sleep() doesn't adapt.
- WebDriverWait polls repeatedly (every ~0.5s by default) and returns
  AS SOON AS the condition is met, so it's faster when the app is fast,
  and it's more reliable when the app is slow (waits up to the full
  timeout instead of failing early).
"""

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Normal Success Message']"))
)
button.click()

"""
Comment:
- visibility_of_element_located: only checks that the element exists in
  the DOM AND has a size greater than 0 (i.e., it's visible on screen).
  It does NOT check whether the element can actually be interacted with.
  An element can be visible but still disabled, or visible but covered
  by another element (e.g. a loading spinner or modal overlay) sitting
  on top of it.

- element_to_be_clickable: checks visibility() is true, AND that the
  element is enabled, AND that it isn't obscured by another element
  intercepting the click. This is why it's the safer choice right
  before calling .click() — it prevents ElementClickInterceptedException
  and "element not interactable" errors that can happen even when
  visibility_of_element_located already passed.
"""

driver.get("https://www.testmuai.com/selenium-playground/table-search-filter-demo/")
search_box = driver.find_element(By.ID, "task-table-filter")
search_box.send_keys("Ricky")

fluent_wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException],
)

row = fluent_wait.until(
    lambda d: d.find_element(
        By.XPATH, "//table[@id='task-table']//td[contains(text(),'Ricky')]/.."
    )
)

print("Row found:", row.text)
assert "Ricky" in row.text
print("Test Case Passed: Ricky row located via FluentWait")

"""
Comment:
- This is Selenium Python's equivalent of Java's FluentWait.
- poll_frequency=0.5 means Selenium checks the condition every 0.5 seconds
  instead of the default polling interval.
- ignored_exceptions=[NoSuchElementException] means that if the row
  doesn't exist YET (common with dynamically-loaded/AJAX content),
  the wait won't crash immediately — it just retries until either the
  row appears or the 10-second timeout is reached, at which point it
  raises TimeoutException.
- This is more resilient than a single find_element() call for content
  that loads asynchronously after page load.
"""


driver.quit()