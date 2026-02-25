import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

const api = axios.create({
    baseURL: API_URL,
    headers: { 'Content-Type': 'application/json' },
})

// Auto-attach JWT token
api.interceptors.request.use((config) => {
    if (typeof window !== 'undefined') {
        const token = localStorage.getItem('forge_token')
        if (token) config.headers.Authorization = `Bearer ${token}`
    }
    return config
})

// Auth
export const authApi = {
    login: (username: string, password: string) =>
        api.post('/api/auth/login', new URLSearchParams({ username, password }), {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        }),
    register: (data: { username: string; email: string; password: string; full_name?: string }) =>
        api.post('/api/auth/register', data),
    me: () => api.get('/api/auth/me'),
}

// Levels
export const levelsApi = {
    getAll: () => api.get('/api/levels'),
    getExercises: (levelNumber: number) => api.get(`/api/levels/${levelNumber}/exercises`),
}

// Exercises
export const exercisesApi = {
    getById: (id: number) => api.get(`/api/exercises/${id}`),
}

// Submissions
export const submissionsApi = {
    run: (exerciseId: number, code: string, customInput?: string) =>
        api.post(`/api/submissions/${exerciseId}/run`, { code, custom_input: customInput }),
    submit: (exerciseId: number, code: string) =>
        api.post(`/api/submissions/${exerciseId}/submit`, { code }),
}

// Progress
export const progressApi = {
    dashboard: () => api.get('/api/progress/dashboard'),
}

// Users
export const usersApi = {
    leaderboard: () => api.get('/api/users/leaderboard'),
}

// Achievements
export const achievementsApi = {
    getAll: () => api.get('/api/achievements'),
    getAvailable: () => api.get('/api/achievements/available'),
}

export default api

