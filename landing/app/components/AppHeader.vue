<template>
  <header 
    class="fixed top-0 left-0 right-0 z-[50] transition-all duration-300 border-b border-transparent backdrop-blur-sm"
    :class="{ 'border-white/10 bg-black/20': scrolled }"
  >
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="grid h-20 grid-cols-2 md:grid-cols-[1fr_auto_1fr] items-center">
        <!-- Logo -->
        <div class="flex items-center gap-2">
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-white text-dream-deep shadow-lg">
            <LogoIcon class="w-6 h-6 stroke-dream-deep fill-dream-deep" />
          </div>
          <span class="text-xl font-bold tracking-tight text-white">
            Story<span class="text-white/80 italic">Me</span>
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
              class="px-2 py-1 text-[10px] font-bold uppercase transition-all rounded"
              :class="currentLocale === locale ? 'bg-white text-dream-deep shadow-sm' : 'text-white/60 hover:text-white'"
            >
              {{ locale }}
            </button>
          </div>

          <button 
            class="hidden sm:block text-sm font-semibold text-white/80 hover:text-white transition-colors"
            @click="openAuth('login')"
          >
            {{ $t('header.login') }}
          </button>
          <button 
            class="rounded-full bg-white px-6 py-2.5 text-sm font-bold text-dream-deep shadow-[0_8px_20px_rgba(0,0,0,0.25)] transition-all hover:scale-105 hover:shadow-[0_12px_24px_rgba(255,255,255,0.15)] active:scale-95"
            @click="openAuth('register')"
          >
            {{ $t('header.getStarted') }}
          </button>
          
          <!-- Mobile Menu Toggle -->
          <button class="md:hidden text-white p-2" @click="isMenuOpen = !isMenuOpen">
            <Icon :name="isMenuOpen ? 'lucide:x' : 'lucide:menu'" class="size-6" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Navigation -->
    <div v-if="isMenuOpen" class="md:hidden border-t border-border/50 bg-white px-4 py-6 shadow-xl animate-in fade-in slide-in-from-top-4 duration-300">
      <nav class="flex flex-col gap-4">
        <NuxtLink to="/" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.features') }}
        </NuxtLink>
        <NuxtLink to="/about" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.about') }}
        </NuxtLink>
        <NuxtLink to="/blog" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.blog') }}
        </NuxtLink>
        <NuxtLink to="/pricing" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.pricing') }}
        </NuxtLink>

        <div class="flex items-center gap-2 mt-2">
          <span class="text-xs text-brand-gray font-medium uppercase">Language:</span>
          <div class="flex gap-2">
            <button 
              v-for="locale in ['en', 'ru']" 
              :key="locale"
              @click="setLocale(locale as any)"
              class="px-3 py-1 text-xs font-bold uppercase border border-border rounded-lg"
              :class="currentLocale === locale ? 'bg-primary text-white border-primary' : 'text-brand-gray bg-white'"
            >
              {{ locale }}
            </button>
          </div>
        </div>

        <hr class="border-border/50 my-2" />
        <button 
          class="w-full rounded-xl bg-primary py-3 text-center font-bold text-white shadow-md"
          @click="openAuth('register')"
        >
          {{ $t('header.getStarted') }}
        </button>
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

const { t, locale: currentLocale, setLocale } = useI18n();
const { isAuthOpen, authMode, triggerAuth, closeAuth } = useAuth();

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
