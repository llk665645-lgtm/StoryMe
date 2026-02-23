import { useAuthStore } from '~/stores/auth'

export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore()

    // If not authenticated, redirect to home
    if (!authStore.accessToken) {
        return navigateTo('/')
    }
})
