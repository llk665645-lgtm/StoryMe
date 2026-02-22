import { defineStore } from 'pinia'
import type { User } from '../types/auth'
import { authApi } from '../api/auth'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null as User | null,
        accessToken: typeof window !== 'undefined' ? localStorage.getItem('access_token') : null,
        refreshToken: typeof window !== 'undefined' ? localStorage.getItem('refresh_token') : null,
        isLoading: false,
    }),

    getters: {
        isAuthenticated: (state) => !!state.accessToken,
    },

    actions: {
        async login(credentials: URLSearchParams) {
            this.isLoading = true
            try {
                const { data } = await authApi.login(credentials)
                this.setTokens(data.access_token, data.refresh_token)
                await this.fetchUser()
            } finally {
                this.isLoading = false
            }
        },

        async register(userData: any) {
            this.isLoading = true
            try {
                const { data } = await authApi.register(userData)
                this.setTokens(data.access_token, data.refresh_token)
                await this.fetchUser()
            } finally {
                this.isLoading = false
            }
        },

        async fetchUser() {
            if (!this.accessToken) return
            try {
                const { data } = await authApi.getMe(this.accessToken)
                this.user = data
            } catch (error) {
                this.logout()
            }
        },

        setTokens(access: string, refresh: string) {
            this.accessToken = access
            this.refreshToken = refresh
            if (typeof window !== 'undefined') {
                localStorage.setItem('access_token', access)
                localStorage.setItem('refresh_token', refresh)
            }
        },

        logout() {
            this.user = null
            this.accessToken = null
            this.refreshToken = null
            if (typeof window !== 'undefined') {
                localStorage.removeItem('access_token')
                localStorage.removeItem('refresh_token')
            }
            navigateTo('/login')
        }
    }
})
