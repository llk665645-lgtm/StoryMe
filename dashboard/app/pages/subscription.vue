<script setup lang="ts">
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { IconCheck, IconCreditCard, IconHistory, IconAlertCircle } from '@tabler/icons-vue'

const currentPlan = {
  name: 'Storyteller',
  price: '$9/mo',
  status: 'Active',
  renewal: 'Oct 28, 2024',
  credits: '3 / 5'
}

const tiers = [
  { name: 'Single Magic', price: '$3', description: 'One special story', features: ['1 Story', 'AI Illustrations', 'Print Ready'] },
  { name: 'Storyteller', price: '$9', description: 'Monthly subscription', features: ['5 Stories/mo', 'Private Library', 'Priority Queue'], current: true },
  { name: 'Creator', price: '$19', description: 'Unlimited imagination', features: ['Unlimited Stories', 'Custom Themes', 'Family Sharing'] },
]
</script>

<template>
  <div class="mx-auto max-w-5xl p-4 lg:p-6 pb-20">
    <div class="mb-8">
      <h1 class="text-3xl font-bold tracking-tight">Subscription</h1>
      <p class="text-muted-foreground">Manage your plan and billing details.</p>
    </div>

    <div class="grid gap-8 lg:grid-cols-3">
      <div class="lg:col-span-2 space-y-8">
        <Card class="bg-primary text-primary-foreground relative overflow-hidden">
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
                <span>Monthly Credits used</span>
                <span>{{ currentPlan.credits }}</span>
              </div>
              <div class="h-2 w-full bg-white/20 rounded-full overflow-hidden">
                 <div class="h-full bg-white w-[60%]" />
              </div>
            </div>
          </CardContent>
          <CardFooter class="flex gap-2">
            <Button variant="secondary" class="bg-white text-primary hover:bg-white/90">Upgrade Plan</Button>
            <Button variant="ghost" class="text-white hover:bg-white/10">Manage Billing</Button>
          </CardFooter>
        </Card>

        <div>
          <h2 class="text-xl font-bold mb-4 flex items-center gap-2">
            <IconHistory class="size-5" /> Billing History
          </h2>
          <div class="rounded-lg border overflow-hidden">
             <table class="w-full text-sm">
               <thead class="bg-muted">
                 <tr>
                   <th class="p-3 text-left font-medium">Date</th>
                   <th class="p-3 text-left font-medium">Description</th>
                   <th class="p-3 text-right font-medium">Amount</th>
                   <th class="p-3 text-right font-medium">Receipt</th>
                 </tr>
               </thead>
               <tbody class="divide-y">
                 <tr v-for="i in 3" :key="i">
                   <td class="p-3">Sep {{ 28 - i }}, 2024</td>
                   <td class="p-3">Storyteller Plan Monthly</td>
                   <td class="p-3 text-right">$9.00</td>
                   <td class="p-3 text-right"><Button variant="link" size="sm" class="h-auto p-0">PDF</Button></td>
                 </tr>
               </tbody>
             </table>
          </div>
        </div>
      </div>

      <div class="space-y-6">
        <Card>
          <CardHeader>
            <CardTitle>Payment Method</CardTitle>
          </CardHeader>
          <CardContent class="flex items-center gap-4">
            <div class="h-10 w-14 rounded bg-muted flex items-center justify-center border">
              <IconCreditCard class="size-6 text-muted-foreground" />
            </div>
            <div class="flex-1">
              <p class="text-sm font-medium">Visa ending in 4242</p>
              <p class="text-xs text-muted-foreground">Expires 04/26</p>
            </div>
            <Button variant="ghost" size="sm">Edit</Button>
          </CardContent>
        </Card>

        <Card class="border-orange-200 bg-orange-50/50">
          <CardHeader class="pb-2">
            <CardTitle class="text-sm flex items-center gap-2 text-orange-800">
              <IconAlertCircle class="size-4" /> Need more credits?
            </CardTitle>
          </CardHeader>
          <CardContent class="text-xs text-orange-800/80">
            You can buy a single story credit for $3 anytime without upgrading your plan.
          </CardContent>
          <CardFooter>
            <Button size="sm" class="w-full bg-orange-500 hover:bg-orange-600 border-0">Buy 1 Credit</Button>
          </CardFooter>
        </Card>
      </div>
    </div>
  </div>
</template>
