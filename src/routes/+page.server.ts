import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => ({
	user: locals.user ?? null
});
