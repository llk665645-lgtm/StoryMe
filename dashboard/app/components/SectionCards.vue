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
          12
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            <IconTrendingUp />
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
        <CardDescription>Remaining Credits</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          3
        </CardTitle>
        <CardAction>
          <Badge variant="outline" class="text-orange-500 border-orange-200">
            Top up
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Ready for more stories
        </div>
        <div class="text-muted-foreground">
          Storyteller plan active
        </div>
      </CardFooter>
    </Card>
    <Card class="@container/card">
      <CardHeader>
        <CardDescription>Child Profiles</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          3
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            <IconPlus class="size-3 mr-1" /> Add
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
        <CardDescription>Favorite Theme</CardDescription>
        <CardTitle class="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          Forest
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            Popular
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter class="flex-col items-start gap-1.5 text-sm">
        <div class="line-clamp-1 flex gap-2 font-medium">
          Magic & Nature <IconTrendingUp class="size-4" />
        </div>
        <div class="text-muted-foreground">
          Most used world theme
        </div>
      </CardFooter>
    </Card>

  </div>
</template>
