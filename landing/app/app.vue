<template>
  <NuxtLayout>
    <TextCursor
      text="⚛️"
      :delay="0.01"
      :spacing="100"
      :follow-mouse-direction="true"
      :random-float="true"
      :exit-duration="0.5"
      :max-points="10"
    />
    <Analytics/>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { Analytics } from '@vercel/analytics/nuxt'
</script>