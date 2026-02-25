'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import api from '@/lib/api'
import Link from 'next/link'
import toast from 'react-hot-toast'

export default function AdminPage() {
    const { user, loading } = useAuth()
    const router = useRouter()
    const [stats, setStats] = useState<any>(null)
    const [exercises, setExercises] = useState<any[]>([])
    const [users, setUsers] = useState<any[]>([])
    const [activeTab, setActiveTab] = useState<'overview' | 'exercises' | 'users'>('overview')
    const [fetching, setFetching] = useState(true)

    useEffect(() => {
        if (!loading && !user) router.push('/')
        if (!loading && user && user.role !== 'admin') {
            toast.error('Admin access required')
            router.push('/dashboard')
        }
    }, [user, loading])

    useEffect(() => {
        if (user && user.role === 'admin') {
            Promise.all([
                api.get('/api/admin/stats'),
                api.get('/api/admin/exercises'),
                api.get('/api/admin/users'),
            ]).then(([s, e, u]) => {
                setStats(s.data)
                setExercises(e.data)
                setUsers(u.data)
            }).catch(() => toast.error('Failed to load admin data'))
                .finally(() => setFetching(false))
        }
    }, [user])

    const handleDeleteExercise = async (id: number) => {
        if (!confirm('Delete this exercise?')) return
        try {
            await api.delete(`/api/admin/exercises/${id}`)
            setExercises(prev => prev.filter(e => e.id !== id))
            toast.success('Exercise deleted')
        } catch { toast.error('Delete failed') }
    }

    const handleRoleUpdate = async (userId: number, role: string) => {
        try {
            await api.put(`/api/admin/users/${userId}/role?role=${role}`)
            setUsers(prev => prev.map(u => u.id === userId ? { ...u, role } : u))
            toast.success('Role updated')
        } catch { toast.error('Update failed') }
    }

    if (loading || fetching) return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="w-8 h-8 border-2 border-[#00FF88] border-t-transparent rounded-full animate-spin" />
        </div>
    )

    return (
        <div className="min-h-screen bg-[#0a0e1a]">
            <nav className="border-b border-[#1f2937] bg-[#111827]/80 backdrop-blur sticky top-0 z-50">
                <div className="max-w-6xl mx-auto px-6 py-3 flex items-center gap-4">
                    <Link href="/dashboard" className="text-gray-400 hover:text-white transition text-sm">← Dashboard</Link>
                    <span className="text-gray-600">|</span>
                    <span className="text-red-400 font-semibold text-sm">🛡️ Admin Panel</span>
                </div>
            </nav>

            <div className="max-w-6xl mx-auto px-6 py-10">
                {/* Tabs */}
                <div className="flex gap-1 mb-8 bg-[#111827] rounded-lg p-1 w-fit">
                    {(['overview', 'exercises', 'users'] as const).map(t => (
                        <button key={t} onClick={() => setActiveTab(t)}
                            className={`px-4 py-2 text-sm rounded-md font-medium capitalize transition ${activeTab === t ? 'bg-[#00FF88] text-black' : 'text-gray-400 hover:text-white'}`}>
                            {t}
                        </button>
                    ))}
                </div>

                {/* Overview */}
                {activeTab === 'overview' && stats && (
                    <div className="space-y-6 animate-fadein">
                        <h2 className="text-xl font-bold">Platform Overview</h2>
                        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
                            {[
                                { label: 'Users', value: stats.total_users, color: '#3b82f6' },
                                { label: 'Exercises', value: stats.total_exercises, color: '#10b981' },
                                { label: 'Levels', value: stats.total_levels, color: '#f59e0b' },
                                { label: 'Submissions', value: stats.total_submissions, color: '#8b5cf6' },
                                { label: 'Pass Rate', value: `${stats.avg_pass_rate}%`, color: '#00FF88' },
                            ].map(s => (
                                <div key={s.label} className="bg-[#111827] border border-[#1f2937] rounded-xl p-5 text-center">
                                    <div className="text-2xl font-bold" style={{ color: s.color }}>{s.value}</div>
                                    <div className="text-xs text-gray-500 mt-1">{s.label}</div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

                {/* Exercises Table */}
                {activeTab === 'exercises' && (
                    <div className="animate-fadein">
                        <div className="flex items-center justify-between mb-4">
                            <h2 className="text-xl font-bold">Exercises ({exercises.length})</h2>
                        </div>
                        <div className="bg-[#111827] border border-[#1f2937] rounded-xl overflow-hidden">
                            <table className="w-full text-sm">
                                <thead>
                                    <tr className="border-b border-[#1f2937] text-gray-500 text-xs uppercase">
                                        <th className="text-left p-3">ID</th>
                                        <th className="text-left p-3">Title</th>
                                        <th className="text-left p-3">Difficulty</th>
                                        <th className="text-left p-3">XP</th>
                                        <th className="text-left p-3">Tests</th>
                                        <th className="text-left p-3">Submissions</th>
                                        <th className="text-right p-3">Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {exercises.map(ex => (
                                        <tr key={ex.id} className="border-b border-[#1f2937]/50 hover:bg-[#1f2937]/20">
                                            <td className="p-3 font-mono text-xs text-gray-500">{ex.id}</td>
                                            <td className="p-3 truncate max-w-[200px]">{ex.title}</td>
                                            <td className="p-3">
                                                <span className={ex.difficulty === 'easy' ? 'badge-easy' : ex.difficulty === 'medium' ? 'badge-medium' : 'badge-hard'}>
                                                    {ex.difficulty}
                                                </span>
                                            </td>
                                            <td className="p-3 text-[#00FF88]">{ex.xp_reward}</td>
                                            <td className="p-3">{ex.test_case_count}</td>
                                            <td className="p-3">{ex.submission_count}</td>
                                            <td className="p-3 text-right">
                                                <button onClick={() => handleDeleteExercise(ex.id)}
                                                    className="text-xs text-red-400 hover:text-red-300 transition">Delete</button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                )}

                {/* Users Table */}
                {activeTab === 'users' && (
                    <div className="animate-fadein">
                        <h2 className="text-xl font-bold mb-4">Users ({users.length})</h2>
                        <div className="bg-[#111827] border border-[#1f2937] rounded-xl overflow-hidden">
                            <table className="w-full text-sm">
                                <thead>
                                    <tr className="border-b border-[#1f2937] text-gray-500 text-xs uppercase">
                                        <th className="text-left p-3">Username</th>
                                        <th className="text-left p-3">Email</th>
                                        <th className="text-left p-3">Role</th>
                                        <th className="text-left p-3">XP</th>
                                        <th className="text-left p-3">Level</th>
                                        <th className="text-left p-3">Submissions</th>
                                        <th className="text-right p-3">Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {users.map(u => (
                                        <tr key={u.id} className="border-b border-[#1f2937]/50 hover:bg-[#1f2937]/20">
                                            <td className="p-3 font-semibold">{u.username}</td>
                                            <td className="p-3 text-gray-400">{u.email}</td>
                                            <td className="p-3">
                                                <span className={u.role === 'admin' ? 'text-red-400 text-xs font-bold' : 'text-gray-500 text-xs'}>
                                                    {u.role}
                                                </span>
                                            </td>
                                            <td className="p-3 text-[#00FF88]">{u.total_xp}</td>
                                            <td className="p-3">{u.current_level}</td>
                                            <td className="p-3">{u.total_submissions}</td>
                                            <td className="p-3 text-right">
                                                {u.role === 'user' ? (
                                                    <button onClick={() => handleRoleUpdate(u.id, 'admin')}
                                                        className="text-xs text-blue-400 hover:text-blue-300 transition">Make Admin</button>
                                                ) : (
                                                    <button onClick={() => handleRoleUpdate(u.id, 'user')}
                                                        className="text-xs text-gray-400 hover:text-gray-300 transition">Demote</button>
                                                )}
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                )}
            </div>
        </div>
    )
}
