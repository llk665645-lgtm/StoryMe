<template>
  <main class="min-h-screen bg-brand-light">
    <div class="pt-20">
      <PricingSection />
    </div>

    <!-- FAQ Section for better SEO -->
    <section class="py-24 bg-white">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-3xl font-bold tracking-tight text-brand-dark sm:text-4xl text-center mb-16">
          {{ $t('pricing.faq_title') }}
        </h2>
        <div class="grid grid-cols-1 gap-8 md:grid-cols-2">
          <div v-for="faq in faqs" :key="faq.question" class="rounded-2xl bg-brand-light p-8">
            <h3 class="text-lg font-bold text-brand-dark mb-3">{{ faq.question }}</h3>
            <p class="text-brand-gray leading-relaxed">{{ faq.answer }}</p>
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

// SEO Optimization
useSeoMeta({
  title: t('seo.pricing_title'),
  description: t('seo.pricing_description'),
  ogTitle: t('seo.pricing_title'),
  ogDescription: t('seo.pricing_description'),
  ogImage: '/og-pricing.png',
  twitterCard: 'summary_large_image',
})

interface FAQ {
  question: string
  answer: string
}

const faqs = computed(() => (tm('pricing.faqs') as any) as FAQ[])
</script>
