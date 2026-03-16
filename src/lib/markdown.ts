import { createMarkdownProcessor } from "@astrojs/markdown-remark";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import remarkParse from "remark-parse";
import remarkStringify from "remark-stringify";
import { unified } from "unified";
import { visit } from "unist-util-visit";

type MarkdownNode = {
  type: string;
  value?: string;
  alt?: string;
  children?: MarkdownNode[];
  [key: string]: unknown;
};

type MarkdownRoot = {
  type: "root";
  children: MarkdownNode[];
};

type RenderedExcerpt = {
  html: string;
};

const [repoOwner = "localhost", repoName = "blog-savvym"] = (
  process.env.GITHUB_REPOSITORY ?? ""
).split("/");

const isUserPagesRepo = repoName === `${repoOwner}.github.io`;
const siteBase =
  process.env.BASE_PATH ??
  (process.env.GITHUB_ACTIONS === "true" && !isUserPagesRepo ? `/${repoName}/` : "/");

const excerptParser = unified().use(remarkParse).use(remarkGfm).use(remarkMath);
const excerptStringifier = unified().use(remarkStringify).use(remarkGfm).use(remarkMath);
const excerptRenderer = createMarkdownProcessor({
  remarkPlugins: [remarkGfm, remarkMath],
  rehypePlugins: [rehypeKatex, prefixBaseUrls(siteBase)],
  shikiConfig: {
    theme: "github-dark"
  }
});

function prefixBaseUrls(basePath: string) {
  return () => {
    return (tree: MarkdownNode) => {
      visit(tree, "element", (node: MarkdownNode) => {
        const properties = typeof node.properties === "object" ? node.properties : null;
        if (!properties) {
          return;
        }

        const key = node.tagName === "img" ? "src" : node.tagName === "a" ? "href" : null;
        if (!key) {
          return;
        }

        const value = properties[key];
        if (typeof value !== "string" || !value.startsWith("/") || value.startsWith("//")) {
          return;
        }

        properties[key] = `${basePath}${value.replace(/^\//, "")}`;
      });
    };
  };
}

function plainTextFromNode(node: MarkdownNode): string {
  if (node.type === "text" || node.type === "inlineCode" || node.type === "code") {
    return String(node.value ?? "");
  }

  if (node.type === "math" || node.type === "inlineMath") {
    return String(node.value ?? "");
  }

  if (node.type === "image") {
    return String(node.alt ?? "");
  }

  return (node.children ?? []).map((child) => plainTextFromNode(child)).join(" ");
}

function sanitizeNode(node: MarkdownNode): MarkdownNode | null {
  if (["yaml", "html", "definition", "footnoteDefinition", "image", "code", "table"].includes(node.type)) {
    return null;
  }

  if (Array.isArray(node.children)) {
    const children = node.children
      .map((child) => sanitizeNode(child))
      .filter((child): child is MarkdownNode => child !== null);

    if (!children.length && plainTextFromNode(node).trim().length === 0) {
      return null;
    }

    return {
      ...node,
      children
    };
  }

  if (node.type === "break" || node.type === "thematicBreak") {
    return node;
  }

  return plainTextFromNode(node).trim().length ? { ...node } : null;
}

function extractExcerptMarkdown(markdown: string, maxBlocks = 3, maxCharacters = 360) {
  const tree = excerptParser.parse(markdown) as MarkdownRoot;
  const visibleNodes = (tree.children ?? [])
    .map((rawNode) => sanitizeNode(rawNode))
    .filter((node): node is MarkdownNode => {
      if (!node) {
        return false;
      }

      const text = plainTextFromNode(node).replace(/\s+/g, " ").trim();
      return Boolean(text || node.type === "math");
    });

  const children: MarkdownNode[] = [];
  let totalCharacters = 0;
  let truncated = false;

  for (const [index, node] of visibleNodes.entries()) {
    const text = plainTextFromNode(node).replace(/\s+/g, " ").trim();
    children.push(node);
    totalCharacters += text.length;

    if (children.length >= maxBlocks || totalCharacters >= maxCharacters) {
      truncated = index < visibleNodes.length - 1 || text.length > maxCharacters;
      break;
    }
  }

  if (!children.length) {
    return {
      markdown: "",
      truncated: false
    };
  }

  return {
    markdown: String(excerptStringifier.stringify({
      type: "root",
      children
    } as MarkdownRoot)).trim(),
    truncated
  };
}

export async function renderExcerptHtml(markdown: string): Promise<RenderedExcerpt> {
  const excerpt = extractExcerptMarkdown(markdown);
  if (!excerpt.markdown) {
    return {
      html: ""
    };
  }

  const renderer = await excerptRenderer;
  const { code } = await renderer.render(excerpt.markdown);

  return {
    html: code
  };
}
