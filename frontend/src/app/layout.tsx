import type { Metadata } from 'next'
import './globals.css'
import { Toaster } from 'react-hot-toast'
import { AuthProvider } from '@/context/AuthContext'

export const metadata: Metadata = {
    title: 'DevOps Python Forge',
    description: 'Transform DevOps engineers into Python automation experts through exercise-driven learning',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en">
            <body className="bg-[#0a0e1a] text-gray-100 antialiased">
                <AuthProvider>
                    {children}
                    <Toaster
                        position="top-right"
                        toastOptions={{
                            style: {
                                background: '#111827',
                                color: '#e5e7eb',
                                border: '1px solid #1f2937',
                            },
                        }}
                    />
                </AuthProvider>
            </body>
        </html>
    )
}
