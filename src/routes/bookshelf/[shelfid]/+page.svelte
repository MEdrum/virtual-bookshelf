<script lang="ts">
	import BookRow from '$lib/components/BookRow.svelte';
	import type { PageServerData } from './$types';

	let { data }: { data: PageServerData } = $props();
</script>

<BookRow shelf={data.shelf} />
