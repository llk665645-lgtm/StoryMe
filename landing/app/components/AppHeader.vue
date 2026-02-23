<template>
  <header 
    class="fixed top-0 left-0 right-0 z-[50] transition-all duration-300 border-b border-transparent backdrop-blur-sm"
    :class="{ 'border-white/10 bg-black/20': scrolled }"
  >
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="grid h-20 grid-cols-2 md:grid-cols-[1fr_auto_1fr] items-center">
        <!-- Logo -->
        <div class="flex items-center gap-2">
          <div class="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-[#8B5CF6] to-[#D946EF] text-white border border-white/20">
            <LogoIcon class="w-6 h-6 stroke-white fill-white" />
          </div>
          <span class="text-xl font-bold tracking-tight text-white group cursor-default">
            Story<span class="text-transparent bg-clip-text bg-gradient-to-r from-white to-purple-200 italic">Me</span>
          </span>
        </div>

        <!-- Desktop Navigation - Perfectly Centered -->
        <nav class="hidden md:flex items-center justify-center gap-8 px-4">
          <NuxtLink to="/" class="text-sm font-medium text-white/70 hover:text-white transition-colors whitespace-nowrap">
            {{ $t('header.features') }}
          </NuxtLink>
          <NuxtLink to="/about" class="text-sm font-medium text-white/70 hover:text-white transition-colors whitespace-nowrap">
            {{ $t('header.about') }}
          </NuxtLink>
          <NuxtLink to="/blog" class="text-sm font-medium text-white/70 hover:text-white transition-colors whitespace-nowrap">
            {{ $t('header.blog') }}
          </NuxtLink>
          <NuxtLink to="/pricing" class="text-sm font-medium text-white/70 hover:text-white transition-colors whitespace-nowrap">
            {{ $t('header.pricing') }}
          </NuxtLink>
        </nav>

        <!-- CTA Action -->
        <div class="flex items-center justify-end gap-3">
          <!-- Language Switcher -->
          <div class="hidden sm:flex items-center bg-white/5 rounded-lg p-1 border border-white/10">
            <button 
              v-for="locale in ['en', 'ru']" 
              :key="locale"
              @click="setLocale(locale as any)"
              class="px-2 py-1 text-[10px] font-black uppercase transition-all rounded-md"
              :class="currentLocale === locale ? 'bg-[#8B5CF6] text-white' : 'text-white/60 hover:text-white'"
            >
              {{ locale }}
            </button>
          </div>

          <template v-if="!authStore.isAuthenticated">
            <button 
              class="hidden sm:block text-sm font-semibold text-white/80 hover:text-white transition-colors"
              @click="openAuth('login')"
            >
              {{ $t('header.login') }}
            </button>
            <button 
              class="rounded-full bg-gradient-to-r from-[#8B5CF6] to-[#D946EF] px-8 py-3 text-sm font-black text-white transition-all hover:scale-105 active:scale-95 border border-white/20"
              @click="openAuth('register')"
            >
              {{ $t('header.getStarted') }}
            </button>
          </template>
          
          <template v-else>
            <div class="flex items-center gap-4">
              <span class="hidden lg:block text-sm font-bold text-white/60">
                Hi, {{ authStore.user?.full_name || 'Hero' }}
              </span>
              <button 
                @click="authStore.logout()"
                class="text-sm font-semibold text-white/60 hover:text-white transition-colors"
              >
                Logout
              </button>
            </div>
          </template>
          
          <!-- Mobile Menu Toggle -->
          <button class="md:hidden text-white p-2" @click="isMenuOpen = !isMenuOpen">
            <Icon :name="isMenuOpen ? 'lucide:x' : 'lucide:menu'" class="size-6" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Navigation -->
    <div v-if="isMenuOpen" class="md:hidden border-t border-white/10 bg-slate-950/95 backdrop-blur-xl px-4 py-8 shadow-2xl animate-in fade-in slide-in-from-top-4 duration-500">
      <nav class="flex flex-col gap-4">
        <NuxtLink to="/" class="text-base font-bold text-white/70 hover:text-white" @click="isMenuOpen = false">
          {{ $t('header.features') }}
        </NuxtLink>
        <NuxtLink to="/about" class="text-base font-bold text-white/70 hover:text-white" @click="isMenuOpen = false">
          {{ $t('header.about') }}
        </NuxtLink>
        <NuxtLink to="/blog" class="text-base font-bold text-white/70 hover:text-white" @click="isMenuOpen = false">
          {{ $t('header.blog') }}
        </NuxtLink>
        <NuxtLink to="/pricing" class="text-base font-bold text-white/70 hover:text-white" @click="isMenuOpen = false">
          {{ $t('header.pricing') }}
        </NuxtLink>

        <div class="flex items-center gap-3 mt-4">
          <span class="text-[10px] text-white/40 font-black uppercase tracking-widest">Language:</span>
          <div class="flex gap-2 bg-white/5 p-1 rounded-lg border border-white/10">
            <button 
              v-for="locale in ['en', 'ru']" 
              :key="locale"
              @click="setLocale(locale as any)"
              class="px-3 py-1.5 text-[10px] font-black uppercase transition-all rounded-md"
              :class="currentLocale === locale ? 'bg-purple-600 text-white' : 'text-white/40'"
            >
              {{ locale }}
            </button>
          </div>
        </div>

        <hr class="border-white/10 my-6" />
        <template v-if="!authStore.isAuthenticated">
          <button 
            class="w-full rounded-2xl bg-white/10 py-4 text-center font-bold text-white mb-2"
            @click="openAuth('login')"
          >
            {{ $t('header.login') }}
          </button>
          <button 
            class="w-full rounded-2xl bg-gradient-to-r from-[#8B5CF6] to-[#D946EF] py-4 text-center font-black text-white shadow-lg shadow-purple-900/20"
            @click="openAuth('register')"
          >
            {{ $t('header.getStarted') }}
          </button>
        </template>
        <template v-else>
          <button 
            @click="authStore.logout()"
            class="w-full py-4 text-center font-bold text-white/60"
          >
            Logout
          </button>
        </template>
      </nav>
    </div>

    <!-- Auth Modal - Teleported to Body for perfect layout -->
    <Teleport to="body">
      <AuthModal 
        :is-open="isAuthOpen" 
        :initial-mode="authMode" 
        @close="isAuthOpen = false" 
      />
    </Teleport>

  </header>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { useI18n } from 'vue-i18n';
import { useAuth } from '~/composables/useAuth';
import { useAuthStore } from '~/stores/auth';

const { t, locale: currentLocale, setLocale } = useI18n();
const { isAuthOpen, authMode, triggerAuth, closeAuth } = useAuth();
const authStore = useAuthStore();

const scrolled = ref(false);
const isMenuOpen = ref(false);

const openAuth = (mode: 'login' | 'register') => {
  triggerAuth(mode);
  isMenuOpen.value = false;
};

const handleScroll = () => {
  scrolled.value = window.scrollY > 20;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>
