<template>
  <section id="pricing" class="bg-transparent py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-4xl text-center">
        <h2 class="text-base font-semibold leading-7 text-white/50 uppercase tracking-widest">{{ $t('pricing.title') }}</h2>
        <p class="mt-2 text-4xl font-bold tracking-tight text-white sm:text-5xl">
          {{ $t('pricing.subtitle') }}
        </p>
      </div>
      <p class="mx-auto mt-6 max-w-2xl text-center text-lg leading-8 text-white/60">
        {{ $t('pricing.description') }}
      </p>

      <div class="isolate mx-auto mt-16 grid max-w-md grid-cols-1 gap-y-12 sm:mt-20 lg:mx-0 lg:max-w-none lg:grid-cols-3 lg:gap-x-8 xl:gap-x-12">
        <div v-for="tier in tierList" :key="tier.name" 
             class="relative flex flex-col justify-between rounded-[2.5rem] bg-white/5 backdrop-blur-xl p-8 border border-white/10 sm:p-10 transition-all duration-500 hover:bg-white/10 hover:shadow-2xl"
             :class="{ 'border-white bg-white/10 scale-105 z-10 shadow-[0_0_40px_rgba(255,255,255,0.05)]': tier.mostPopular }">
          <div v-if="tier.mostPopular" class="absolute -top-4 left-1/2 -translate-x-1/2 rounded-full bg-white px-4 py-1 text-[10px] font-black text-dream-deep uppercase tracking-widest shadow-lg">
            {{ $t('pricing.mostPopular') }}
          </div>
          <div>
            <h3 class="text-base font-bold leading-7 text-white/80">
              {{ tier.name }}
            </h3>
            <div class="mt-4 flex items-baseline gap-x-1">
              <span class="text-4xl font-bold tracking-tight text-white">{{ tier.price }}</span>
              <span v-if="tier.price !== 'Custom'" class="text-sm font-semibold leading-6 text-white/40">{{ $t('pricing.perMonth') }}</span>
            </div>
            <p class="mt-6 text-base leading-7 text-white/60">
              {{ tier.description }}
            </p>
            <ul role="list" class="mt-10 space-y-4 text-sm leading-6 text-white/70">
              <li v-for="feature in tier.features" :key="feature" class="flex gap-x-3">
                <Icon name="lucide:check" class="h-6 w-5 flex-none text-white/40" aria-hidden="true" />
                {{ feature }}
              </li>
            </ul>
          </div>
          <button
            @click="triggerAuth('register')"
            class="mt-8 block rounded-2xl px-6 py-4 text-center text-sm font-bold leading-6 transition-all duration-300 shadow-[0_8px_20px_rgba(0,0,0,0.25)]"
            :class="tier.mostPopular 
              ? 'bg-white text-dream-deep hover:scale-105 hover:shadow-[0_12px_30px_rgba(255,255,255,0.15)] active:scale-95' 
              : 'bg-white/10 text-white border border-white/10 hover:border-white/40 hover:bg-white/15'"
          >
            {{ tier.cta }}
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useAuth } from '~/composables/useAuth'

const { tm } = useI18n()
const { triggerAuth } = useAuth()

interface Tier {
  name: string
  price: string
  description: string
  features: string[]
  cta: string
  mostPopular?: boolean
}

const tierList = computed(() => tm('pricing.tiers') as Tier[])
</script>
