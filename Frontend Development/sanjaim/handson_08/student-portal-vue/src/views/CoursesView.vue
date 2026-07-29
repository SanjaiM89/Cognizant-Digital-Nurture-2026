<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const courses = ref([])
const searchTerm = ref('')
const loading = ref(true)
const router = useRouter()
const enrollmentStore = useEnrollmentStore()

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:8000/posts')
  courses.value = await response.json()
  loading.value = false
})

const filteredCourses = computed(() =>
  courses.value.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
)

function handleEnroll(course) {
  enrollmentStore.enroll(course)
  router.push('/profile')
}
</script>

<template>
  <div class="courses">
    <h2>Courses</h2>
    <input type="text" placeholder="Search by Name" v-model="searchTerm" class="search-input" />

    <p v-if="loading">Loading courses...</p>
    <p v-else-if="filteredCourses.length === 0">No courses found</p>

    <div class="course-grid" v-else>
      <CourseCard
        v-for="course in filteredCourses"
        :key="course.id"
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
        @enroll="handleEnroll(course)"
      />
    </div>
  </div>
</template>

<style scoped>
.courses {
  padding: 20px 40px;
}

.search-input {
  padding: 8px 12px;
  border: 1px solid #dfe1e5;
  border-radius: 6px;
  width: 300px;
  margin-bottom: 20px;
  font-size: 14px;
}

.course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}
</style>
