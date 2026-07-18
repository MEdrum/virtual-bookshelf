import { relations, sql } from 'drizzle-orm';
import { index, integer, real, sqliteTable, text } from 'drizzle-orm/sqlite-core';
import { user } from './auth.schema';

export const visibilityOptions = ['private', 'friends', 'public'] as const;
export const genreOptions = ['', 'romance', 'non-fiction', 'thriller', 'fantasy'] as const;
export const languageOptions = ['', 'german', 'english', 'spanish', 'italian'] as const;

export const shelf = sqliteTable(
	'shelf',
	{
		id: text('id')
			.primaryKey()
			.$defaultFn(() => crypto.randomUUID()),
		name: text('name').notNull(),
		ownerId: text('owner_id')
			.notNull()
			.references(() => user.id, { onDelete: 'cascade' }),
		latitude: real('latitude').notNull(),
		longitude: real('longitude').notNull()
	},
	(table) => [index('shelf_owner_idx').on(table.ownerId)]
);

export const book = sqliteTable(
	'book',
	{
		id: text('id')
			.primaryKey()
			.$defaultFn(() => crypto.randomUUID()),
		isbn: text('isbn').notNull().unique(),
		title: text('title').notNull(),
		author: text('author').notNull(),
		genre: text('genre').notNull().default(''),
		language: text('language').notNull().default(''),
		yearOfPublication: integer('year_of_publication'),
		visibility: text('visibility').notNull().default('private'),
		borrowable: integer('borrowable', { mode: 'boolean' }).notNull().default(true),
		ownerId: text('owner_id')
			.notNull()
			.references(() => user.id, { onDelete: 'cascade' }),
		shelfId: text('shelf_id')
			.notNull()
			.references(() => shelf.id, { onDelete: 'cascade' }),
		coverUrl: text('cover_url')
	},
	(table) => [index('book_shelf_idx').on(table.shelfId), index('book_owner_idx').on(table.ownerId)]
);

export const friendRequest = sqliteTable(
	'friend_request',
	{
		id: text('id')
			.primaryKey()
			.$defaultFn(() => crypto.randomUUID()),
		state: integer('state').notNull().default(0),
		requesterId: text('requester_id')
			.notNull()
			.references(() => user.id, { onDelete: 'cascade' }),
		receiverId: text('receiver_id')
			.notNull()
			.references(() => user.id, { onDelete: 'cascade' }),
		createdAt: integer('created_at', { mode: 'timestamp_ms' })
			.default(sql`(cast(unixepoch('subsecond') * 1000 as integer))`)
			.notNull()
	},
	(table) => [
		index('friend_request_requester_idx').on(table.requesterId),
		index('friend_request_receiver_idx').on(table.receiverId)
	]
);

export const loanRequest = sqliteTable(
	'loan_request',
	{
		id: text('id')
			.primaryKey()
			.$defaultFn(() => crypto.randomUUID()),
		state: integer('state').notNull().default(0),
		requesterId: text('requester_id')
			.notNull()
			.references(() => user.id, { onDelete: 'cascade' }),
		receiverId: text('receiver_id')
			.notNull()
			.references(() => user.id, { onDelete: 'cascade' }),
		requestedBookId: text('requested_book_id')
			.notNull()
			.references(() => book.id, { onDelete: 'cascade' }),
		createdAt: integer('created_at', { mode: 'timestamp_ms' })
			.default(sql`(cast(unixepoch('subsecond') * 1000 as integer))`)
			.notNull()
	},
	(table) => [
		index('loan_request_requester_idx').on(table.requesterId),
		index('loan_request_receiver_idx').on(table.receiverId),
		index('loan_request_book_idx').on(table.requestedBookId)
	]
);

export const shelfRelations = relations(shelf, ({ one, many }) => ({
	owner: one(user, {
		fields: [shelf.ownerId],
		references: [user.id]
	}),
	books: many(book)
}));

export const bookRelations = relations(book, ({ one, many }) => ({
	owner: one(user, {
		fields: [book.ownerId],
		references: [user.id]
	}),
	shelf: one(shelf, {
		fields: [book.shelfId],
		references: [shelf.id]
	}),
	loanRequests: many(loanRequest)
}));

export const friendRequestRelations = relations(friendRequest, ({ one }) => ({
	requester: one(user, {
		fields: [friendRequest.requesterId],
		references: [user.id]
	}),
	receiver: one(user, {
		fields: [friendRequest.receiverId],
		references: [user.id]
	})
}));

export const loanRequestRelations = relations(loanRequest, ({ one }) => ({
	requester: one(user, {
		fields: [loanRequest.requesterId],
		references: [user.id]
	}),
	receiver: one(user, {
		fields: [loanRequest.receiverId],
		references: [user.id]
	}),
	requestedBook: one(book, {
		fields: [loanRequest.requestedBookId],
		references: [book.id]
	})
}));

export * from './auth.schema';
