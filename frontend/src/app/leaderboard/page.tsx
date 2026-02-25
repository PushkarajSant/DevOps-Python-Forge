'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import { usersApi } from '@/lib/api'
import Link from 'next/link'

export default function LeaderboardPage() {
    const { user, loading } = useAuth()
    const router = useRouter()
    const [leaders, setLeaders] = useState<any[]>([])
    const [fetching, setFetching] = useState(true)

    useEffect(() => { if (!loading && !user) router.push('/') }, [user, loading])

    useEffect(() => {
        if (user) {
            usersApi.leaderboard().then(r => setLeaders(r.data)).finally(() => setFetching(false))
        }
    }, [user])

    if (loading || fetching) return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="w-8 h-8 border-2 border-[#00FF88] border-t-transparent rounded-full animate-spin" />
        </div>
    )

    const medals = ['🥇', '🥈', '🥉']

    return (
        <div className="min-h-screen bg-[#0a0e1a]">
            <nav className="border-b border-[#1f2937] bg-[#111827]/80 backdrop-blur sticky top-0 z-50">
                <div className="max-w-3xl mx-auto px-6 py-3 flex items-center gap-4">
                    <Link href="/dashboard" className="text-gray-400 hover:text-white transition text-sm">← Dashboard</Link>
                    <span className="text-gray-600">|</span>
                    <span className="text-[#00FF88] font-semibold text-sm">🏆 Leaderboard</span>
                </div>
            </nav>

            <div className="max-w-3xl mx-auto px-6 py-10">
                <h1 className="text-2xl font-bold mb-6">Global Leaderboard</h1>

                <div className="space-y-2">
                    {leaders.map((leader, i) => {
                        const isMe = leader.username === user?.username
                        return (
                            <div key={leader.id}
                                className={`flex items-center gap-4 p-4 rounded-xl border transition-all ${isMe ? 'border-[#00FF88]/40 bg-[#00FF88]/5' : 'border-[#1f2937] bg-[#111827]'}`}>
                                <div className="w-10 text-center">
                                    {i < 3 ? (
                                        <span className="text-2xl">{medals[i]}</span>
                                    ) : (
                                        <span className="text-gray-500 font-mono text-sm">#{i + 1}</span>
                                    )}
                                </div>
                                <div className="flex-1">
                                    <div className="flex items-center gap-2">
                                        <span className={`font-semibold ${isMe ? 'text-[#00FF88]' : 'text-white'}`}>
                                            {leader.username}
                                        </span>
                                        {isMe && <span className="text-xs bg-[#00FF88]/20 text-[#00FF88] px-2 py-0.5 rounded-full">You</span>}
                                    </div>
                                    <div className="text-xs text-gray-500">Level {leader.current_level} · {leader.streak_days}d streak</div>
                                </div>
                                <div className="text-right">
                                    <div className="text-[#00FF88] font-bold">{leader.total_xp} XP</div>
                                    <div className="text-xs text-gray-500">{leader.total_submissions} submissions</div>
                                </div>
                            </div>
                        )
                    })}

                    {leaders.length === 0 && (
                        <div className="text-center text-gray-500 py-10">No users yet. Be the first!</div>
                    )}
                </div>
            </div>
        </div>
    )
}
