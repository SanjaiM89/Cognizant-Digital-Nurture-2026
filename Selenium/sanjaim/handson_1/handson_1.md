**QA Concepts, Functional Testing & Defect Lifecycle**

**Task 1: Map Testing Types to a Real System**

1. For the Course Management API, identify and describe one concrete test case for each of the
following testing types: Unit Testing (test a single function in isolation), Integration Testing (test two
components working together, e.g., the API endpoint + database), System Testing (test a full end-to-
end flow from API request to database response), User Acceptance Testing (test from the perspective
of an actual college admin user)
```
Unit Testing (Functional): Testing the data validation function for a new course in isolation. For example, passing an empty course_name string to the Python function and asserting it raises a validation error, without ever connecting to a database.

Integration Testing (Functional): Testing the connection between the API logic and the MySQL database. For example, sending a valid payload to the POST /api/courses/ function and verifying that a new row is actually inserted into the courses database table.

System Testing (Functional): Testing the entire application as a whole. For example, creating a course via POST /api/courses/, then calling GET /api/courses/{id} to verify the data returns correctly, checking the full request-to-database-to-response cycle.

User Acceptance Testing (Functional): Testing from the client's perspective. For example, a College Administrator logs into the frontend dashboard, fills out the "Add Course" form, submits it, and verifies the new course appears correctly in their course catalogue.
```


2. Classify each test case as either Functional (does it do what it should?) or Non-Functional (how well
does it do it?). Give one non-functional test example for the API (e.g., performance, security, or
reliability).

```

Funtional Testing is a type of blakc box testing that validates the system against its functional requirements.
-> The main primary objective is to verify the application behaviour to be exactly as it is intended to be, the system should do what it is supposed to do
-> It ensures the quality of the software and its functions and enhance the security via validation of each and every components of the function which reduces
risk invloving software or privacy bugs.
It includes Unit Testing, Integration Testing, Systen Testing, Regression Testing

NonFunctional Testing checks the how well the system performs in terms of quality attributes
-> It focuses on performance,security, reliablity and scalability and ensues the software performs efficiently and securely
It includes Performance testing, Load testing, Stress Testing, Usability Testing

Ex: Sending 1000 request simultaneously to GET /api/courses to verify that it respondes to all request under 100 milliseconds without any crasking shows how the
system performs on load

```

3. Explain the difference between Black-Box Testing (testing without knowledge of internal code) and
White-Box Testing (testing with knowledge of the code). State which type a QA tester typically
performs and which a developer performs.

```
Black Box testing : -

-> It is a software technique where the internal code or the strucutre of the application is not koown to the tester.
-> It verifies the functionality of the software based on input and expected output
-> It ensures that the system behaves as per the user requirements
-> Focuses only on inputs and outputs not the internal code
-> It can be performed without the knowledge of programming or system logic
-> It is used to validate the function requirements and the user expectations

White Box testing:-

->It is a software technique where the tester has the knowledge of the internal code ands trcutre of the application.
-> It focuses on verifying the flow of logic conditions and focuses on the internal code and the structure
-> It requires programming knowlege
-> it is used to test code and find any hiddhen errors or logic flaws
```

4. Write 3 formal test cases for the POST /api/courses/ endpoint in a table format with columns: Test
Case ID, Description, Preconditions, Test Steps, Expected Result, Actual Result (leave blank),
Pass/Fail (leave blank)


| Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| --- | --- | --- | --- | --- | --- | --- |
| Test Case 1 | Add Course | API server need to be running and accessible | Send POST request to /api/courses/ with valid json | The response needs to be stats code 201 which implies the course is added |  |  |
| Test Case 2 | Reject missing field | API server need to be running and accessible | Send POST request to /api/courses/ with a mission field that is required | Status code 400 which implies bad request and the response contains a mission field that is required |  |  |
| Test Case 3 | Reject duplicate course code | A course that is sent needs to be already there | Send POST request to /api/courses/ that is already in database | Status code 409 which implies that the course code must be unique |  |  |


**Task 2: Defect Lifecycle & Severity Classification**

5. Draw or describe (in text) the complete defect lifecycle with all states: New → Assigned → Open →
Fixed → Retest → Verified → Closed. Also describe the Rejected and Deferred paths.

```
Defect lifecycle is the journey a bug is identified by a QA tester to the time it is confirmed, resolved and closed

The lifecycle is

New Bug Identified -> Assigned -> Open -> Fixed -> Retest the bug -> Verify -> Close

-> New Bug Identifed by QA tester
-> Assigned to a Developer (Developer Reviews it and either rejects/ accepts/ deferred the bug. The Rejection is due to either it may not be a bug or the developer may not be able to reproduce the bug or the same bug is already reported) and deferred is the bug is valid bug but it is not severe and is posponded to future release 
-> If the bug is accepted, The status is kept Open where the developer is actively working on fixing the bug. 
-> Once the bug is fixed the stauts is changed to FIXED
-> The QA tester then test the same bug again on the new build
-> The QA tester verifies the bug is there or not
-> Once QA tester confirms the bug is not appearing any more the stauts is changed to Closed

```

6. For each of the following hypothetical bugs in the Course Management API, classify the Severity
(Critical / High / Medium / Low) and Priority (P1 / P2 / P3 / P4), and justify your classification: a)
POST /api/courses/ returns 500 Internal Server Error for all requests. b) Course names longer than
150 characters are silently truncated without an error. c) The /docs Swagger page has a typo in the
API description. d) Login with correct credentials occasionally returns 401 on the first attempt
(intermittent)

 a)POST /api/courses/ returns 500 Internal Server Error for all requests.

```
Severity is Critical
Priority P: P1 (highest)
Adding course is the core primary funtion in Course Management API, an error 500 means the system is creasjing and the feature is completely blocked
for all users with no possible workaround and this requires immediate optimization and fix
```
b) Course names longer than 150 characters are silently truncated without an error.

```
Severity : Medium
Priority : P3 (Medium)
Here, the system is not crashing and also majority of users will never have the course name longer than 150 characters however without there is be error thrown
with status code 400 for Back request instead of just manupulating the data. 
```

c) The /docs Swagger page has a typo in the API description. 

```
Severity : Low
Priority : P4 (lowest)
This has zero impact on the actual functionality or the performance or the security of the application.
```

d) Login with correct credentials occasionally returns 401 on the first attempt (intermittent)

```
Severity : Medium
Priority : P1(Highest)

Since the user can login in their futhur attempt the system is not completely broken or not functional. But since the issue is realted to login issue
having a flaw in the login will break user trust and increase their frustration so the priority is high
```

7. Write a complete defect report for bug (a) above using standard fields: Defect ID, Title, Environment,
Build Version, Severity, Priority, Steps to Reproduce, Expected Result, Actual Result, Attachments
(state 'screenshot of 500 error').

```
Defect ID: BUG-01
Title: 500 Internal Server Error returned when creating a new course via POST /api/courses/
Environment: QA / Staging (Ubuntu 22.04, MySQL 8.0)Build Version: v1.0.0
Severity: Critical
Priority: P1 (Highest)

Steps to Reproduce:
-> Open an API client like postman
->Set the HTTP method to POST and the endpoint URL to [Base_URL]/api/courses/
->Add a valid JSON payload to the request body.(Example payload: {"course_name": "TOC", "course_code": "CS201", "credits": 3})
->Execute/Send the request.

Expected Result:The API should return an HTTP 201 Created status code, the new course should be saved to the database, and the response body should contain the newly created course details (including the generated course_id)

Actual Result:The API returns an HTTP 500 Internal Server Error status code. The response body contains a server crash stack trace, and the course is not inserted into the database. This occurs consistently for all valid payloads

Attachments:screenshot of 500 error

```

8. Explain the difference between Severity and Priority with a real-world example where High Severity
does not mean High Priority.

```
Severity

-> Severity is defined as the extent to which a particualr defect can create impact on software.
-> It is a parameter to denote the implication and the impact of the defect on the functionality of the software
-> It defines the impact on the system functionality

Priorty

-> Protioty is defined as a parameter that decides the order in which a defect should be fixed. Defects having highes priority should
be fixed first
-> Defects that leave the softwate unusable are given higher priority over the defects that cause a small functionality of the software to fail
-> It aslo provides the order in which developers should fix bugs based on business impact, reveue and user experience

```