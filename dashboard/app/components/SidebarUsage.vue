<script setup lang="ts">
import { IconTargetArrow, IconTrophy } from "@tabler/icons-vue"
import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarGroupContent,
} from "@/components/ui/sidebar"

const careerStrength = 82
const creditsUsed = 12
const creditsTotal = 20
</script>

<template>
  <SidebarGroup class="group-data-[collapsible=icon]:hidden">
    <SidebarGroupLabel>Career Growth</SidebarGroupLabel>
    <SidebarGroupContent class="px-2 py-2">
      <div class="space-y-4">
        <!-- Profile Strength -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-[11px] font-medium">
            <div class="flex items-center gap-1.5 text-muted-foreground">
              <IconTrophy class="size-3 text-amber-500" />
              <span>Career Strength</span>
            </div>
            <span class="text-primary">{{ careerStrength }}%</span>
          </div>
          <div class="h-1.5 w-full bg-primary/10 rounded-full overflow-hidden">
            <div 
              class="h-full bg-primary transition-all duration-500" 
              :style="{ width: `${careerStrength}%` }"
            />
          </div>
        </div>

        <!-- Credits Usage -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-[11px] font-medium">
            <div class="flex items-center gap-1.5 text-muted-foreground">
              <IconTargetArrow class="size-3 text-blue-500" />
              <span>AI Credits</span>
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
            Next renewal in 12 days.
          </p>
        </div>
      </div>
    </SidebarGroupContent>
  </SidebarGroup>
</template>
