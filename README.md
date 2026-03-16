# SavvyM's Blog

这个仓库现在是一个基于 `Astro + Markdown` 的源码版博客，使用当前站点样式，并已迁移旧 Hugo 博客内容，可直接部署到 GitHub Pages。

## 内容结构

```bash
src/content/blog/*.md
```

博客文章通过 Markdown 渲染。新增或修改文章时，直接编辑 `src/content/blog/` 下的文件即可。

## 本地开发

```bash
npm install
npm run dev
```

然后打开 <http://localhost:4321>。

## 本地构建预览

```bash
npm run build
npm run preview
```

## 迁移旧博客内容

如果需要从旧 Hugo 仓库重新导入文章：

```bash
npm run migrate:hugo
```

该脚本会重新生成 `src/content/blog/` 下的文章、同步 `public/nb_images/`，并更新 `public/llms.txt`。

## 部署到 GitHub Pages

1. 把代码推到 GitHub 仓库的 `main` 分支。
2. 在 GitHub 仓库设置里打开 `Settings > Pages`。
3. `Build and deployment` 选择 `GitHub Actions`。
4. 推送后等待 `.github/workflows/deploy.yml` 执行完成。

## 说明

- 站点使用 Astro 静态构建，产物输出到 `dist/`。
- GitHub Pages 工作流会自动执行 `npm ci` 和 `npm run build`。
- 已迁移旧博客文章、标签页、Sitemap 和首页搜索。
- 当前仓库对 `savvym.github.io` 这类用户主页仓库会自动使用根路径部署。
