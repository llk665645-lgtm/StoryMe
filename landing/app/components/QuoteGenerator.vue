<template>
  <div class="w-full max-w-4xl mx-auto mt-12 p-8 md:p-12 rounded-[3.5rem] bg-white/10 backdrop-blur-xl border border-white/10 shadow-3xl overflow-hidden">
    <div class="flex flex-col gap-10">
        <!-- Input Form -->
        <div v-if="!hasResult" class="grid grid-cols-1 md:grid-cols-2 gap-8 animate-in fade-in duration-700">
          <!-- Left Column -->
          <div class="flex flex-col gap-6 text-left">
            <div class="flex flex-col gap-2">
               <label class="text-sm font-bold text-white ml-1">{{ $t('generator.nameLabel') }}</label>
               <input 
                 v-model="form.name"
                 type="text"
                 :placeholder="$t('generator.namePlaceholder')"
                 class="w-full p-5 rounded-2xl bg-white/10 border border-white/20 text-white placeholder:text-white/50 focus:border-white/40 focus:bg-white/15 focus:ring-4 focus:ring-white/10 transition-all outline-none"
               />
            </div>
            <div class="flex flex-col gap-2">
               <label class="text-sm font-bold text-white ml-1">{{ $t('generator.ageLabel') }}</label>
               <input 
                 v-model="form.age"
                 type="number"
                 min="2"
                 max="12"
                 class="w-full p-5 rounded-2xl bg-white/10 border border-white/20 text-white focus:border-white/40 focus:bg-white/15 focus:ring-4 focus:ring-white/10 transition-all outline-none"
               />
            </div>
            <div class="flex flex-col gap-2">
               <label class="text-sm font-bold text-white ml-1">{{ $t('generator.favLabel') }}</label>
               <textarea 
                 v-model="form.favorites"
                 :placeholder="$t('generator.favPlaceholder')"
                 class="w-full h-32 p-5 rounded-2xl bg-white/10 border border-white/20 text-white placeholder:text-white/50 focus:border-white/40 focus:bg-white/15 focus:ring-4 focus:ring-white/10 transition-all outline-none resize-none"
               ></textarea>
               <p v-if="form.favorites.length > 0 && form.favorites.length <= 5" class="text-[10px] text-orange-300 font-medium ml-1">
                 {{ $t('generator.validationHint') }}
               </p>
            </div>
          </div>

          <!-- Right Column (Themes) -->
          <div class="flex flex-col gap-4 text-left">
             <label class="text-sm font-bold text-white ml-1">{{ $t('generator.themeLabel') }}</label>
             <div class="flex flex-col sm:flex-row gap-6">
                <div class="grid grid-cols-2 gap-3 flex-1">
                   <button 
                     v-for="(label, key) in themes" 
                     :key="key"
                     @click="form.theme = key"
                     class="flex flex-col items-center gap-3 p-5 rounded-2xl border transition-all group relative overflow-hidden"
                     :class="[
                       form.theme === key ? 'border-white/60 bg-white/25 shadow-lg scale-[1.02]' : 'border-white/10 hover:border-white/30 hover:bg-white/10',
                       key === 'forest' && form.theme === key ? 'shadow-green-500/20' : '',
                       key === 'space' && form.theme === key ? 'shadow-purple-500/20' : '',
                       key === 'ocean' && form.theme === key ? 'shadow-blue-500/20' : '',
                       key === 'dino' && form.theme === key ? 'shadow-orange-500/20' : '',
                       key === 'magic' && form.theme === key ? 'shadow-pink-500/20' : '',
                       key === 'super' && form.theme === key ? 'shadow-red-500/20' : ''
                     ]"
                   >
                      <div v-if="form.theme === key" class="absolute inset-0 opacity-20 bg-gradient-to-br" :class="[
                        key === 'forest' ? 'from-green-400 to-emerald-600' : '',
                        key === 'space' ? 'from-purple-400 to-indigo-600' : '',
                        key === 'ocean' ? 'from-blue-400 to-cyan-600' : '',
                        key === 'dino' ? 'from-orange-400 to-yellow-600' : '',
                        key === 'magic' ? 'from-pink-400 to-rose-600' : '',
                        key === 'super' ? 'from-red-400 to-orange-600' : ''
                      ]"></div>
                      <Icon :name="(themeIcons[key] as string)" class="size-8 transition-transform group-hover:scale-110 relative z-10" :class="form.theme === key ? 'text-white' : 'text-white/50'" />
                      <span class="text-[10px] font-bold uppercase tracking-[0.1em] text-center relative z-10" :class="form.theme === key ? 'text-white' : 'text-white/50'">{{ label }}</span>
                   </button>
                </div>
             </div>

             <!-- Price / Action -->
             <div class="mt-auto pt-8 flex flex-col gap-4">
                <button
                  @click="generateStory"
                  :disabled="isGenerating || !isFormValid"
                  class="w-full relative group px-8 py-5 rounded-full font-bold text-xl overflow-hidden transition-all shadow-[0_8px_30px_rgba(0,0,0,0.3)]"
                  :class="[
                    isFormValid 
                      ? 'bg-gradient-to-r from-pink-500 via-purple-500 to-indigo-500 text-white hover:scale-[1.02] hover:shadow-purple-500/40 active:scale-95' 
                      : 'bg-white/20 text-white/40 cursor-not-allowed border border-white/10'
                  ]"
                >
                  <span class="relative z-10 flex items-center justify-center gap-3">
                    <Icon v-if="isGenerating" name="svg-spinners:90-ring-with-bg" class="size-6" />
                    <Icon v-else :name="isFormValid ? 'lucide:sparkles' : 'lucide:lock'" class="size-6" />
                    {{ isGenerating ? $t('generator.processing') : $t('generator.processBtn') }}
                  </span>
                  
                  <!-- Gloss effect for active button -->
                  <div v-if="isFormValid" class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
                </button>
                <div class="flex items-center justify-center gap-2 text-[10px] text-white/50 font-bold uppercase tracking-widest">
                   <Icon name="lucide:shield-check" class="size-3 text-emerald-400" />
                   Secure AI Processing
                </div>
             </div>
          </div>
        </div>

        <!-- Result Page -->
        <Transition
          enter-active-class="transition duration-[2000ms] ease-out"
          enter-from-class="opacity-0 translate-y-12"
          enter-to-class="opacity-100 translate-y-0"
        >
          <div v-if="hasResult" class="flex flex-col gap-10">
             <!-- Header -->
             <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-white/10 pb-8">
                <div class="text-left">
                   <span class="text-[10px] font-black uppercase tracking-[0.3em] text-white/50 mb-2 block">Premium Storybook</span>
                   <h2 class="text-3xl font-serif italic text-white font-bold">{{ result.title }}</h2>
                </div>
                <div class="flex gap-3">
                   <button class="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/10 transition-all text-xs font-bold text-white">
                      <Icon name="lucide:printer" class="size-4" />
                      {{ $t('generator.saveAsImage') }}
                   </button>
                   <button @click="hasResult = false" class="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white/5 border border-white/10 hover:border-white/30 transition-all text-xs font-bold text-white">
                      <Icon name="lucide:rotate-ccw" class="size-4" />
                      New Story
                   </button>
                </div>
             </div>

             <!-- Story Layout -->
             <div class="flex flex-col gap-6 text-left">
                  <div class="prose prose-invert max-w-none">
                     <p class="story-paragraph !text-white/90">
                        {{ result.storyContent }}
                     </p>
                  </div>
             </div>

             <!-- Footer Actions -->
             <div class="mt-8 flex flex-wrap justify-center gap-4">
                <button @click="copyToClipboard" class="flex items-center gap-2 px-8 py-4 rounded-2xl bg-white text-dream-deep hover:bg-white/90 transition-all text-sm font-bold shadow-xl">
                   <Icon name="lucide:copy" class="size-5 text-dream-mid" />
                   {{ $t('generator.share') }}
                </button>
                <button @click="triggerAuth('register')" class="flex items-center gap-2 px-8 py-4 rounded-2xl bg-white/10 border border-white/20 text-white hover:bg-white/15 transition-all text-sm font-bold backdrop-blur-md">
                   <Icon name="lucide:sparkles" class="size-5 text-white" />
                   {{ $t('generator.wantMore') }}
                </button>
             </div>
          </div>
        </Transition>


      </div>
    </div>
  </template>

  <script setup lang="ts">
  import { ref, reactive, computed } from 'vue'
  import { useI18n } from 'vue-i18n'
  import { useAuth } from '~/composables/useAuth'

  const { t, tm } = useI18n()
  const { triggerAuth } = useAuth()

  const form = reactive({
    name: '',
    age: 5,
    favorites: '',
    theme: 'magic'
  })

  const isGenerating = ref(false)
  const hasResult = ref(false)

  const result = reactive({
    title: '',
    storyContent: '',
    image: ''
  })



  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(`${result.title}\n\n${result.storyContent}`)
      // Could add a toast here
    } catch (err) {
      console.error('Failed to copy text: ', err)
    }
  }

  const themeIcons: Record<string, string> = {
    forest: 'lucide:tree-pine',
    space: 'lucide:rocket',
    ocean: 'lucide:waves',
    dino: 'lucide:bone',
    magic: 'lucide:sparkles',
    super: 'lucide:zap'
  }

  const themeKeys = ['forest', 'space', 'ocean', 'dino', 'magic', 'super']
  const themes = computed(() => {
    const result: Record<string, string> = {}
    themeKeys.forEach(key => {
      result[key] = t(`generator.themes.${key}`)
    })
    return result
  })
  
  const moodKeywords: Record<string, string> = {
    forest: 'magical-forest,glowing-mushrooms,fairy-tale-woods,watercolor-illustration',
    space: 'cosmic-adventure,astronaut-child,stars-and-planets,outer-space-watercolor',
    ocean: 'underwater-kingdom,sea-creatures,magical-ocean,coral-reef-illustration',
    dino: 'friendly-dinosaurs,prehistoric-jungle,ancient-world,dinosaur-watercolor',
    magic: 'fairytale-castle,magic-wand,enchanted-garden,storybook-watercolor',
    super: 'child-superhero,comic-book-style,heroic-city,superpower-illustration'
  }


  const isFormValid = computed(() => {
    return form.name.length > 1 && form.favorites.length > 5
  })

  async function generateStory() {
    isGenerating.value = true
    
    // 1. Simulate Stripe Checkout Delay
    await new Promise(resolve => setTimeout(resolve, 800))
    
    // 2. Generate Content
    const demo = tm('generator.demo') as any
    const themeVariations = demo.variations?.[form.theme]
    const heroNames = demo.heroNames?.[form.theme] || ['the Magic Friend']
    const heroName = Array.isArray(heroNames) 
      ? heroNames[Math.floor(Math.random() * heroNames.length)]
      : heroNames

    let storyContent = ''
    
    if (Array.isArray(themeVariations) && themeVariations.length > 0) {
      // Pick random variation
      const randomVar = themeVariations[Math.floor(Math.random() * themeVariations.length)]
      storyContent = randomVar
        .replace(/\[NAME\]/g, form.name)
        .replace(/\[HERO\]/g, heroName)
        .replace(/\[FAVOURITES\]/g, form.favorites)
    } else {
      // Use standard starter + template
      const themeStarters = demo.starters?.[form.theme]
      const rawStarter = Array.isArray(themeStarters) 
        ? themeStarters[Math.floor(Math.random() * themeStarters.length)]
        : (themeStarters || '')
      
      const starterText = rawStarter.replace(/\[NAME\]/g, form.name)
      storyContent = demo.story
        .replace('[STARTER]', starterText)
        .replace(/\[NAME\]/g, form.name)
        .replace(/\[FAVOURITES\]/g, form.favorites)
        .replace(/\[THEME\]/g, (themes.value as any)[form.theme])
    }

    result.title = demo.title.replace('[NAME]', form.name)
    result.storyContent = storyContent

    // 3. Set Visual (Using local theme images)
    result.image = `/images/themes/${form.theme}.webp`

    // 4. Final Processing Time
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    hasResult.value = true
    isGenerating.value = false
  }
  </script>
