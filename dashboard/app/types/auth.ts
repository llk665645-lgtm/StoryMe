export interface User {
    id: string
    email: string
    full_name?: string
    avatar_url?: string
    provider: 'email' | 'github'
    subscription_tier: 'free' | 'pro'
    last_login?: string
    created_at: string
}

export interface Token {
    access_token: string
    refresh_token: string
    token_type: string
}

export interface AuthResponse {
    data: Token
}

export interface UserResponse {
    data: User
}

export interface ApiError {
    error: string
    message: string
}
