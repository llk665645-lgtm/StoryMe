<script setup lang="ts">
import { ref } from 'vue'
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { IconSearch, IconFilter, IconPlus } from '@tabler/icons-vue'

const stories = [
  { id: 1, title: 'The Brave Little Fox', child: 'Oliver', theme: 'Forest', date: '2024-10-12', image: '/themes/forest-preview.jpg', status: 'Ready' },
  { id: 2, title: 'Space Adventure', child: 'Sophia', theme: 'Space', date: '2024-10-10', image: '/themes/space-preview.jpg', status: 'Ready' },
  { id: 3, title: "Dino's Big Secret", child: 'Oliver', theme: 'Dino', date: '2024-10-05', image: '/themes/dino-preview.jpg', status: 'Ready' },
  { id: 4, title: "The Mermaid's Song", child: 'Sophia', theme: 'Ocean', date: '2024-10-01', image: '/themes/ocean-preview.jpg', status: 'Ready' },
  { id: 5, title: 'Super Leo', child: 'Leo', theme: 'Super', date: '2024-09-28', image: '/themes/super-preview.jpg', status: 'Ready' },
  { id: 6, title: 'Magic wand', child: 'Sophia', theme: 'Magic', date: '2024-09-25', image: '/themes/magic-preview.jpg', status: 'Ready' },
]

const searchQuery = ref('')
</script>

<template>
  <div class="flex flex-col gap-6 p-4 lg:p-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold tracking-tight">My Stories</h1>
        <p class="text-muted-foreground">Manage and read all your created magical stories.</p>
      </div>
      <Button as-child>
        <NuxtLink to="/create">
          <IconPlus class="mr-2 size-4" /> Create New
        </NuxtLink>
      </Button>
    </div>

    <div class="flex items-center gap-4">
      <div class="relative flex-1">
        <IconSearch class="absolute left-3 top-1/2 size-4 -translate-y-1/2 text-muted-foreground" />
        <Input v-model="searchQuery" placeholder="Search stories..." class="pl-10" />
      </div>
      <Button variant="outline">
        <IconFilter class="mr-2 size-4" /> Filter
      </Button>
    </div>

    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      <Card v-for="story in stories" :key="story.id" class="overflow-hidden transition-all hover:ring-2 hover:ring-primary/20">
        <div class="aspect-[4/3] w-full bg-muted relative">
           <div class="absolute inset-0 flex items-center justify-center text-muted-foreground opacity-50 italic">
             {{ story.theme }} Illustration
           </div>
        </div>
        <CardHeader class="p-4 pb-2">
          <div class="flex items-center justify-between gap-2">
            <Badge variant="secondary" class="text-[10px] uppercase tracking-wider">
              {{ story.theme }}
            </Badge>
            <span class="text-xs text-muted-foreground">{{ story.date }}</span>
          </div>
          <CardTitle class="mt-2 line-clamp-1 truncate text-lg">
            {{ story.title }}
          </CardTitle>
        </CardHeader>
        <CardContent class="px-4 pb-4 pt-0">
          <p class="text-sm text-muted-foreground">Hero: <span class="font-medium text-foreground">{{ story.child }}</span></p>
        </CardContent>
        <CardFooter class="p-4 pt-0 flex gap-2">
          <Button variant="outline" size="sm" class="flex-1">Read</Button>
          <Button variant="outline" size="sm" class="flex-1">Print</Button>
        </CardFooter>
      </Card>
    </div>
  </div>
</template>
