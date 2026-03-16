/** In production, set VITE_API_URL to your backend (e.g. Railway). In dev, leave unset for proxy. */
export const API_BASE = (import.meta.env.VITE_API_URL as string) || '';

/** Use for profile pictures and other uploads in production. */
export function assetUrl(path: string | null | undefined): string {
  if (!path) return '';
  if (path.startsWith('http')) return path;
  return API_BASE + path;
}
