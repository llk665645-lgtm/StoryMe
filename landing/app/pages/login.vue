<script setup lang="ts">
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { IconBrandGoogle, IconBrandGithub, IconSparkles } from '@tabler/icons-vue'
import LogoIcon from '@/components/LogoIcon.vue'

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
  <div class="relative min-h-screen flex items-center justify-center overflow-hidden">
    <DreamBackground />
    
    <div class="container relative z-10 mx-auto px-4 flex flex-col lg:flex-row items-center justify-center gap-16">
      <!-- Magical Info Side -->
      <div class="relative hidden lg:flex flex-col max-w-lg p-12 text-white bg-white/5 backdrop-blur-xl rounded-[3rem] border border-white/10 shadow-2xl overflow-hidden group">
        <div class="absolute inset-0 bg-gradient-to-br from-purple-500/10 to-pink-500/10 opacity-50 group-hover:opacity-100 transition-opacity"></div>
        <div class="absolute -top-24 -right-24 w-64 h-64 bg-purple-600/20 blur-[100px] rounded-full"></div>
        
        <div class="relative z-20 flex items-center gap-3 text-2xl font-bold tracking-tight mb-12">
          <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-[#8B5CF6] to-[#D946EF] text-white shadow-lg border border-white/20">
            <LogoIcon class="w-7 h-7 stroke-white fill-white" />
          </div>
          <span>Story<span class="text-white italic">Me</span></span>
        </div>
        
        <div class="relative z-20 mt-auto">
          <blockquote class="space-y-6">
            <p class="text-2xl italic font-serif leading-relaxed text-white/90">
              &ldquo;StoryMe has become our favorite bedtime ritual. My daughter loves being the hero of her own magical adventures every night.&rdquo;
            </p>
            <footer class="flex items-center gap-4">
              <div class="h-10 w-10 rounded-full bg-purple-500/30 border border-white/20"></div>
              <div>
                <div class="text-base font-bold text-white">Sarah M.</div>
                <div class="text-sm text-white/40 font-medium">Parent & Educator</div>
              </div>
            </footer>
          </blockquote>
        </div>
      </div>

      <!-- Login Form Side -->
      <div class="w-full max-w-md">
        <div class="bg-white/5 backdrop-blur-2xl p-10 sm:p-12 rounded-[3rem] border border-white/10 shadow-3xl">
          <div class="flex flex-col space-y-4 text-center mb-10">
            <h1 class="text-3xl font-bold tracking-tight text-white font-serif italic">Welcome Back</h1>
            <p class="text-base text-white/50">
              Enter your magic scrolls to continue the journey
            </p>
          </div>
          
          <div class="grid gap-8">
            <form @submit="onSubmit" class="space-y-6">
              <div class="space-y-4">
                <div class="space-y-2">
                  <Label class="text-white/70 ml-1 text-xs uppercase tracking-widest font-bold" for="email">Email</Label>
                  <Input
                    id="email"
                    v-model="email"
                    placeholder="name@example.com"
                    type="email"
                    class="h-14 bg-white/5 border-white/10 text-white placeholder:text-white/20 rounded-2xl focus:ring-purple-500 focus:border-purple-500"
                    :disabled="isLoading"
                  />
                </div>
                <div class="space-y-2">
                  <Label class="text-white/70 ml-1 text-xs uppercase tracking-widest font-bold" for="password">Password</Label>
                  <Input
                    id="password"
                    v-model="password"
                    placeholder="••••••••"
                    type="password"
                    class="h-14 bg-white/5 border-white/10 text-white placeholder:text-white/20 rounded-2xl focus:ring-purple-500 focus:border-purple-500"
                    :disabled="isLoading"
                  />
                </div>
              </div>
              
              <Button 
                class="w-full h-14 rounded-2xl bg-gradient-to-r from-[#8B5CF6] to-[#D946EF] text-white font-black text-base shadow-xl shadow-purple-900/40 hover:scale-[1.02] active:scale-95 transition-all"
                :disabled="isLoading"
              >
                <IconSparkles v-if="!isLoading" class="mr-2 h-5 w-5" />
                <span v-else class="mr-2 h-5 w-5 animate-spin">
                   <IconSparkles class="h-5 w-5" />
                </span>
                Login
              </Button>
            </form>

            <div class="relative">
              <div class="absolute inset-0 flex items-center">
                <span class="w-full border-t border-white/10" />
              </div>
              <div class="relative flex justify-center text-xs uppercase tracking-widest">
                <span class="bg-slate-950 px-4 text-white/40 font-bold">
                  Or continue with
                </span>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <Button variant="outline" type="button" class="h-14 rounded-2xl border-white/10 bg-white/5 text-white hover:bg-white/10 hover:border-white/20" :disabled="isLoading">
                <IconBrandGithub class="mr-2 h-5 w-5" />
                Github
              </Button>
              <Button variant="outline" type="button" class="h-14 rounded-2xl border-white/10 bg-white/5 text-white hover:bg-white/10 hover:border-white/20" :disabled="isLoading">
                <IconBrandGoogle class="mr-2 h-5 w-5" />
                Google
              </Button>
            </div>
          </div>

          <p class="mt-10 text-center text-sm text-white/40">
            By clicking continue, you agree to our
            <a href="/terms" class="text-purple-400 hover:text-purple-300 underline underline-offset-4">Terms</a>
            and
            <a href="/privacy" class="text-purple-400 hover:text-purple-300 underline underline-offset-4">Privacy</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
