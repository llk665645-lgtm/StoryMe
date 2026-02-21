<script setup lang="ts">
import { IconBook, IconSparkles } from "@tabler/icons-vue"
import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarGroupContent,
} from "@/components/ui/sidebar"

const libraryProgress = 65
const creditsUsed = 12
const creditsTotal = 20
</script>

<template>
  <SidebarGroup class="group-data-[collapsible=icon]:hidden">
    <SidebarGroupLabel>Your Magic Garden</SidebarGroupLabel>
    <SidebarGroupContent class="px-2 py-2">
      <div class="space-y-4">
        <!-- Collection Progress -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-[11px] font-medium">
            <div class="flex items-center gap-1.5 text-muted-foreground">
              <IconBook class="size-3 text-amber-500" />
              <span>Story Collection</span>
            </div>
            <span class="text-primary">{{ libraryProgress }}%</span>
          </div>
          <div class="h-1.5 w-full bg-primary/10 rounded-full overflow-hidden">
            <div 
              class="h-full bg-primary transition-all duration-500" 
              :style="{ width: `${libraryProgress}%` }"
            />
          </div>
        </div>

        <!-- Magic Credits -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-[11px] font-medium">
            <div class="flex items-center gap-1.5 text-muted-foreground">
              <IconSparkles class="size-3 text-blue-500" />
              <span>Magic Credits</span>
            </div>
            <span class="text-muted-foreground">{{ creditsUsed }}/{{ creditsTotal }}</span>
          </div>
          <div class="h-1.5 w-full bg-primary/10 rounded-full overflow-hidden">
            <div 
              class="h-full bg-primary transition-all duration-500" 
              :style="{ width: `${(creditsUsed / creditsTotal) * 100}%` }"
            />
          </div>
          <p class="text-[10px] text-muted-foreground/70 leading-tight">
            20 credits renew on Mar 21.
          </p>
        </div>
      </div>
    </SidebarGroupContent>
  </SidebarGroup>
</template>
