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
import { Switch } from '@/components/ui/switch'
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
        <div class="max-w-4xl mx-auto w-full">
          <h1 class="text-3xl font-bold tracking-tight mb-8">Settings</h1>

          <div class="grid gap-8">
            <Card>
              <CardHeader>
                <CardTitle>Parental Profile</CardTitle>
                <CardDescription>Manage your account info and storytelling preferences.</CardDescription>
              </CardHeader>
              <CardContent class="grid gap-4">
                <div class="grid gap-2">
                  <Label for="name">Full Name</Label>
                  <Input id="name" value="Alex Parent" />
                </div>
                <div class="grid gap-2">
                  <Label for="email">Email</Label>
                  <Input id="email" value="alex@example.com" disabled />
                </div>
              </CardContent>
              <CardFooter class="border-t bg-muted/20 pt-4">
                <Button>Update Profile</Button>
              </CardFooter>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Preferences</CardTitle>
                <CardDescription>Control how your stories are generated and shared.</CardDescription>
              </CardHeader>
              <CardContent class="grid gap-6">
                <div class="flex items-center justify-between space-x-2">
                  <Label for="email-notif" class="flex flex-col space-y-1">
                    <span>Email Notifications</span>
                    <span class="font-normal text-muted-foreground text-xs">Receive an email when your story is ready.</span>
                  </Label>
                  <Switch id="email-notif" :default-checked="true" />
                </div>
                <div class="flex items-center justify-between space-x-2">
                  <Label for="public-sharing" class="flex flex-col space-y-1">
                    <span>Community Sharing</span>
                    <span class="font-normal text-muted-foreground text-xs">Allow your stories to be showcased in the gallery.</span>
                  </Label>
                  <Switch id="public-sharing" />
                </div>
              </CardContent>
            </Card>

            <Card class="border-destructive/20 bg-destructive/5">
              <CardHeader>
                <CardTitle class="text-destructive">Danger Zone</CardTitle>
                <CardDescription>Permanently delete your account and all magical stories.</CardDescription>
              </CardHeader>
              <CardContent>
                <p class="text-sm text-destructive/80">This action cannot be undone. All your children's profiles and generated stories will be lost forever.</p>
              </CardContent>
              <CardFooter class="border-t border-destructive/10 pt-4">
                <Button variant="destructive">Delete Everything</Button>
              </CardFooter>
            </Card>
          </div>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
