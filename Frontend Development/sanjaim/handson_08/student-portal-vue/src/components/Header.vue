<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const enrollmentStore = useEnrollmentStore()
</script>

<template>
  <header class="header">
    <h1 class="title">Student Portal</h1>
    <nav>
      <ul class="nav-list">
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/courses">Courses</RouterLink></li>
        <li><RouterLink to="/profile">Profile</RouterLink></li>
        <li class="enrolled">Enrolled Course: {{ enrollmentStore.enrolledCourses.length }}</li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
.header {
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #2c3e50;
  color: #fff;
}

.title {
  font-size: 1.5rem;
  margin: 0;
}

.nav-list {
  list-style: none;
  display: flex;
  gap: 30px;
  padding: 0;
  margin: 0;
  align-items: center;
}

.nav-list a {
  color: #fff;
  text-decoration: none;
}

.enrolled {
  color: #90cdf4;
  font-weight: bold;
}
</style>
