import { and, eq, or } from 'drizzle-orm';
import { redirect } from '@sveltejs/kit';
import { db } from '$lib/server/db';
import {
	book,
	genreOptions,
	languageOptions,
	shelf,
	user,
	visibilityOptions
} from '$lib/server/db/schema';

const optionTitle = (value: string) =>
	value ? value.charAt(0).toUpperCase() + value.slice(1) : '';

export const genreLabels = genreOptions.map(optionTitle);
export const languageLabels = languageOptions.map(optionTitle);

export const visibilityLabelMap: Record<string, string> = {
	private: 'Private',
	friends: 'Friends',
	public: 'Public'
};

export const normalizeVisibility = (value: string) =>
	visibilityOptions.includes(value as (typeof visibilityOptions)[number]) ? value : 'private';

export const normalizeGenre = (value: string) => {
	const lowered = value.toLowerCase();
	return genreOptions.includes(lowered as (typeof genreOptions)[number]) ? lowered : '';
};

export const normalizeLanguage = (value: string) => {
	const lowered = value.toLowerCase();
	return languageOptions.includes(lowered as (typeof languageOptions)[number]) ? lowered : '';
};

export const requireAuthenticatedUser = (locals: App.Locals) => {
	if (!locals.user) {
		throw redirect(302, '/accounts/login/');
	}

	return locals.user;
};

export const getShelfWithOwner = async (shelfId: string) => {
	const [selectedShelf] = await db
		.select({
			id: shelf.id,
			name: shelf.name,
			latitude: shelf.latitude,
			longitude: shelf.longitude,
			ownerId: shelf.ownerId,
			ownerName: user.name
		})
		.from(shelf)
		.innerJoin(user, eq(shelf.ownerId, user.id))
		.where(eq(shelf.id, shelfId))
		.limit(1);

	return selectedShelf ?? null;
};

export const getBookInShelfByIsbnOrId = async (shelfId: string, identifier: string) => {
	const [selectedBook] = await db
		.select()
		.from(book)
		.where(and(eq(book.shelfId, shelfId), or(eq(book.isbn, identifier), eq(book.id, identifier))))
		.limit(1);

	return selectedBook ?? null;
};
