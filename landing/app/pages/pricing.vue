<template>
  <main class="min-h-screen bg-transparent pt-32">
    <div>
      <PricingSection />
    </div>

    <!-- FAQ Section with Magic Theme -->
    <section class="py-24 bg-transparent border-t border-white/5">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-5xl text-center mb-16 font-serif italic">
          {{ $t('pricing.faq_title') }}
        </h2>
        <div class="grid grid-cols-1 gap-8 md:grid-cols-2">
          <div v-for="faq in faqs" :key="faq.question" class="rounded-[2.5rem] bg-white/5 backdrop-blur-md p-10 border border-white/10 hover:bg-white/10 transition-all duration-500">
            <h3 class="text-xl font-bold text-white mb-4">{{ faq.question }}</h3>
            <p class="text-white/50 leading-relaxed text-lg">{{ faq.answer }}</p>
          </div>
        </div>
      </div>
    </section>

    <CTASection />
  </main>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t, tm, rt } = useI18n()

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

const faqs = computed(() => {
  const list = tm('pricing.faqs') as any[]
  if (!Array.isArray(list)) return []
  return list.map((faq: any) => ({
    question: rt(faq.question),
    answer: rt(faq.answer)
  })) as FAQ[]
})
</script>
