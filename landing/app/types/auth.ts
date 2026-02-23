export interface User {
    id: string
    email: string
    full_name?: string
    avatar_url?: string
    provider: 'email' | 'github'
    subscription_tier: 'free' | 'paid' | 'enterprise'
    last_login?: string
    created_at: string
}

export interface Token {
    access_token: string
    refresh_token: string
    token_type: string
}

export interface AuthResponse {
    success: boolean
    data: Token
}

export interface UserResponse {
    success: boolean
    data: User
}

export interface ApiError {
    error: string
    message: string
}
