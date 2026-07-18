<script lang="ts">
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();
</script>

<h2>Change password</h2>
<form method="post" class="contact-form">
	<label for="currentPassword">Current password:</label>
	<input id="currentPassword" name="currentPassword" type="password" required />

	<label for="newPassword1">New password:</label>
	<input id="newPassword1" name="newPassword1" type="password" required />

	<label for="newPassword2">New password (repeat):</label>
	<input id="newPassword2" name="newPassword2" type="password" required />

	<input type="submit" value="Change password" />
</form>

{#if form?.message}
	<p>{form.message}</p>
{/if}
