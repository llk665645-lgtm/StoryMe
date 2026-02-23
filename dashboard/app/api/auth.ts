import type { User, Token, AuthResponse, UserResponse } from '../types/auth'

const API_BASE_URL = 'http://127.0.0.1:8000'

export const authApi = {
    async register(data: any): Promise<AuthResponse> {
        return $fetch<AuthResponse>(`${API_BASE_URL}/auth/register`, {
            method: 'POST',
            body: data
        })
    },

    async login(credentials: URLSearchParams): Promise<AuthResponse> {
        return $fetch<AuthResponse>(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            body: credentials,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
    },

    async getMe(token: string): Promise<UserResponse> {
        return $fetch<UserResponse>(`${API_BASE_URL}/auth/me`, {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
    },

    async refresh(refreshToken: string): Promise<AuthResponse> {
        return $fetch<AuthResponse>(`${API_BASE_URL}/auth/refresh`, {
            method: 'POST',
            body: { refresh_token: refreshToken }
        })
    }
}
