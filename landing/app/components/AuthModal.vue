<template>
  <AnimatePresence>
    <div 
      v-if="isOpen" 
      class="fixed inset-0 z-[100] flex items-center justify-center p-4 sm:p-6"
    >
      <!-- Backdrop -->
      <Motion
        class="absolute inset-0 bg-brand-dark/40 backdrop-blur-sm"
        :initial="{ opacity: 0 }"
        :animate="{ opacity: 1 }"
        :exit="{ opacity: 0 }"
        @click="$emit('close')"
      />

      <!-- Modal Container -->
      <Motion
        class="relative w-full max-w-md overflow-hidden rounded-3xl bg-white shadow-2xl ring-1 ring-border"
        :initial="{ opacity: 0, scale: 0.9, y: 20 }"
        :animate="{ opacity: 1, scale: 1, y: 0 }"
        :exit="{ opacity: 0, scale: 0.9, y: 20 }"
        :transition="{ type: 'spring', damping: 25, stiffness: 300 }"
      >
        <!-- Top accent bar -->
        <div class="h-2 bg-primary" />

        <div class="px-8 py-10">
          <div class="mb-8 text-center">
            <h2 class="text-3xl font-bold tracking-tight text-brand-dark">
              {{ isLogin ? 'Welcome Back' : 'Join the Community' }}
            </h2>
            <p class="mt-2 text-sm text-brand-gray">
              {{ isLogin ? 'Sign in to access your personalized wisdom' : 'Start your journey to daily inspiration' }}
            </p>
          </div>

          <form @submit.prevent="handleSubmit" class="space-y-4">
            <div v-if="!isLogin" class="space-y-1">
              <label class="text-xs font-bold uppercase tracking-wider text-brand-gray ml-1">Full Name</label>
              <input 
                type="text" 
                placeholder="Mindful Soul"
                class="w-full rounded-xl border border-border bg-brand-light/50 px-4 py-3 text-sm transition-all focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none"
              />
            </div>

            <div class="space-y-1">
              <label class="text-xs font-bold uppercase tracking-wider text-brand-gray ml-1">Email Address</label>
              <input 
                type="email" 
                placeholder="you@example.com"
                class="w-full rounded-xl border border-border bg-brand-light/50 px-4 py-3 text-sm transition-all focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none"
              />
            </div>

            <div class="space-y-1">
              <label class="text-xs font-bold uppercase tracking-wider text-brand-gray ml-1">Password</label>
              <input 
                type="password" 
                placeholder="••••••••"
                class="w-full rounded-xl border border-border bg-brand-light/50 px-4 py-3 text-sm transition-all focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none"
              />
            </div>

            <button 
              type="submit"
              class="group relative w-full overflow-hidden rounded-xl bg-primary py-4 text-sm font-bold text-white shadow-lg transition-all hover:scale-[1.02] active:scale-[0.98]"
            >
              <span class="relative z-10">{{ isLogin ? 'Sign In' : 'Create Account' }}</span>
              <div class="absolute inset-0 -z-0 bg-gradient-to-r from-white/0 via-white/10 to-white/0 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700" />
            </button>
          </form>

          <div class="mt-8 flex items-center justify-center gap-2 text-sm">
            <span class="text-brand-gray">
              {{ isLogin ? "Don't have an account?" : "Already have an account?" }}
            </span>
            <button 
              class="font-bold text-primary hover:underline"
              @click="isLogin = !isLogin"
            >
              {{ isLogin ? 'Sign up' : 'Log in' }}
            </button>
          </div>
        </div>

        <!-- Social Auth (Visual only) -->
        <div class="bg-brand-light/50 border-t border-border px-8 py-6">
          <div class="flex items-center gap-3">
             <div class="h-px flex-1 bg-border" />
             <span class="text-[10px] font-bold uppercase tracking-widest text-brand-gray">Or continue with</span>
             <div class="h-px flex-1 bg-border" />
          </div>
          <div class="mt-4 grid grid-cols-2 gap-3">
            <button class="flex items-center justify-center gap-2 rounded-xl border border-border bg-white py-2 text-xs font-bold text-brand-dark hover:bg-brand-light transition-colors">
              <Icon name="logos:google-icon" class="size-4" />
              Google
            </button>
            <button class="flex items-center justify-center gap-2 rounded-xl border border-border bg-white py-2 text-xs font-bold text-brand-dark hover:bg-brand-light transition-colors">
              <Icon name="logos:github-icon" class="size-4" />
              GitHub
            </button>
          </div>
        </div>

        <!-- Close Button -->
        <button 
          class="absolute top-4 right-4 p-2 text-brand-gray hover:text-brand-dark transition-colors"
          @click="$emit('close')"
        >
          <Icon name="lucide:x" class="size-5" />
        </button>
      </Motion>
    </div>
  </AnimatePresence>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { Motion, AnimatePresence } from 'motion-v';

const props = defineProps<{
  isOpen: boolean;
  initialMode?: 'login' | 'register';
}>();

const emit = defineEmits<{
  (e: 'close'): void;
}>();

const isLogin = ref(props.initialMode === 'login');

// Sync mode when modal opens if provided
watch(() => props.isOpen, (val) => {
  if (val && props.initialMode) {
    isLogin.value = props.initialMode === 'login';
  }
});

const handleSubmit = () => {
  // Logic placeholder
  console.log('Auth submitted');
};
</script>
