<template>
  <div class="w-full max-w-5xl mx-auto mt-12 p-8 rounded-[2.5rem] bg-white border border-brand-dark/5 shadow-2xl overflow-hidden">
    <div class="flex flex-col gap-10">
        <!-- Input Section -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <!-- CV Upload -->
          <div class="flex flex-col gap-4">
             <label class="text-sm font-bold text-brand-dark flex items-center gap-2">
                <Icon name="lucide:file-text" class="text-primary size-4" />
                {{ $t('generator.uploadCV') }}
             </label>
             <div 
               class="flex-1 min-h-[160px] border-2 border-dashed border-brand-dark/10 rounded-3xl flex flex-col items-center justify-center gap-3 hover:border-primary/40 hover:bg-primary/5 transition-all cursor-pointer group p-6"
               @click="simulateUpload"
             >
                <div class="w-12 h-12 bg-white rounded-2xl flex items-center justify-center shadow-sm group-hover:scale-110 transition-transform">
                   <Icon :name="cvUploaded ? 'lucide:check-circle' : 'lucide:plus'" :class="cvUploaded ? 'text-green-500' : 'text-primary'" class="size-6" />
                </div>
                <span class="text-sm font-medium text-brand-gray">
                   {{ cvUploaded ? 'CV_Final_v2.pdf' : 'Drop your CV here' }}
                </span>
             </div>
          </div>

          <!-- Job Description -->
          <div class="flex flex-col gap-4">
             <label class="text-sm font-bold text-brand-dark flex items-center gap-2">
                <Icon name="lucide:briefcase" class="text-primary size-4" />
                {{ $t('generator.jobDescription') }}
             </label>
             <textarea 
               v-model="jobDescription"
               :placeholder="$t('generator.jobPlaceholder')"
               class="flex-1 min-h-[160px] p-6 rounded-3xl bg-brand-light/50 border border-brand-dark/5 focus:border-primary/30 focus:bg-white focus:ring-4 focus:ring-primary/10 transition-all outline-none text-sm resize-none"
             ></textarea>
          </div>
        </div>

        <!-- Action Button -->
        <div class="flex justify-center -mt-4">
          <button
            @click="processApplication"
            :disabled="isGenerating || !jobDescription || !cvUploaded"
            class="relative group px-12 py-5 rounded-full bg-brand-dark text-white font-bold text-xl overflow-hidden transition-all hover:scale-105 active:scale-95 disabled:opacity-30 flex items-center gap-3 shadow-xl"
          >
            <Icon v-if="isGenerating" name="svg-spinners:90-ring-with-bg" class="size-6" />
            <Icon v-else name="lucide:sparkles" class="size-6 text-primary" />
            {{ isGenerating ? $t('generator.processing') : $t('generator.processBtn') }}
          </button>
        </div>

        <!-- Result Area (Tabs) -->
        <Transition
          enter-active-class="transition duration-700 ease-out"
          enter-from-class="opacity-0 translate-y-12 scale-95"
          enter-to-class="opacity-100 translate-y-0 scale-100"
        >
          <div v-if="hasResult" class="relative mt-4 flex flex-col gap-6">
            <div class="flex flex-wrap justify-center gap-2 p-1.5 bg-brand-light rounded-2xl border border-brand-dark/5 mx-auto">
               <button 
                 v-for="tab in tabs" 
                 :key="tab.id"
                 @click="activeTab = tab.id"
                 class="px-6 py-2.5 rounded-xl text-sm font-bold transition-all"
                 :class="activeTab === tab.id ? 'bg-white text-brand-dark shadow-sm scale-105' : 'text-brand-gray hover:text-brand-dark hover:bg-white/50'"
               >
                  {{ $t(`generator.tab${tab.label}`) }}
               </button>
            </div>

            <!-- Content Container -->
            <div class="relative min-h-[400px] w-full bg-white rounded-4xl border border-brand-dark/5 shadow-inner p-8 md:p-12 overflow-hidden flex flex-col">
               <!-- ATS Score Header -->
               <div v-if="activeTab === 'cv'" class="flex items-center gap-6 mb-8 p-6 bg-green-50 rounded-3xl border border-green-100 animate-in fade-in slide-in-from-top-4 duration-500">
                  <div class="flex flex-col">
                     <span class="text-3xl font-black text-green-600">98%</span>
                     <span class="text-[10px] font-bold text-green-700 uppercase tracking-widest">ATS Compatibility Score</span>
                  </div>
                  <div class="h-10 w-[1px] bg-green-200" />
                  <p class="text-sm font-medium text-green-800 italic">
                     "We've optimized your key achievements using the STAR method and synchronized them with the job's core requirements."
                  </p>
               </div>

               <!-- Tab Content -->
               <div class="flex-1 relative font-mono text-sm text-brand-dark leading-relaxed whitespace-pre-wrap">
                  {{ currentResultContent }}
               </div>

               <!-- Actions Overlay -->
               <div class="mt-8 pt-8 border-t border-brand-dark/5 flex flex-wrap justify-center gap-4">
                  <button class="flex items-center gap-2 px-6 py-3 rounded-2xl bg-brand-dark text-white hover:bg-brand-dark/90 transition-all text-sm font-bold shadow-lg">
                    <Icon name="lucide:download" class="size-4 text-primary" />
                    {{ $t('generator.saveAsImage') }}
                  </button>
                  <button class="flex items-center gap-2 px-6 py-3 rounded-2xl bg-white hover:bg-brand-light border border-brand-dark/10 transition-all text-sm font-bold">
                    <Icon name="lucide:copy" class="size-4 text-brand-gray" />
                    {{ $t('generator.copyText') }}
                  </button>
               </div>
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

  const tabs = [
    { id: 'cv', label: 'CV' },
    { id: 'cover', label: 'Cover' },
    { id: 'questions', label: 'Questions' }
  ]

  const activeTab = ref('cv')
  const jobDescription = ref('')
  const cvUploaded = ref(false)
  const isGenerating = ref(false)
  const hasResult = ref(false)

  const currentResultContent = computed(() => {
    if (!hasResult.value) return ''
    return tm(`generator.demo.${activeTab.value}`) as any
  })

  function simulateUpload() {
    cvUploaded.value = true
  }

  async function processApplication() {
    isGenerating.value = true
    hasResult.value = false
    
    // Simulate AI analysis complexity
    await new Promise(resolve => setTimeout(resolve, 2500))
    
    hasResult.value = true
    isGenerating.value = false
  }
  </script>
