'use client'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import { authApi } from '@/lib/api'
import toast from 'react-hot-toast'

export default function LoginPage() {
    const { user, login, register } = useAuth()
    const router = useRouter()
    const [tab, setTab] = useState<'login' | 'register'>('login')
    const [form, setForm] = useState({ username: '', email: '', password: '', full_name: '' })
    const [loading, setLoading] = useState(false)

    useEffect(() => { if (user) router.push('/dashboard') }, [user])

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        setLoading(true)
        try {
            if (tab === 'login') {
                await login(form.username, form.password)
                toast.success('Welcome back!')
            } else {
                await register(form)
                toast.success('Account created!')
            }
            router.push('/dashboard')
        } catch (err: any) {
            toast.error(err?.response?.data?.detail || 'Authentication failed')
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-[#0a0e1a] p-4">
            {/* Background grid */}
            <div className="fixed inset-0 bg-[linear-gradient(rgba(0,255,136,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(0,255,136,0.03)_1px,transparent_1px)] bg-[size:60px_60px] pointer-events-none" />

            <div className="w-full max-w-md relative z-10">
                {/* Logo */}
                <div className="text-center mb-8">
                    <div className="inline-flex items-center gap-2 mb-3">
                        <span className="text-3xl">⚙️</span>
                        <h1 className="text-2xl font-bold text-[#00FF88] glow-green-text">DevOps Python Forge</h1>
                    </div>
                    <p className="text-gray-400 text-sm">Transform your DevOps skills with Python automation</p>
                </div>

                <div className="bg-[#111827] border border-[#1f2937] rounded-2xl p-8 shadow-2xl">
                    {/* Tabs */}
                    <div className="flex rounded-lg bg-[#0a0e1a] p-1 mb-6">
                        {(['login', 'register'] as const).map(t => (
                            <button key={t} onClick={() => setTab(t)}
                                className={`flex-1 py-2 rounded-md text-sm font-medium transition-all ${tab === t ? 'bg-[#00FF88] text-black' : 'text-gray-400 hover:text-white'}`}>
                                {t === 'login' ? 'Sign In' : 'Create Account'}
                            </button>
                        ))}
                    </div>

                    <form onSubmit={handleSubmit} className="space-y-4">
                        {tab === 'register' && (
                            <input className="w-full bg-[#0a0e1a] border border-[#1f2937] rounded-lg px-4 py-3 text-sm focus:border-[#00FF88] outline-none transition"
                                placeholder="Full Name (optional)" value={form.full_name}
                                onChange={e => setForm(p => ({ ...p, full_name: e.target.value }))} />
                        )}
                        <input required className="w-full bg-[#0a0e1a] border border-[#1f2937] rounded-lg px-4 py-3 text-sm focus:border-[#00FF88] outline-none transition"
                            placeholder="Username" value={form.username}
                            onChange={e => setForm(p => ({ ...p, username: e.target.value }))} />
                        {tab === 'register' && (
                            <input required type="email" className="w-full bg-[#0a0e1a] border border-[#1f2937] rounded-lg px-4 py-3 text-sm focus:border-[#00FF88] outline-none transition"
                                placeholder="Email" value={form.email}
                                onChange={e => setForm(p => ({ ...p, email: e.target.value }))} />
                        )}
                        <input required type="password" className="w-full bg-[#0a0e1a] border border-[#1f2937] rounded-lg px-4 py-3 text-sm focus:border-[#00FF88] outline-none transition"
                            placeholder="Password" value={form.password}
                            onChange={e => setForm(p => ({ ...p, password: e.target.value }))} />
                        <button type="submit" disabled={loading}
                            className="w-full bg-[#00FF88] text-black font-semibold py-3 rounded-lg hover:bg-[#00cc6a] transition disabled:opacity-60">
                            {loading ? '...' : tab === 'login' ? 'Sign In' : 'Create Account'}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}
