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

import LogoIcon from '@/components/LogoIcon.vue'
import NavDocuments from '@/components/NavDocuments.vue'
import NavMain from '@/components/NavMain.vue'
import NavSecondary from '@/components/NavSecondary.vue'
import NavUser from '@/components/NavUser.vue'
import SidebarUsage from '@/components/SidebarUsage.vue'
import { useAuthStore } from '@/stores/auth'
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
      badge: "18",
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
const auth = useAuthStore()

const currentUser = computed(() => {
  return {
    name: auth.user?.full_name || 'Adventurer',
    email: auth.user?.email || 'magic@storyme.com',
    avatar: auth.user?.avatar_url || '/avatars/parent.jpg',
  }
})
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
            <NuxtLink to="/dashboard" class="flex items-center gap-3 font-bold group">
              <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-[#8B5CF6] to-[#D946EF] text-white shadow-lg border border-white/20 transition-transform group-hover:scale-105">
                <LogoIcon class="size-6 stroke-white fill-white" />
              </div>
              <span class="text-xl tracking-tight text-white">Story<span class="text-white/60 italic">Me</span></span>
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
      <NavUser :user="currentUser" />
    </SidebarFooter>
  </Sidebar>
</template>

