'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import { progressApi } from '@/lib/api'
import Link from 'next/link'

export default function DashboardPage() {
    const { user, logout, loading } = useAuth()
    const router = useRouter()
    const [progress, setProgress] = useState({ total_exercises: 0, completed: 0 })
    const [fetching, setFetching] = useState(true)

    useEffect(() => {
        if (!loading && !user) router.push('/')
    }, [user, loading])

    useEffect(() => {
        if (user) {
            progressApi.global().then(r => setProgress(r.data)).finally(() => setFetching(false))
        }
    }, [user])

    if (loading || fetching) return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="w-8 h-8 border-2 border-[#00FF88] border-t-transparent rounded-full animate-spin" />
        </div>
    )

    const pythonPct = progress.total_exercises > 0 ? Math.round((progress.completed / progress.total_exercises) * 100) : 0

    return (
        <div className="min-h-screen bg-[#0a0e1a]">
            {/* Nav */}
            <nav className="border-b border-[#1f2937] bg-[#111827]/80 backdrop-blur sticky top-0 z-50">
                <div className="max-w-6xl mx-auto px-6 py-3 flex items-center justify-between">
                    <span className="font-mono font-bold text-[#00FF88] text-lg tracking-tight">devops_forge<span className="animate-pulse">_</span></span>
                    <div className="flex items-center gap-5">
                        <Link href="/progress" className="text-xs text-gray-400 hover:text-[#00FF88] transition">📊 Progress</Link>
                        <Link href="/leaderboard" className="text-xs text-gray-400 hover:text-[#00FF88] transition">🏆 Leaderboard</Link>
                        <Link href="/achievements" className="text-xs text-gray-400 hover:text-[#00FF88] transition">🏅 Badges</Link>
                        {user?.role === 'admin' && (
                            <Link href="/admin" className="text-xs text-red-400 hover:text-red-300 transition">🛡️ Admin</Link>
                        )}
                        <div className="text-right ml-2">
                            <div className="text-sm font-semibold text-[#00FF88]">{user?.total_xp || 0} XP</div>
                            <div className="text-xs text-gray-500">{user?.username}</div>
                        </div>
                        <button onClick={logout} className="text-xs text-gray-400 hover:text-white transition">Logout</button>
                    </div>
                </div>
            </nav>

            <div className="max-w-6xl mx-auto px-6 py-10">
                {/* Header */}
                <div className="mb-10">
                    <h1 className="text-3xl font-bold mb-2">
                        Welcome back, <span className="text-[#00FF88]">{user?.username}</span> 🚀
                    </h1>
                    <p className="text-gray-400">Select a learning track to continue your journey.</p>
                </div>

                {/* Track Grid */}
                <h2 className="text-xl font-semibold mb-6">Learning Tracks</h2>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

                    {/* Python - Active */}
                    <div className="relative bg-[#111827] border border-[#1f2937] rounded-xl p-6 hover:border-[#00FF88]/40 transition-all duration-200 cursor-pointer group">
                        <Link href="/dashboard/python" className="absolute inset-0" />
                        <div className="flex items-start justify-between mb-4">
                            <div>
                                <h3 className="font-bold text-lg group-hover:text-[#00FF88] transition">Python Automation</h3>
                            </div>
                            <span className="text-2xl">🐍</span>
                        </div>
                        <p className="text-sm text-gray-400 mb-6">Master Python fundamentals, API interaction, async programming, and CLI tool building.</p>

                        <div className="flex items-center justify-between text-xs text-gray-500 mb-2">
                            <span>{progress.completed}/{progress.total_exercises} exercises</span>
                            <span>{pythonPct}%</span>
                        </div>
                        <div className="h-2 bg-[#1f2937] rounded-full overflow-hidden">
                            <div className="h-full bg-[#3b82f6] rounded-full transition-all" style={{ width: `${pythonPct}%` }} />
                        </div>
                    </div>

                    {/* Bash - Disabled */}
                    <div className="relative bg-[#111827] border border-[#1f2937] opacity-60 rounded-xl p-6 cursor-not-allowed">
                        <div className="flex items-start justify-between mb-4">
                            <div>
                                <h3 className="font-bold text-lg text-gray-300">Bash Scripting</h3>
                            </div>
                            <span className="text-2xl">🐚</span>
                        </div>
                        <p className="text-sm text-gray-500 mb-6">Learn advanced shell scripting, system administration, and automation.</p>
                        <div className="mt-auto inline-block px-3 py-1 bg-[#1f2937] text-gray-400 text-xs rounded-full font-medium">Coming Soon</div>
                    </div>

                    {/* Kubernetes - Disabled */}
                    <div className="relative bg-[#111827] border border-[#1f2937] opacity-60 rounded-xl p-6 cursor-not-allowed">
                        <div className="flex items-start justify-between mb-4">
                            <div>
                                <h3 className="font-bold text-lg text-gray-300">Kubernetes</h3>
                            </div>
                            <span className="text-2xl">☸️</span>
                        </div>
                        <p className="text-sm text-gray-500 mb-6">Container orchestration, deployments, operators, and cluster management.</p>
                        <div className="mt-auto inline-block px-3 py-1 bg-[#1f2937] text-gray-400 text-xs rounded-full font-medium">Coming Soon</div>
                    </div>

                </div>
            </div>
        </div>
    )
}
