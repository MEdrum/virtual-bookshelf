<script lang="ts">
	import { resolve } from '$app/paths';
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import type { LayoutServerData } from './$types';

	let { children, data }: { children: import('svelte').Snippet; data: LayoutServerData } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<header>
	<nav>
		<button type="button">Menu</button>
		<img
			src="https://cdn-icons-png.flaticon.com/512/9815/9815472.png"
			alt="Virtual Bookshelf Logo"
		/>
	</nav>
</header>

<main>
	{#if data.user || data.isAuthPage}
		{@render children()}
	{:else}
		<p>You are not logged in</p>
		<p><a href={resolve('/accounts/signup')}>Sign up</a></p>
		<p><a href={resolve('/accounts/login')}>Log in</a></p>
		<p><a href={resolve('/accounts/password_reset')}>Forgot Password?</a></p>
	{/if}
</main>

<footer></footer>
