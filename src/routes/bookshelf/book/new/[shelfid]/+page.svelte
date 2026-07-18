<script lang="ts">
	import { resolve } from '$app/paths';
	import type { ActionData, PageServerData } from './$types';

	let { data, form }: { data: PageServerData; form: ActionData } = $props();
</script>

{#if form?.success}
	<p>Book successfully created!!</p>
	<p><a href={resolve('/bookshelf')}>Back to my bookshelves</a></p>
{:else}
	<h2>Add a new book</h2>
	<h3>
		<a href={resolve(`/user/${data.shelf.ownerName}/`)}>{data.shelf.ownerName}</a>
		&gt;
		<a href={resolve(`/bookshelf/${data.shelf.id}/`)}>{data.shelf.name}</a>
	</h3>

	<form class="contact-form" method="post">
		<label for="title">Title:</label><br />
		<input type="text" id="title" name="title" value={data.formDefaults.title} />
		<label for="author">Author:</label><br />
		<input type="text" id="author" name="author" value={data.formDefaults.author} />
		<label for="isbn">ISBN:</label><br />
		<input type="text" id="isbn" name="isbn" value={data.formDefaults.isbn} />
		<label for="genre">Genre:</label><br />
		<select name="genre" id="genre">
			{#each data.genres as genre (genre)}
				<option value={genre}>{genre}</option>
			{/each}
		</select>
		<label for="language">Language:</label><br />
		<select name="language" id="language">
			{#each data.languages as language (language)}
				<option value={language}>{language}</option>
			{/each}
		</select>
		<label for="pubYear">Pub. year:</label><br />
		<input type="number" id="pubYear" name="pubYear" value={data.formDefaults.pubYear} /><br />
		<label for="borrowable">Borrowable?</label><br />
		<input
			type="checkbox"
			id="borrowable"
			name="borrowable"
			checked={data.formDefaults.borrowable}
		/><br />
		<label for="visibility">Visibility:</label><br />
		<select name="visibility" id="visibility">
			<option value="public">Public</option>
			<option value="friends">Friends</option>
			<option value="private">Private</option>
		</select>
		<label for="coverURL">URL to cover:</label>
		<input type="url" id="coverURL" name="coverURL" value={data.formDefaults.coverURL} />
		<input type="submit" value="Save" />
	</form>

	{#if form?.message}
		<p>{form.message}</p>
	{/if}
{/if}
