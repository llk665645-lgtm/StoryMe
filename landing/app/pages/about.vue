<template>
  <main class="min-h-screen bg-transparent pt-32">
    <!-- Hero Section -->
    <section class="relative py-24 overflow-hidden">
      <div class="relative z-10 mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-3xl text-center">
          <h1 class="text-4xl font-bold tracking-tight text-white sm:text-7xl mb-8 font-serif italic">
            {{ $t('about.hero_title') }}
          </h1>
          <p class="text-xl text-white/60 leading-relaxed mb-12">
            {{ $t('about.hero_description') }}
          </p>
        </div>
      </div>
    </section>

    <!-- Mission Section -->
    <section class="py-24 bg-transparent border-t border-white/5">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-20 items-center">
          <div class="relative aspect-square rounded-[3rem] overflow-hidden shadow-3xl border border-white/10">
            <img src="https://images.unsplash.com/photo-1550399105-c4db5fb85c18?q=80&w=1000&auto=format&fit=crop" alt="Magical Library" class="object-cover w-full h-full transition-all duration-1000 hover:scale-110" />
            <div class="absolute inset-0 bg-gradient-to-t from-dream-deep/80 to-transparent"></div>
          </div>
          <div class="text-left">
            <h2 class="text-4xl font-bold text-white mb-8 font-serif italic">{{ $t('about.mission_title') }}</h2>
            <div class="space-y-8 text-white/70 text-lg leading-relaxed">
              <p>{{ $t('about.mission_p1') }}</p>
              <p>{{ $t('about.mission_p2') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Values Section -->
    <section class="py-24 bg-transparent border-t border-white/5">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-4xl font-bold text-white text-center mb-20 font-serif italic">{{ $t('about.values_title') }}</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
          <div v-for="value in values" :key="value.title" class="bg-white/5 backdrop-blur-md p-10 rounded-[2.5rem] border border-white/10 hover:bg-white/10 transition-all duration-500 shadow-xl group">
            <div class="size-16 rounded-2xl bg-white flex items-center justify-center mb-8 shadow-lg group-hover:scale-110 transition-transform">
              <Icon :name="value.icon" class="size-8 text-dream-deep" />
            </div>
            <h3 class="text-2xl font-bold text-white mb-4">{{ value.title }}</h3>
            <p class="text-white/50 leading-relaxed">{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <CTASection />
  </main>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t, tm } = useI18n()

useSeoMeta({
  title: t('seo.about_title'),
  description: t('seo.about_description'),
  ogTitle: t('seo.about_title'),
  ogDescription: t('seo.about_description'),
})

const values = computed(() => [
  {
    title: t('about.value1_title'),
    description: t('about.value1_desc'),
    icon: 'lucide:heart'
  },
  {
    title: t('about.value2_title'),
    description: t('about.value2_desc'),
    icon: 'lucide:shield'
  },
  {
    title: t('about.value3_title'),
    description: t('about.value3_desc'),
    icon: 'lucide:sparkles'
  }
])
</script>
