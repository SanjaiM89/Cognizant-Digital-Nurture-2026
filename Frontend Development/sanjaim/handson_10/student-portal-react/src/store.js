import { configureStore } from '@reduxjs/toolkit'
import enrollmentReducer from './store/enrollmentSlice'
import coursesReducer from './store/coursesSlice'

const store = configureStore({
  reducer: {
    enrollment: enrollmentReducer,
    courses: coursesReducer
  }
})

export default store
