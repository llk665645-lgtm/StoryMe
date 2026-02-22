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
                v-model="form.fullName"
                type="text" 
                required
                :placeholder="$t('auth.form.fullNamePlaceholder')"
                class="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-white transition-all focus:border-purple-400 focus:ring-4 focus:ring-purple-500/10 placeholder:text-white/30 outline-none"
              />
            </div>

            <div class="space-y-1">
              <label class="text-xs font-bold uppercase tracking-wider text-brand-gray ml-1">{{ $t('auth.form.email') }}</label>
              <input 
                v-model="form.email"
                type="email" 
                required
                :placeholder="$t('auth.form.emailPlaceholder')"
                class="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-white transition-all focus:border-purple-400 focus:ring-4 focus:ring-purple-500/10 placeholder:text-white/30 outline-none"
              />
            </div>

            <div class="space-y-1">
              <label class="text-xs font-bold uppercase tracking-wider text-brand-gray ml-1">{{ $t('auth.form.password') }}</label>
              <input 
                v-model="form.password"
                type="password" 
                required
                placeholder="••••••••"
                class="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3.5 text-sm text-white transition-all focus:border-purple-400 focus:ring-4 focus:ring-purple-500/10 placeholder:text-white/30 outline-none"
              />
            </div>

            <p v-if="error" class="text-red-400 text-xs font-bold px-1 mt-2">
              {{ error }}
            </p>

            <button 
              type="submit"
              :disabled="isLoading"
              class="group relative w-full overflow-hidden rounded-2xl bg-gradient-to-r from-[#8B5CF6] to-[#D946EF] py-4 text-sm font-black text-white shadow-[0_8px_30px_rgba(139,92,246,0.3)] transition-all hover:scale-[1.02] active:scale-[0.98] border border-white/20 disabled:opacity-50 disabled:scale-100"
            >
              <span class="relative z-10">
                {{ isLoading ? 'Processing...' : (isLogin ? $t('auth.login.submit') : $t('auth.register.submit')) }}
              </span>
              <div class="absolute inset-0 -z-0 bg-gradient-to-r from-white/0 via-white/20 to-white/0 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000" />
            </button>
          </form>

          <div class="mt-8 flex items-center justify-center gap-2 text-sm font-bold">
            <span class="text-white/40">
              {{ isLogin ? $t('auth.login.switch') : $t('auth.register.switch') }}
            </span>
            <button 
              class="text-purple-400 hover:text-purple-300 transition-colors"
              @click="isLogin = !isLogin; error = ''"
            >
              {{ isLogin ? $t('auth.login.action') : $t('auth.register.action') }}
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
import { ref, reactive, watch } from 'vue';
import { Motion, AnimatePresence } from 'motion-v';
import { useAuthStore } from '~/stores/auth';

const authStore = useAuthStore();

const props = defineProps<{
  isOpen: boolean;
  initialMode?: 'login' | 'register';
}>();

const emit = defineEmits<{
  (e: 'close'): void;
}>();

const isLogin = ref(props.initialMode === 'login');
const isLoading = ref(false);
const error = ref('');

const form = reactive({
  fullName: '',
  email: '',
  password: ''
});

// Sync mode when modal opens if provided
watch(() => props.isOpen, (val) => {
  if (val && props.initialMode) {
    isLogin.value = props.initialMode === 'login';
  }
  if (!val) {
    error.value = '';
    form.fullName = '';
    form.email = '';
    form.password = '';
  }
});

const handleSubmit = async () => {
  isLoading.value = true;
  error.value = '';
  
  try {
    const endpoint = isLogin.value ? '/auth/login' : '/auth/register';
    const body = isLogin.value 
      ? new URLSearchParams({ username: form.email, password: form.password })
      : JSON.stringify({ email: form.email, password: form.password, full_name: form.fullName });
    
    const headers: Record<string, string> = {};
    if (!isLogin.value) {
      headers['Content-Type'] = 'application/json';
    } else {
      headers['Content-Type'] = 'application/x-www-form-urlencoded';
    }

    const response = await fetch(`http://127.0.0.1:8000${endpoint}`, {
      method: 'POST',
      headers,
      body: body
    });

    let data;
    try {
      data = await response.json();
    } catch (parseError) {
      error.value = 'Server returned an invalid response. Please try again later.';
      return;
    }

    if (!response.ok) {
      error.value = data.detail || (data.message || 'Authentication failed');
      return;
    }

    if (!data.data || !data.data.access_token) {
      error.value = 'Invalid response format from server';
      return;
    }

    // Store tokens
    const { access_token, refresh_token } = data.data;
    authStore.setTokens(access_token, refresh_token);
    await authStore.fetchUser();

    emit('close');
    // Instead of dashboard, we stay on home or refresh
    window.location.reload();
  } catch (e: any) {
    console.error('Auth error:', e);
    error.value = 'Connection error. Is the backend running?';
  } finally {
    isLoading.value = false;
  }
};
</script>
