import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { getAllCourses } from '../api/courseApi'

export const fetchAllCourses = createAsyncThunk('courses/fetchAll', async () => {
  return await getAllCourses()
})

const coursesSlice = createSlice({
  name: 'courses',
  initialState: {
    courses: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true
        state.error = null
      })
      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.courses = action.payload
        state.loading = false
      })
      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.error = action.error.message
        state.loading = false
      })
  },
})

export const selectCourses = (state) => state.courses.courses
export const selectCoursesLoading = (state) => state.courses.loading
export const selectCoursesError = (state) => state.courses.error

export default coursesSlice.reducer
