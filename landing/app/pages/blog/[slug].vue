<template>
  <main v-if="post" class="min-h-screen bg-brand-light">
    <!-- Article Header -->
    <header class="bg-white pt-32 pb-16">
      <div class="mx-auto max-w-4xl px-6 lg:px-8">
        <NuxtLink to="/blog" class="inline-flex items-center text-brand-gray hover:text-primary mb-8 transition-colors">
          <Icon name="lucide:arrow-left" class="size-4 mr-2" />
          {{ $t('header.blog') }}
        </NuxtLink>
        <div class="flex items-center gap-4 mb-6">
          <span v-for="tag in localizedContent.tags" :key="tag" class="px-3 py-1 bg-primary/10 text-primary text-xs font-bold rounded-full uppercase">
            {{ tag }}
          </span>
          <span class="text-brand-gray text-sm">{{ post.date }}</span>
        </div>
        <h1 class="text-4xl font-bold tracking-tight text-brand-dark sm:text-6xl mb-8 leading-tight">
          {{ localizedContent.title }}
        </h1>
        <div class="flex items-center gap-4">
          <div class="size-12 rounded-full bg-brand-light flex items-center justify-center font-bold text-primary border border-border">
            {{ localizedContent.author.charAt(0) }}
          </div>
          <div>
            <div class="font-bold text-brand-dark">{{ localizedContent.author }}</div>
            <div class="text-xs text-brand-gray">Author at StoryMe</div>
          </div>
        </div>
      </div>
    </header>

    <!-- Post Image -->
    <div class="mx-auto max-w-5xl px-6 lg:px-8 -mt-8 relative z-10">
      <div class="aspect-[21/9] rounded-3xl overflow-hidden shadow-2xl">
        <img :src="post.image" :alt="localizedContent.title" class="w-full h-full object-cover" />
      </div>
    </div>

    <!-- Article Content -->
    <article class="py-20">
      <div class="mx-auto max-w-3xl px-6 lg:px-8">
        <div 
          class="prose prose-lg prose-primary max-w-none text-brand-gray leading-relaxed
                 prose-headings:text-brand-dark prose-headings:font-bold
                 prose-h2:text-3xl prose-h2:mt-12 prose-h2:mb-6
                 prose-h3:text-2xl prose-h3:mt-8 prose-h3:mb-4
                 prose-p:mb-6 prose-strong:text-brand-dark"
          v-html="localizedContent.content"
        ></div>
        
        <!-- Social Share -->
        <div class="mt-16 pt-8 border-t border-border flex flex-col sm:flex-row items-center justify-between gap-6">
          <div class="flex gap-4">
            <button class="size-10 rounded-full bg-white border border-border flex items-center justify-center hover:text-primary transition-colors">
              <Icon name="lucide:twitter" class="size-5" />
            </button>
            <button class="size-10 rounded-full bg-white border border-border flex items-center justify-center hover:text-primary transition-colors">
              <Icon name="lucide:facebook" class="size-5" />
            </button>
            <button class="size-10 rounded-full bg-white border border-border flex items-center justify-center hover:text-primary transition-colors">
              <Icon name="lucide:link" class="size-5" />
            </button>
          </div>
          <NuxtLink to="/blog" class="text-primary font-bold hover:underline">
            {{ $t('blog.readMore') }}
          </NuxtLink>
        </div>
      </div>
    </article>

    <CTASection />
    <AppFooter />
  </main>
  <div v-else class="min-h-screen flex items-center justify-center">
    <div class="text-center">
      <h1 class="text-6xl font-bold text-brand-dark mb-4">404</h1>
      <p class="text-brand-gray mb-8">Article not found</p>
      <NuxtLink to="/blog" class="px-8 py-4 bg-primary text-white rounded-2xl font-bold">
        Back to blog
      </NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { BLOG_POSTS } from '@/utils/blogData'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'

const route = useRoute()
const { locale } = useI18n()
const post = BLOG_POSTS.find(p => p.slug === route.params.slug)

const localizedContent = computed(() => {
  if (!post) return null
  return post[locale.value as 'en' | 'ru'] || post.en
})

if (post && localizedContent.value) {
  useSeoMeta({
    title: `${localizedContent.value.title} | StoryMe Blog`,
    description: localizedContent.value.description,
    ogTitle: localizedContent.value.title,
    ogDescription: localizedContent.value.description,
    ogImage: post.image,
    twitterCard: 'summary_large_image',
    author: localizedContent.value.author
  })
}
</script>

<style scoped>
/* Individual adjustments if prose doesn't cover everything */
:deep(h2) {
  margin-top: 2rem;
  margin-bottom: 1rem;
  font-weight: 700;
  color: var(--brand-dark);
}
</style>
