<template>
  <section id="pricing" class="bg-[#0A0514]/80 py-24 sm:py-32 relative overflow-hidden">
    <!-- Inner stars and dark overlay for the section -->
    <div class="absolute inset-0 pointer-events-none">
      <div v-for="i in 50" :key="`local-star-${i}`" 
        class="absolute rounded-full bg-white opacity-20"
        :style="{
          top: `${Math.random() * 100}%`,
          left: `${Math.random() * 100}%`,
          width: '1px',
          height: '1px',
        }"
      />
    </div>
    
    <!-- Magical background glows -->
    <div class="absolute top-1/2 left-1/4 -translate-y-1/2 w-[600px] h-[600px] bg-purple-600/10 blur-[150px] rounded-full pointer-events-none"></div>
    <div class="absolute bottom-0 right-1/4 w-[500px] h-[500px] bg-pink-600/10 blur-[150px] rounded-full pointer-events-none"></div>

    <div class="mx-auto max-w-7xl px-6 lg:px-8 relative">
      <div class="mx-auto max-w-4xl text-center mb-16">
        <h2 class="text-base font-semibold leading-7 text-purple-400 uppercase tracking-widest">{{ $t('pricing.title') }}</h2>
        <p class="mt-4 text-4xl font-bold tracking-tight text-white sm:text-6xl font-serif italic">
          {{ $t('pricing.subtitle') }}
        </p>
        <p class="mt-6 text-lg leading-8 text-white/60 max-w-2xl mx-auto">
          {{ $t('pricing.description') }}
        </p>
      </div>

      <div class="isolate mx-auto mt-16 grid max-w-md grid-cols-1 gap-y-10 sm:mt-20 lg:mx-0 lg:max-w-none lg:grid-cols-3 lg:gap-x-8 xl:gap-x-12">
        <div v-for="tier in tierList" :key="tier.name" 
             class="relative flex flex-col justify-between rounded-[3rem] p-8 sm:p-10 transition-all duration-500 group hover:-translate-y-2 overflow-hidden"
             :class="tier.mostPopular 
               ? 'bg-[#1E1B4B]/60 backdrop-blur-3xl border-2 border-purple-500/50 shadow-[0_0_50px_-12px_rgba(168,85,247,0.4)] z-10 scale-105' 
               : 'bg-slate-950/40 backdrop-blur-2xl border border-white/10 hover:border-white/20 hover:bg-slate-900/40'">
          
          <div v-if="tier.mostPopular" class="absolute -top-px left-0 right-0 h-1 bg-gradient-to-r from-purple-500 via-pink-500 to-purple-500"></div>
          
          <div v-if="tier.mostPopular" class="absolute top-6 right-8">
             <span class="rounded-full bg-purple-500/20 px-3 py-1 text-xs font-bold text-purple-300 border border-purple-500/30">
               {{ $t('pricing.mostPopular') }}
             </span>
          </div>

          <div>
            <h3 class="text-lg font-bold leading-7 text-white/90 mb-6">
              {{ tier.name }}
            </h3>
            <div class="flex items-baseline gap-x-2">
              <span class="text-5xl font-black tracking-tight text-white">{{ tier.price }}</span>
              <span v-if="tier.price !== 'Custom'" class="text-sm font-medium leading-6 text-white/40 uppercase tracking-widest">{{ $t('pricing.perMonth') }}</span>
            </div>
            <p class="mt-6 text-base leading-7 text-white/50">
              {{ tier.description }}
            </p>
            
            <ul role="list" class="mt-8 space-y-4 text-sm leading-6 text-white/70">
              <li v-for="feature in tier.features" :key="feature" class="flex items-center gap-x-3">
                <div class="flex-none rounded-full bg-purple-500/10 p-1 border border-purple-500/20">
                  <Icon name="lucide:check" class="h-4 w-4 text-purple-400" aria-hidden="true" />
                </div>
                {{ feature }}
              </li>
            </ul>
          </div>

          <button
            @click="triggerAuth('register')"
            class="mt-10 block w-full rounded-2xl px-6 py-4 text-center text-sm font-black transition-all duration-300"
            :class="tier.mostPopular 
              ? 'bg-violet-600 text-white shadow-lg shadow-violet-900/20 hover:scale-[1.03] hover:shadow-violet-900/40 active:scale-95' 
              : 'bg-white/5 text-white border border-white/10 hover:bg-white/10 hover:border-white/30'"
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

const { t, tm, rt } = useI18n()
const { triggerAuth } = useAuth()

interface Tier {
  name: string
  price: string
  description: string
  features: string[]
  cta: string
  mostPopular?: boolean
}

const tierList = computed(() => {
  const raw = tm('pricing.tiers') as any[]
  if (!Array.isArray(raw)) return []
  return raw.map((item: any, index: number) => ({
    name: t(`pricing.tiers[${index}].name`),
    price: t(`pricing.tiers[${index}].price`),
    description: t(`pricing.tiers[${index}].description`),
    features: Array.isArray(item.features) ? item.features.map((_ : any, fIndex : number) => t(`pricing.tiers[${index}].features[${fIndex}]`)) : [],
    cta: t(`pricing.tiers[${index}].cta`),
    mostPopular: !!item.mostPopular
  })) as Tier[]
})
</script>
