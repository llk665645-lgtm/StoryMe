<template>
  <main class="min-h-screen bg-transparent pt-32">
    <!-- Header -->
    <section class="py-24 bg-transparent border-b border-white/5">
      <div class="mx-auto max-w-7xl px-6 lg:px-8 text-center">
        <h1 class="text-4xl font-bold tracking-tight text-white sm:text-7xl mb-8 font-serif italic">
          {{ $t('blog.title') }}
        </h1>
        <p class="text-xl text-white/50 max-w-2xl mx-auto leading-relaxed">
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
            class="group bg-white/5 backdrop-blur-md rounded-[2.5rem] overflow-hidden border border-white/10 hover:border-white/30 hover:bg-white/10 transition-all duration-500 flex flex-col shadow-2xl"
          >
            <div class="aspect-[16/9] overflow-hidden">
              <img 
                :src="post.image" 
                :alt="post.title" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000 brightness-75 group-hover:brightness-100 grayscale hover:grayscale-0" 
              />
            </div>
            <div class="p-10 flex-1 flex flex-col">
              <div class="flex items-center gap-4 mb-6">
                <span class="text-[10px] font-black text-white px-3 py-1 rounded-full bg-white/10 uppercase tracking-widest">{{ post.tags[0] }}</span>
                <span class="text-[10px] font-bold text-white/30 uppercase tracking-widest">{{ post.date }}</span>
              </div>
              <h2 class="text-2xl font-bold text-white mb-4 group-hover:text-white transition-colors font-serif italic">
                {{ post.title }}
              </h2>
              <p class="text-white/50 mb-8 line-clamp-3 leading-relaxed">
                {{ post.description }}
              </p>
              <div class="mt-auto flex items-center text-white/80 font-bold text-xs uppercase tracking-widest">
                {{ $t('blog.readMore') }}
                <Icon name="lucide:arrow-right" class="size-4 ml-2 transition-transform group-hover:translate-x-1" />
              </div>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <CTASection />
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
