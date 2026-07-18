import { APIError } from 'better-auth/api';
import { fail, redirect } from '@sveltejs/kit';
import { auth } from '$lib/server/auth';
import { requireAuthenticatedUser } from '$lib/server/books';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	requireAuthenticatedUser(locals);
	return {};
};

export const actions: Actions = {
	default: async ({ request, locals }) => {
		requireAuthenticatedUser(locals);

		const formData = await request.formData();
		const currentPassword = formData.get('currentPassword')?.toString() ?? '';
		const newPassword1 = formData.get('newPassword1')?.toString() ?? '';
		const newPassword2 = formData.get('newPassword2')?.toString() ?? '';

		if (!currentPassword || !newPassword1 || !newPassword2) {
			return fail(400, { message: 'All password fields are required.' });
		}

		if (newPassword1 !== newPassword2) {
			return fail(400, { message: 'New passwords do not match.' });
		}

		try {
			await auth.api.changePassword({
				headers: request.headers,
				body: {
					currentPassword,
					newPassword: newPassword1,
					revokeOtherSessions: false
				}
			});
		} catch (error) {
			if (error instanceof APIError) {
				return fail(400, { message: error.message || 'Password change failed.' });
			}

			throw error;
		}

		throw redirect(302, '/accounts/password_change/done/');
	}
};
