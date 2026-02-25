'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import { progressApi, levelsApi } from '@/lib/api'
import Link from 'next/link'

export default function ProgressPage() {
    const { user, loading } = useAuth()
    const router = useRouter()
    const [dashboard, setDashboard] = useState<any>(null)
    const [levels, setLevels] = useState<any[]>([])
    const [fetching, setFetching] = useState(true)

    useEffect(() => { if (!loading && !user) router.push('/') }, [user, loading])

    useEffect(() => {
        if (user) {
            Promise.all([progressApi.dashboard(), levelsApi.getAll()])
                .then(([d, l]) => {
                    setDashboard(d.data)
                    setLevels(l.data)
                })
                .finally(() => setFetching(false))
        }
    }, [user])

    if (loading || fetching) return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="w-8 h-8 border-2 border-[#00FF88] border-t-transparent rounded-full animate-spin" />
        </div>
    )

    const u = dashboard?.user
    const totalExercises = levels.reduce((sum: number, l: any) => sum + (l.exercise_count || 0), 0)
    const completedExercises = levels.reduce((sum: number, l: any) => sum + (l.completed_count || 0), 0)
    const overallPct = totalExercises > 0 ? Math.round((completedExercises / totalExercises) * 100) : 0

    return (
        <div className="min-h-screen bg-[#0a0e1a]">
            <nav className="border-b border-[#1f2937] bg-[#111827]/80 backdrop-blur sticky top-0 z-50">
                <div className="max-w-5xl mx-auto px-6 py-3 flex items-center gap-4">
                    <Link href="/dashboard" className="text-gray-400 hover:text-white transition text-sm">← Dashboard</Link>
                    <span className="text-gray-600">|</span>
                    <span className="text-[#00FF88] font-semibold text-sm">Progress & Stats</span>
                </div>
            </nav>

            <div className="max-w-5xl mx-auto px-6 py-10 space-y-8">
                {/* Summary Cards */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    {[
                        { label: 'Total XP', value: u?.total_xp || 0, icon: '⚡', color: '#00FF88' },
                        { label: 'Current Level', value: u?.current_level || 0, icon: '📊', color: '#3b82f6' },
                        { label: 'Streak', value: `${u?.streak_days || 0} days`, icon: '🔥', color: '#f59e0b' },
                        { label: 'Exercises Done', value: `${completedExercises}/${totalExercises}`, icon: '✅', color: '#10b981' },
                    ].map((card) => (
                        <div key={card.label} className="bg-[#111827] border border-[#1f2937] rounded-xl p-5 text-center">
                            <div className="text-2xl mb-2">{card.icon}</div>
                            <div className="text-2xl font-bold" style={{ color: card.color }}>{card.value}</div>
                            <div className="text-xs text-gray-500 mt-1">{card.label}</div>
                        </div>
                    ))}
                </div>

                {/* Overall Progress */}
                <div className="bg-[#111827] border border-[#1f2937] rounded-xl p-6">
                    <h2 className="font-semibold mb-4">Overall Completion</h2>
                    <div className="flex items-center gap-4">
                        <div className="flex-1 h-4 bg-[#1f2937] rounded-full overflow-hidden">
                            <div className="h-full bg-gradient-to-r from-[#00FF88] to-[#3b82f6] rounded-full transition-all duration-700"
                                style={{ width: `${overallPct}%` }} />
                        </div>
                        <span className="text-sm font-bold text-[#00FF88]">{overallPct}%</span>
                    </div>
                    <p className="text-xs text-gray-500 mt-2">{completedExercises} of {totalExercises} exercises completed</p>
                </div>

                {/* Per-Level Breakdown */}
                <h2 className="font-semibold text-lg">Level Breakdown</h2>
                <div className="space-y-3">
                    {levels.map((level) => {
                        const pct = level.exercise_count > 0 ? Math.round((level.completed_count / level.exercise_count) * 100) : 0
                        return (
                            <div key={level.id} className="bg-[#111827] border border-[#1f2937] rounded-xl p-4">
                                <div className="flex items-center justify-between mb-2">
                                    <div className="flex items-center gap-3">
                                        <span className="text-xs text-gray-500 font-mono">L{level.level_number}</span>
                                        <span className="font-medium text-sm">{level.title}</span>
                                        <span className={level.is_unlocked ? 'text-xs text-[#00FF88]' : 'text-xs text-gray-600'}>
                                            {level.is_unlocked ? '🔓' : '🔒'}
                                        </span>
                                    </div>
                                    <span className="text-xs text-gray-500">{level.completed_count}/{level.exercise_count}</span>
                                </div>
                                <div className="h-2 bg-[#1f2937] rounded-full overflow-hidden">
                                    <div className="h-full rounded-full transition-all duration-500"
                                        style={{ width: `${pct}%`, backgroundColor: level.color || '#00FF88' }} />
                                </div>
                            </div>
                        )
                    })}
                </div>

                {/* Activity Heatmap placeholder */}
                <div className="bg-[#111827] border border-[#1f2937] rounded-xl p-6">
                    <h2 className="font-semibold mb-4">Coding Activity</h2>
                    <div className="grid grid-cols-7 gap-1">
                        {Array.from({ length: 49 }).map((_, i) => {
                            const intensity = Math.random()
                            return (
                                <div
                                    key={i}
                                    className="w-full aspect-square rounded-sm"
                                    style={{
                                        backgroundColor: intensity > 0.7 ? '#00FF88' : intensity > 0.4 ? '#00FF8855' : intensity > 0.15 ? '#00FF8822' : '#1f2937',
                                    }}
                                    title={`Day ${i + 1}`}
                                />
                            )
                        })}
                    </div>
                    <div className="flex justify-between mt-2 text-xs text-gray-600">
                        <span>7 weeks ago</span>
                        <span>Today</span>
                    </div>
                </div>
            </div>
        </div>
    )
}
