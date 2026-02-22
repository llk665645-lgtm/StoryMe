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
        class="relative w-full max-w-md overflow-hidden rounded-[2.5rem] bg-[#0F172A]/90 backdrop-blur-2xl shadow-[0_20px_60px_rgba(0,0,0,0.5)] border border-white/10"
        :initial="{ opacity: 0, scale: 0.9, y: 20 }"
        :animate="{ opacity: 1, scale: 1, y: 0 }"
        :exit="{ opacity: 0, scale: 0.9, y: 20 }"
        :transition="{ type: 'spring', damping: 25, stiffness: 300 }"
      >
        <!-- Top accent bar -->
        <div class="h-1.5 bg-gradient-to-r from-[#8B5CF6] via-[#D946EF] to-[#8B5CF6] animate-gradient-x" />

        <div class="px-8 py-10">
          <div class="mb-8 text-center">
            <h2 class="text-3xl font-black tracking-tight text-white">
              {{ isLogin ? $t('auth.login.title') : $t('auth.register.title') }}
            </h2>
            <p class="mt-2 text-sm text-white/50 font-medium">
              {{ isLogin ? $t('auth.login.subtitle') : $t('auth.register.subtitle') }}
            </p>
          </div>

          <form @submit.prevent="handleSubmit" class="space-y-4">
            <div v-if="!isLogin" class="space-y-1">
              <label class="text-xs font-bold uppercase tracking-wider text-brand-gray ml-1">{{ $t('auth.form.fullName') }}</label>
              <input 
                type="text" 
                :placeholder="$t('auth.form.fullNamePlaceholder')"
                class="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-white transition-all focus:border-purple-400 focus:ring-4 focus:ring-purple-500/10 placeholder:text-white/30 outline-none"
              />
            </div>

            <div class="space-y-1">
              <label class="text-xs font-bold uppercase tracking-wider text-brand-gray ml-1">{{ $t('auth.form.email') }}</label>
              <input 
                type="email" 
                :placeholder="$t('auth.form.emailPlaceholder')"
                class="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-white transition-all focus:border-purple-400 focus:ring-4 focus:ring-purple-500/10 placeholder:text-white/30 outline-none"
              />
            </div>

            <div class="space-y-1">
              <label class="text-xs font-bold uppercase tracking-wider text-brand-gray ml-1">{{ $t('auth.form.password') }}</label>
              <input 
                type="password" 
                placeholder="••••••••"
                class="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-white transition-all focus:border-purple-400 focus:ring-4 focus:ring-purple-500/10 placeholder:text-white/30 outline-none"
              />
            </div>

            <button 
              type="submit"
              class="group relative w-full overflow-hidden rounded-2xl bg-gradient-to-r from-[#8B5CF6] to-[#D946EF] py-4 text-sm font-black text-white shadow-[0_8px_30px_rgba(139,92,246,0.3)] transition-all hover:scale-[1.02] active:scale-[0.98] border border-white/20"
            >
              <span class="relative z-10">{{ isLogin ? $t('auth.login.submit') : $t('auth.register.submit') }}</span>
              <div class="absolute inset-0 -z-0 bg-gradient-to-r from-white/0 via-white/20 to-white/0 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000" />
            </button>
          </form>

          <div class="mt-8 flex items-center justify-center gap-2 text-sm font-bold">
            <span class="text-white/40">
              {{ isLogin ? $t('auth.login.switch') : $t('auth.register.switch') }}
            </span>
            <button 
              class="text-purple-400 hover:text-purple-300 transition-colors"
              @click="isLogin = !isLogin"
            >
              {{ isLogin ? $t('auth.login.action') : $t('auth.register.action') }}
            </button>
          </div>
        </div>

        <!-- Social Auth -->
        <div class="bg-white/[0.03] border-t border-white/10 px-8 py-8">
          <div class="flex items-center gap-3">
             <div class="h-px flex-1 bg-white/10" />
             <span class="text-[10px] font-black uppercase tracking-widest text-white/40">{{ $t('auth.form.social') }}</span>
             <div class="h-px flex-1 bg-white/10" />
          </div>
          <div class="mt-6 grid grid-cols-2 gap-4">
            <button class="flex items-center justify-center gap-2 rounded-xl border border-white/10 bg-white/5 py-3 text-xs font-black text-white hover:bg-white/10 transition-all">
              <Icon name="logos:google-icon" class="size-4" />
              Google
            </button>
            <button class="flex items-center justify-center gap-2 rounded-xl border border-white/10 bg-white/5 py-3 text-xs font-black text-white hover:bg-white/10 transition-all">
              <Icon name="logos:github-icon" class="size-4" />
              GitHub
            </button>
          </div>
        </div>

        <!-- Close Button -->
        <button 
          class="absolute top-6 right-6 p-2 text-white/30 hover:text-white transition-colors"
          @click="$emit('close')"
        >
          <Icon name="lucide:x" class="size-6" />
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
  // Simulate auth delay
  setTimeout(() => {
    emit('close');
    navigateTo('/dashboard');
  }, 500);
};
</script>
