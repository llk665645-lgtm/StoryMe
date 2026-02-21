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
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { IconSparkles } from '@tabler/icons-vue'

const isLoading = ref(false)

function handleGenerate() {
  isLoading.value = true
  setTimeout(() => {
    isLoading.value = false
    navigateTo('/dashboard/stories')
  }, 2000)
}
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
      <div class="flex flex-1 flex-col p-4 md:p-6">
        <div class="max-w-2xl mx-auto w-full">
          <div class="mb-8 text-center sm:text-left">
            <h1 class="text-3xl font-bold tracking-tight">Create Magic</h1>
            <p class="text-muted-foreground mt-2">Personalize a magical story for your little hero.</p>
          </div>

          <Card class="border-primary/20 shadow-lg shadow-primary/5">
            <CardHeader class="border-b bg-muted/30">
              <CardTitle>Story Details</CardTitle>
              <CardDescription>Tell the AI about the hero of the story.</CardDescription>
            </CardHeader>
            <CardContent class="grid gap-6 p-6">
              <div class="grid gap-2">
                <Label for="name">Child's Name</Label>
                <Input id="name" placeholder="Hero's name?" />
              </div>
              
              <div class="grid grid-cols-2 gap-4">
                <div class="grid gap-2">
                  <Label for="age">Age</Label>
                  <Input id="age" type="number" placeholder="2-10" min="2" max="10" />
                </div>
                <div class="grid gap-2">
                  <Label for="theme">Theme</Label>
                  <Select id="theme">
                    <SelectTrigger>
                      <SelectValue placeholder="Choose world" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="forest">Forest Adventure</SelectItem>
                      <SelectItem value="space">Space Journey</SelectItem>
                      <SelectItem value="ocean">Ocean Wonders</SelectItem>
                      <SelectItem value="dino">Dinosaur Land</SelectItem>
                      <SelectItem value="magic">Fairytale World</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
              </div>

              <div class="grid gap-2">
                <Label for="interests">Favorite Things / Interests</Label>
                <textarea 
                  id="interests" 
                  class="flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                  placeholder="Cars, cats, ice cream, space travel..."
                ></textarea>
              </div>
            </CardContent>
            <CardFooter class="bg-muted/30 border-t">
              <Button class="w-full text-lg h-12" :disabled="isLoading" @click="handleGenerate">
                <IconSparkles v-if="!isLoading" class="mr-2 h-5 w-5" />
                <span v-else class="mr-2 h-5 w-5 animate-spin">
                   <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="lucide lucide-loader-2"
                  >
                    <path d="M21 12a9 9 0 1 1-6.219-8.56" />
                  </svg>
                </span>
                {{ isLoading ? 'AI is Writing and Drawing...' : 'Create Magic for $3' }}
              </Button>
            </CardFooter>
          </Card>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
