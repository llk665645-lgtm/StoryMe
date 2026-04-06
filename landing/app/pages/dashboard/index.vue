<script setup lang="ts">
import { IconSparkles, IconCrown, IconHistory, IconPlus } from "@tabler/icons-vue"
import DataTable from "@/components/DataTable.vue"
import SectionCards from "@/components/SectionCards.vue"
import { useAuthStore } from '~/stores/auth'

definePageMeta({
  layout: "dashboard",
  middleware: "auth"
})

const authStore = useAuthStore()
const userName = computed(() => authStore.user?.full_name || 'Adventurer')

const data = [
  {
    id: 1,
    header: "The Brave Little Dino",
    type: "Fairytale",
    status: "Completed",
    target: "Alex (4)",
    limit: "Watercolor",
    reviewer: "Forest",
  },
  {
    id: 2,
    header: "Starry Night Adventure",
    type: "Educational",
    status: "Completed",
    target: "Sophia (6)",
    limit: "Ink & Wash",
    reviewer: "Space",
  },
  {
    id: 3,
    header: "The Lost Key of Magic",
    type: "Fantasy",
    status: "In Progress",
    target: "Leo (3)",
    limit: "3D Render",
    reviewer: "Fairytale",
  },
  {
    id: 4,
    header: "Superhero for a Day",
    type: "Action",
    status: "Completed",
    target: "Alex (4)",
    limit: "Comic Style",
    reviewer: "Superheroes",
  },
]
</script>

<template>
  <div class="flex flex-1 flex-col p-4 md:p-8">
    <div class="mb-10 relative overflow-hidden rounded-[2.5rem] bg-gradient-to-br from-violet-600/20 to-fuchsia-600/20 border border-white/10 p-8 sm:p-10 backdrop-blur-md">
      <div class="absolute -top-20 -right-20 w-64 h-64 bg-violet-500/20 blur-[100px] rounded-full"></div>
      <div class="absolute -bottom-20 -left-20 w-64 h-64 bg-fuchsia-500/10 blur-[100px] rounded-full"></div>
      
      <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div class="space-y-2">
          <div class="flex items-center gap-2 text-violet-400 font-bold tracking-widest text-xs uppercase">
            <IconSparkles class="size-4" />
            <span>Welcome Back</span>
          </div>
          <h1 class="text-4xl md:text-5xl font-black text-white tracking-tight">
            Greetings, <span class="text-transparent bg-clip-text bg-gradient-to-r from-violet-400 to-fuchsia-400 font-serif italic">{{ userName }}</span>!
          </h1>
          <p class="text-white/60 text-lg max-w-xl">
            Your magical library is growing. What adventure will we create today?
          </p>
        </div>
        
        <NuxtLink 
          to="/dashboard/stories/new" 
          class="inline-flex items-center gap-3 px-8 py-4 bg-violet-600 hover:bg-violet-500 text-white rounded-2xl font-black transition-all hover:scale-[1.02] active:scale-[0.98] shadow-lg shadow-violet-900/40 border border-white/20 whitespace-nowrap self-start md:self-center"
        >
          <IconPlus class="size-6" />
          Create New Story
        </NuxtLink>
      </div>
    </div>

    <div class="@container/main flex flex-1 flex-col gap-10">
      <div class="flex flex-col gap-10">
        <!-- Overview Cards -->
        <div class="space-y-6">
          <div class="flex items-center justify-between px-2">
            <h2 class="text-2xl font-bold text-white flex items-center gap-3">
              <IconCrown class="size-6 text-yellow-400" />
              <span>Scroll Overview</span>
            </h2>
          </div>
          <SectionCards />
        </div>

        <!-- Recent Stories -->
        <div class="space-y-6">
          <div class="flex items-center justify-between px-2">
            <h2 class="text-2xl font-bold text-white flex items-center gap-3">
              <IconHistory class="size-6 text-pink-400" />
              <span>Recent Adventures</span>
            </h2>
            <NuxtLink to="/dashboard/stories" class="text-sm font-bold text-violet-400 hover:text-violet-300 transition-colors">View All Stories →</NuxtLink>
          </div>
          <div class="bg-white/5 border border-white/5 rounded-[2rem] overflow-hidden backdrop-blur-sm shadow-2xl">
            <DataTable :data="data" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
