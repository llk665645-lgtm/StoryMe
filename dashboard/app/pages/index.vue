<template>
  <div class="flex min-h-screen items-center justify-center bg-background p-4">
    <div class="mx-auto w-full max-w-sm space-y-6 text-center">
      <div class="space-y-2">
        <h1 class="text-3xl font-bold">StoryMe Dashboard</h1>
        <p class="text-muted-foreground text-sm">
          Management portal for StoryMe AI
        </p>
      </div>
      <div class="grid gap-4">
        <Button as-child class="w-full">
          <NuxtLink to="/login">Go to Login</NuxtLink>
        </Button>
        <Button variant="outline" as-child class="w-full">
          <NuxtLink to="/dashboard">Go to Dashboard</NuxtLink>
        </Button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Button } from '@/components/ui/button'
</script>
