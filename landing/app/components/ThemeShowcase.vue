<template>
  <section id="worlds" class="py-24 bg-transparent relative overflow-hidden">
    <div class="mx-auto max-w-7xl px-6 lg:px-8 relative">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-base font-semibold leading-7 text-white/50 uppercase tracking-widest">{{ $t('generator.themeLabel') }}</h2>
        <p class="mt-2 text-4xl font-bold tracking-tight text-white sm:text-5xl font-serif">
          {{ $t('generator.showcase.title') }}
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div 
          v-for="(label, key) in themes" 
          :key="key"
          class="group relative aspect-[4/5] rounded-[2.5rem] overflow-hidden border border-white/10 shadow-lg transition-all duration-500 hover:-translate-y-2 hover:shadow-2xl"
          :class="themeGradients[key] || 'bg-white/5'"
        >
          <!-- Background Image -->
          <div v-if="themeImages[key]" class="absolute inset-0 z-0">
            <img 
              :src="themeImages[key]" 
              :alt="label" 
              class="w-full h-full object-cover opacity-40 group-hover:opacity-60 group-hover:scale-110 transition-all duration-1000"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-[#0F172A] via-[#0F172A]/40 to-transparent"></div>
          </div>

          <!-- Animated Background Glow -->
          <div class="absolute inset-0 opacity-20 group-hover:opacity-40 transition-opacity duration-500 bg-[radial-gradient(circle_at_50%_0%,rgba(255,255,255,0.2),transparent_70%)]"></div>
          
          <div class="absolute inset-x-0 bottom-0 flex flex-col justify-end p-10 text-white z-10">
            <div class="flex items-center gap-3 mb-2 translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
              <div class="p-2 rounded-xl bg-white/20 backdrop-blur-md">
                <Icon :name="themeIcons[key] || 'lucide:sparkles'" class="size-6 text-white" />
              </div>
              <span class="text-sm font-bold uppercase tracking-widest text-white/90">{{ label }}</span>
            </div>
            <h3 class="text-3xl font-serif italic font-bold mb-6 translate-y-4 group-hover:translate-y-0 transition-transform duration-500 delay-75 capitalize">
              {{ label }}
            </h3>
            
            <button 
              @click="scrollToGenerator"
              class="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-white bg-gradient-to-r from-white/10 to-white/20 backdrop-blur-xl border border-white/20 px-6 py-3.5 rounded-full w-fit opacity-0 group-hover:opacity-100 transition-all duration-500 delay-150 transform scale-90 group-hover:scale-100 shadow-xl hover:bg-white/30 hover:shadow-white/10"
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

const { t } = useI18n()

const themeKeys = ['forest', 'space', 'ocean', 'dino', 'magic', 'super']

const themes = computed(() => {
  const result: Record<string, string> = {}
  themeKeys.forEach(key => {
    const label = t(`generator.themes.${key}`)
    result[key] = typeof label === 'string' ? label : key
  })
  return result
})

const themeIcons: Record<string, string> = {
  forest: 'lucide:tree-pine',
  space: 'lucide:rocket',
  ocean: 'lucide:waves',
  dino: 'lucide:bone',
  magic: 'lucide:sparkles',
  super: 'lucide:zap'
}

const themeImages: Record<string, string> = {
  forest: '/images/themes/forest.jpg',
  ocean: '/images/themes/beautiful-fantasy-landscape.jpg',
  space: '/images/themes/cosmos.jpg',
  super: '/images/themes/17083.jpg',
  magic: '/images/themes/taless.jpg',
  dino: '/images/themes/dinasour.jpg'
}

const themeGradients: Record<string, string> = {
  forest: 'bg-gradient-to-br from-emerald-900/40 via-green-950/60 to-[#0F172A]',
  space: 'bg-gradient-to-br from-indigo-900/40 via-purple-950/60 to-[#0F172A]',
  ocean: 'bg-gradient-to-br from-blue-900/40 via-cyan-950/60 to-[#0F172A]',
  dino: 'bg-gradient-to-br from-orange-900/40 via-yellow-950/60 to-[#0F172A]',
  magic: 'bg-gradient-to-br from-pink-900/40 via-rose-950/60 to-[#0F172A]',
  super: 'bg-gradient-to-br from-red-900/40 via-orange-950/60 to-[#0F172A]'
}

function scrollToGenerator() {
  const element = document.getElementById('generator')
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>