<script setup>
import { ref } from 'vue'
import { useEnrollmentStore } from '../stores/enrollment'

const enrollmentStore = useEnrollmentStore()

const name = ref('')
const email = ref('')
const semester = ref('')
</script>

<template>
  <div class="profile">
    <h2>Student Profile</h2>
    <input type="text" placeholder="Name" v-model="name" />
    <input type="email" placeholder="Email" v-model="email" />
    <input type="text" placeholder="Semester" v-model="semester" />

    <h2>Enrolled Courses ({{ enrollmentStore.enrolledCourses.length }})</h2>
    <p v-if="enrollmentStore.enrolledCourses.length === 0">No courses enrolled yet.</p>
    <ul v-else>
      <li v-for="course in enrollmentStore.enrolledCourses" :key="course.id">
        {{ course.name }} ({{ course.code }})
        <button @click="enrollmentStore.unenroll(course.id)">Remove</button>
      </li>
    </ul>
    <p>Total Credits: {{ enrollmentStore.totalCredits }}</p>
  </div>
</template>

<style scoped>
.profile {
  padding: 20px 40px;
}

input {
  display: block;
  margin-bottom: 10px;
  padding: 8px;
  border: 1px solid #dfe1e5;
  border-radius: 6px;
}
</style>
