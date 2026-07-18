<script lang="ts">
	import BookRow from '$lib/components/BookRow.svelte';
	import type { PageServerData } from './$types';

	let { data }: { data: PageServerData } = $props();
</script>

<h2>{data.username}'s bookshelves</h2>

{#each data.shelves as shelf (shelf.id)}
	<BookRow {shelf} />
{/each}
