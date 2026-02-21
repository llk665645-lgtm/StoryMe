<script setup lang="ts">
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { IconBrandGoogle, IconBrandGithub } from '@tabler/icons-vue'

definePageMeta({
  layout: false
})

const email = ref('')
const password = ref('')
const isLoading = ref(false)

async function onSubmit(event: Event) {
  event.preventDefault()
  isLoading.value = true
  
  // Simulate login
  setTimeout(() => {
    isLoading.value = false
    navigateTo('/dashboard')
  }, 1000)
}
</script>

<template>
  <div class="container relative min-h-screen flex-col items-center justify-center grid lg:max-w-none lg:grid-cols-2 lg:px-0">
    <div class="relative hidden h-full flex-col bg-muted p-10 text-white dark:border-r lg:flex">
      <div class="absolute inset-0 bg-zinc-900" />
      <div class="relative z-20 flex items-center text-lg font-medium">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="mr-2 h-6 w-6"
        >
          <path d="M15 6v12a3 3 0 1 0 3-3H6a3 3 0 1 0 3 3V6a3 3 0 1 0-3 3h12a3 3 0 1 0-3-3" />
        </svg>
        StoryMe
      </div>
      <div class="relative z-20 mt-auto">
        <blockquote class="space-y-2">
          <p class="text-lg">
            &ldquo;This dashboard has saved me countless hours of work and helped me deliver stunning stories to my children faster than ever before.&rdquo;
          </p>
          <footer class="text-sm">Sofia Davis</footer>
        </blockquote>
      </div>
    </div>
    <div class="lg:p-8">
      <div class="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]">
        <div class="flex flex-col space-y-2 text-center">
          <h1 class="text-2xl font-semibold tracking-tight">Login to your account</h1>
          <p class="text-sm text-muted-foreground">
            Enter your email below to login to your account
          </p>
        </div>
        <div class="grid gap-6">
          <form @submit="onSubmit">
            <div class="grid gap-2">
              <div class="grid gap-1">
                <Label class="sr-only" for="email">
                  Email
                </Label>
                <Input
                  id="email"
                  v-model="email"
                  placeholder="name@example.com"
                  type="email"
                  auto-capitalize="none"
                  auto-complete="email"
                  auto-correct="off"
                  :disabled="isLoading"
                />
              </div>
              <div class="grid gap-1">
                <Label class="sr-only" for="password">
                  Password
                </Label>
                <Input
                  id="password"
                  v-model="password"
                  placeholder="••••••••"
                  type="password"
                  auto-complete="current-password"
                  :disabled="isLoading"
                />
              </div>
              <Button :disabled="isLoading">
                <span v-if="isLoading" class="mr-2 h-4 w-4 animate-spin">
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
                Login
              </Button>
            </div>
          </form>
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <span class="w-full border-t" />
            </div>
            <div class="relative flex justify-center text-xs uppercase">
              <span class="bg-background px-2 text-muted-foreground">
                Or continue with
              </span>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <Button variant="outline" type="button" :disabled="isLoading">
              <IconBrandGithub class="mr-2 h-4 w-4" />
              Github
            </Button>
            <Button variant="outline" type="button" :disabled="isLoading">
              <IconBrandGoogle class="mr-2 h-4 w-4" />
              Google
            </Button>
          </div>
        </div>
        <p class="px-8 text-center text-sm text-muted-foreground">
          By clicking continue, you agree to our
          <a href="/terms" class="underline underline-offset-4 hover:text-primary">
            Terms of Service
          </a>
          and
          <a href="/privacy" class="underline underline-offset-4 hover:text-primary">
            Privacy Policy
          </a>
          .
        </p>
      </div>
    </div>
  </div>
</template>
