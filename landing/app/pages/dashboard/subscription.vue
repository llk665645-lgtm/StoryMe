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
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { IconHistory, IconAlertCircle, IconSparkles } from '@tabler/icons-vue'

const currentPlan = {
  name: 'Storyteller',
  price: '$9/mo',
  status: 'Active',
  renewal: 'Mar 21, 2026',
  credits: '12 / 20'
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
      <div class="flex flex-1 flex-col p-4 md:p-6 lg:p-8">
        <div class="mx-auto max-w-5xl w-full">
          <div class="mb-8">
            <h1 class="text-3xl font-bold tracking-tight">Subscription & Billing</h1>
            <p class="text-muted-foreground">Manage your plan and create more magical stories.</p>
          </div>

          <div class="grid gap-8 lg:grid-cols-3">
            <div class="lg:col-span-2 space-y-8">
              <Card class="bg-primary text-primary-foreground relative overflow-hidden border-0 shadow-xl shadow-primary/20">
                <div class="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-white/10" />
                <CardHeader>
                  <div class="flex items-center justify-between">
                    <Badge variant="secondary" class="bg-white/20 text-white border-0">Current Plan</Badge>
                    <span class="text-sm opacity-80 font-medium italic">Renews on {{ currentPlan.renewal }}</span>
                  </div>
                  <CardTitle class="text-4xl mt-4">{{ currentPlan.name }}</CardTitle>
                  <CardDescription class="text-primary-foreground/80">{{ currentPlan.price }}</CardDescription>
                </CardHeader>
                <CardContent>
                  <div class="space-y-2 mt-4">
                    <div class="flex justify-between text-sm">
                      <span>Monthly Magic Credits used</span>
                      <span>{{ currentPlan.credits }}</span>
                    </div>
                    <div class="h-2 w-full bg-white/20 rounded-full overflow-hidden">
                       <div class="h-full bg-white w-[60%]" />
                    </div>
                  </div>
                </CardContent>
                <CardFooter class="flex gap-2">
                  <Button variant="secondary" class="bg-white text-primary hover:bg-white/90">Upgrade Magic</Button>
                  <Button variant="ghost" class="text-white hover:bg-white/10">Billing Details</Button>
                </CardFooter>
              </Card>

              <div>
                <h2 class="text-xl font-bold mb-4 flex items-center gap-2">
                  <IconHistory class="size-5" /> Story History
                </h2>
                <div class="rounded-lg border overflow-hidden">
                   <table class="w-full text-sm">
                     <thead class="bg-muted">
                       <tr>
                         <th class="p-3 text-left font-medium">Date</th>
                         <th class="p-3 text-left font-medium">Plan</th>
                         <th class="p-3 text-right font-medium">Amount</th>
                         <th class="p-3 text-right font-medium">Status</th>
                       </tr>
                     </thead>
                     <tbody class="divide-y text-card-foreground">
                       <tr v-for="i in 3" :key="i">
                         <td class="p-3 font-medium">Feb {{ 21 - i }}, 2026</td>
                         <td class="p-3">Storyteller Plan Monthly</td>
                         <td class="p-3 text-right">$9.00</td>
                         <td class="p-3 text-right"><Badge variant="outline" class="text-green-500 border-green-200">Paid</Badge></td>
                       </tr>
                     </tbody>
                   </table>
                </div>
              </div>
            </div>

            <div class="space-y-6">
              <Card class="border-primary/20 bg-primary/5">
                <CardHeader class="pb-2">
                  <CardTitle class="text-sm flex items-center gap-2 text-primary">
                    <IconAlertCircle class="size-4" /> Running out of magic?
                  </CardTitle>
                </CardHeader>
                <CardContent class="text-xs text-muted-foreground">
                  You can buy 5 extra story credits for just $3 anytime.
                </CardContent>
                <CardFooter>
                  <Button size="sm" class="w-full">
                    <IconSparkles class="size-3 mr-2" /> Buy Credits
                  </Button>
                </CardFooter>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle class="text-sm">Why Storyteller?</CardTitle>
                </CardHeader>
                <CardContent class="grid gap-4 text-xs">
                  <div class="flex items-center gap-2">
                    <div class="size-1.5 rounded-full bg-primary" />
                    <span>5 Stories per month</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="size-1.5 rounded-full bg-primary" />
                    <span>Private Gallery for your family</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="size-1.5 rounded-full bg-primary" />
                    <span>Unlimited Theme access</span>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
