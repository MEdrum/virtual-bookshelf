import { fail, redirect } from '@sveltejs/kit';
import { db } from '$lib/server/db';
import { shelf } from '$lib/server/db/schema';
import { requireAuthenticatedUser } from '$lib/server/books';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	requireAuthenticatedUser(locals);
	return {};
};

export const actions: Actions = {
	default: async ({ request, locals }) => {
		const authenticatedUser = requireAuthenticatedUser(locals);
		const formData = await request.formData();

		const name = formData.get('name')?.toString().trim() ?? '';
		const latitude = Number(formData.get('latitude')?.toString() ?? '');
		const longitude = Number(formData.get('longitude')?.toString() ?? '');

		if (!name || Number.isNaN(latitude) || Number.isNaN(longitude)) {
			return fail(400, { message: 'Name, latitude, and longitude are required.' });
		}

		await db.insert(shelf).values({
			name,
			latitude,
			longitude,
			ownerId: authenticatedUser.id
		});

		throw redirect(302, '/bookshelf/');
	}
};
