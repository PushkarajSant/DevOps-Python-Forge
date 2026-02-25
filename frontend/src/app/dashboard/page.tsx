'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import { levelsApi } from '@/lib/api'
import Link from 'next/link'

export default function DashboardPage() {
    const { user, logout, loading } = useAuth()
    const router = useRouter()
    const [levels, setLevels] = useState<any[]>([])
    const [fetching, setFetching] = useState(true)

    useEffect(() => {
        if (!loading && !user) router.push('/')
    }, [user, loading])

    useEffect(() => {
        if (user) {
            levelsApi.getAll().then(r => setLevels(r.data)).finally(() => setFetching(false))
        }
    }, [user])

    if (loading || fetching) return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="w-8 h-8 border-2 border-[#00FF88] border-t-transparent rounded-full animate-spin" />
        </div>
    )

    const totalXP = user?.total_xp || 0
    const nextLevelXP = levels.find(l => !l.is_unlocked)?.unlock_xp_required || 9999

    return (
        <div className="min-h-screen bg-[#0a0e1a]">
            {/* Nav */}
            <nav className="border-b border-[#1f2937] bg-[#111827]/80 backdrop-blur sticky top-0 z-50">
                <div className="max-w-6xl mx-auto px-6 py-3 flex items-center justify-between">
                    <span className="text-[#00FF88] font-bold text-lg">⚙️ DevOps Python Forge</span>
                    <div className="flex items-center gap-5">
                        <Link href="/progress" className="text-xs text-gray-400 hover:text-[#00FF88] transition">📊 Progress</Link>
                        <Link href="/leaderboard" className="text-xs text-gray-400 hover:text-[#00FF88] transition">🏆 Leaderboard</Link>
                        <Link href="/achievements" className="text-xs text-gray-400 hover:text-[#00FF88] transition">🏅 Badges</Link>
                        {user?.role === 'admin' && (
                            <Link href="/admin" className="text-xs text-red-400 hover:text-red-300 transition">🛡️ Admin</Link>
                        )}
                        <div className="text-right ml-2">
                            <div className="text-sm font-semibold text-[#00FF88]">{totalXP} XP</div>
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
                    <p className="text-gray-400">Total XP: {totalXP} · Level {user?.current_level} · {user?.streak_days} day streak 🔥</p>
                    {/* XP progress to next level */}
                    <div className="mt-4 flex items-center gap-3">
                        <div className="flex-1 h-2 bg-[#1f2937] rounded-full overflow-hidden">
                            <div className="h-full bg-[#00FF88] transition-all duration-500"
                                style={{ width: `${Math.min((totalXP / nextLevelXP) * 100, 100)}%` }} />
                        </div>
                        <span className="text-xs text-gray-500">{totalXP}/{nextLevelXP} XP</span>
                    </div>
                </div>

                {/* Level Grid */}
                <h2 className="text-xl font-semibold mb-6">Learning Path</h2>
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                    {levels.map((level) => {
                        const pct = level.total > 0 ? Math.round((level.completed_count / level.exercise_count) * 100) : 0
                        return (
                            <div key={level.id}
                                className={`relative bg-[#111827] border rounded-xl p-5 transition-all duration-200 ${level.is_unlocked ? 'border-[#1f2937] hover:border-[#00FF88]/40 cursor-pointer group' : 'border-[#1f2937] opacity-50 cursor-not-allowed'}`}>
                                {level.is_unlocked ? (
                                    <Link href={`/levels/${level.level_number}`} className="absolute inset-0" />
                                ) : null}

                                <div className="flex items-start justify-between mb-3">
                                    <div>
                                        <div className="text-xs text-gray-500 mb-1">Level {level.level_number}</div>
                                        <h3 className="font-semibold text-sm group-hover:text-[#00FF88] transition" style={{ color: level.is_unlocked ? undefined : '#9ca3af' }}>
                                            {level.title}
                                        </h3>
                                    </div>
                                    <span className="text-lg">{level.is_unlocked ? '🔓' : '🔒'}</span>
                                </div>

                                <p className="text-xs text-gray-500 line-clamp-2 mb-4">{level.description}</p>

                                <div className="flex items-center justify-between text-xs text-gray-500 mb-2">
                                    <span>{level.completed_count}/{level.exercise_count} exercises</span>
                                    <span>{pct}%</span>
                                </div>
                                <div className="h-1.5 bg-[#1f2937] rounded-full overflow-hidden">
                                    <div className="h-full rounded-full transition-all" style={{ width: `${pct}%`, backgroundColor: level.color }} />
                                </div>

                                {!level.is_unlocked && (
                                    <div className="mt-3 text-xs text-amber-400">🔒 Requires {level.unlock_xp_required} XP</div>
                                )}
                            </div>
                        )
                    })}
                </div>
            </div>
        </div>
    )
}
