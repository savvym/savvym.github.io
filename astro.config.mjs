import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import rehypeSlug from "rehype-slug";
import rehypeAutolinkHeadings from "rehype-autolink-headings";
import { visit } from "unist-util-visit";

const [repoOwner = "localhost", repoName = "blog-savvym"] = (
  process.env.GITHUB_REPOSITORY ?? ""
).split("/");

const isUserPagesRepo = repoName === `${repoOwner}.github.io`;
const site = process.env.SITE_URL ?? `https://${repoOwner}.github.io`;
const base =
  process.env.BASE_PATH ??
  (process.env.GITHUB_ACTIONS === "true" && !isUserPagesRepo ? `/${repoName}/` : "/");

function prefixBaseUrls(siteBase) {
  return () => {
    return (tree) => {
      visit(tree, "element", (node) => {
        if (!node.properties) {
          return;
        }

        const key = node.tagName === "img" ? "src" : node.tagName === "a" ? "href" : null;
        if (!key) {
          return;
        }

        const value = node.properties[key];
        if (typeof value !== "string" || !value.startsWith("/") || value.startsWith("//")) {
          return;
        }

        node.properties[key] = `${siteBase}${value.replace(/^\//, "")}`;
      });
    };
  };
}

export default defineConfig({
  site,
  base,
  trailingSlash: "always",
  integrations: [sitemap()],
  markdown: {
    remarkPlugins: [remarkGfm, remarkMath],
    rehypePlugins: [
      rehypeKatex,
      rehypeSlug,
      prefixBaseUrls(base),
      [
        rehypeAutolinkHeadings,
        {
          behavior: "append",
          content: [
            {
              type: "text",
              value: "#"
            }
          ],
          properties: {
            className: ["heading-link"],
            ariaHidden: "true",
            tabIndex: -1
          }
        }
      ]
    ],
    shikiConfig: {
      theme: "github-dark"
    }
  }
});
