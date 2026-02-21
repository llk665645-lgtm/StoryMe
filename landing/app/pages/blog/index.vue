<template>
  <main class="min-h-screen bg-brand-light">
    <!-- Header -->
    <section class="py-24 bg-white border-b border-border">
      <div class="mx-auto max-w-7xl px-6 lg:px-8 text-center">
        <h1 class="text-4xl font-bold tracking-tight text-brand-dark sm:text-6xl mb-6">
          {{ $t('blog.title') }}
        </h1>
        <p class="text-xl text-brand-gray max-w-2xl mx-auto">
          {{ $t('blog.subtitle') }}
        </p>
      </div>
    </section>

    <!-- Articles Grid -->
    <section class="py-24">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">
          <NuxtLink 
            v-for="post in localizedPosts" 
            :key="post.slug" 
            :to="`/blog/${post.slug}`"
            class="group bg-white rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col"
          >
            <div class="aspect-[16/9] overflow-hidden">
              <img 
                :src="post.image" 
                :alt="post.title" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" 
              />
            </div>
            <div class="p-8 flex-1 flex flex-col">
              <div class="flex items-center gap-4 mb-4">
                <span class="text-xs font-bold text-primary uppercase tracking-widest">{{ post.tags[0] }}</span>
                <span class="text-xs text-brand-gray">{{ post.date }}</span>
              </div>
              <h2 class="text-2xl font-bold text-brand-dark mb-4 group-hover:text-primary transition-colors">
                {{ post.title }}
              </h2>
              <p class="text-brand-gray mb-6 line-clamp-3">
                {{ post.description }}
              </p>
              <div class="mt-auto flex items-center text-primary font-bold group-hover:gap-2 transition-all">
                {{ $t('blog.readMore') }}
                <Icon name="lucide:arrow-right" class="size-4 ml-1" />
              </div>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <CTASection />
    <AppFooter />
  </main>
</template>

<script setup lang="ts">
import { BLOG_POSTS } from '@/utils/blogData'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()

const localizedPosts = computed(() => {
  return BLOG_POSTS.map(post => {
    const content = post[locale.value as 'en' | 'ru'] || post.en
    return {
      slug: post.slug,
      date: post.date,
      image: post.image,
      ...content
    }
  })
})

useSeoMeta({
  title: t('seo.blog_title') || 'Blog - StoryMe',
  description: t('seo.blog_description') || 'Insights into personalized AI storytelling for kids.',
  ogTitle: t('seo.blog_title'),
  ogDescription: t('seo.blog_description'),
})
</script>
