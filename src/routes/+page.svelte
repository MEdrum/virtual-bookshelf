<script lang="ts">
	import { resolve } from '$app/paths';
	import type { PageServerData } from './$types';

	let { data }: { data: PageServerData } = $props();
</script>

<h1>Home</h1>

{#if data.user}
	<h2>Hi {data.user.name}!</h2>
	<a href={resolve('/bookshelf')}>Bookshelves</a><br />
	<a href={resolve('/friend_request')}>Friend Requests</a><br />
	<a href={resolve('/loan_request')}>Loan Requests</a>
	<p><a href={resolve('/accounts/password_change')}>Change Password</a></p>
	<form method="post" action={resolve('/accounts/logout')} class="auth-controls">
		<button type="submit">Log Out</button>
	</form>
{/if}
