'use client'
import { createContext, useContext, useEffect, useState } from 'react'
import { authApi } from '@/lib/api'

interface User {
    id: number
    username: string
    email: string
    full_name: string | null
    role: string
    total_xp: number
    current_level: number
    streak_days: number
    total_submissions: number
}

interface AuthContextType {
    user: User | null
    loading: boolean
    login: (username: string, password: string) => Promise<void>
    register: (data: { username: string; email: string; password: string; full_name?: string }) => Promise<void>
    logout: () => void
}

const AuthContext = createContext<AuthContextType | null>(null)

export function AuthProvider({ children }: { children: React.ReactNode }) {
    const [user, setUser] = useState<User | null>(null)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const token = localStorage.getItem('forge_token')
        if (token) {
            authApi.me().then(r => setUser(r.data)).catch(() => localStorage.removeItem('forge_token')).finally(() => setLoading(false))
        } else {
            setLoading(false)
        }
    }, [])

    const login = async (username: string, password: string) => {
        const r = await authApi.login(username, password)
        localStorage.setItem('forge_token', r.data.access_token)
        const me = await authApi.me()
        setUser(me.data)
    }

    const register = async (data: Parameters<typeof authApi.register>[0]) => {
        await authApi.register(data)
        await login(data.username, data.password)
    }

    const logout = () => {
        localStorage.removeItem('forge_token')
        setUser(null)
    }

    return <AuthContext.Provider value={{ user, loading, login, register, logout }}>{children}</AuthContext.Provider>
}

export const useAuth = () => {
    const ctx = useContext(AuthContext)
    if (!ctx) throw new Error('useAuth must be used within AuthProvider')
    return ctx
}
