'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import api from '@/lib/api'
import Link from 'next/link'
import toast from 'react-hot-toast'

export default function AchievementsPage() {
    const { user, loading } = useAuth()
    const router = useRouter()
    const [badges, setBadges] = useState<any[]>([])
    const [fetching, setFetching] = useState(true)

    useEffect(() => { if (!loading && !user) router.push('/') }, [user, loading])

    useEffect(() => {
        if (user) {
            api.get('/api/achievements/available').then(r => setBadges(r.data)).finally(() => setFetching(false))
        }
    }, [user])

    if (loading || fetching) return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="w-8 h-8 border-2 border-[#00FF88] border-t-transparent rounded-full animate-spin" />
        </div>
    )

    const earned = badges.filter(b => b.earned)
    const locked = badges.filter(b => !b.earned)

    return (
        <div className="min-h-screen bg-[#0a0e1a]">
            <nav className="border-b border-[#1f2937] bg-[#111827]/80 backdrop-blur sticky top-0 z-50">
                <div className="max-w-4xl mx-auto px-6 py-3 flex items-center gap-4">
                    <Link href="/dashboard" className="text-gray-400 hover:text-white transition text-sm">← Dashboard</Link>
                    <span className="text-gray-600">|</span>
                    <span className="text-[#00FF88] font-semibold text-sm">🏅 Achievements</span>
                </div>
            </nav>

            <div className="max-w-4xl mx-auto px-6 py-10 space-y-8">
                <div className="flex items-center justify-between">
                    <h1 className="text-2xl font-bold">Achievements</h1>
                    <span className="text-sm text-gray-400">{earned.length}/{badges.length} earned</span>
                </div>

                {/* Earned Badges */}
                {earned.length > 0 && (
                    <div>
                        <h2 className="text-sm font-semibold text-[#00FF88] mb-3 uppercase tracking-wide">Earned</h2>
                        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                            {earned.map(b => (
                                <div key={b.badge_type} className="bg-[#111827] border border-[#00FF88]/30 rounded-xl p-4 text-center glow-green animate-fadein">
                                    <div className="text-3xl mb-2">{b.badge_name.split(' ')[0]}</div>
                                    <div className="font-semibold text-xs text-[#00FF88]">{b.badge_name.split(' ').slice(1).join(' ')}</div>
                                    <div className="text-xs text-gray-500 mt-1">{b.description}</div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

                {/* Locked Badges */}
                <div>
                    <h2 className="text-sm font-semibold text-gray-500 mb-3 uppercase tracking-wide">Locked</h2>
                    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                        {locked.map(b => (
                            <div key={b.badge_type} className="bg-[#111827] border border-[#1f2937] rounded-xl p-4 text-center opacity-50">
                                <div className="text-3xl mb-2 grayscale">🔒</div>
                                <div className="font-semibold text-xs text-gray-400">{b.badge_name.split(' ').slice(1).join(' ')}</div>
                                <div className="text-xs text-gray-600 mt-1">{b.description}</div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}
