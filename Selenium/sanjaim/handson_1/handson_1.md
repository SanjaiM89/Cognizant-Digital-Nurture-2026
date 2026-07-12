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