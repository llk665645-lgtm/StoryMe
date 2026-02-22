<template>
  <section id="uniqueness" class="py-24 bg-transparent relative overflow-hidden">
    <!-- Subtle Aurora glow behind the main block -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1200px] h-[500px] bg-purple-600/5 blur-[120px] rounded-full pointer-events-none"></div>

    <div class="w-full relative">
      <div class="mx-auto max-w-2xl text-center mb-16 px-6">
        <h2 class="text-4xl font-bold tracking-tight text-white font-serif italic mb-4">
          {{ $t('uniqueness.title') }}
        </h2>
      </div>

      <!-- Full-Width Cohesive Block Container with Premium Shine -->
      <div class="relative w-full bg-gradient-to-b from-white/10 to-transparent p-[1px] shadow-2xl overflow-hidden border-y border-white/10 group/block">
        <!-- Moving Shine Effect -->
        <div class="absolute inset-0 translate-x-[-100%] group-hover/block:translate-x-[100%] transition-transform duration-[3000ms] ease-in-out bg-gradient-to-r from-transparent via-white/5 to-transparent pointer-events-none"></div>
        
        <div class="absolute inset-0 bg-[#0F172A]/40 backdrop-blur-3xl"></div>
        
        <!-- Decorative Glow Spots Inside -->
        <div class="absolute top-0 left-1/4 w-64 h-64 bg-purple-500/10 blur-[100px] rounded-full pointer-events-none"></div>
        <div class="absolute bottom-0 right-1/4 w-64 h-64 bg-pink-500/10 blur-[100px] rounded-full pointer-events-none"></div>
        
        <div class="relative max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-y-16 gap-x-8 p-12 lg:p-24">
          <div 
            v-for="(item, index) in uniquenessList" 
            :key="index" 
            class="group flex flex-col items-center text-center transition-all duration-500 p-6 rounded-[2.5rem] hover:bg-white/5 hover:scale-[1.02] cursor-default"
          >
            <!-- Refined Icon Badge at the top -->
            <div class="flex h-16 w-16 items-center justify-center rounded-[1.5rem] bg-white/5 backdrop-blur-md border border-white/10 shadow-lg mb-6 group-hover:border-purple-500/50 transition-all duration-500 group-hover:-translate-y-1">
              <Icon :name="icons[index] || 'lucide:sparkles'" class="size-8 text-purple-300" />
            </div>
            
            <h3 class="text-xl font-bold text-white mb-3 leading-tight group-hover:text-purple-200 transition-colors">
              {{ item.name }}
            </h3>
            <p class="text-base leading-relaxed text-white/50 max-w-xs group-hover:text-white/70 transition-colors">
              {{ item.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { tm, rt } = useI18n()

interface UniquenessItem {
  name: string
  description: string
}

const uniquenessList = computed(() => {
  const list = tm('uniqueness.list') as any[]
  if (!Array.isArray(list)) return []
  return list.map((item: any) => ({
    name: rt(item.name),
    description: rt(item.description)
  })) as UniquenessItem[]
})
const icons = [
  'lucide:user',
  'lucide:palette',
  'lucide:sparkles',
  'lucide:printer'
]

const images = [
  'https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=600&auto=format&fit=crop',
  'https://images.unsplash.com/photo-1513364776144-60967b0f800f?q=80&w=600&auto=format&fit=crop',
  '/images/themes/d.jpg',
  'https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=600&auto=format&fit=crop'
]
</script>
