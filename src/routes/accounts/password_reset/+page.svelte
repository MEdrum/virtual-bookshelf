<script lang="ts">
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();
</script>

<h2>Reset password</h2>
<form method="post" class="contact-form">
	<label for="email">Email:</label>
	<input id="email" name="email" type="email" required />
	<input type="submit" value="Reset password" />
</form>

{#if form?.message}
	<p>{form.message}</p>
{/if}
