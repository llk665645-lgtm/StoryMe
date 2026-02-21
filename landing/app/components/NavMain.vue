<script setup lang="ts">
import type { Component } from "vue"
import { IconCirclePlusFilled, IconMail } from "@tabler/icons-vue"

import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from '@/components/ui/sidebar'

interface NavItem {
  title: string
  url: string
  icon?: Component
  badge?: string | number
}

defineProps<{
  items: NavItem[]
}>()
</script>

<template>
  <SidebarGroup>
    <SidebarGroupContent class="flex flex-col gap-2">
      <SidebarMenu>
        <SidebarMenuItem class="flex items-center gap-2">
          <SidebarMenuButton
            as-child
            tooltip="Quick Create"
            class="bg-primary text-primary-foreground hover:bg-primary/90 hover:text-primary-foreground active:bg-primary/90 active:text-primary-foreground min-w-8 duration-200 ease-linear shadow-sm"
          >
            <NuxtLink to="/dashboard/stories/new" class="flex items-center gap-2">
              <IconCirclePlusFilled class="size-4" />
              <span class="font-semibold">Quick Create</span>
            </NuxtLink>
          </SidebarMenuButton>
          <Button
            size="icon"
            class="size-8 group-data-[collapsible=icon]:opacity-0"
            variant="outline"
          >
            <IconMail class="size-4" />
            <span class="sr-only">Inbox</span>
          </Button>
        </SidebarMenuItem>
      </SidebarMenu>
      <SidebarMenu>
        <SidebarMenuItem v-for="item in items" :key="item.title">
          <SidebarMenuButton as-child :tooltip="item.title">
            <NuxtLink :to="item.url" class="flex items-center justify-between w-full">
              <div class="flex items-center gap-2">
                <component :is="item.icon" v-if="item.icon" class="size-4" />
                <span>{{ item.title }}</span>
              </div>
              <Badge v-if="item.badge" variant="secondary" class="ml-auto text-[10px] px-1.5 h-4 min-w-4 flex items-center justify-center bg-primary/10 text-primary border-0">
                {{ item.badge }}
              </Badge>
            </NuxtLink>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarGroupContent>
  </SidebarGroup>
</template>
