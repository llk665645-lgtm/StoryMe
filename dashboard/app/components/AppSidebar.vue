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
      url: "/stories",
      icon: IconFileDescription,
    },
    {
      title: "Create New",
      url: "/create",
      icon: IconPlus,
    },
    {
      title: "Children Profiles",
      url: "/profiles",
      icon: IconUsers,
    },
    {
      title: "Library",
      url: "/library",
      icon: IconDatabase,
    },
  ],
  navSecondary: [
    {
      title: "Settings",
      url: "/settings",
      icon: IconSettings,
    },
    {
      title: "Support",
      url: "/support",
      icon: IconHelp,
    },
  ],
  documents: [
    {
      name: "Subscription",
      url: "/subscription",
      icon: IconCreditCard,
    },
    {
      name: "Activity Log",
      url: "/activity",
      icon: IconReport,
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
            <NuxtLink to="/dashboard" class="flex items-center gap-2 font-bold text-primary">
              <div class="flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-white shadow-lg">
                <IconSparkles class="size-5" />
              </div>
              <span class="text-base tracking-tight">Story<span class="text-primary">Me</span></span>
            </NuxtLink>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="data.navMain" />
      <NavDocuments :items="data.documents" />
      <NavSecondary :items="data.navSecondary" class="mt-auto" />
    </SidebarContent>
    <SidebarFooter>
      <NavUser :user="data.user" />
    </SidebarFooter>
  </Sidebar>
</template>
