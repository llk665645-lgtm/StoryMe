<template>
  <div class="w-full max-w-4xl mx-auto mt-12 p-8 md:p-12 rounded-[3rem] bg-white border border-brand-dark/5 shadow-2xl overflow-hidden">
    <div class="flex flex-col gap-10">
        <!-- Input Form -->
        <div v-if="!hasResult" class="grid grid-cols-1 md:grid-cols-2 gap-8 animate-in fade-in duration-700">
          <!-- Left Column -->
          <div class="flex flex-col gap-6">
            <div class="flex flex-col gap-2">
               <label class="text-sm font-bold text-brand-dark ml-1">{{ $t('generator.nameLabel') }}</label>
               <input 
                 v-model="form.name"
                 type="text"
                 :placeholder="$t('generator.namePlaceholder')"
                 class="w-full p-4 rounded-2xl bg-brand-light border border-transparent focus:border-primary/30 focus:bg-white focus:ring-4 focus:ring-primary/5 transition-all outline-none"
               />
            </div>
            <div class="flex flex-col gap-2">
               <label class="text-sm font-bold text-brand-dark ml-1">{{ $t('generator.ageLabel') }}</label>
               <input 
                 v-model="form.age"
                 type="number"
                 min="2"
                 max="10"
                 class="w-full p-4 rounded-2xl bg-brand-light border border-transparent focus:border-primary/30 focus:bg-white focus:ring-4 focus:ring-primary/5 transition-all outline-none"
               />
            </div>
            <div class="flex flex-col gap-2">
               <label class="text-sm font-bold text-brand-dark ml-1">{{ $t('generator.favLabel') }}</label>
               <textarea 
                 v-model="form.favorites"
                 :placeholder="$t('generator.favPlaceholder')"
                 class="w-full h-32 p-4 rounded-2xl bg-brand-light border border-transparent focus:border-primary/30 focus:bg-white focus:ring-4 focus:ring-primary/5 transition-all outline-none resize-none"
               ></textarea>
            </div>
          </div>

          <!-- Right Column (Themes) -->
          <div class="flex flex-col gap-4">
             <label class="text-sm font-bold text-brand-dark ml-1">{{ $t('generator.themeLabel') }}</label>
             <div class="flex flex-col sm:flex-row gap-6">
                <div class="grid grid-cols-2 gap-3 flex-1">
                   <button 
                     v-for="(label, key) in themes" 
                     :key="key"
                     @click="form.theme = key"
                     class="flex flex-col items-center gap-2 p-4 rounded-2xl border-2 transition-all group"
                     :class="form.theme === key ? 'border-primary bg-primary/5' : 'border-brand-dark/5 hover:border-primary/20 hover:bg-brand-light'"
                   >
                      <Icon :name="(themeIcons[key] as string)" class="size-8 transition-transform group-hover:scale-110" :class="form.theme === key ? 'text-primary' : 'text-brand-gray'" />
                      <span class="text-[10px] font-bold uppercase tracking-wider text-center" :class="form.theme === key ? 'text-primary' : 'text-brand-gray'">{{ label }}</span>
                   </button>
                </div>
                <!-- Theme Preview Card -->
                <div class="hidden sm:block w-40 shrink-0">
                   <div class="relative aspect-[4/5] rounded-2xl overflow-hidden border border-brand-dark/5 shadow-inner bg-brand-light group">
                      <Transition
                        enter-active-class="transition duration-500 ease-out"
                        enter-from-class="opacity-0 scale-95"
                        enter-to-class="opacity-100 scale-100"
                        leave-active-class="transition duration-300 ease-in"
                        leave-from-class="opacity-100 scale-100"
                        leave-to-class="opacity-0 scale-95"
                        mode="out-in"
                      >
                        <img 
                          :key="form.theme"
                          :src="`/images/themes/${form.theme}.webp`" 
                          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                          :alt="String(form.theme)"
                        />
                      </Transition>
                      <div class="absolute inset-x-0 bottom-0 p-3 bg-gradient-to-t from-black/60 to-transparent">
                         <span class="text-[10px] font-bold text-white uppercase tracking-widest">{{ (themes as any)[form.theme] }}</span>
                      </div>
                   </div>
                </div>
             </div>

             <!-- Price / Action -->
             <div class="mt-auto pt-6 flex flex-col gap-4">
                <button
                  @click="generateStory"
                  :disabled="isGenerating || !isFormValid"
                  class="w-full relative group px-8 py-5 rounded-full bg-brand-dark text-white font-bold text-xl overflow-hidden transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-30 shadow-xl"
                >
                  <span class="relative z-10 flex items-center justify-center gap-3">
                    <Icon v-if="isGenerating" name="svg-spinners:90-ring-with-bg" class="size-6" />
                    <Icon v-else name="lucide:wand-2" class="size-6 text-primary" />
                    {{ isGenerating ? $t('generator.processing') : $t('generator.processBtn') }}
                  </span>
                </button>
                <div class="flex items-center justify-center gap-2 text-[10px] text-brand-gray font-bold uppercase tracking-widest opacity-60">
                   <Icon name="lucide:shield-check" class="size-3" />
                   Secure Payment via Stripe
                </div>
             </div>
          </div>
        </div>

        <!-- Result Page -->
        <Transition
          enter-active-class="transition duration-1000 ease-out"
          enter-from-class="opacity-0 translate-y-12"
          enter-to-class="opacity-100 translate-y-0"
        >
          <div v-if="hasResult" class="flex flex-col gap-10">
             <!-- Header -->
             <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-brand-dark/5 pb-8">
                <div>
                   <span class="text-[10px] font-black uppercase tracking-[0.3em] text-primary mb-2 block">Premium Storybook</span>
                   <h2 class="text-3xl font-serif italic text-brand-dark font-bold">{{ result.title }}</h2>
                </div>
                <div class="flex gap-3">
                   <button class="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-brand-light hover:bg-white border border-brand-dark/5 transition-all text-xs font-bold">
                      <Icon name="lucide:printer" class="size-4" />
                      {{ $t('generator.saveAsImage') }}
                   </button>
                   <button @click="hasResult = false" class="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white border border-brand-dark/10 hover:border-primary/30 transition-all text-xs font-bold">
                      <Icon name="lucide:rotate-ccw" class="size-4" />
                      New Story
                   </button>
                </div>
             </div>

             <!-- Story Layout -->
             <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
                <!-- Illustration -->
                <div class="relative aspect-square rounded-[2rem] overflow-hidden shadow-2xl border-[12px] border-white group/img transition-transform duration-700 hover:rotate-1">
                   <div v-if="isGenerating" class="absolute inset-0 bg-brand-light z-10 flex flex-col items-center justify-center gap-4">
                      <Icon name="svg-spinners:90-ring-with-bg" class="size-12 text-primary" />
                      <span class="font-bold text-brand-gray animate-pulse">{{ $t('generator.findingVisual') }}</span>
                   </div>
                   <img 
                     :src="result.image" 
                     class="w-full h-full object-cover group-hover/img:scale-105 transition-transform duration-1000"
                     alt="Story Illustration"
                   />
                </div>

                <!-- Text Content -->
                <div class="flex flex-col gap-6">
                   <div class="prose prose-brand max-w-none">
                      <p class="text-xl leading-relaxed font-serif italic text-brand-dark first-letter:text-5xl first-letter:font-bold first-letter:mr-3 first-letter:float-left first-letter:text-primary whitespace-pre-wrap">
                         {{ result.storyContent }}
                      </p>
                   </div>
                </div>
             </div>

             <!-- Footer Actions -->
             <div class="mt-8 flex justify-center gap-4">
                <button class="flex items-center gap-2 px-8 py-4 rounded-2xl bg-brand-dark text-white hover:bg-brand-dark/90 transition-all text-sm font-bold shadow-xl">
                   <Icon name="lucide:copy" class="size-5 text-primary" />
                   {{ $t('generator.share') }}
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

  const { t, tm } = useI18n()

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

  const themeIcons: Record<string, string> = {
    forest: 'lucide:tree-pine',
    space: 'lucide:rocket',
    ocean: 'lucide:waves',
    dino: 'lucide:bone',
    magic: 'lucide:sparkles',
    super: 'lucide:zap'
  }

  const themes = computed(() => (tm('generator.themes') || {}) as Record<string, string>)
  
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
    const themeStarters = demo.starters?.[form.theme]
    const rawStarter = Array.isArray(themeStarters) 
      ? themeStarters[Math.floor(Math.random() * themeStarters.length)]
      : (themeStarters || '')
    
    const starterText = rawStarter.replace(/\[NAME\]/g, form.name)

    result.title = demo.title.replace('[NAME]', form.name)
    result.storyContent = demo.story
      .replace('[STARTER]', starterText)
      .replace(/\[NAME\]/g, form.name)
      .replace(/\[FAVOURITES\]/g, form.favorites)
      .replace(/\[THEME\]/g, (themes.value as any)[form.theme])

    // 3. Set Visual (Using local theme images)
    result.image = `/images/themes/${form.theme}.webp`

    // 4. Final Processing Time
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    hasResult.value = true
    isGenerating.value = false
  }
  </script>
