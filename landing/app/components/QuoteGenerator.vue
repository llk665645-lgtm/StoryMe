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
            class="relative group px-10 py-5 rounded-full bg-brand-dark text-white font-bold text-xl overflow-hidden transition-all hover:scale-105 active:scale-95 disabled:opacity-50"
          >
            <span class="relative z-10 flex items-center gap-3">
              <Icon v-if="isGenerating" name="svg-spinners:90-ring-with-bg" class="size-6" />
              <Icon v-else name="lucide:sparkles" class="size-6 text-primary" />
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
          enter-active-class="transition duration-700 ease-out"
          enter-from-class="opacity-0 translate-y-12 scale-95"
          enter-to-class="opacity-100 translate-y-0 scale-100"
          leave-active-class="transition duration-300 ease-in"
          leave-from-class="opacity-100 scale-100"
          leave-to-class="opacity-0 scale-95"
        >
          <div v-if="generatedQuote" class="relative mt-8 flex flex-col items-center">
            
            <!-- 1. Aesthetic Photo -->
            <div class="relative w-full max-w-2xl aspect-[4/5] rounded-[2.5rem] overflow-hidden shadow-2xl border-8 border-white group/photo">
              <div v-if="isGeneratingVisual" class="absolute inset-0 z-10 flex flex-col items-center justify-center bg-brand-light/90 backdrop-blur-sm transition-all">
                <Icon name="svg-spinners:ring-resize" class="size-16 text-primary mb-4" />
                <span class="text-brand-dark font-bold animate-pulse text-lg">{{ $t('generator.findingVisual') }}</span>
              </div>
              
              <img 
                v-if="generatedQuote.visual"
                :src="generatedQuote.visual" 
                class="w-full h-full object-cover transition-transform duration-1000 group-hover/photo:scale-105"
                alt="Aesthetic visual"
              />

              <!-- Floating Quote Overlay on Image -->
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-black/20 flex flex-col justify-end p-10">
                 <Icon name="lucide:quote" class="size-10 text-white/40 mb-4" />
                 <p class="text-2xl md:text-3xl font-serif italic text-white leading-tight drop-shadow-xl mb-6">
                    {{ generatedQuote.text }}
                 </p>
                 <div class="flex items-center gap-3">
                    <div class="w-10 h-[2px] bg-primary" />
                    <span class="text-lg font-bold text-white tracking-wide uppercase">{{ generatedQuote.author }}</span>
                 </div>
              </div>

              <!-- Regenerate Visual Button -->
              <button 
                @click="generateVisual"
                class="absolute top-6 right-6 z-20 p-4 rounded-full bg-white/20 backdrop-blur-xl border border-white/30 text-white hover:bg-primary hover:border-transparent transition-all shadow-xl hover:rotate-90 duration-500"
                :title="$t('generator.generateVisualBtn')"
              >
                <Icon name="lucide:refresh-cw" class="size-6" />
              </button>
            </div>

            <!-- 2. Meme / Caption Text -->
            <div class="mt-8 w-full max-w-2xl px-6 py-8 rounded-3xl bg-primary/5 border border-primary/10 relative overflow-hidden group">
               <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                  <Icon name="lucide:message-circle" class="size-12" />
               </div>
               <p class="text-lg md:text-xl font-medium text-brand-dark leading-relaxed relative z-10 italic">
                  {{ generatedQuote.caption }}
               </p>
            </div>

            <!-- 3. Post Summary Actions -->
            <div class="mt-10 flex flex-wrap justify-center gap-4 relative z-10">
              <button class="flex items-center gap-3 px-8 py-4 rounded-2xl bg-brand-dark text-white hover:bg-brand-dark/90 transition-all text-sm font-bold shadow-xl hover:-translate-y-1">
                <Icon name="lucide:download" class="size-5 text-primary" />
                {{ $t('generator.saveAsImage') }}
              </button>
              <button class="flex items-center gap-3 px-8 py-4 rounded-2xl bg-primary text-white hover:bg-primary/90 transition-all text-sm font-bold shadow-xl hover:-translate-y-1">
                <Icon name="lucide:send" class="size-5" />
                {{ $t('generator.share') }}
              </button>
              <button class="flex items-center gap-3 px-8 py-4 rounded-2xl bg-white hover:bg-brand-light border border-brand-dark/10 transition-all text-sm font-bold shadow-lg hover:-translate-y-1">
                <Icon name="lucide:copy" class="size-5 text-brand-gray" />
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
    caption: string
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

  const moodKeywords:Record<string, string> = {
    motivation: 'mountain-peak,climbing,adventure,running-trail,wilderness',
    inspiration: 'forest-path,misty-mountains,sunrise-landscape,pine-trees,waterfall',
    calm: 'serene-lake,nature-minimalism,green-forest,morning-dew,field-flowers',
    confidence: 'ocean-cliff,desert-dunes,stormy-sky,wildlife-eagle,survival',
    love: 'sunset-cliffs,wild-flowers,nature-romance,spring-bloom,scenery-aesthetic',
  }

  const currentMoodColor = computed(() => {
    const mood = moods.find(m => m.id === selectedMood.value)
    return mood ? mood.color : '#ba445b'
  })

  async function generateVisual() {
    if (!generatedQuote.value) return
    isGeneratingVisual.value = true
    
    // Simulate searching for the perfect nature/motivation shot
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    // Using nature and motivation as core tags for all categories
    const moodTags = moodKeywords[selectedMood.value] || 'nature'
    const tagArray = moodTags.split(',')
    const randomTag = tagArray[Math.floor(Math.random() * tagArray.length)]
    
    // Using a much larger random range and adding multiple keywords to ensure variety
    const randomId = Math.floor(Math.random() * 1000000)
    const timestamp = Date.now()
    
    // Target Pinterest-style nature and motivation photography
    generatedQuote.value.visual = `https://loremflickr.com/1000/1250/nature,motivation,${randomTag}?lock=${randomId}&t=${timestamp}`
    
    isGeneratingVisual.value = false
  }

  async function generateQuote() {
    isGenerating.value = true
    generatedQuote.value = null
    
    // Initial wait
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    const moodQuotes = tm(`generator.quotes.${selectedMood.value}`) as Quote[]
    
    if (moodQuotes && moodQuotes.length > 0) {
      const randomIndex = Math.floor(Math.random() * moodQuotes.length)
      const quote = moodQuotes[randomIndex] as Quote
      generatedQuote.value = { 
        text: quote.text, 
        author: quote.author,
        caption: quote.caption
      }
      
      // Automatically generate visual
      generateVisual()
    } else {
      generatedQuote.value = { 
        text: "Stay focused and keep moving.", 
        author: "Unknown",
        caption: "A vibe is a vibe. Don't ruin it. ✨" 
      }
      generateVisual()
    }
    
    isGenerating.value = false
  }
  </script>
