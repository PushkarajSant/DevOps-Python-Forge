'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'
import { useAuth } from '@/context/AuthContext'

export default function LandingPage() {
    const { user, loading } = useAuth()
    const [mounted, setMounted] = useState(false)

    useEffect(() => {
        setMounted(true)
    }, [])

    return (
        <div className="min-h-screen bg-[#0a0e1a] text-gray-200 font-sans selection:bg-[#00FF88]/30 overflow-x-hidden">
            {/* Background Texture */}
            <div className="fixed inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:64px_64px] pointer-events-none opacity-50" />
            <div className="fixed inset-0 bg-gradient-to-b from-transparent via-[#0a0e1a]/80 to-[#0a0e1a] pointer-events-none" />

            {/* Navigation */}
            <nav className="relative z-50 border-b border-[#1f2937] bg-[#0a0e1a]/80 backdrop-blur top-0">
                <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
                    <div className="font-mono font-bold text-[#00FF88] tracking-tight">devops_forge<span className="animate-pulse">_</span></div>
                    {mounted && !loading && (
                        <div className="flex items-center gap-4">
                            {user ? (
                                <Link href="/dashboard" className="text-sm font-medium text-white hover:text-[#00FF88] transition">
                                    Dashboard →
                                </Link>
                            ) : (
                                <Link href="/login" className="text-sm font-medium text-gray-400 hover:text-white transition">
                                    Login
                                </Link>
                            )}
                        </div>
                    )}
                </div>
            </nav>

            <main className="relative z-10">
                {/* 1. Hero Section */}
                <section className="pt-32 pb-24 px-6">
                    <div className="max-w-4xl mx-auto text-center">
                        <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight text-white mb-6 leading-tight">
                            Practice Python for DevOps in a <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#00FF88] to-[#3b82f6]">Real Sandbox</span>
                        </h1>
                        <p className="text-lg md:text-xl text-gray-400 mb-10 max-w-2xl mx-auto font-light leading-relaxed">
                            Hands-on labs focused on automation, log parsing, cloud scripting, and Kubernetes workflows.
                        </p>

                        {/* CTAs */}
                        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
                            {mounted && !loading ? (
                                user ? (
                                    <Link href="/dashboard"
                                        className="px-8 py-3.5 bg-[#00FF88] text-black font-semibold rounded hover:bg-[#00cc6a] transition-all flex items-center gap-2">
                                        Go to Dashboard
                                    </Link>
                                ) : (
                                    <>
                                        <Link href="/login"
                                            className="px-8 py-3.5 bg-[#00FF88] text-black font-semibold rounded hover:bg-[#00cc6a] transition-all flex items-center gap-2">
                                            Get Started
                                        </Link>
                                        <Link href="/login"
                                            className="px-8 py-3.5 bg-transparent border border-[#374151] text-white font-medium rounded hover:bg-[#1f2937] transition-all flex items-center gap-2">
                                            Login
                                        </Link>
                                    </>
                                )
                            ) : (
                                <div className="h-12" /> // placeholder during load
                            )}
                        </div>
                    </div>
                </section>

                {/* 2. What Makes This Different */}
                <section className="py-24 px-6 border-y border-[#1f2937] bg-[#111827]/30">
                    <div className="max-w-6xl mx-auto">
                        <div className="grid md:grid-cols-3 gap-6">

                            {/* Python Active */}
                            <div className="p-8 border border-[#1f2937] bg-[#0a0e1a] rounded-lg">
                                <div className="text-3xl mb-4">🐍</div>
                                <h3 className="text-xl font-bold text-white mb-3">Python Automation Labs</h3>
                                <p className="text-sm text-gray-400 mb-4">Solve real DevOps problems:</p>
                                <ul className="space-y-2 font-mono text-xs text-gray-500">
                                    <li className="flex gap-2"><span>&gt;</span> Parse production logs</li>
                                    <li className="flex gap-2"><span>&gt;</span> Handle retries</li>
                                    <li className="flex gap-2"><span>&gt;</span> Process infrastructure data</li>
                                </ul>
                            </div>

                            {/* Bash Upcoming */}
                            <div className="p-8 border border-[#1f2937] bg-[#0a0e1a]/50 rounded-lg relative overflow-hidden group">
                                <div className="absolute top-4 right-4 text-[10px] uppercase tracking-widest font-bold text-[#3b82f6] bg-[#3b82f6]/10 px-2 py-1 rounded">Beta</div>
                                <div className="text-3xl mb-4 opacity-50">🖥</div>
                                <h3 className="text-xl font-bold text-gray-300 mb-3">Bash & Shell</h3>
                                <p className="text-sm text-gray-500">Practice CLI pipelines and system scripting.</p>
                            </div>

                            {/* K8s Upcoming */}
                            <div className="p-8 border border-[#1f2937] bg-[#0a0e1a]/50 rounded-lg relative overflow-hidden group">
                                <div className="absolute top-4 right-4 text-[10px] uppercase tracking-widest font-bold text-[#00FF88] bg-[#00FF88]/10 px-2 py-1 rounded">Coming Soon</div>
                                <div className="text-3xl mb-4 opacity-50">☸</div>
                                <h3 className="text-xl font-bold text-gray-300 mb-3">Kubernetes Labs</h3>
                                <p className="text-sm text-gray-500">Debug YAML, validate configs, simulate real cluster issues.</p>
                            </div>

                        </div>
                    </div>
                </section>

                {/* 3. How It Works */}
                <section className="py-32 px-6">
                    <div className="max-w-4xl mx-auto text-center mb-16">
                        <h2 className="text-3xl font-bold text-white mb-4">How It Works</h2>
                    </div>
                    <div className="max-w-4xl mx-auto grid md:grid-cols-3 gap-12 text-center">
                        <div>
                            <div className="w-12 h-12 rounded border border-[#1f2937] bg-[#111827] flex items-center justify-center mx-auto mb-6 text-xl font-mono text-[#00FF88]">1</div>
                            <h4 className="font-semibold text-white mb-2">Choose a lab</h4>
                        </div>
                        <div>
                            <div className="w-12 h-12 rounded border border-[#1f2937] bg-[#111827] flex items-center justify-center mx-auto mb-6 text-xl font-mono text-[#00FF88]">2</div>
                            <h4 className="font-semibold text-white mb-2">Write code in a sandbox</h4>
                        </div>
                        <div>
                            <div className="w-12 h-12 rounded border border-[#1f2937] bg-[#111827] flex items-center justify-center mx-auto mb-6 text-xl font-mono text-[#00FF88]">3</div>
                            <h4 className="font-semibold text-white mb-2">Run & validate instantly</h4>
                        </div>
                    </div>
                </section>

                {/* 4. Who This Is For */}
                <section className="py-24 px-6 border-t border-[#1f2937] bg-[#111827]/30">
                    <div className="max-w-4xl mx-auto text-center">
                        <h2 className="text-2xl font-bold text-white mb-8">Built specifically for</h2>
                        <div className="flex flex-wrap justify-center gap-4">
                            <span className="px-5 py-2 rounded-full border border-[#374151] bg-[#0a0e1a] text-sm text-gray-300">DevOps Engineers</span>
                            <span className="px-5 py-2 rounded-full border border-[#374151] bg-[#0a0e1a] text-sm text-gray-300">SREs</span>
                            <span className="px-5 py-2 rounded-full border border-[#374151] bg-[#0a0e1a] text-sm text-gray-300">Cloud Engineers</span>
                            <span className="px-5 py-2 rounded-full border border-[#374151] bg-[#0a0e1a] text-sm text-gray-300">System Administrators</span>
                        </div>
                    </div>
                </section>
            </main>

            {/* 5. Minimal Footer */}
            <footer className="border-t border-[#1f2937] py-8 px-6 relative z-10 bg-[#0a0e1a]">
                <div className="max-w-6xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-4">
                    <div className="text-xs text-gray-500 font-mono">
                        Built for DevOps Engineers
                    </div>
                    <div className="flex items-center gap-6 text-xs text-gray-500">
                        <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="hover:text-white transition">GitHub</a>
                        <a href="mailto:support@example.com" className="hover:text-white transition">Contact</a>
                        <span className="text-[#374151]">|</span>
                        <span>v0.1 MVP</span>
                    </div>
                </div>
            </footer>
        </div>
    )
}
