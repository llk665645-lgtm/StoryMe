<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()

onMounted(async () => {
  if (auth.isAuthenticated) {
    await auth.fetchUser()
  }
})
</script>

<template>
  <div class="relative min-h-screen">
    <DreamBackground />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

