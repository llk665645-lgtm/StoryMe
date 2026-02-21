<script setup lang="ts">
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from '@/components/ui/card'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { IconSparkles, IconChevronRight, IconAlertCircle } from '@tabler/icons-vue'

const form = ref({
  childName: '',
  age: '',
  interests: '',
  theme: 'forest'
})

const isGenerating = ref(false)

function handleCreate() {
  isGenerating.value = true
  setTimeout(() => {
    isGenerating.value = false
    navigateTo('/stories')
  }, 3000)
}
</script>

<template>
  <div class="mx-auto max-w-4xl p-4 lg:p-6 pb-20">
    <div class="mb-8">
      <h1 class="text-3xl font-bold tracking-tight">Create New Magic</h1>
      <p class="text-muted-foreground">Personalize a new story for your child. Powered by AI.</p>
    </div>

    <div class="grid gap-8 lg:grid-cols-3">
      <div class="lg:col-span-2 space-y-6">
        <Card shadow-lg>
          <CardHeader>
            <CardTitle>Journey Details</CardTitle>
            <CardDescription>Enter the magic ingredients for your child's story.</CardDescription>
          </CardHeader>
          <CardContent class="space-y-4">
            <div class="grid gap-4 sm:grid-cols-2">
              <div class="space-y-2">
                <Label for="child-name">Child's Name</Label>
                <Input id="child-name" v-model="form.childName" placeholder="e.g. Oliver" />
              </div>
              <div class="space-y-2">
                <Label for="age">Age (optional)</Label>
                <Input id="age" v-model="form.age" type="number" placeholder="4" />
              </div>
            </div>
            
            <div class="space-y-2">
              <Label for="interests">What does your child love?</Label>
              <Textarea 
                id="interests" 
                v-model="form.interests" 
                placeholder="Trains, red apples, talking bears..." 
                class="min-h-[100px]"
              />
            </div>

            <div class="space-y-2">
              <Label>Choose Story Theme</Label>
              <div class="grid grid-cols-2 gap-3 sm:grid-cols-3">
                <button 
                  v-for="theme in ['forest', 'space', 'ocean', 'dino', 'magic', 'super']" 
                  :key="theme"
                  @click="form.theme = theme"
                  :class="[
                    'flex flex-col items-center gap-2 rounded-xl border p-3 transition-all hover:bg-accent',
                    form.theme === theme ? 'border-primary ring-1 ring-primary' : 'border-muted'
                  ]"
                >
                  <div class="h-10 w-10 flex items-center justify-center rounded-lg bg-primary/10 text-primary">
                    <IconSparkles v-if="theme === 'magic'" class="size-6" />
                    <!-- Placeholder icons -->
                    <span v-else class="text-xs font-bold uppercase">{{ theme[0] }}</span>
                  </div>
                  <span class="text-xs font-medium capitalize">{{ theme }}</span>
                </button>
              </div>
            </div>
          </CardContent>
          <CardFooter class="border-t bg-muted/30 p-6">
            <Button size="lg" class="w-full h-12 text-lg font-bold" @click="handleCreate" :disabled="isGenerating">
              <IconSparkles v-if="!isGenerating" class="mr-2 size-5" />
              <div v-else class="mr-2 h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" />
              {{ isGenerating ? 'AI is Writing...' : 'Create Magic Story' }}
            </Button>
          </CardFooter>
        </Card>

        <div class="rounded-lg bg-orange-50 p-4 border border-orange-200 flex gap-3 text-orange-800">
          <IconAlertCircle class="size-5 shrink-0" />
          <p class="text-sm">
            Generation takes about 30-40 seconds. You have <strong>3 credits</strong> remaining on your plan.
          </p>
        </div>
      </div>

      <div class="space-y-6">
        <Card>
          <CardHeader>
            <CardTitle>Child Profiles</CardTitle>
          </CardHeader>
          <CardContent class="space-y-3">
            <button 
              v-for="profile in ['Oliver (4)', 'Sophia (6)', 'Leo (2)']" 
              :key="profile"
              class="flex w-full items-center justify-between rounded-lg border p-3 text-sm hover:bg-accent"
              @click="form.childName = profile.split(' ')[0]; form.age = profile.match(/\d+/)?.[0] || ''"
            >
              <span>{{ profile }}</span>
              <IconChevronRight class="size-4 text-muted-foreground" />
            </button>
            <Button variant="ghost" size="sm" class="w-full text-xs" as-child>
               <NuxtLink to="/profiles">+ Add New Profile</NuxtLink>
            </Button>
          </CardContent>
        </Card>

        <Card class="bg-primary text-primary-foreground">
          <CardHeader>
            <CardTitle>Pro Tip</CardTitle>
          </CardHeader>
          <CardContent class="text-sm opacity-90">
             The more specific the interests, the more magical the story! Instead of "Dogs", try "A Golden Retriever named Buddy".
          </CardContent>
        </Card>
      </div>
    </div>
  </div>
</template>
