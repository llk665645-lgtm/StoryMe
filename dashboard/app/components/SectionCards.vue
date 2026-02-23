<script setup lang="ts">
import { IconTrendingDown, IconTrendingUp } from "@tabler/icons-vue"

import { Badge } from '@/components/ui/badge'
import {
  Card,
  CardAction,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
</script>

<template>
  <div class="*:data-[slot=card]:from-primary/5 *:data-[slot=card]:to-card dark:*:data-[slot=card]:bg-card grid grid-cols-1 gap-4 px-4 *:data-[slot=card]:bg-gradient-to-t *:data-[slot=card]:shadow-xs lg:px-6 @xl/main:grid-cols-2 @5xl/main:grid-cols-4">
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>Stories Created</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          18
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            <IconTrendingUp class="size-3" />
            +2 this week
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Growing library <IconTrendingUp class="size-4" />
        </div>
        <div class="text-muted-foreground">
          Total magical moments created
        </div>
      </CardFooter>
    </Card>
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>Characters</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          3
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            View all
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Oliver, Sophia, Leo
        </div>
        <div class="text-muted-foreground">
          Personalized per each child
        </div>
      </CardFooter>
    </Card>
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>Gallery Images</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          48
        </CardTitle>
        <CardAction>
          <Badge variant="outline" class="text-green-500 border-green-200">
            Watercolor
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          AI Illustrations
        </div>
        <div class="text-muted-foreground">
          Unique art for every story
        </div>
      </CardFooter>
    </Card>
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>AI Credits</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          15
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            Top up
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Storyteller plan active <IconTrendingUp class="size-4" />
        </div>
        <div class="text-muted-foreground">
          Renews in 12 days
        </div>
      </CardFooter>
    </Card>

  </div>
</template>
