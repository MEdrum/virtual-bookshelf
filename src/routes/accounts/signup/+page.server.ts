import { APIError } from 'better-auth/api';
import { eq } from 'drizzle-orm';
import { fail, redirect } from '@sveltejs/kit';
import { auth } from '$lib/server/auth';
import { db } from '$lib/server/db';
import { user } from '$lib/server/db/schema';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	if (locals.user) {
		throw redirect(302, '/');
	}

	return {};
};

export const actions: Actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const username = formData.get('username')?.toString().trim() ?? '';
		const email = formData.get('email')?.toString().trim() ?? '';
		const password1 = formData.get('password1')?.toString() ?? '';
		const password2 = formData.get('password2')?.toString() ?? '';

		if (!username || !email || !password1 || !password2) {
			return fail(400, { message: 'Username, email, and both password fields are required.' });
		}

		if (password1 !== password2) {
			return fail(400, { message: 'Passwords do not match.' });
		}

		const [existingUser] = await db
			.select({ id: user.id })
			.from(user)
			.where(eq(user.name, username))
			.limit(1);
		if (existingUser) {
			return fail(400, { message: 'Username is already in use.' });
		}

		try {
			await auth.api.signUpEmail({
				body: {
					name: username,
					email,
					password: password1,
					callbackURL: '/'
				}
			});
			await auth.api.signInEmail({
				body: {
					email,
					password: password1,
					callbackURL: '/'
				}
			});
		} catch (error) {
			if (error instanceof APIError) {
				return fail(400, { message: error.message || 'Sign up failed.' });
			}

			throw error;
		}

		throw redirect(302, '/');
	}
};
