<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
    <Analytics />
  </div>
</template>

<script setup lang="ts">
import { Analytics } from '@vercel/analytics/nuxt'
import { useAuthStore } from '~/stores/auth'

const authStore = useAuthStore()

onMounted(() => {
  authStore.init()
})

useHead({
  link: [
    { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }
  ]
})
</script>