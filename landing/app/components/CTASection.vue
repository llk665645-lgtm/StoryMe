<template>
  <section class="bg-transparent py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="relative isolate overflow-hidden bg-white/5 backdrop-blur-3xl px-6 py-24 text-center shadow-2xl rounded-[3.5rem] border border-white/10 sm:px-16">
        <h2 class="mx-auto max-w-2xl text-3xl font-bold tracking-tight text-white sm:text-4xl">
          {{ $t('cta.title') }}
          <span class="block text-white/60 italic font-serif mt-2">{{ $t('cta.subtitle') }}</span>
        </h2>
        <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-white/50">
          {{ $t('cta.description') }}
        </p>
        <div class="mt-10 flex items-center justify-center gap-x-6">
          <button 
            @click="triggerAuth('register')"
            class="rounded-2xl bg-white px-8 py-4 text-base font-bold text-dream-deep shadow-[0_8px_30px_rgba(0,0,0,0.3)] hover:scale-105 active:scale-95 transition-all duration-300"
          >
            {{ $t('cta.button') }}
          </button>
          <a href="#how-it-works" class="text-sm font-semibold leading-6 text-white hover:text-white/70 transition-colors">
            {{ $t('cta.link') }} <span aria-hidden="true">→</span>
          </a>
        </div>
        
        <!-- Subtle Glow -->
        <div class="absolute -top-24 left-1/2 -z-10 -translate-x-1/2 blur-3xl" aria-hidden="true">
          <div class="aspect-[1155/678] w-[72.1875rem] bg-gradient-to-tr from-white/10 to-white/5 opacity-30" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useAuth } from '~/composables/useAuth'
const { triggerAuth } = useAuth()
</script>
