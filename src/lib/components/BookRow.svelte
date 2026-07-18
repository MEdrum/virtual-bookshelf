<script lang="ts">
	import { resolve } from '$app/paths';

	type Book = {
		id: string;
		isbn: string;
		title: string;
		author: string;
		coverUrl: string | null;
	};

	type ShelfWithBooks = {
		id: string;
		name: string;
		books: Book[];
	};

	let { shelf }: { shelf: ShelfWithBooks } = $props();
</script>

<div class="book-row">
	<fieldset>
		<legend>
			<h3>{shelf.name}</h3>
		</legend>
		<div class="carousel">
			{#each shelf.books as bookEntry (bookEntry.id)}
				<div class="book">
					<a href={resolve(`/bookshelf/${shelf.id}/${bookEntry.isbn}`)}>
						<img
							src={bookEntry.coverUrl || 'https://placehold.co/160x240?text=No+Cover'}
							alt={bookEntry.title}
						/>
					</a>
					<h4>{bookEntry.title}</h4>
					<p>Author: {bookEntry.author}</p>
				</div>
			{/each}
		</div>
	</fieldset>
	<a href={resolve(`/bookshelf/book/new/${shelf.id}/`)}>Add Book</a>
</div>
