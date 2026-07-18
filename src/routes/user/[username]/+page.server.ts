import { asc, eq } from 'drizzle-orm';
import { error } from '@sveltejs/kit';
import { db } from '$lib/server/db';
import { book, shelf, user } from '$lib/server/db/schema';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const [selectedUser] = await db
		.select({ id: user.id, name: user.name })
		.from(user)
		.where(eq(user.name, params.username))
		.limit(1);

	if (!selectedUser) {
		throw error(404, 'User not found.');
	}

	const shelves = await db
		.select({
			id: shelf.id,
			name: shelf.name
		})
		.from(shelf)
		.where(eq(shelf.ownerId, selectedUser.id))
		.orderBy(asc(shelf.name));

	const books = await db
		.select({
			id: book.id,
			shelfId: book.shelfId,
			isbn: book.isbn,
			title: book.title,
			author: book.author,
			coverUrl: book.coverUrl
		})
		.from(book)
		.orderBy(asc(book.title));

	return {
		username: selectedUser.name,
		shelves: shelves.map((shelfRow) => ({
			...shelfRow,
			books: books.filter((bookRow) => bookRow.shelfId === shelfRow.id)
		}))
	};
};
