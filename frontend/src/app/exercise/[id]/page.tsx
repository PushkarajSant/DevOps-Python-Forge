'use client'
import { useEffect, useState, useCallback } from 'react'
import { useRouter, useParams } from 'next/navigation'
import dynamic from 'next/dynamic'
import { useAuth } from '@/context/AuthContext'
import { exercisesApi, submissionsApi } from '@/lib/api'
import toast from 'react-hot-toast'
import Link from 'next/link'

// Load Monaco with no SSR
const MonacoEditor = dynamic(() => import('@monaco-editor/react'), { ssr: false })

export default function ExercisePage() {
    const { user, loading } = useAuth()
    const router = useRouter()
    const { id } = useParams()
    const [exercise, setExercise] = useState<any>(null)
    const [code, setCode] = useState('')
    const [output, setOutput] = useState<any>(null)
    const [result, setResult] = useState<any>(null)
    const [ran, setRan] = useState(false)
    const [running, setRunning] = useState(false)
    const [submitting, setSubmitting] = useState(false)
    const [activeTab, setActiveTab] = useState<'problem' | 'hints' | 'concepts'>('problem')
    const [customInput, setCustomInput] = useState('')

    useEffect(() => { if (!loading && !user) router.push('/') }, [user, loading])

    useEffect(() => {
        if (user && id) {
            exercisesApi.getById(Number(id)).then(r => {
                setExercise(r.data)
                setCode(r.data.starter_code || '# Write your solution here\n')
            }).catch(() => router.push('/dashboard'))
        }
    }, [user, id])

    const handleRun = useCallback(async () => {
        if (!exercise) return
        setRunning(true)
        setRan(false)
        try {
            const r = await submissionsApi.run(exercise.id, code, customInput)
            setOutput(r.data)
            setRan(true)
        } catch {
            toast.error('Run failed')
        } finally { setRunning(false) }
    }, [exercise, code, customInput])

    const handleSubmit = useCallback(async () => {
        if (!exercise) return
        setSubmitting(true)
        try {
            const r = await submissionsApi.submit(exercise.id, code)
            setResult(r.data)
            if (r.data.passed) {
                toast.success(`✅ All tests passed! +${r.data.xp_awarded} XP`)
            } else {
                toast.error('Some tests failed. Check the results below.')
            }
        } catch {
            toast.error('Submission failed')
        } finally { setSubmitting(false) }
    }, [exercise, code])

    // Ctrl+Enter to run
    useEffect(() => {
        const handler = (e: KeyboardEvent) => {
            if (e.ctrlKey && e.key === 'Enter') handleRun()
            if (e.ctrlKey && e.shiftKey && e.key === 'Enter') handleSubmit()
        }
        window.addEventListener('keydown', handler)
        return () => window.removeEventListener('keydown', handler)
    }, [handleRun, handleSubmit])

    if (loading || !exercise) return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="w-8 h-8 border-2 border-[#00FF88] border-t-transparent rounded-full animate-spin" />
        </div>
    )

    return (
        <div className="h-screen flex flex-col bg-[#0a0e1a] overflow-hidden">
            {/* Nav */}
            <nav className="border-b border-[#1f2937] bg-[#111827] flex items-center justify-between px-4 py-2 shrink-0">
                <div className="flex items-center gap-3">
                    <Link href="/dashboard" className="text-gray-400 hover:text-white text-sm">← Back</Link>
                    <span className="text-gray-600">|</span>
                    <span className="font-medium text-sm truncate max-w-[200px]">{exercise.title}</span>
                    <span className={exercise.difficulty === 'easy' ? 'badge-easy' : exercise.difficulty === 'medium' ? 'badge-medium' : 'badge-hard'}>
                        {exercise.difficulty}
                    </span>
                </div>
                <div className="flex items-center gap-2">
                    <span className="text-xs text-gray-500">Attempt {exercise.attempt_count + 1}</span>
                    <span className="text-[#00FF88] text-xs font-bold">+{exercise.xp_reward} XP</span>
                    {exercise.is_completed && <span className="text-xs text-[#00FF88] bg-[#00FF88]/10 px-2 py-1 rounded-full">✓ Completed</span>}
                </div>
            </nav>

            {/* Main Split */}
            <div className="flex flex-1 overflow-hidden">
                {/* LEFT: Problem Panel */}
                <div className="w-[42%] flex flex-col border-r border-[#1f2937] overflow-hidden">
                    {/* Tabs */}
                    <div className="flex border-b border-[#1f2937] shrink-0">
                        {(['problem', 'hints', 'concepts'] as const).map(t => (
                            <button key={t} onClick={() => setActiveTab(t)}
                                className={`px-4 py-2.5 text-xs font-medium capitalize transition ${activeTab === t ? 'text-[#00FF88] border-b-2 border-[#00FF88]' : 'text-gray-400 hover:text-white'}`}>
                                {t} {t === 'hints' && exercise.unlocked_hints?.length > 0 && `(${exercise.unlocked_hints.length})`}
                            </button>
                        ))}
                    </div>

                    <div className="flex-1 overflow-y-auto p-5 text-sm">
                        {activeTab === 'problem' && (
                            <div className="space-y-4 animate-fadein">
                                {/* Scenario badge */}
                                <div className="bg-blue-900/20 border border-blue-500/20 rounded-lg p-3 text-blue-300 text-xs">
                                    <span className="font-semibold text-blue-400">💼 DevOps Context: </span>{exercise.scenario}
                                </div>

                                {/* Problem */}
                                <div>
                                    <h2 className="font-semibold text-base mb-2">{exercise.title}</h2>
                                    <div className="text-gray-300 leading-relaxed whitespace-pre-wrap text-xs">
                                        {exercise.problem_statement}
                                    </div>
                                </div>

                                {/* Visible test cases */}
                                {exercise.visible_test_cases?.length > 0 && (
                                    <div>
                                        <h3 className="font-semibold text-xs text-gray-400 mb-2 uppercase tracking-wide">Example</h3>
                                        {exercise.visible_test_cases.map((tc: any, i: number) => (
                                            <div key={i} className="space-y-2 mb-3">
                                                {tc.input_data && (
                                                    <div>
                                                        <div className="text-xs text-gray-500 mb-1">Input:</div>
                                                        <div className="terminal text-xs">{tc.input_data || '(no input)'}</div>
                                                    </div>
                                                )}
                                                <div>
                                                    <div className="text-xs text-gray-500 mb-1">Expected Output:</div>
                                                    <div className="terminal terminal-success text-xs">{tc.expected_output}</div>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                )}

                                {/* Allowed imports */}
                                {exercise.allowed_imports?.length > 0 && (
                                    <div className="text-xs text-gray-500">
                                        <span className="font-medium">Allowed imports:</span> {exercise.allowed_imports.join(', ')}
                                    </div>
                                )}
                            </div>
                        )}

                        {activeTab === 'hints' && (
                            <div className="space-y-3 animate-fadein">
                                {exercise.unlocked_hints?.length === 0 ? (
                                    <p className="text-gray-500 text-xs">Hints unlock after failed attempts. Keep trying!</p>
                                ) : (
                                    exercise.unlocked_hints.map((h: any, i: number) => (
                                        <div key={h.id} className="bg-amber-900/10 border border-amber-500/20 rounded-lg p-3">
                                            <div className="text-xs text-amber-400 font-semibold mb-1">Hint {i + 1}</div>
                                            <div className="text-xs text-gray-300 whitespace-pre-wrap">{h.content}</div>
                                        </div>
                                    ))
                                )}
                            </div>
                        )}

                        {activeTab === 'concepts' && (
                            <div className="space-y-4 animate-fadein">
                                {exercise.concepts?.length === 0 ? (
                                    <p className="text-gray-500 text-xs">Concepts unlock after 3+ failed attempts.</p>
                                ) : (
                                    exercise.concepts.map((c: any) => (
                                        <div key={c.id} className="space-y-2">
                                            <h3 className="font-semibold text-[#00FF88] text-xs">{c.title}</h3>
                                            <p className="text-gray-300 text-xs leading-relaxed">{c.explanation}</p>
                                            {c.code_example && (
                                                <div className="terminal text-xs">{c.code_example}</div>
                                            )}
                                        </div>
                                    ))
                                )}
                            </div>
                        )}
                    </div>
                </div>

                {/* RIGHT: Editor + Output */}
                <div className="flex-1 flex flex-col overflow-hidden">
                    {/* Monaco Editor */}
                    <div className="flex-1 overflow-hidden">
                        <MonacoEditor
                            height="100%"
                            language="python"
                            value={code}
                            onChange={v => setCode(v || '')}
                            theme="vs-dark"
                            options={{
                                fontSize: 14,
                                fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
                                fontLigatures: true,
                                minimap: { enabled: false },
                                scrollBeyondLastLine: false,
                                automaticLayout: true,
                                tabSize: 4,
                                insertSpaces: true,
                                wordWrap: 'on',
                                lineNumbers: 'on',
                                renderLineHighlight: 'line',
                                cursorBlinking: 'smooth',
                                smoothScrolling: true,
                            }}
                        />
                    </div>

                    {/* Custom input */}
                    <div className="border-t border-[#1f2937] bg-[#111827] px-4 py-2 flex items-center gap-3 shrink-0">
                        <span className="text-xs text-gray-500">Custom input (optional):</span>
                        <textarea
                            className="flex-1 bg-[#0a0e1a] border border-[#1f2937] rounded px-2 py-1 text-xs font-mono resize-none focus:border-[#00FF88] outline-none"
                            rows={1}
                            placeholder="stdin..."
                            value={customInput}
                            onChange={e => setCustomInput(e.target.value)}
                        />
                    </div>

                    {/* Action bar */}
                    <div className="border-t border-[#1f2937] bg-[#111827] px-4 py-3 flex items-center gap-3 shrink-0">
                        <button onClick={handleRun} disabled={running}
                            className="px-5 py-2 bg-[#1f2937] hover:bg-[#374151] text-white text-sm rounded-lg transition disabled:opacity-50 flex items-center gap-2">
                            {running ? <span className="w-3 h-3 border border-white border-t-transparent rounded-full animate-spin" /> : '▶'}
                            Run <kbd className="text-xs text-gray-500 ml-1">Ctrl+Enter</kbd>
                        </button>
                        <button onClick={handleSubmit} disabled={submitting}
                            className="px-5 py-2 bg-[#00FF88] text-black font-semibold text-sm rounded-lg hover:bg-[#00cc6a] transition disabled:opacity-50 flex items-center gap-2">
                            {submitting ? <span className="w-3 h-3 border border-black border-t-transparent rounded-full animate-spin" /> : '✓'}
                            Submit
                        </button>
                        <div className="ml-auto flex items-center gap-4">
                            <span className="text-xs text-gray-600">Ctrl+Shift+Enter = Submit</span>
                            {result?.passed && exercise?.next_exercise_id && (
                                <Link href={`/exercise/${exercise.next_exercise_id}`}
                                    className="px-4 py-2 bg-[#3b82f6] hover:bg-[#2563eb] text-white font-semibold text-sm rounded-lg transition flex items-center gap-2 shadow-[0_0_15px_rgba(59,130,246,0.5)]">
                                    Next Exercise ➔
                                </Link>
                            )}
                            {result?.passed && !exercise?.next_exercise_id && (
                                <Link href="/dashboard"
                                    className="px-4 py-2 bg-[#3b82f6] hover:bg-[#2563eb] text-white font-semibold text-sm rounded-lg transition flex items-center gap-2 shadow-[0_0_15px_rgba(59,130,246,0.5)]">
                                    Back to Dashboard ➔
                                </Link>
                            )}
                        </div>
                    </div>

                    {/* Output Panel */}
                    {(ran || result) && (
                        <div className="border-t border-[#1f2937] bg-[#0a0e1a] h-48 overflow-y-auto p-4 shrink-0">
                            {/* Run output */}
                            {ran && !result && output && (
                                <div>
                                    <div className="text-xs text-gray-500 mb-1">Run output ({output.execution_time_ms}ms):</div>
                                    <div className={`terminal text-xs ${output.error ? 'terminal-error' : 'terminal-success'}`}>
                                        {output.error || output.stdout || '(no output)'}
                                    </div>
                                </div>
                            )}

                            {/* Submit result */}
                            {result && (
                                <div className="space-y-3">
                                    <div className={`text-sm font-bold ${result.passed ? 'text-[#00FF88]' : 'text-red-400'}`}>
                                        {result.passed ? `✅ All ${result.test_results.length} tests passed! +${result.xp_awarded} XP` : '❌ Some tests failed'}
                                    </div>

                                    {result.failure_message && (
                                        <div className="terminal terminal-warning text-xs">{result.failure_message}</div>
                                    )}

                                    <div className="space-y-1">
                                        {result.test_results.map((t: any, i: number) => (
                                            <div key={i} className="flex items-center gap-2 text-xs">
                                                <span className={t.passed ? 'text-[#00FF88]' : 'text-red-400'}>{t.passed ? '✓' : '✗'}</span>
                                                <span className="text-gray-400">{t.is_hidden ? 'Hidden test' : `Test ${i + 1}`}</span>
                                                <span className="text-gray-600">{t.execution_time_ms}ms</span>
                                                {!t.passed && t.feedback && !t.is_hidden && (
                                                    <span className="text-red-400 truncate">{t.feedback.split('\n')[0]}</span>
                                                )}
                                            </div>
                                        ))}
                                    </div>

                                    {/* New total XP */}
                                    <div className="text-xs text-gray-500">Total XP: {result.total_xp}</div>
                                </div>
                            )}
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}
