import { redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions: Actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const email = formData.get('email')?.toString().trim() ?? '';

		if (!email) {
			return { message: 'Please provide an email address.' };
		}

		throw redirect(302, '/accounts/password_reset/done/');
	}
};
