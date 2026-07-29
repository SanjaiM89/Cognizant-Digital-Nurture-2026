# Microservices Decomposition — Course Management System

## Task 1: Bounded contexts

Reviewing the Course Management API built across the earlier hands-on's, four
natural bounded contexts emerge:

| Service Name | Responsibility | Endpoints it owns | Database it owns |
|---|---|---|---|
| Course Service | Department and course CRUD | `GET/POST /api/courses/`, `GET /api/courses/{id}/` | `course_service.sqlite3` |
| Student Service | Student CRUD, enrollment | `GET/POST /api/students/`, `GET /api/students/{id}/`, `POST /api/students/{id}/enroll` | `student_service.sqlite3` |
| Auth Service | Registration, login, token validation | `POST /api/auth/register/`, `POST /api/auth/login/` | its own `users` table |
| Notification Service | Email confirmations on enrollment | none (consumes events) | none — stateless |

Only **Course Service** and **Student Service** are actually built for this
exercise, per the hint not to over-engineer a 2-service problem into four
running processes. Auth and Notification stay as identified-but-unbuilt
contexts: Auth already exists as JWT logic inside the FastAPI app from
Hands-On 9, and Notification is just the `send_confirmation_email` background
task from Hands-On 7/9 — neither needed a dedicated process to prove the
decomposition concept here.

## Task 2: Inter-service communication and the API Gateway

- `course_service/` (port 5001) — owns courses, nothing else. No knowledge of
  students or enrollments.
- `student_service/` (port 5002) — owns students and enrollments. Its
  `POST /api/students/{id}/enroll` endpoint needs to confirm a course exists
  before creating the enrollment row, but it does **not** query
  `course_service.sqlite3` directly — that would break service ownership of
  data. Instead it calls Course Service's `GET /api/courses/{id}/` over HTTP
  using `requests`, and returns `503 Service Unavailable` if that call raises
  `ConnectionError` (Course Service is down).
- `gateway/` (port 5000) — a thin Flask app with no business logic of its
  own. It looks at the first path segment (`courses` or `students`) and
  forwards the request to the matching service with `requests.request()`,
  returning whatever that service responded with. `/api/courses/*` →
  Course Service, `/api/students/*` → Student Service.

### Sync (HTTP) vs async (message queue)

The enrollment call (Student Service → Course Service) is synchronous: the
client waits on the HTTP round-trip, and if Course Service is slow or down,
enrollment fails immediately with a 503. That's the tight coupling a
synchronous call always creates — one service's availability becomes a
dependency of another's.

A message queue (RabbitMQ, Kafka) would decouple this: Student Service
publishes an "enrollment requested" event and returns right away; a consumer
validates the course asynchronously and confirms or rejects the enrollment
later. That trades immediate consistency (the client doesn't know
immediately whether enrollment succeeded) for availability (Student Service
no longer goes down when Course Service does).

Use synchronous HTTP when the caller genuinely needs the answer before
proceeding (this exercise: you can't create an enrollment for a course that
may not exist). Reach for a queue when the two operations don't actually need
to happen in the same request/response cycle — e.g. the
`send_confirmation_email` background task pattern from Hands-On 7/9 is
already this same idea, just via FastAPI's in-process `BackgroundTasks`
instead of a real broker.

The gateway itself is deliberately minimal — a real API Gateway also handles
auth, rate limiting, and SSL termination, none of which this proxy does. It
only demonstrates the routing concept.
