<script setup lang="ts">
import AppSidebar from "@/components/AppSidebar.vue"
import SiteHeader from "@/components/SiteHeader.vue"
import {
  SidebarInset,
  SidebarProvider,
} from "@/components/ui/sidebar"
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { 
  IconTrees, 
  IconRocket, 
  IconFish, 
  IconBone, 
  IconSparkles, 
  IconBolt 
} from '@tabler/icons-vue'

const themes = [
  { name: 'Forest', icon: IconTrees, description: 'Tall trees and hidden trails', count: 12, color: 'bg-green-500' },
  { name: 'Space', icon: IconRocket, description: 'Stars, robots and aliens', count: 8, color: 'bg-indigo-500' },
  { name: 'Ocean', icon: IconFish, description: 'Mermaids and underwater cities', count: 5, color: 'bg-blue-500' },
  { name: 'Dinosaurs', icon: IconBone, description: 'Jurassic adventures and T-Rex', count: 7, color: 'bg-orange-500' },
  { name: 'Fairytale', icon: IconSparkles, description: 'Wizards, dragons and fairies', count: 10, color: 'bg-purple-500' },
  { name: 'Superheroes', icon: IconBolt, description: 'Capes and extraordinary powers', count: 4, color: 'bg-red-500' },
]
</script>

<template>
  <SidebarProvider
    :style=" {
      '--sidebar-width': 'calc(var(--spacing) * 72)',
      '--header-height': 'calc(var(--spacing) * 12)',
    }"
  >
    <AppSidebar variant="inset" />
    <SidebarInset>
      <SiteHeader />
      <div class="flex flex-1 flex-col p-4 md:p-6 lg:p-8">
        <div class="max-w-5xl mx-auto w-full">
          <div class="mb-8">
            <h1 class="text-3xl font-bold tracking-tight">Fairytale Worlds</h1>
            <p class="text-muted-foreground mt-2">Discover and choose the universe for your next story.</p>
          </div>

          <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <Card v-for="theme in themes" :key="theme.name" class="group hover:shadow-lg transition-all duration-300">
              <CardHeader>
                <div class="flex items-center justify-between">
                  <div :class="[theme.color, 'p-2.5 rounded-xl text-white shadow-sm transition-transform group-hover:scale-110']">
                    <component :is="theme.icon" class="size-6" />
                  </div>
                  <Badge variant="secondary">Active</Badge>
                </div>
                <CardTitle class="mt-4">{{ theme.name }}</CardTitle>
                <CardDescription>{{ theme.description }}</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="flex items-center justify-between text-sm text-muted-foreground">
                  <span>{{ theme.count }} Stories used</span>
                  <div class="flex -space-x-2">
                    <div v-for="i in 3" :key="i" class="size-6 rounded-full border-2 border-background bg-muted text-[8px] flex items-center justify-center font-bold">
                      H
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
