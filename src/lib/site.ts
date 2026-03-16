export const SITE_TITLE = "SavvyM's Blog";
export const SITE_DESCRIPTION =
  "Notes from SavvyM on algorithms, programming languages, Linux, and reading papers.";
export const SITE_TAGLINE = "";
export const SITE_AUTHOR = "SavvyM";
export const SITE_GITHUB = "https://github.com/savvym";
export const SITE_LINKEDIN = "";
export const SITE_LEETCODE = "https://leetcode.cn/u/savvym/";

export const NAV_LINKS = [
  { label: "About", href: "/about/" },
  { label: "GitHub", href: SITE_GITHUB, external: true }
] as const;

export const HEADER_TOPICS = [
  "Algorithm",
  "C++",
  "linux",
  "Java",
  "Golang"
] as const;

export const FOOTER_LINKS = [
  { label: "About", href: "/about/" },
  { label: "GitHub", href: SITE_GITHUB, external: true }
] as const;

export function withBase(path: string) {
  if (/^https?:\/\//.test(path)) {
    return path;
  }

  const base = import.meta.env.BASE_URL ?? "/";
  const trimmed = path.replace(/^\//, "");

  if (!trimmed) {
    return base;
  }

  return `${base}${trimmed}`;
}
