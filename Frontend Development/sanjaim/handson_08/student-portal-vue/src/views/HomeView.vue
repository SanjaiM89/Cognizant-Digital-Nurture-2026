<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="hero">
    <h1>Welcome to the Student Portal</h1>
    <p>View your enrolled courses, browse the course catalog, and manage your profile.</p>
    <RouterLink to="/courses" class="button">Explore Courses</RouterLink>
  </div>
</template>

<style scoped>
.hero {
  text-align: center;
  padding: 60px 20px;
}

.button {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 24px;
  background-color: #2c3e50;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
}
</style>
