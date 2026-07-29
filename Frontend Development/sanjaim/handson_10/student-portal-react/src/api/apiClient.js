import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 5000,
})

// mock token for now - replace with a real auth flow once /auth/login exists
const MOCK_TOKEN = 'mock-token-123'

apiClient.interceptors.request.use((config) => {
  config.headers.Authorization = `Bearer ${MOCK_TOKEN}`
  return config
})

apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const standardError = new Error(
      error.response?.data?.message || error.message || 'Something went wrong'
    )
    standardError.statusCode = error.response?.status || 500
    return Promise.reject(standardError)
  }
)

export default apiClient
