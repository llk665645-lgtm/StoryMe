<template>
  <section id="worlds" class="py-24 bg-white relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-0 right-0 -translate-y-1/2 translate-x-1/2 w-96 h-96 bg-primary/5 rounded-full blur-3xl"></div>
    <div class="absolute bottom-0 left-0 translate-y-1/2 -translate-x-1/2 w-96 h-96 bg-primary/5 rounded-full blur-3xl"></div>

    <div class="mx-auto max-w-7xl px-6 lg:px-8 relative">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-base font-semibold leading-7 text-primary uppercase tracking-widest">{{ $t('generator.themeLabel') }}</h2>
        <p class="mt-2 text-4xl font-bold tracking-tight text-brand-dark sm:text-5xl font-serif">
          {{ $t('generator.showcase.title') }}
        </p>
        <p class="mt-6 text-lg leading-8 text-brand-gray">
          {{ $t('generator.showcase.subtitle') }}
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div 
          v-for="(label, key) in themes" 
          :key="key"
          class="group relative aspect-[4/5] rounded-[2.5rem] overflow-hidden bg-brand-light border border-brand-dark/5 shadow-lg transition-all duration-500 hover:-translate-y-2 hover:shadow-2xl"
        >
          <!-- Theme Image -->
          <img 
            :src="`/images/themes/${key}.webp`" 
            :alt="label"
            class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
          />
          
          <!-- Overlay -->
          <div class="absolute inset-0 bg-gradient-to-t from-brand-dark/80 via-brand-dark/20 to-transparent opacity-60 group-hover:opacity-80 transition-opacity"></div>
          
          <!-- Content -->
          <div class="absolute inset-0 flex flex-col justify-end p-8 text-white">
            <div class="flex items-center gap-3 mb-2 translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
               <div class="p-2 rounded-xl bg-white/20 backdrop-blur-md">
                 <Icon :name="themeIcons[key] || 'lucide:sparkles'" class="size-6 text-white" />
               </div>
               <span class="text-sm font-bold uppercase tracking-widest">{{ label }}</span>
            </div>
            <h3 class="text-2xl font-serif italic font-bold mb-4 translate-y-4 group-hover:translate-y-0 transition-transform duration-500 delay-75">
               Мир {{ label.toLowerCase() }}
            </h3>
            
            <button 
              @click="scrollToGenerator"
              class="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-primary bg-white px-5 py-3 rounded-full w-fit opacity-0 group-hover:opacity-100 transition-all duration-500 delay-150 transform scale-90 group-hover:scale-100"
            >
              {{ $t('generator.showcase.cta') }}
              <Icon name="lucide:arrow-right" class="size-3" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { tm } = useI18n()

const themes = computed(() => (tm('generator.themes') || {}) as Record<string, string>)

const themeIcons: Record<string, string> = {
  forest: 'lucide:tree-pine',
  space: 'lucide:rocket',
  ocean: 'lucide:waves',
  dino: 'lucide:bone',
  magic: 'lucide:sparkles',
  super: 'lucide:zap'
}

function scrollToGenerator() {
  const element = document.getElementById('generator')
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>
