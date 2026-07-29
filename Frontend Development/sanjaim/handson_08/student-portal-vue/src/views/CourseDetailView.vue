<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const route = useRoute()
const router = useRouter()
const enrollmentStore = useEnrollmentStore()
const course = ref(null)

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:8000/posts')
  const courses = await response.json()
  course.value = courses.find((c) => c.id === Number(route.params.id))
})

function handleEnroll() {
  enrollmentStore.enroll(course.value)
  router.push('/profile')
}
</script>

<template>
  <div v-if="course" class="detail">
    <h1>{{ course.name }}</h1>
    <p>Code: {{ course.code }}</p>
    <p>Credits: {{ course.credits }}</p>
    <p>Grade: {{ course.grade }}</p>
    <button @click="handleEnroll">Enroll</button>
  </div>
  <h2 v-else class="detail">Course not found</h2>
</template>

<style scoped>
.detail {
  padding: 20px 40px;
}

button {
  margin-top: 15px;
  padding: 8px 16px;
  background-color: #2c3e50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
