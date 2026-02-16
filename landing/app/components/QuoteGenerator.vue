<template>
  <div class="w-full max-w-4xl mx-auto mt-12 p-8 rounded-3xl bg-white/50 backdrop-blur-xl border border-white/20 shadow-2xl overflow-hidden">
    <div class="flex flex-col gap-8">
        <!-- Mood Selector -->
        <div class="flex flex-wrap justify-center gap-4">
          <button
            v-for="mood in moods"
            :key="mood.id"
            @click="selectedMood = mood.id"
            class="group relative flex flex-col items-center gap-2 p-4 rounded-2xl transition-all duration-300"
            :class="[
              selectedMood === mood.id 
                ? 'bg-white shadow-lg scale-110 z-10' 
                : 'hover:bg-white/40 grayscale hover:grayscale-0'
            ]"
          >
            <div 
              class="w-12 h-12 flex items-center justify-center rounded-xl text-2xl transition-transform duration-500 group-hover:rotate-12"
              :style="{ backgroundColor: mood.color + '20', color: mood.color }"
            >
              <Icon :name="mood.icon" />
            </div>
            <span class="text-sm font-semibold text-brand-dark">{{ $t(`generator.moods.${mood.id}`) }}</span>
            
            <div 
              v-if="selectedMood === mood.id"
              class="absolute -bottom-1 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full"
              :style="{ backgroundColor: mood.color }"
            />
          </button>
        </div>

        <!-- Action Button -->
        <div class="flex justify-center">
          <button
            @click="generateQuote"
            :disabled="isGenerating"
            class="relative group px-8 py-4 rounded-full bg-brand-dark text-white font-bold text-lg overflow-hidden transition-all hover:scale-105 active:scale-95 disabled:opacity-50"
          >
            <span class="relative z-10 flex items-center gap-2">
              <Icon v-if="isGenerating" name="svg-spinners:90-ring-with-bg" class="size-5" />
              <Icon v-else name="lucide:sparkles" class="size-5" />
              {{ isGenerating ? $t('generator.findingWisdom') : $t('generator.revealQuote') }}
            </span>
            <div 
              class="absolute inset-0 bg-gradient-to-r opacity-0 group-hover:opacity-100 transition-opacity duration-300"
              :style="{ backgroundImage: `linear-gradient(to right, ${currentMoodColor}40, ${currentMoodColor}80)` }"
            />
          </button>
        </div>

        <!-- Result Area -->
        <Transition
          enter-active-class="transition duration-500 ease-out"
          enter-from-class="opacity-0 translate-y-8 scale-95"
          enter-to-class="opacity-100 translate-y-0 scale-100"
          leave-active-class="transition duration-300 ease-in"
          leave-from-class="opacity-100 scale-100"
          leave-to-class="opacity-0 scale-95"
        >
          <div v-if="generatedQuote" class="relative mt-8 p-12 rounded-4xl bg-white shadow-inner overflow-hidden min-h-[300px] flex flex-col items-center justify-center text-center">
            <Icon name="lucide:quote" class="absolute top-8 left-8 size-12 opacity-10" :style="{ color: currentMoodColor }" />
            
            <blockquote class="relative z-10">
              <p class="text-3xl md:text-4xl font-serif italic text-brand-dark leading-snug">
                {{ generatedQuote.text }}
              </p>
              <footer class="mt-8 flex flex-col items-center gap-2">
                <span class="text-xl font-bold text-brand-dark">— {{ generatedQuote.author }} —</span>
                <span class="text-brand-gray font-medium tracking-wide uppercase text-[10px] opacity-60">
                  {{ $t('generator.wisdomOfGreats') }}
                </span>
              </footer>
            </blockquote>

            <!-- Image visual if generated -->
            <div v-if="generatedQuote.visual" class="mt-10 w-full max-w-sm rounded-2xl overflow-hidden shadow-2xl border-4 border-white animate-in zoom-in slide-in-from-bottom-4 duration-700">
               <img :src="generatedQuote.visual" class="w-full h-auto" />
            </div>

            <!-- Card Actions -->
            <div class="mt-12 flex flex-wrap justify-center gap-4 relative z-10">
              <button 
                v-if="!generatedQuote.visual && !isGeneratingVisual"
                @click="generateVisual"
                class="flex items-center gap-2 px-4 py-2 rounded-xl bg-primary text-white hover:bg-primary/90 transition-all text-sm font-semibold shadow-md"
              >
                <Icon name="lucide:brush" class="size-4" />
                {{ $t('generator.generateVisualBtn') || 'Generate Design' }}
              </button>

              <div v-if="isGeneratingVisual" class="flex items-center gap-2 px-4 py-2 text-sm text-brand-gray italic bg-brand-light rounded-xl">
                <Icon name="svg-spinners:90-ring-with-bg" class="size-4" />
                {{ $t('generator.findingVisual') }}
              </div>

              <button class="flex items-center gap-2 px-4 py-2 rounded-xl bg-brand-light hover:bg-white border border-brand-dark/5 transition-colors text-sm font-semibold">
                <Icon name="lucide:download" class="size-4" />
                {{ $t('generator.saveAsImage') }}
              </button>
              <button class="flex items-center gap-2 px-4 py-2 rounded-xl bg-brand-light hover:bg-white border border-brand-dark/5 transition-colors text-sm font-semibold">
                <Icon name="lucide:share-2" class="size-4" />
                {{ $t('generator.share') }}
              </button>
              <button class="flex items-center gap-2 px-4 py-2 rounded-xl bg-brand-light hover:bg-white border border-brand-dark/5 transition-colors text-sm font-semibold">
                <Icon name="lucide:copy" class="size-4" />
                {{ $t('generator.copyText') }}
              </button>
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </template>

  <script setup lang="ts">
  import { ref, computed } from 'vue'
  import { useI18n } from 'vue-i18n'

  const { t, tm } = useI18n()

  interface Mood {
    id: string
    icon: string
    color: string
  }

  interface Quote {
    text: string
    author: string
    visual?: string
  }

  const moods: Mood[] = [
    { id: 'motivation', icon: 'lucide:rocket', color: '#f43f5e' },
    { id: 'inspiration', icon: 'lucide:lightbulb', color: '#8b5cf6' },
    { id: 'calm', icon: 'lucide:wind', color: '#10b981' },
    { id: 'confidence', icon: 'lucide:shield', color: '#0ea5e9' },
    { id: 'love', icon: 'lucide:heart', color: '#ec4899' },
  ]

  const selectedMood = ref<string>(moods[0]?.id || 'motivation')
  const isGenerating = ref(false)
  const isGeneratingVisual = ref(false)
  const generatedQuote = ref<Quote | null>(null)

  const moodKeywords: Record<string, string> = {
    motivation: 'fitness,sport,mountain',
    inspiration: 'sunset,stars,nebula',
    calm: 'forest,zen,waterfall',
    confidence: 'business,eagle,city-skyline',
    love: 'flowers,romance,couple',
  }

  const currentMoodColor = computed(() => {
    const mood = moods.find(m => m.id === selectedMood.value)
    return mood ? mood.color : '#ba445b'
  })

  async function generateVisual() {
    if (!generatedQuote.value) return
    isGeneratingVisual.value = true
    
    // Simulate AI thinking time for design
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    const keywords = moodKeywords[selectedMood.value] || 'abstract'
    const randomId = Math.floor(Math.random() * 1000)
    generatedQuote.value.visual = `https://loremflickr.com/800/800/${keywords.split(',')[0]}?lock=${randomId}`
    
    isGeneratingVisual.value = false
  }

  async function generateQuote() {
    isGenerating.value = true
    generatedQuote.value = null
    
    await new Promise(resolve => setTimeout(resolve, 800))
    
    const moodQuotes = tm(`generator.quotes.${selectedMood.value}`) as Quote[]
    
    if (moodQuotes && moodQuotes.length > 0) {
      const randomIndex = Math.floor(Math.random() * moodQuotes.length)
      const quote = moodQuotes[randomIndex] as Quote
      generatedQuote.value = { 
        text: quote.text, 
        author: quote.author 
      }
    } else {
      generatedQuote.value = { 
        text: "Stay positive and keep moving forward.", 
        author: "Unknown" 
      }
    }
    
    isGenerating.value = false
  }
  </script>
