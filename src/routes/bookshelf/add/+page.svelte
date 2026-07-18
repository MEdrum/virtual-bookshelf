<script lang="ts">
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();
</script>

<h2>Add a new bookshelf</h2>

<form class="contact-form" method="post">
	<label for="name">Bookshelf name:</label><br />
	<input type="text" id="name" name="name" required /><br /><br />

	<label for="latitude">Latitude:</label><br />
	<input type="number" id="latitude" name="latitude" step="0.000001" required /><br /><br />

	<label for="longitude">Longitude:</label><br />
	<input type="number" id="longitude" name="longitude" step="0.000001" required /><br /><br />

	<input type="submit" value="Save" />
</form>

{#if form?.message}
	<p>{form.message}</p>
{/if}
