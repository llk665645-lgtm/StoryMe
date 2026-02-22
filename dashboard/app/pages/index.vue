<template>
  <div class="flex min-h-screen items-center justify-center p-4">
    <div class="mx-auto w-full max-w-sm space-y-10 text-center relative z-10">
      <div class="space-y-4">
        <div class="flex justify-center mb-6">
           <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-[#8B5CF6] to-[#D946EF] text-white shadow-2xl border border-white/20">
            <LogoIcon class="w-9 h-9 stroke-white fill-white" />
          </div>
        </div>
        <h1 class="text-4xl font-bold font-serif italic text-white">StoryMe <span class="text-white/60">Dashboard</span></h1>
        <p class="text-white/50 text-base leading-relaxed">
          Create personalized bedtime stories with AI illustrations for your child in 30 seconds.
        </p>
      </div>
      <div class="grid gap-4">
        <Button as-child class="w-full h-12 rounded-xl bg-gradient-to-r from-purple-600 to-pink-600 border-none text-white font-bold hover:scale-[1.02] transition-transform">
          <NuxtLink to="/login">Continue the Journey</NuxtLink>
        </Button>
        <Button variant="outline" as-child class="w-full h-12 rounded-xl border-white/10 bg-white/5 text-white hover:bg-white/10 hover:border-white/20">
          <NuxtLink to="/dashboard">My Library</NuxtLink>
        </Button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Button } from '@/components/ui/button'
import LogoIcon from '@/components/LogoIcon.vue'

useSeoMeta({
  title: 'Dashboard - StoryMe',
  description: 'Manage your magical stories and profile.'
})
</script>
