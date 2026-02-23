import { useAuthStore } from '../stores/auth'

export default defineNuxtRouteMiddleware((to) => {
    const auth = useAuthStore()

    // Public pages
    const publicPages = ['/login', '/auth/callback']
    const isPublicPage = publicPages.includes(to.path)

    if (!auth.isAuthenticated && !isPublicPage) {
        return navigateTo('/login')
    }

    if (auth.isAuthenticated && to.path === '/login') {
        return navigateTo('/dashboard')
    }
})
