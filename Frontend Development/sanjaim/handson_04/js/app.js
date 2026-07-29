import { courses } from "./data.js"

// Task 1: Promises and async/await

function fetchUser(id) {
  return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then(response => response.json())
    .then(user => {
      console.log(user.name)
      return user
    })
}

async function fetchUserAsync(id) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    const user = await response.json()
    console.log(user.name)
    return user
  } catch (err) {
    console.log(err.message)
  }
}

fetchUserAsync(1)

function fetchAllCourses() {
  return new Promise(resolve => {
    setTimeout(() => resolve(courses), 1000)
  })
}

const courseGrid = document.querySelector(".course-grid")

function renderCourses(list) {
  courseGrid.innerHTML = ""
  const fragment = document.createDocumentFragment()

  list.forEach(course => {
    const article = document.createElement("article")
    article.className = "course-card"
    article.innerHTML = `
      <h3>${course.name}</h3>
      <p>${course.code}</p>
      <p><span class="credits">Credits: ${course.credits}</span></p>
    `
    fragment.appendChild(article)
  })

  courseGrid.appendChild(fragment)
}

async function loadCourses() {
  courseGrid.innerHTML = "<p>Loading courses...</p>"
  const list = await fetchAllCourses()
  renderCourses(list)
}

loadCourses()

Promise.all([fetchUser(1), fetchUser(2)]).then(([user1, user2]) => {
  console.log(`Both loaded: ${user1.name}, ${user2.name}`)
})


// Task 2: Fetch API with Error Handling

async function apiFetch(url) {
  const response = await fetch(url)
  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`)
  }
  return response.json()
}

const notificationsBody = document.querySelector(".notifications-body")

function renderNotifications(posts) {
  notificationsBody.innerHTML = ""
  const list = document.createElement("div")
  list.className = "notification-list"

  posts.forEach((post, index) => {
    const card = document.createElement("article")
    card.className = "notification-card"
    card.innerHTML = `<h4>Notification ${index + 1}</h4><p>This is the content for notification ${index + 1}</p>`
    list.appendChild(card)
  })

  notificationsBody.appendChild(list)
}

function renderNotificationsError(message, retryHandler) {
  notificationsBody.innerHTML = `<p class="error-message">${message}</p>`
  const retryButton = document.createElement("button")
  retryButton.type = "button"
  retryButton.textContent = "Retry"
  retryButton.addEventListener("click", retryHandler)
  notificationsBody.appendChild(retryButton)
}

async function loadNotifications(url = "https://jsonplaceholder.typicode.com/posts?_limit=5") {
  notificationsBody.innerHTML = "<p class='loading-spinner'>Loading...</p>"

  try {
    const posts = await apiFetch(url)
    renderNotifications(posts)
  } catch (err) {
    renderNotificationsError("Could not load notifications. Please try again.", () => loadNotifications(url))
  }
}

loadNotifications()

document.getElementById("reload-notifications").addEventListener("click", () => loadNotifications())
document.getElementById("simulate-error").addEventListener("click", () => loadNotifications("https://jsonplaceholder.typicode.com/nonexistent"))


// Task 3: Introduction to Axios
/*
Fetch vs Axios:
1. Fetch is built into the browser, no install needed. Axios is a separate library that needs to be added via CDN or npm.
2. Fetch does not reject on HTTP error responses like 404/500, only on network failure — response.ok has to be checked manually. Axios throws automatically on any non-2xx response.
3. Fetch requires an extra response.json() call to parse the body. Axios parses JSON automatically and gives the data directly on response.data.
*/

axios.interceptors.request.use(config => {
  console.log(`API call started: ${config.url}`)
  return config
})

axios.get("https://jsonplaceholder.typicode.com/posts", {
  params: { userId: 1 }
}).then(response => {
  console.log(response.data)
})
