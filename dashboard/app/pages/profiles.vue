<script setup lang="ts">
import { ref } from 'vue'
import { Card, CardContent, CardFooter, CardHeader, CardTitle, CardDescription } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { IconPlus, IconTrash, IconPencil, IconUser } from '@tabler/icons-vue'

const profiles = ref([
  { id: 1, name: 'Oliver', age: 4, interests: 'Dinosaurs, building blocks, chocolate cake' },
  { id: 2, name: 'Sophia', age: 6, interests: 'Mermaids, drawing, space travel' },
  { id: 3, name: 'Leo', age: 2, interests: 'Trains, ducks, music' },
])

const isAdding = ref(false)
const newProfile = ref({ name: '', age: '', interests: '' })

function addProfile() {
  if (newProfile.value.name) {
    profiles.value.push({ 
      id: Date.now(), 
      name: newProfile.value.name, 
      age: parseInt(newProfile.value.age as string), 
      interests: newProfile.value.interests 
    })
    newProfile.value = { name: '', age: '', interests: '' }
    isAdding.value = false
  }
}
</script>

<template>
  <div class="mx-auto max-w-5xl p-4 lg:p-6 pb-20">
    <div class="flex items-center justify-between mb-8">
      <div>
        <h1 class="text-3xl font-bold tracking-tight">Children Profiles</h1>
        <p class="text-muted-foreground">Manage profiles to create stories faster.</p>
      </div>
      <Button @click="isAdding = !isAdding">
        <IconPlus class="mr-2 size-4" /> {{ isAdding ? 'Cancel' : 'Add Child' }}
      </Button>
    </div>

    <div v-if="isAdding" class="mb-10">
      <Card>
        <CardHeader>
          <CardTitle>Add New Profile</CardTitle>
          <CardDescription>Tell us about your little hero.</CardDescription>
        </CardHeader>
        <CardContent class="grid gap-4 sm:grid-cols-2">
          <div class="space-y-2">
            <Label>Name</Label>
            <Input v-model="newProfile.name" placeholder="Name" />
          </div>
          <div class="space-y-2">
            <Label>Age</Label>
            <Input v-model="newProfile.age" type="number" placeholder="Age" />
          </div>
          <div class="space-y-2 sm:col-span-2">
            <Label>Interests (comma separated)</Label>
            <Input v-model="newProfile.interests" placeholder="Interests" />
          </div>
        </CardContent>
        <CardFooter class="flex justify-end gap-2">
           <Button variant="outline" @click="isAdding = false">Cancel</Button>
           <Button @click="addProfile">Save Profile</Button>
        </CardFooter>
      </Card>
    </div>

    <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      <Card v-for="profile in profiles" :key="profile.id">
        <CardHeader class="relative">
          <div class="flex h-12 w-12 items-center justify-center rounded-full bg-primary/10 text-primary mb-4">
            <IconUser class="size-6" />
          </div>
          <CardTitle>{{ profile.name }}</CardTitle>
          <CardDescription>{{ profile.age }} years old</CardDescription>
          <div class="absolute top-4 right-4 flex gap-1">
            <Button variant="ghost" size="icon" class="h-8 w-8 text-muted-foreground hover:text-foreground">
              <IconPencil class="size-4" />
            </Button>
            <Button variant="ghost" size="icon" class="h-8 w-8 text-muted-foreground hover:text-destructive">
              <IconTrash class="size-4" />
            </Button>
          </div>
        </CardHeader>
        <CardContent>
          <p class="text-sm font-medium text-muted-foreground mb-1">Favorite Things:</p>
          <p class="text-sm">{{ profile.interests }}</p>
        </CardContent>
        <CardFooter class="border-t pt-4">
           <Button variant="link" class="p-0 h-auto text-xs" as-child>
             <NuxtLink :to="`/create?child=${profile.name}`">Create story for {{ profile.name }}</NuxtLink>
           </Button>
        </CardFooter>
      </Card>
      
      <button 
        v-if="!isAdding"
        @click="isAdding = true"
        class="flex flex-col items-center justify-center gap-2 rounded-xl border border-dashed border-muted-foreground/30 p-10 transition-all hover:bg-muted/50 hover:border-primary/50 group"
      >
        <div class="flex h-12 w-12 items-center justify-center rounded-full border border-dashed border-muted-foreground/50 group-hover:border-primary group-hover:bg-primary/10 group-hover:text-primary">
          <IconPlus class="size-6" />
        </div>
        <p class="font-medium text-muted-foreground group-hover:text-primary">Add another profile</p>
      </button>
    </div>
  </div>
</template>
