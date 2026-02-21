<script setup lang="ts">
import {
  IconDashboard,
  IconDatabase,
  IconFileDescription,
  IconHelp,
  IconReport,
  IconSettings,
  IconUsers,
  IconPlus,
  IconCreditCard,
  IconSparkles,
} from "@tabler/icons-vue"

import NavDocuments from '@/components/NavDocuments.vue'
import NavMain from '@/components/NavMain.vue'
import NavSecondary from '@/components/NavSecondary.vue'
import NavUser from '@/components/NavUser.vue'
import SidebarUsage from '@/components/SidebarUsage.vue'
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from '@/components/ui/sidebar'

const data = {
  user: {
    name: "Alex Parent",
    email: "alex@example.com",
    avatar: "/avatars/parent.jpg",
  },
  navMain: [
    {
      title: "Overview",
      url: "/dashboard",
      icon: IconDashboard,
    },
    {
      title: "My Stories",
      url: "/dashboard/stories",
      icon: IconFileDescription,
      badge: "12",
    },
    {
      title: "Children Profiles",
      url: "/dashboard/profiles",
      icon: IconUsers,
      badge: "3",
    },
    {
      title: "Fairytale Themes",
      url: "/dashboard/themes",
      icon: IconSparkles,
      badge: "6",
    },
    {
      title: "Gallery",
      url: "/dashboard/gallery",
      icon: IconDatabase,
    },
  ],
  navSecondary: [
    {
      title: "Settings",
      url: "/dashboard/settings",
      icon: IconSettings,
    },
    {
      title: "Support",
      url: "/dashboard/support",
      icon: IconHelp,
    },
  ],
  documents: [
    {
      name: "Subscription",
      url: "/dashboard/subscription",
      icon: IconCreditCard,
    },
    {
      name: "Storytelling Tips",
      url: "/dashboard/tips",
      icon: IconDatabase,
    },
  ],
}
</script>

<template>
  <Sidebar collapsible="offcanvas">
    <SidebarHeader>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton
            as-child
            class="data-[slot=sidebar-menu-button]:!p-1.5"
          >
            <NuxtLink to="/dashboard" class="flex items-center gap-3 font-bold">
              <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-primary text-white shadow-lg">
                <IconSparkles class="size-6" />
              </div>
              <span class="text-xl tracking-tight text-foreground">Story<span class="text-primary">Me</span></span>
            </NuxtLink>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="data.navMain" />
      <SidebarUsage />
      <NavDocuments :items="data.documents" />
      <NavSecondary :items="data.navSecondary" class="mt-auto" />
    </SidebarContent>
    <SidebarFooter>
      <NavUser :user="data.user" />
    </SidebarFooter>
  </Sidebar>
</template>
