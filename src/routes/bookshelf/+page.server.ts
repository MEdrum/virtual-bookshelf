import { asc, eq } from 'drizzle-orm';
import { db } from '$lib/server/db';
import { book, shelf, user } from '$lib/server/db/schema';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const shelves = await db
		.select({
			id: shelf.id,
			name: shelf.name,
			ownerId: shelf.ownerId,
			ownerName: user.name
		})
		.from(shelf)
		.innerJoin(user, eq(shelf.ownerId, user.id))
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
		shelves: shelves.map((shelfRow) => ({
			...shelfRow,
			books: books.filter((bookRow) => bookRow.shelfId === shelfRow.id)
		}))
	};
};
