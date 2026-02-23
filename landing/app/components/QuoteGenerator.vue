<template>
  <div class="w-full max-w-4xl mx-auto mt-12 p-8 md:p-12 rounded-[3.5rem] bg-[#0F172A]/80 backdrop-blur-2xl border border-white/10 overflow-hidden">
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
                 class="w-full p-5 rounded-2xl bg-white/10 border border-white/20 text-white placeholder:text-white/50 focus:border-purple-400 focus:bg-white/15 focus:ring-4 focus:ring-purple-500/20 transition-all outline-none"
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
                       form.theme === key ? themeGradients[key] : ''
                     ]"
                   >
                      <div v-if="form.theme === key" class="absolute inset-0 opacity-40 bg-gradient-to-br" :class="[
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
                 <div v-if="limitReached" class="p-4 rounded-2xl bg-orange-500/10 border border-orange-500/20 text-orange-200 text-xs font-medium text-center animate-in fade-in slide-in-from-top-2 duration-300">
                   <div class="flex items-center justify-center gap-2 mb-1">
                     <Icon name="lucide:alert-circle" class="size-4" />
                     <span class="font-bold">Limit Reached</span>
                   </div>
                   {{ $t('generator.limitReached') }}
                 </div>

                 <button
                   @click="generateStory"
                   :disabled="isGenerating || !isFormValid || (limitReached && !authStore.isAuthenticated)"
                   class="w-full relative group px-8 py-5 rounded-full font-black text-xl overflow-hidden transition-all border border-white/20"
                   :class="[
                     isFormValid && (!limitReached || authStore.isAuthenticated)
                       ? 'bg-gradient-to-r from-pink-500 via-purple-500 to-indigo-500 text-white hover:scale-[1.02] active:scale-95' 
                       : 'bg-white/10 text-white/40 cursor-not-allowed border border-white/10'
                   ]"
                 >
                   <span class="relative z-10 flex items-center justify-center gap-3">
                     <Icon v-if="isGenerating" name="svg-spinners:90-ring-with-bg" class="size-6" />
                     <Icon v-else :name="isFormValid && (!limitReached || authStore.isAuthenticated) ? 'lucide:sparkles' : 'lucide:lock'" class="size-6" />
                     {{ isGenerating ? $t('generator.processing') : $t('generator.processBtn') }}
                   </span>
                   
                   <!-- Gloss effect for active button -->
                   <div v-if="isFormValid && (!limitReached || authStore.isAuthenticated)" class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
                 </button>
                 <div class="flex items-center justify-center gap-2 text-[10px] text-white/50 font-bold uppercase tracking-widest">
                    <Icon name="lucide:shield-check" class="size-3 text-emerald-400" />
                    Secure AI Processing
                 </div>
              </div>
          </div>
        </div>

        <!-- Loading Magic Overlay -->
        <Transition
          enter-active-class="transition duration-500 ease-out"
          enter-from-class="opacity-0"
          enter-to-class="opacity-100"
          leave-active-class="transition duration-500 ease-in"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <div v-if="isGenerating" class="absolute inset-0 z-50 flex flex-col items-center justify-center bg-[#0F172A]/90 backdrop-blur-xl">
            <div class="relative">
              <div class="size-32 rounded-full border-4 border-purple-500/20 border-t-purple-500 animate-spin"></div>
              <div class="absolute inset-0 flex items-center justify-center">
                <Icon name="lucide:sparkles" class="size-10 text-purple-400 animate-pulse" />
              </div>
            </div>
            <h3 class="mt-8 text-2xl font-black text-white tracking-tight animate-pulse">
              {{ $t('generator.processing') }}
            </h3>
            <p class="mt-2 text-white/50 font-medium">Creating a world for {{ form.name }}...</p>
          </div>
        </Transition>

        <!-- Result Page -->
        <Transition
          enter-active-class="transition duration-[1000ms] ease-out"
          enter-from-class="opacity-0 translate-y-12"
          enter-to-class="opacity-100 translate-y-0"
        >
          <div v-if="hasResult" class="flex flex-col gap-10 result-content">
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
                      <div v-if="result.image" class="w-full h-80 rounded-3xl overflow-hidden mb-8 border border-white/10 shadow-2xl">
                        <img :src="result.image" alt="Story Illustration" class="w-full h-full object-cover" />
                      </div>
                      <div class="space-y-4">
                        <p v-for="(p, i) in formattedStory" :key="i" class="story-paragraph">
                           {{ p }}
                        </p>
                      </div>
                   </div>
              </div>

              <!-- Footer Actions -->
              <div class="mt-8 flex flex-wrap justify-center gap-4">
                 <button v-if="result.is_demo" @click="triggerAuth('register')" class="group relative flex items-center gap-2 px-8 py-4 rounded-2xl bg-gradient-to-r from-pink-500 to-purple-600 text-white hover:scale-[1.05] active:scale-95 transition-all text-sm font-black border border-white/30 shadow-[0_0_20px_rgba(236,72,153,0.3)]">
                    <Icon name="lucide:sparkles" class="size-5 text-white animate-pulse" />
                    {{ $t('generator.wantMore') }}
                    <div class="absolute inset-0 bg-white/20 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000" />
                 </button>
                 <button @click="copyToClipboard" class="flex items-center gap-2 px-8 py-4 rounded-2xl bg-white/10 border border-white/20 text-white hover:bg-white/15 transition-all text-sm font-bold backdrop-blur-md">
                    <Icon name="lucide:copy" class="size-5 text-white" />
                    {{ $t('generator.share') }}
                 </button>
                 <button v-if="!result.is_demo" @click="hasResult = false" class="flex items-center gap-2 px-8 py-4 rounded-2xl bg-white/5 border border-white/10 text-white/70 hover:text-white transition-all text-sm font-bold">
                    Create New Story
                 </button>
              </div>
          </div>
        </Transition>


      </div>
    </div>
  </template>

  <script setup lang="ts">
  import { useAuthStore } from '~/stores/auth'
  import { STORIES_RU, STORIES_EN, THEME_DEMO_IMAGES } from '~/utils/storyDemo'

  const { t, locale } = useI18n()
  const { triggerAuth } = useAuth()
  const authStore = useAuthStore()

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
    image: '',
    is_demo: true
  })

  const formattedStory = computed(() => {
    return result.storyContent.split('\n').filter(p => p.trim())
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
      const label = t(`generator.themes.${key}`)
      result[key] = typeof label === 'string' ? label : key
    })
    return result
  })
  
  const themeGradients: Record<string, string> = {
    forest: 'bg-emerald-500/20 border-emerald-500/30',
    space: 'bg-indigo-500/20 border-indigo-500/30',
    ocean: 'bg-blue-500/20 border-blue-500/30',
    dino: 'bg-orange-500/20 border-orange-500/30',
    magic: 'bg-pink-500/20 border-pink-500/30',
    super: 'bg-red-500/20 border-red-500/30'
  }

  const moodKeywords: Record<string, string> = {
    forest: 'magical-forest,glowing-mushrooms,fairy-tale-woods,watercolor-illustration',
    space: 'cosmic-adventure,astronaut-child,stars-and-planets,outer-space-watercolor',
    ocean: 'underwater-kingdom,sea-creatures,magical-ocean,coral-reef-illustration',
    dino: 'friendly-dinosaurs,prehistoric-jungle,ancient-world,dinosaur-watercolor',
    magic: 'fairytale-castle,magic-wand,enchanted-garden,storybook-watercolor',
    super: 'child-superhero,comic-book-style,heroic-city,superpower-illustration'
  }


  const isFormValid = computed(() => {
    return form.name.length > 1 && form.favorites.length >= 0
  })

  const generateLocalDemo = () => {
    const data = locale.value === 'ru' ? STORIES_RU : STORIES_EN
    const theme = form.theme
    
    // Pick random hero and variation
    const heroes = data.heroNames[theme] || data.heroNames['magic'] || []
    const variations = data.variations[theme] || data.variations['magic'] || []
    
    if (heroes.length === 0 || variations.length === 0) return
    
    const randomHero = heroes[Math.floor(Math.random() * heroes.length)] || 'Hero'
    const randomVariation = variations[Math.floor(Math.random() * variations.length)] || ''
    
    // Replace placeholders
    const story = randomVariation
      .replace(/\[NAME\]/g, form.name)
      .replace(/\[HERO\]/g, randomHero)
      .replace(/\[FAVOURITES\]/g, form.favorites || (locale.value === 'ru' ? 'любимые вещи' : 'favorite things'))

    result.title = t('generator.resultHeader')
    result.storyContent = story
    result.image = THEME_DEMO_IMAGES[theme] || THEME_DEMO_IMAGES['magic'] || ''
    result.is_demo = true
    hasResult.value = true
    
    setTimeout(() => {
      const el = document.querySelector('.result-content')
      el?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }, 100)
  }

  const limitReached = ref(false)
  const localGenCount = ref(0)

  onMounted(() => {
    const saved = localStorage.getItem('story_gen_count')
    const savedDate = localStorage.getItem('story_gen_date')
    const today = new Date().toDateString()
    
    if (savedDate !== today) {
      localGenCount.value = 0
      localStorage.setItem('story_gen_count', '0')
      localStorage.setItem('story_gen_date', today)
    } else if (saved) {
      localGenCount.value = parseInt(saved, 10)
    }
  })

  async function generateStory() {
    if (!isFormValid.value) return
    
    // Check local limit first for unauthenticated users
    if (!authStore.isAuthenticated && localGenCount.value >= 3) {
      limitReached.value = true
      return
    }

    isGenerating.value = true
    limitReached.value = false
    
    // For unauthenticated users, always use local demo
    if (!authStore.isAuthenticated) {
      setTimeout(() => {
        localGenCount.value++
        localStorage.setItem('story_gen_count', localGenCount.value.toString())
        generateLocalDemo()
        isGenerating.value = false
      }, 1500)
      return
    }

    try {
      const headers: Record<string, string> = {
        'Content-Type': 'application/json'
      }
      
      if (authStore.accessToken) {
        headers['Authorization'] = `Bearer ${authStore.accessToken}`
      }

      const config = useRuntimeConfig()
      const response = await fetch(`${config.public.apiBase}/story/generate`, {
        method: 'POST',
        headers,
        body: JSON.stringify({
          name: form.name,
          age: form.age,
          theme: form.theme,
          additional_params: form.favorites
        })
      })

      const data = await response.json()

      if (!response.ok) {
        if (response.status === 403 && data.error === 'limit_reached') {
          limitReached.value = true
          isGenerating.value = false
          return
        }
        generateLocalDemo()
        return
      }
      
      result.title = t('generator.resultHeader')
      result.storyContent = data.story
      result.image = data.image
      result.is_demo = data.is_demo
      
      hasResult.value = true
      
      setTimeout(() => {
        const el = document.querySelector('.result-content')
        el?.scrollIntoView({ behavior: 'smooth', block: 'start' })
      }, 100)
    } catch (error) {
      console.error('Generation error:', error)
      generateLocalDemo()
    } finally {
      isGenerating.value = false
    }
  }
  </script>
