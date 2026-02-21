<template>
  <main v-if="post && localizedContent" class="min-h-screen bg-transparent">
    <!-- Article Header -->
    <header class="bg-transparent pt-40 pb-16">
      <div class="mx-auto max-w-4xl px-6 lg:px-8">
        <NuxtLink to="/blog" class="inline-flex items-center text-white/50 hover:text-white mb-12 transition-colors uppercase text-[10px] font-black tracking-[0.2em]">
          <Icon name="lucide:arrow-left" class="size-4 mr-2" />
          {{ $t('header.blog') }}
        </NuxtLink>
        <div class="flex items-center gap-4 mb-8">
          <span v-for="tag in localizedContent.tags" :key="tag" class="px-4 py-1 bg-white/10 text-white text-[10px] font-black rounded-full uppercase tracking-widest">
            {{ tag }}
          </span>
          <span class="text-white/30 text-[10px] font-black uppercase tracking-widest">{{ post.date }}</span>
        </div>
        <h1 class="text-4xl font-bold tracking-tight text-white sm:text-7xl mb-12 leading-tight font-serif italic">
          {{ localizedContent.title }}
        </h1>
        <div class="flex items-center gap-6">
          <div class="size-14 rounded-full bg-white flex items-center justify-center font-bold text-dream-deep shadow-xl">
            {{ localizedContent.author.charAt(0) }}
          </div>
          <div>
            <div class="font-bold text-white text-lg">{{ localizedContent.author }}</div>
            <div class="text-xs text-white/40 uppercase tracking-widest font-bold">Author at StoryMe</div>
          </div>
        </div>
      </div>
    </header>

    <!-- Post Image -->
    <div class="mx-auto max-w-5xl px-6 lg:px-8 mt-8 relative z-10">
      <div class="aspect-[21/9] rounded-[3rem] overflow-hidden shadow-3xl border border-white/10">
        <img :src="post.image" :alt="localizedContent.title" class="w-full h-full object-cover shadow-2xl" />
      </div>
    </div>

    <!-- Article Content -->
    <article class="py-24">
      <div class="mx-auto max-w-3xl px-6 lg:px-8">
        <div 
          class="prose prose-lg prose-invert max-w-none text-white/70 leading-relaxed
                 prose-headings:text-white prose-headings:font-serif prose-headings:italic
                 prose-h2:text-4xl prose-h2:mt-16 prose-h2:mb-8
                 prose-h3:text-3xl prose-h3:mt-12 prose-h3:mb-6
                 prose-p:mb-8 prose-strong:text-white"
          v-html="localizedContent.content"
        ></div>
        
        <!-- Social Share -->
        <div class="mt-20 pt-10 border-t border-white/10 flex flex-col sm:flex-row items-center justify-between gap-8">
          <div class="flex gap-4">
            <button class="size-12 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-white hover:bg-white/15 transition-all">
              <Icon name="lucide:twitter" class="size-5" />
            </button>
            <button class="size-12 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-white hover:bg-white/15 transition-all">
              <Icon name="lucide:facebook" class="size-5" />
            </button>
            <button class="size-12 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-white hover:bg-white/15 transition-all">
              <Icon name="lucide:link" class="size-5" />
            </button>
          </div>
          <NuxtLink to="/blog" class="text-white font-black uppercase text-xs tracking-widest hover:text-white/70 transition-colors">
            {{ $t('blog.readMore') }}
          </NuxtLink>
        </div>
      </div>
    </article>

    <CTASection />
  </main>
  <div v-else class="min-h-screen flex items-center justify-center bg-dream-deep text-white">
    <div class="text-center">
      <h1 class="text-9xl font-black text-white/5 mb-[-2rem]">404</h1>
      <h2 class="text-3xl font-serif italic mb-8">Article not found</h2>
      <NuxtLink to="/blog" class="inline-block px-10 py-4 bg-white text-dream-deep rounded-2xl font-bold transition-transform hover:scale-105">
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
