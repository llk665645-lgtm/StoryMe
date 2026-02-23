<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const auth = useAuthStore()

onMounted(async () => {
  const accessToken = route.query.access_token as string
  const refreshToken = route.query.refresh_token as string

  if (accessToken && refreshToken) {
    auth.setTokens(accessToken, refreshToken)
    await auth.fetchUser()
    navigateTo('/dashboard')
  } else {
    navigateTo('/login?error=oauth_failed')
  }
})
</script>

<template>
  <div class="min-h-svh flex items-center justify-center bg-background">
    <div class="text-center space-y-4">
      <div class="animate-spin size-8 border-4 border-primary border-t-transparent rounded-full mx-auto" />
      <p class="text-muted-foreground animate-pulse">Completing the magical ritual...</p>
    </div>
  </div>
</template>
