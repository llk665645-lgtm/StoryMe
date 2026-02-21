import { ref } from 'vue'

const isAuthOpen = ref(false)
const authMode = ref<'login' | 'register'>('register')

export const useAuth = () => {
    const triggerAuth = (mode: 'login' | 'register' = 'register') => {
        authMode.value = mode
        isAuthOpen.value = true
    }

    const closeAuth = () => {
        isAuthOpen.value = false
    }

    return {
        isAuthOpen,
        authMode,
        triggerAuth,
        closeAuth
    }
}
