<script lang="ts">
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();
</script>

<h2>Log In</h2>
<form method="post" class="contact-form">
	<label for="email">Email:</label>
	<input id="email" name="email" type="email" required />

	<label for="password">Password:</label>
	<input id="password" name="password" type="password" required />

	<input type="submit" value="Log In" />
</form>

{#if form?.message}
	<p>{form.message}</p>
{/if}

<h2>
	<label for="user-table" style="background-color: red; display: inline-block"
		>Tip: The following test users already exist:</label
	>
</h2>
<table id="user-table">
	<tbody>
		<tr>
			<th>Username:</th>
			<th>Password:</th>
		</tr>
		<tr>
			<td>Anna</td>
			<td>Anna1234</td>
		</tr>
		<tr>
			<td>Charlie</td>
			<td>woozy chew reach wheat basil slang</td>
		</tr>
		<tr>
			<td>Lucy</td>
			<td>Lucy1234</td>
		</tr>
	</tbody>
</table>
