import { error } from '@sveltejs/kit';
import { getBookInShelfByIsbnOrId, getShelfWithOwner, visibilityLabelMap } from '$lib/server/books';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const selectedShelf = await getShelfWithOwner(params.shelfid);
	if (!selectedShelf) {
		throw error(404, 'Shelf not found.');
	}

	const selectedBook = await getBookInShelfByIsbnOrId(selectedShelf.id, params.isbn);
	if (!selectedBook) {
		throw error(404, 'Book not found in this shelf.');
	}

	return {
		shelf: selectedShelf,
		book: {
			...selectedBook,
			yearOfPublication: selectedBook.yearOfPublication || 'Unknown',
			genre: selectedBook.genre
				? selectedBook.genre[0].toUpperCase() + selectedBook.genre.slice(1)
				: '',
			language: selectedBook.language
				? selectedBook.language[0].toUpperCase() + selectedBook.language.slice(1)
				: '',
			visibilityDisplay: visibilityLabelMap[selectedBook.visibility] ?? 'Private'
		}
	};
};
