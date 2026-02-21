<template>
  <main class="min-h-screen bg-brand-light">
    <!-- Hero Section -->
    <section class="relative py-24 overflow-hidden">
      <div class="absolute inset-0 z-0">
        <div class="absolute top-0 right-0 -translate-y-1/2 translate-x-1/2 size-96 rounded-full bg-primary/10 blur-3xl"></div>
        <div class="absolute bottom-0 left-0 translate-y-1/2 -translate-x-1/2 size-96 rounded-full bg-primary/10 blur-3xl"></div>
      </div>

      <div class="relative z-10 mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-3xl text-center">
          <h1 class="text-4xl font-bold tracking-tight text-brand-dark sm:text-6xl mb-8">
            {{ $t('about.hero_title') }}
          </h1>
          <p class="text-xl text-brand-gray leading-relaxed mb-12">
            {{ $t('about.hero_description') }}
          </p>
        </div>
      </div>
    </section>

    <!-- Mission Section -->
    <section class="py-24 bg-white">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
          <div class="relative aspect-square rounded-3xl overflow-hidden shadow-2xl">
            <img src="https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=1000&auto=format&fit=crop" alt="Magical Book" class="object-cover w-full h-full" />
            <div class="absolute inset-0 bg-gradient-to-t from-brand-dark/40 to-transparent"></div>
          </div>
          <div>
            <h2 class="text-3xl font-bold text-brand-dark mb-6">{{ $t('about.mission_title') }}</h2>
            <div class="space-y-6 text-brand-gray text-lg leading-relaxed">
              <p>{{ $t('about.mission_p1') }}</p>
              <p>{{ $t('about.mission_p2') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Values Section -->
    <section class="py-24">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-brand-dark text-center mb-16">{{ $t('about.values_title') }}</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="value in values" :key="value.title" class="bg-white p-8 rounded-2xl shadow-sm border border-border hover:shadow-md transition-shadow">
            <div class="size-12 rounded-xl bg-primary/10 flex items-center justify-center mb-6">
              <Icon :name="value.icon" class="size-6 text-primary" />
            </div>
            <h3 class="text-xl font-bold text-brand-dark mb-4">{{ value.title }}</h3>
            <p class="text-brand-gray">{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <CTASection />
    <AppFooter />
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
