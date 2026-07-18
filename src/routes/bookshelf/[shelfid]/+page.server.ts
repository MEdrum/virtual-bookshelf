import { asc, eq } from 'drizzle-orm';
import { error } from '@sveltejs/kit';
import { db } from '$lib/server/db';
import { book } from '$lib/server/db/schema';
import { getShelfWithOwner } from '$lib/server/books';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const selectedShelf = await getShelfWithOwner(params.shelfid);
	if (!selectedShelf) {
		throw error(404, 'Shelf not found.');
	}

	const shelfBooks = await db
		.select({
			id: book.id,
			isbn: book.isbn,
			title: book.title,
			author: book.author,
			coverUrl: book.coverUrl
		})
		.from(book)
		.where(eq(book.shelfId, selectedShelf.id))
		.orderBy(asc(book.title));

	return {
		shelf: {
			id: selectedShelf.id,
			name: selectedShelf.name,
			books: shelfBooks
		}
	};
};
