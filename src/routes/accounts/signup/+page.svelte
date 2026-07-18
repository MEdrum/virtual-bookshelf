<script lang="ts">
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();
</script>

<h2>Sign Up</h2>
<form method="post" class="contact-form">
	<label for="username">Username:</label>
	<input id="username" name="username" type="text" required />

	<label for="email">Email:</label>
	<input id="email" name="email" type="email" required />

	<label for="password1">Password:</label>
	<input id="password1" name="password1" type="password" required />

	<label for="password2">Password again:</label>
	<input id="password2" name="password2" type="password" required />

	<input type="submit" value="Sign Up" />
</form>

{#if form?.message}
	<p>{form.message}</p>
{/if}
