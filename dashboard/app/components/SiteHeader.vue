<script setup lang="ts">
import { Button } from '@/components/ui/button'
import { Separator } from '@/components/ui/separator'
import { SidebarTrigger } from '@/components/ui/sidebar'
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const pageTitle = computed(() => {
  const path = route.path.split('/').filter(Boolean).pop() || 'Dashboard'
  return path.charAt(0).toUpperCase() + path.slice(1).replace(/-/g, ' ')
})
</script>

<template>
  <header class="flex h-(--header-height) shrink-0 items-center gap-2 border-b transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-(--header-height) bg-background/95 backdrop-blur supports-backdrop-filter:bg-background/60 sticky top-0 z-30">
    <div class="flex w-full items-center gap-1 px-4 lg:gap-2 lg:px-6">
      <SidebarTrigger class="-ml-1" />
      <Separator
        orientation="vertical"
        class="mx-2 data-[orientation=vertical]:h-4"
      />
      <h2 class="text-sm font-semibold tracking-tight">
        {{ pageTitle }}
      </h2>
      <div class="ml-auto flex items-center gap-3">
        <Button variant="outline" size="sm" class="hidden sm:flex" as-child>
           <NuxtLink to="/create">
             Create magic
           </NuxtLink>
        </Button>
        <div class="h-8 w-8 rounded-full bg-primary/10 flex items-center justify-center text-[10px] font-bold text-primary">
          AP
        </div>
      </div>
    </div>
  </header>
</template>
