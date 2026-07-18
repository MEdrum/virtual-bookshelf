<script lang="ts">
	import { resolve } from '$app/paths';
	import type { ActionData, PageServerData } from './$types';

	let { data, form }: { data: PageServerData; form: ActionData } = $props();
</script>

{#if form?.success}
	<p>Book successfully edited!</p>
	<p><a href={resolve('/bookshelf')}>Back to my bookshelves</a></p>
{:else}
	<h2>Edit book</h2>
	<h3>
		<a href={resolve(`/user/${data.shelf.ownerName}/`)}>{data.shelf.ownerName}</a>
		&gt;
		<a href={resolve(`/bookshelf/${data.shelf.id}/`)}>{data.shelf.name}</a>
	</h3>

	<form class="contact-form" method="post">
		<label for="title">Title:</label><br />
		<input type="text" id="title" name="title" value={data.book.title} />
		<label for="author">Author:</label><br />
		<input type="text" id="author" name="author" value={data.book.author} />
		<label for="isbn">ISBN:</label><br />
		<input type="text" id="isbn" name="isbn" value={data.book.isbn} />
		<label for="genre">Genre:</label><br />
		<select name="genre" id="genre">
			{#each data.genres as genre (genre)}
				<option value={genre} selected={genre.toLowerCase() === data.book.genre}>{genre}</option>
			{/each}
		</select>
		<label for="language">Language:</label><br />
		<select name="language" id="language">
			{#each data.languages as language (language)}
				<option value={language} selected={language.toLowerCase() === data.book.language}
					>{language}</option
				>
			{/each}
		</select>
		<label for="pubYear">Pub. year:</label><br />
		<input type="number" id="pubYear" name="pubYear" value={data.book.yearOfPublication ?? ''} /><br
		/>
		<label for="borrowable">Borrowable?</label><br />
		<input type="checkbox" id="borrowable" name="borrowable" checked={data.book.borrowable} /><br />
		<label for="visibility">Visibility:</label><br />
		<select name="visibility" id="visibility">
			<option value="public" selected={data.book.visibility === 'public'}>Public</option>
			<option value="friends" selected={data.book.visibility === 'friends'}>Friends</option>
			<option value="private" selected={data.book.visibility === 'private'}>Private</option>
		</select>
		<label for="coverURL">URL to cover:</label>
		<input type="url" id="coverURL" name="coverURL" value={data.book.coverUrl ?? ''} />
		<input type="submit" value="Save" />
	</form>

	{#if form?.message}
		<p>{form.message}</p>
	{/if}
{/if}
