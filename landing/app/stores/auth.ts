import { defineStore } from 'pinia'
import type { User } from '../types/auth'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null as User | null,
        accessToken: typeof window !== 'undefined' ? localStorage.getItem('access_token') : null,
        refreshToken: typeof window !== 'undefined' ? localStorage.getItem('refresh_token') : null,
        isLoading: false,
        isInitialized: false
    }),

    getters: {
        isAuthenticated: (state) => !!state.accessToken,
        isPaid: (state) => state.user?.subscription_tier === 'paid'
    },

    actions: {
        setTokens(access: string, refresh: string) {
            this.accessToken = access
            this.refreshToken = refresh
            if (typeof window !== 'undefined') {
                localStorage.setItem('access_token', access)
                localStorage.setItem('refresh_token', refresh)
            }
        },

        clearAuth() {
            this.user = null
            this.accessToken = null
            this.refreshToken = null
            if (typeof window !== 'undefined') {
                localStorage.removeItem('access_token')
                localStorage.removeItem('refresh_token')
            }
        },

        async init() {
            if (this.isInitialized) return
            if (this.accessToken) {
                await this.fetchUser()
            }
            this.isInitialized = true
        },

        async fetchUser() {
            if (!this.accessToken) return
            const config = useRuntimeConfig()
            try {
                const response = await fetch(`${config.public.apiBase}/auth/me`, {
                    headers: {
                        'Authorization': `Bearer ${this.accessToken}`
                    }
                })

                if (response.ok) {
                    const data = await response.json()
                    this.user = data.data
                } else if (response.status === 401) {
                    // Token expired, try refresh
                    const refreshed = await this.refreshTokens()
                    if (refreshed) {
                        await this.fetchUser()
                    } else {
                        this.clearAuth()
                    }
                }
            } catch (error) {
                console.error('Failed to fetch user:', error)
            }
        },

        async refreshTokens() {
            if (!this.refreshToken) return false
            const config = useRuntimeConfig()
            try {
                const response = await fetch(`${config.public.apiBase}/auth/refresh`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ refresh_token: this.refreshToken })
                })

                if (response.ok) {
                    const data = await response.json()
                    this.setTokens(data.data.access_token, data.data.refresh_token)
                    return true
                }
            } catch (error) {
                console.error('Token refresh failed:', error)
            }
            this.clearAuth()
            return false
        },

        logout() {
            this.clearAuth()
            window.location.reload()
        }
    }
})
