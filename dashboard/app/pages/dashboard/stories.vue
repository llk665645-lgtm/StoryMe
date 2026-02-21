<script setup lang="ts">
import AppSidebar from "@/components/AppSidebar.vue"
import DataTable from "@/components/DataTable.vue"
import SiteHeader from "@/components/SiteHeader.vue"
import {
  SidebarInset,
  SidebarProvider,
} from "@/components/ui/sidebar"
import { Button } from '@/components/ui/button'
import { IconPlus } from '@tabler/icons-vue'

const stories = [
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
      <div class="flex flex-1 flex-col">
        <div class="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
          <div class="flex items-center justify-between px-4 lg:px-6">
            <div>
              <h1 class="text-2xl font-bold tracking-tight">My Stories</h1>
              <p class="text-muted-foreground">Manage your collection of magical children's stories</p>
            </div>
            <Button as-child>
              <NuxtLink to="/dashboard/stories/new">
                <IconPlus class="mr-2 h-4 w-4" /> Create New Story
              </NuxtLink>
            </Button>
          </div>
          <DataTable :data="stories" />
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
