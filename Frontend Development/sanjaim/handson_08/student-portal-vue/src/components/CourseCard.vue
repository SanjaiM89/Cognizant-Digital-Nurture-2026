<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String,
})

defineEmits(['enroll'])
</script>

<template>
  <div class="course-card">
    <div class="course-card-header">
      <h3>{{ name }}</h3>
      <span class="code">{{ code }}</span>
    </div>
    <p><strong>Credits:</strong> {{ credits }}</p>
    <p><strong>Grade:</strong> {{ grade }}</p>
    <button @click="$emit('enroll')">Enroll</button>
  </div>
</template>

<style scoped>
.course-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  background-color: #ffffff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
}

.course-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid #f0f0f0;
  padding-bottom: 12px;
  margin-bottom: 12px;
}

.course-card-header h3 {
  margin: 0;
  font-size: 1.25rem;
  color: #2c3e50;
}

.code {
  background-color: #edf2f7;
  color: #4a5568;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: bold;
}

button {
  margin-top: 15px;
  padding: 6px 12px;
  background-color: #6b7280;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}
</style>
