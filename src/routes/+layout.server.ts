import type { LayoutServerLoad } from './$types';

const authPathPrefixes = ['/accounts/login/', '/accounts/signup/', '/accounts/password_reset/'];

export const load: LayoutServerLoad = async ({ locals, url }) => {
	const pathname = url.pathname.endsWith('/') ? url.pathname : `${url.pathname}/`;
	const isAuthPage = authPathPrefixes.some((prefix) => pathname.startsWith(prefix));

	return {
		user: locals.user ?? null,
		isAuthPage
	};
};
