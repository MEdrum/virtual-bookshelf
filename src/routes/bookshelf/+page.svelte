<script lang="ts">
	import { resolve } from '$app/paths';
	import BookRow from '$lib/components/BookRow.svelte';
	import type { PageServerData } from './$types';

	let { data }: { data: PageServerData } = $props();
</script>

<a href={resolve('/bookshelf/add')}>Add Bookshelf</a>

{#each data.shelves as shelf (shelf.id)}
	<BookRow {shelf} />
{/each}
