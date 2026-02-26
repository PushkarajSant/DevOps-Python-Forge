'use client'
import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import { levelsApi } from '@/lib/api'
import Link from 'next/link'

export default function LevelPage() {
    const { user, loading } = useAuth()
    const router = useRouter()
    const { levelNumber } = useParams()
    const [exercises, setExercises] = useState<any[]>([])
    const [fetching, setFetching] = useState(true)

    useEffect(() => { if (!loading && !user) router.push('/') }, [user, loading])

    useEffect(() => {
        if (user) {
            levelsApi.getExercises(Number(levelNumber)).then(r => setExercises(r.data))
                .catch(() => router.push('/dashboard'))
                .finally(() => setFetching(false))
        }
    }, [user, levelNumber])

    if (loading || fetching) return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="w-8 h-8 border-2 border-[#00FF88] border-t-transparent rounded-full animate-spin" />
        </div>
    )

    const completed = exercises.filter(e => e.is_completed).length

    return (
        <div className="min-h-screen bg-[#0a0e1a]">
            <nav className="border-b border-[#1f2937] bg-[#111827]/80 backdrop-blur sticky top-0 z-50">
                <div className="max-w-4xl mx-auto px-6 py-3 flex items-center gap-4">
                    <Link href="/dashboard" className="text-gray-400 hover:text-white transition text-sm">← Dashboard</Link>
                    <span className="text-gray-600">|</span>
                    <span className="text-[#00FF88] font-semibold text-sm">Level {levelNumber}</span>
                </div>
            </nav>

            <div className="max-w-4xl mx-auto px-6 py-10">
                <div className="flex items-center justify-between mb-8">
                    <h1 className="text-2xl font-bold">Level {levelNumber} Exercises</h1>
                    <span className="text-sm text-gray-400">{completed}/{exercises.length} completed</span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {exercises.map((ex, i) => (
                        <Link key={ex.id} href={`/dashboard/python/${ex.id}`}
                            className={`block bg-[#1f2937] p-4 rounded-lg border border-[#374151] hover:border-[#00FF88] transition cursor-pointer group ${ex.is_completed ? 'border-[#00FF88]/30 bg-[#00FF88]/5' : 'border-[#1f2937] bg-[#111827] hover:border-[#00FF88]/30'}`}>
                            <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-mono font-bold ${ex.is_completed ? 'bg-[#00FF88] text-black' : 'bg-[#1f2937] text-gray-400'}`}>
                                {ex.is_completed ? '✓' : i + 1}
                            </div>
                            <div className="flex-1 min-w-0">
                                <div className="font-medium group-hover:text-[#00FF88] transition truncate">{ex.title}</div>
                                <div className="flex items-center gap-2 mt-1">
                                    <span className={
                                        ex.difficulty === 'easy' ? 'badge-easy' :
                                            ex.difficulty === 'medium' ? 'badge-medium' : 'badge-hard'
                                    }>{ex.difficulty}</span>
                                    {ex.tags?.map((t: string) => (
                                        <span key={t} className="text-xs text-gray-500 bg-[#1f2937] px-2 py-0.5 rounded-full">{t}</span>
                                    ))}
                                </div>
                            </div>
                            <div className="text-right shrink-0">
                                <div className="text-[#00FF88] text-sm font-semibold">+{ex.xp_reward} XP</div>
                                {ex.attempts > 0 && <div className="text-xs text-gray-500">{ex.attempts} attempts</div>}
                            </div>
                        </Link>
                    ))}
                </div>
            </div>
        </div>
    )
}
