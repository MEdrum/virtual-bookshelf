import { error, fail } from '@sveltejs/kit';
import { db } from '$lib/server/db';
import { book } from '$lib/server/db/schema';
import {
	genreLabels,
	getShelfWithOwner,
	languageLabels,
	normalizeGenre,
	normalizeLanguage,
	normalizeVisibility,
	requireAuthenticatedUser
} from '$lib/server/books';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals, params }) => {
	const authenticatedUser = requireAuthenticatedUser(locals);
	const selectedShelf = await getShelfWithOwner(params.shelfid);
	if (!selectedShelf) {
		throw error(404, 'Shelf not found.');
	}

	if (selectedShelf.ownerId !== authenticatedUser.id) {
		throw error(403, 'You can only add books to your own shelf.');
	}

	return {
		shelf: selectedShelf,
		formDefaults: {
			title: '',
			author: '',
			isbn: '',
			genre: '',
			language: '',
			pubYear: '',
			borrowable: true,
			visibility: 'public',
			coverURL: ''
		},
		genres: genreLabels,
		languages: languageLabels,
		isEdit: false
	};
};

export const actions: Actions = {
	default: async ({ request, locals, params }) => {
		const authenticatedUser = requireAuthenticatedUser(locals);
		const selectedShelf = await getShelfWithOwner(params.shelfid);
		if (!selectedShelf) {
			return fail(404, { message: 'Shelf not found.' });
		}

		if (selectedShelf.ownerId !== authenticatedUser.id) {
			return fail(403, { message: 'You can only add books to your own shelf.' });
		}

		const formData = await request.formData();
		const title = formData.get('title')?.toString().trim() ?? '';
		const author = formData.get('author')?.toString().trim() ?? '';
		const isbn = formData.get('isbn')?.toString().trim() ?? '';
		const genre = normalizeGenre(formData.get('genre')?.toString() ?? '');
		const language = normalizeLanguage(formData.get('language')?.toString() ?? '');
		const yearValue = formData.get('pubYear')?.toString().trim() ?? '';
		const yearOfPublication = yearValue ? Number(yearValue) : null;
		const borrowable = formData.get('borrowable') === 'on';
		const visibility = normalizeVisibility(
			formData.get('visibility')?.toString().toLowerCase() ?? ''
		);
		const coverUrl = formData.get('coverURL')?.toString().trim() || null;

		if (!title || !author || !isbn) {
			return fail(400, { message: 'Title, author, and ISBN are required.' });
		}

		if (yearOfPublication !== null && Number.isNaN(yearOfPublication)) {
			return fail(400, { message: 'Publication year must be a valid number.' });
		}

		await db.insert(book).values({
			title,
			author,
			isbn,
			genre,
			language,
			yearOfPublication,
			borrowable,
			visibility,
			coverUrl,
			ownerId: authenticatedUser.id,
			shelfId: selectedShelf.id
		});

		return {
			success: true,
			isEdit: false
		};
	}
};
