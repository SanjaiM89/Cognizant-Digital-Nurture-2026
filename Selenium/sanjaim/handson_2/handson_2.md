# Task 1: V-Model Mapping — Course Management API

## 9. The V-Model (Development ↔ Testing Phases)

The V-Model is a software development model that shows a mirrored relationship between development (left side) and testing (right side), with each development phase directly corresponding to a testing phase. The two arms meet at Coding, which sits at the bottom vertex of the "V".

```
Requirements               Acceptance Testing
      \                           /
       \                         /
   System Design          System Testing
         \                     /
          \                   /
   Architecture Design   Integration Testing
             \                /
              \              /
        Module Design    Unit Testing
                 \          /
                  \        /
                   \      /
                    Coding
```

**Left side (Development / going down the V):**
Requirements → System Design → Architecture Design → Module Design → Coding

**Right side (Testing / going up the V):**
Coding → Unit Testing → Integration Testing → System Testing → Acceptance Testing

**How to read it:** each level on the left has a direct, corresponding level on the right at the same height. This means test planning starts early — at the same time as the matching development phase — rather than only after coding is finished. For example, Acceptance Testing is planned as soon as Requirements are written, not after the whole system is built.

---

## 10. SDLC Phase → Test Artifact Produced

| SDLC Phase (Left) | Corresponding TDLC Phase (Right)                                            | Test Artifact Produced During This Phase                                                                                                                                                            |
|---|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements | Acceptance Testing                                                          | Acceptance Test Plan is prepared that defines the criteria the College Administrator/client will use to accept the Course Management API (e.g., "Admin can add, view, and search courses without errors") |
| System Design | System Testing                                                              | System Test Plan is prepared defines end-to-end test scenarios covering the full request → database → response flow, such as create-course-then-fetch-course                                        |
| Architecture Design | Integration Testing                                                         | Integration Test Plan is prepared defines how components such as the API layer, the database layer, and any third-party services (e.g., auth service) will be tested together                       |
| Module Design | Unit Testing                                                                | Unit Test Plan is prepared defines test cases for individual functions/modules, such as the course-name validation function or the course-code uniqueness checker                                   |
| Coding | bottom vertex — no separate testing phase this is where Unit Testing begins | Actual code and Unit Test cases/scripts are written together                                                                                                                                        |

---

## 11. Entry and Exit Criteria for Each Testing Level

### Unit Testing
**Entry Criteria:**
- Module/function code (e.g., course validation function) has been written and compiles without errors
- Unit test cases have been designed based on the Module Design document
- Test environment/framework (e.g., pytest) is set up

**Exit Criteria:**
- All planned unit test cases have been executed
- All critical and high-severity defects found during unit testing are fixed and retested
- Code coverage meets the agreed threshold (e.g., 80%)

### Integration Testing
**Entry Criteria:**
- Unit testing is complete and individual modules are stable
- The modules to be integrated (e.g., API layer and MySQL database layer) are available and deployed to the test environment
- Integration test cases are ready, based on the Architecture Design document

**Exit Criteria:**
- All interfaces between integrated components (e.g., POST /api/courses/ successfully writing to the database) have been tested
- No critical/high defects remain open in the integration points
- Data flows correctly between all integrated modules

### System Testing
**Entry Criteria:**
- Integration testing is complete and all modules are integrated into a complete system
- A stable, feature-complete build is deployed to the QA/staging environment
- System test cases are ready, based on the System Design document

**Exit Criteria:**
- All end-to-end test cases (e.g., full create → retrieve → update → delete course flow) have passed
- All critical and high severity defects are closed; only low-severity/deferred defects may remain, with sign-off
- Non-functional requirements (performance, security) have been validated

### Acceptance Testing
**Entry Criteria:**
- System testing is complete and the system has been signed off by QA
- A production-like environment is available for the client/College Administrator to test in
- Acceptance test cases/criteria, based on the original Requirements document, are ready

**Exit Criteria:**
- The College Administrator (or client representative) has executed the acceptance test cases and confirms the system meets business requirements
- Formal sign-off/approval is given for release
- No open critical or high-severity defects remain

---

## 12. Two Places QA Should Engage Beyond the Testing Phases

1. **During the Requirements phase:** QA should participate in requirements reviews for the Course Management API to identify ambiguous, incomplete, or untestable requirements early — for example, checking whether "course_name must be valid" is specific enough to write a test against, or whether it needs a defined character limit and allowed format. Catching this early (via requirements-based Acceptance Test planning) is far cheaper than catching it after coding.

2. **During Architecture/Module Design:** QA should review the design documents (e.g., the API contract for POST /api/courses/, database schema) to plan Integration and Unit test cases in advance, and to flag design issues — such as a missing validation layer or an unclear error-response format — before the developer writes code. This ensures test cases and even testability considerations shape the design, rather than testing being an afterthought once Coding is done.

# Task 2: Agile QA and Shift-Left Testing — Course Management API

## 13. Problems Caused by Testing-After-Development (Waterfall)

1. **Late defect discovery = expensive fixes.** In Waterfall, a flaw in the Course Management API's design — for example, discovering only after the database is built that course codes aren't enforced as unique — is found after coding and integration are already done. Fixing it now means reworking the schema, the API logic, and possibly the frontend, which is far costlier than catching it during design.

2. **No time buffer for fixing defects before release.** Since testing is squeezed into the end of the timeline, if System Testing on the Course Management API reveals critical bugs (e.g., POST /api/courses/ returning 500 errors), there is little schedule left to fix and retest them properly, often forcing rushed patches or a delayed release.

3. **Requirements misunderstandings surface too late.** The College Administrator (end user) only sees and validates the working system during Acceptance Testing, at the very end. If the team misunderstood a requirement — e.g., admins actually needed bulk course upload, not just one-by-one — this is discovered after the whole system is built, requiring significant rework instead of a small adjustment during requirements.

---

## 14. QA's Role in Each Agile Ceremony

**Sprint Planning — Defining Acceptance Criteria:**
The QA engineer works with the Product Owner and developers to turn each user story (e.g., "As a college admin, I want to create a new course") into clear, testable Acceptance Criteria before the sprint starts. This ensures everyone agrees on what "done and correct" looks like for the Course Management API feature before any code is written.

**Daily Standup — Blocking Issues:**
The QA engineer reports any blockers affecting testing — for example, "I can't test the new course creation endpoint because the staging database isn't seeded with test data" — so the team can resolve it quickly instead of it silently delaying the sprint.

**Sprint Review — Demo Testing:**
The QA engineer validates that the feature being demoed to stakeholders (e.g., the new Add Course flow) actually works as intended beforehand, and may participate in or support the live demo, answering questions about what was tested and what edge cases were covered.

**Retrospective — Process Improvement:**
The QA engineer reflects on what testing-related issues slowed the sprint down — for example, "we found the duplicate course code bug too late because we didn't have integration tests for it" — and proposes process changes, such as adding automated integration tests earlier in future sprints.

---

## 15. Four Shift-Left Practices Applied to the Course Management API

**(a) Reviewing Requirements for Testability:**
Before development starts, QA reviews the requirement "Course names must be valid" and pushes for specifics — a max length, allowed characters, and what error should be returned. This turns a vague requirement into one that can actually be tested (e.g., "reject names over 150 characters with a 400 error"), preventing ambiguity from reaching coding.

**(b) Writing Test Cases Before Code (TDD/BDD):**
Before implementing the POST /api/courses/ endpoint, the developer (or QA, in BDD) first writes a failing test — such as "creating a course with a duplicate course_code returns 409" — and only then writes the code to make it pass. This ensures the validation logic is built to satisfy a known, testable requirement from the start.

**(c) Static Code Analysis:**
Tools like pylint, SonarQube, or Bandit are run automatically on the Course Management API codebase (e.g., on every pull request) to catch issues like unused variables, SQL injection risks in database queries, or overly complex functions — before the code is ever merged or reaches a testing environment.

**(d) API Contract Testing Before Integration:**
Before the frontend and backend teams integrate, the API contract for endpoints like POST /api/courses/ (expected request/response schema, status codes) is validated independently — using a tool like Pact or a JSON schema validator — to confirm the API matches what was agreed upon, catching mismatches (e.g., a missing course_id field in the response) before full integration testing begins.

---

## 16. Acceptance Criteria in Gherkin (Given-When-Then)

**User Story:** As a college admin, I want to create a new course, so that it is available in the course catalogue for students to view and enroll in.

```
Feature: Course Creation

  Scenario: Successfully create a new course with valid details
    Given I am logged in as a College Administrator
    And I am on the "Add Course" page
    When I enter a unique course code, a valid course name, and the number of credits
    And I submit the form
    Then the course should be saved to the database
    And I should see a confirmation message that the course was created
    And the new course should appear in the course catalogue

  Scenario: Reject course creation with a missing required field
    Given I am logged in as a College Administrator
    And I am on the "Add Course" page
    When I leave the course name field empty
    And I submit the form
    Then the course should not be saved to the database
    And I should see an error message indicating the course name is required

  Scenario: Reject course creation with a duplicate course code
    Given I am logged in as a College Administrator
    And a course with the code "CS201" already exists
    When I submit a new course using the course code "CS201"
    Then the course should not be saved to the database
    And I should see an error message indicating the course code must be unique
```