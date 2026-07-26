# Task 1: Automation Decision and Test Case Selection — Course Management API

## 17. List and explain 5 criteria for deciding whether a test case should be automated. Apply each criterion to this scenario: "Test that the POST /api/courses/ endpoint returns 201 with the correct course data when valid input is provided."

1. **Repetition, how often the test will run:**
   This test case will be executed every time new code is pushed for regression purposes, potentially dozens of times a week.
   *Applied:* Since it runs repeatedly across builds, it's a strong automation candidate rather than a one-time manual check.

2. **Stability of the feature or requirement:**
   A test should only be automated if the feature it tests isn't expected to change frequently, since unstable features cause constant script rework.
   *Applied:* The core "create a course" behavior and its 201 response contract are stable, well-defined requirements, so automation investment won't be wasted on rework.

3. **Complexity of verification, does it need human judgment:**
   Automation works best for objective, exact checks such as status codes and field values, not subjective checks like visual design or "does this look right?"
   *Applied:* Checking that the response is exactly 201 with specific course fields such as course_id, course_name, and course_code is a precise, objective assertion, ideal for a script and not a human eyeballing it.

4. **Time and effort savings over multiple executions, ROI:**
   If the manual effort to run the test repeatedly outweighs the one-time cost of automating it, automation is worthwhile.
   *Applied:* Manually sending this POST request and checking the response every time code changes is repetitive and time-consuming across dozens of runs, so automation pays off quickly, as shown in Question 19.

5. **Criticality and risk of the feature:**
   High-risk, core business functionality that would badly impact users if broken deserves priority automation coverage, to catch regressions immediately.
   *Applied:* Course creation is a core function of the Course Management API. A regression here, such as silently returning 200 instead of 201 or missing fields, would be a critical or high-severity defect, so it deserves reliable automated coverage.

---

## 18. From the following list of test cases for the Course Management API, mark each as "Automate" or "Manual" and justify your decision: a Regression test for all CRUD endpoints after every code change. b Exploratory testing of a new search feature. c Performance test: 100 concurrent users calling GET /api/courses/. d UI test for the login form. e Verify the API documentation Swagger is accurate. f Smoke test: verify the API is reachable after deployment.

|   | Test Case | Decision | Justification |
|---|---|---|---|
| 1 | Regression test for all CRUD endpoints after every code change | **Automate** | Runs repeatedly on every change, checks are objective status codes and data correctness, and the endpoints are stable, giving high ROI and high value for repeated, frequent execution |
| 2 | Exploratory testing of a new search feature | **Manual** | Exploratory testing relies on human intuition, creativity, and judgment to discover unexpected issues in a new, not-yet-stable feature. This can't be scripted in advance since there's no fixed expected path |
| 3 | Performance test: 100 concurrent users calling GET /api/courses/ | **Automate** | Simulating 100 concurrent users is impossible to do manually. This requires load-testing tools such as JMeter or Locust to generate and measure concurrent traffic accurately |
| 4 | UI test for the login form | **Automate** | The login form is a stable, repetitive, objective check, correct credentials leading to success and wrong credentials leading to an error, making it a good Selenium candidate for frequent regression runs |
| 5 | Verify the API documentation Swagger is accurate | **Manual** | Judging whether documentation descriptions are accurate, clear, and match intent requires human reading and judgment, not something a script can objectively assert |
| 6 | Smoke test: verify the API is reachable after deployment | **Automate** | Simple, objective, and run after every single deployment, making it ideal for a fast, automated health-check script that gives immediate deployment feedback |

---

## 19. Define the term "test automation ROI". Given that automating one regression test takes 4 hours and running it manually takes 30 minutes, calculate how many runs are needed before the automation pays for itself. Account for a 20% maintenance overhead per run after the 10th run.

Test automation ROI, Return on Investment, measures whether the time or cost saved by running an automated test repeatedly over time outweighs the upfront time or cost spent building and later maintaining the automation script, compared to simply running the test manually every time.

**Given:**
- Automating the test: 4 hours = 240 minutes, one-time investment
- Running it manually: 30 minutes per run
- Maintenance overhead: 20% added cost per run, but only after the 10th run

**Step 1, break-even without maintenance overhead:**
Break-even runs = Automation time divided by Manual time per run = 240 divided by 30 = **8 runs**

This means by the 8th time the test would have been run manually, the automated version has already saved enough time to pay back the initial 4-hour investment.

**Step 2, checking the maintenance overhead:**
The 20% maintenance overhead only applies after the 10th run. Since break-even is already reached at run 8, before the 10th run, the overhead does not delay or affect the payback point.

After the 10th run, each additional run's net saving reduces because of the 20% overhead:
- Net saving per run before overhead = 30 minutes manual time saved, since running the automated script is effectively instant and unattended
- Net saving per run after the 10th run = 30 minus 20% of 30 = 30 minus 6 = **24 minutes saved per run**

**Conclusion:** The automation pays for itself after **8 runs**. From the 11th run onward, it still saves time on every run, 24 minutes per run instead of 30, just at a slightly reduced rate due to ongoing maintenance, so automating this test remains worthwhile long-term.

---

## 20. Describe what a "flaky test" is, give one example, and list 3 strategies to prevent or fix flaky tests in a Selenium suite.

A flaky test is a test case that produces inconsistent results, sometimes passing and sometimes failing, when run against the exact same code with no actual change in the application's behavior. It undermines trust in the test suite, since failures may be ignored as probably just flaky even when they indicate a real bug.

**Example:** A Selenium test that clicks Submit on the Add Course form and immediately asserts the success message is displayed, but the assertion sometimes runs before the page has finished processing the request, causing the test to fail even though the feature works correctly.

**3 Strategies to Prevent or Fix Flaky Tests:**

1. **Use explicit waits instead of fixed sleeps:**
   Replace a fixed sleep of several seconds with Selenium's WebDriverWait and expected conditions, waiting until the success message element is visible, so the test only proceeds once the page is actually ready, regardless of variable load time.

2. **Ensure test independence and clean state:**
   Each test should set up its own data and clean up afterward, for example using a fresh test database or resetting state before each run, so tests don't fail due to leftover data from a previous test run or depend on execution order.

3. **Isolate and stabilize the test environment:**
   Run tests against a dedicated, consistent test environment, not shared with other developers or subject to network flakiness, and avoid hard-coded timing assumptions tied to environment speed. Use retries with backoff only as a last resort, not as a substitute for fixing the root cause.


# Task 2: Compare Automation Framework Types — Course Management System

## 21. For each of the 5 framework types, Linear, Modular, Data-Driven, Keyword-Driven, Hybrid, provide: a one-paragraph description, one advantage, one disadvantage, and a brief example of when you would use it for the Course Management system.

### Linear Framework
A linear framework is the simplest form of automation, where test steps are recorded or written in a straight sequential order, exactly as a user would perform them, with no reuse of code or modular structure. Each script runs from top to bottom independently.

**Advantage:** Very quick and easy to create, needs minimal programming knowledge, and is ideal for getting started fast.

**Disadvantage:** Highly repetitive and hard to maintain, since any small UI change, such as the login page layout changing, requires updating every single script that contains those steps.

**Example use for Course Management system:** Writing a one-off script to quickly verify that the Add Course form loads and accepts input during initial development, without needing it to scale or be reused elsewhere.

---

### Modular Framework
A modular framework breaks the application into smaller, independent modules or functions, such as Login, Add Course, and Search Course, with each module tested separately and combined to build larger test cases.

**Advantage:** Easier to maintain than linear scripts, since a change to one module, such as the login flow, only needs to be updated in one place.

**Disadvantage:** Still requires programming knowledge to build and connect modules, and doesn't handle large volumes of varying test data well on its own.

**Example use for Course Management system:** Creating a separate reusable Login module and a separate Add Course module, then combining them to test that a logged-in admin can add a course.

---

### Data-Driven Framework
A data-driven framework separates test logic from test data, storing input values and expected results in external files such as Excel, CSV, or JSON, so the same test script runs multiple times with different data sets.

**Advantage:** Excellent for testing the same flow with many different inputs without duplicating scripts, saving significant time and effort.

**Disadvantage:** Requires more upfront setup effort to build the data-reading logic, and the test logic itself is still fixed, so it isn't suited for testing entirely different flows.

**Example use for Course Management system:** Running the same "create course" test script against a spreadsheet containing 30 different combinations of course names, codes, and credit values to check validation handles each case correctly.

---

### Keyword-Driven Framework
A keyword-driven framework represents test steps as keywords, such as "Login", "EnterCourseName", and "ClickSubmit", stored in a spreadsheet or table, with an underlying engine that interprets each keyword and executes the corresponding code.

**Advantage:** Allows non-technical team members, such as manual testers or business analysts, to write and understand test cases without needing to code.

**Disadvantage:** Takes significant upfront effort and technical skill to build the keyword-interpretation engine itself, and debugging failures can be harder since the logic is abstracted away.

**Example use for Course Management system:** Letting a non-technical College Administrator representative build a test case for the Add Course flow by simply listing keywords like Login, NavigateToAddCourse, EnterCourseDetails, and Submit in a spreadsheet.

---

### Hybrid Framework
A hybrid framework combines elements of the other approaches, typically modular structure, data-driven data separation, and sometimes keyword-driven readability, to get the benefits of each while minimizing their individual weaknesses.

**Advantage:** Highly flexible and scalable, supporting reusable modules, external test data, and readability for different skill levels within one framework.

**Disadvantage:** More complex to design and set up initially, requiring careful planning of folder structure and architecture compared to a simpler single-style framework.

**Example use for Course Management system:** Building the full Selenium suite for the Course Management frontend using reusable login and navigation modules, external data files for test inputs, and a clear structure that both developers and manual testers can contribute to.

---

## 22. The team is building a Selenium suite for the Course Management frontend. They need to: test login with 50 different user/password combinations, reuse login steps across 20 test cases, and support both technical and non-technical team members writing tests. Which framework type or combination would you recommend? Justify your answer.

A Hybrid framework, combining Modular, Data-Driven, and Keyword-Driven approaches is required.

This helps,
- **Testing login with 50 different user or password combinations** calls for a **Data-Driven** approach, storing the 50 combinations in an external file such as a CSV or Excel sheet, and running one script against all of them, rather than writing 50 separate scripts.

- **Reusing login steps across 20 test cases** calls for a **Modular** approach, where the login flow is built once as a reusable function or Page Object, and every one of the 20 test cases simply calls that shared login module instead of duplicating the steps.

- **Supporting both technical and non-technical team members** calls for a **Keyword-Driven** element, so non-technical team members can write test cases using readable keywords such as Login, SearchCourse, and AddCourse, while technical team members maintain the underlying automation code.

Since no single framework type on its own satisfies all three requirements at once, a **Hybrid framework** that layers Data-Driven test data, Modular reusable components such as a Login module, and a Keyword-Driven interface on top is the right recommendation for this Selenium suite.

---

## 23. Draw or describe the folder structure you would create for a Hybrid framework for the Course Management frontend tests. Include: test data files, page object files, utility files, test files, and configuration.

```
course-management-selenium-suite/
│
├── config/
│   ├── config.properties
│   └── log4j.properties
│
├── testdata/
│   ├── login_credentials.csv
│   ├── course_creation_data.xlsx
│   └── testdata_reader.py
│
├── pageobjects/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── add_course_page.py
│   └── search_course_page.py
│
├── utils/
│   ├── driver_factory.py
│   ├── excel_utils.py
│   ├── wait_utils.py
│   └── keyword_engine.py
│
├── keywords/
│   └── add_course_keywords.xlsx
│
├── tests/
│   ├── test_login.py
│   ├── test_add_course.py
│   ├── test_search_course.py
│   └── test_regression_suite.py
│
├── reports/
│   └── test_execution_report.html
│
└── requirements.txt
```

**What each folder holds:**

- `config/` — environment URLs, browser type, timeouts, and logging settings.
- `testdata/` — the 50 username/password combinations, course name/code/credit data sets, and a helper to read/parse these files.
- `pageobjects/` — locators and actions for the Login page, Admin dashboard, Add Course form, and Search page.
- `utils/` — WebDriver setup/teardown, Excel read/write helpers, reusable explicit wait functions, and the engine that interprets keywords.
- `keywords/` — keyword-driven test steps written in spreadsheet form for non-technical testers.
- `tests/` — the actual test scripts: data-driven login tests, modular add-course and search-course tests, and the combined regression suite.
- `reports/` — generated test execution reports.
- `requirements.txt` — dependencies such as Selenium, pytest, and openpyxl.

**How this supports the Hybrid design:**
- `pageobjects/` gives the Modular reusability, for example the login module used by 20+ test cases.
- `testdata/` gives the Data-Driven capability, for example the 50 login combinations.
- `keywords/` and `utils/keyword_engine.py` give the Keyword-Driven layer, letting non-technical members build tests from readable keyword sheets.
- `config/` and `utils/` keep environment setup and shared logic centralized, so the whole suite stays maintainable as it grows.