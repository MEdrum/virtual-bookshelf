<script lang="ts">
	import { resolve } from '$app/paths';
	import type { PageServerData } from './$types';

	let { data }: { data: PageServerData } = $props();
</script>

<h3>
	<a href={resolve(`/user/${data.shelf.ownerName}/`)}>{data.shelf.ownerName}</a>
	&gt;
	<a href={resolve(`/bookshelf/${data.shelf.id}/`)}>{data.shelf.name}</a>
</h3>
<h1>{data.book.title}</h1>
<img
	class="bookcover"
	src={data.book.coverUrl || 'https://placehold.co/320x480?text=No+Cover'}
	alt={data.book.title}
/>
<p>Author: {data.book.author}</p>
<p>ISBN: {data.book.isbn}</p>
<p>Genre: {data.book.genre}</p>
<p>Language: {data.book.language}</p>
<p>Pub. date: {data.book.yearOfPublication}</p>
<p>Borrowable: {data.book.borrowable ? 'True' : 'False'}</p>
<p>Visibility: {data.book.visibilityDisplay}</p>

<a href={resolve(`/bookshelf/book/edit/${data.shelf.id}/${data.book.id}/`)}>Edit</a>
