<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
})
import AppSidebar from "@/components/AppSidebar.vue"
import SiteHeader from "@/components/SiteHeader.vue"
import {
  SidebarInset,
  SidebarProvider,
} from "@/components/ui/sidebar"
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { IconPlus, IconUserPlus } from '@tabler/icons-vue'

const profiles = [
  { name: "Alex", age: "4 years", stories: 12, avatar: "/avatars/alex.jpg", initials: "AL" },
  { name: "Sophia", age: "6 years", stories: 8, avatar: "/avatars/sophia.jpg", initials: "SO" },
  { name: "Leo", age: "3 years", stories: 5, avatar: "/avatars/leo.jpg", initials: "LE" },
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
          <div class="flex items-center justify-between mb-8">
            <div>
              <h1 class="text-3xl font-bold tracking-tight">Children Profiles</h1>
              <p class="text-muted-foreground mt-2">Manage profiles for personalized storytelling.</p>
            </div>
            <Button>
              <IconUserPlus class="mr-2 h-4 w-4" /> Add Profile
            </Button>
          </div>

          <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <Card v-for="profile in profiles" :key="profile.name" class="overflow-hidden">
              <CardHeader class="flex flex-row items-center gap-4 space-y-0">
                <Avatar class="size-16 border-2 border-primary/10">
                  <AvatarFallback class="bg-primary/5 text-primary text-xl font-bold">
                    {{ profile.initials }}
                  </AvatarFallback>
                </Avatar>
                <div>
                  <CardTitle>{{ profile.name }}</CardTitle>
                  <CardDescription>{{ profile.age }} old</CardDescription>
                </div>
              </CardHeader>
              <CardContent>
                <div class="flex items-center justify-between text-sm py-2 px-4 rounded-lg bg-muted/50">
                  <span class="text-muted-foreground">Personalized Stories</span>
                  <span class="font-bold">{{ profile.stories }}</span>
                </div>
              </CardContent>
              <CardFooter class="border-t bg-muted/20 flex gap-2 pt-4">
                <Button variant="outline" size="sm" class="flex-1">Edit</Button>
                <Button size="sm" class="flex-1">Create Story</Button>
              </CardFooter>
            </Card>

            <button class="border-2 border-dashed rounded-xl flex flex-col items-center justify-center p-8 text-muted-foreground hover:text-primary hover:border-primary/50 transition-colors">
              <div class="size-12 rounded-full bg-muted flex items-center justify-center mb-4">
                <IconPlus class="size-6" />
              </div>
              <span class="font-medium">Add another child</span>
            </button>
          </div>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
