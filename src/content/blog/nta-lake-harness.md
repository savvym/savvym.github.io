---
title: '使用 Harness 思想进行系统开发'
description: 'Agent Harness'
pubDate: "2026-05-18"
tags:
  - "Agent"
  - "Harness"
---

> 本文件是对项目 `.harness/` 目录与十阶段开发流程的全景梳理。
> 权威定义仍在 `.harness/rules/development-process.md`、`.harness/agents/application-owner.md`。

---

## 一、`.harness/` 目录的整体结构

```
.harness/
├── agents/             ← 角色定义（你在会话里扮演谁）
│   ├── application-owner.md   ← 流程总编排者（你/主会话）
│   └── reviewer-agent.md      ← 独立评审者（必须 spawn 子 agent）
├── rules/              ← 全局硬约束（每次都要遵守）
│   ├── development-process.md ← 十阶段流程权威定义
│   ├── engineering-structure.md
│   └── coding-style.md
├── skills/             ← 可复用 SOP（按阶段加载，不全量）
│   ├── request-analysis/  coding-skill/  expert-reviewer/
│   ├── code-review/  unit-test-write/  unit-test-ci/
│   ├── deploy-verify/  project-analysis/  ci-generate/
├── changes/            ← 所有变更的工作目录
│   ├── _template/         ← 新 change 拷贝模板
│   └── <slug>-<yyyymmdd>/ ← 一个 change = 一个流程实例
├── mcp/                ← Phase 2+ 外部服务接入（占位）
├── design.md           ← 系统设计权威
├── harness.md          ← 方法论参考
└── README.md
```

**关键不变量**：`changes/<id>/summary.md` 是每个变更的 **Single Source of Truth**。

---

## 二、十阶段需求开发流程

```
1 需求分析 → 2 需求评审 → 3 编码实现 → 4 编码评审 → 5 单测编写
         → 6 单测评审 → 7 代码推送 → 8 CI 验证 → 9 部署验证 → 10 用户确认
```

每个阶段都强制四要素：**Entry Criteria · Skill Injection · Quality Gate · Rollback Route**。

| 阶段            | 加载 Skill                     | 产物（落地路径）                                              | 关键门禁                                                                                                                  |
| ------------- | ---------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **1 需求分析**    | `request-analysis`           | `request_analysis/spec.md`、`tasks.md`                 | 必含背景/范围/非范围/验收/风险；AC 可机械化；任务粒度 1–3h                                                                                   |
| **2 需求评审** ⚠️ | `expert-reviewer` (plan)     | `request_analysis/review/{spec,tasks}_review_v{N}.md` | **必须 spawn 独立 reviewer 子 agent**；reviewer 字段 `claude-agent:...` 或 `self-attest (理由)`；MUST FIX 全闭；verdict=APPROVED     |
| **3 编码实现**    | `coding-skill`               | 实际代码 + `coding/coding_report_v{N}.md`                 | lint/type check 通过；改动对应 tasks.md；无未授权依赖                                                                               |
| **4 编码评审** ⚠️ | `code-review`                | `coding/review/code_review_v{N}.md`                   | **独立 reviewer 子 agent**；MUST FIX 全闭；SHOULD FIX 若 deferred 必须写进 summary                                                |
| **5 单测编写**    | `unit-test-write`            | 测试代码 + `unit_test/test_report_v{N}.md`                | **改动驱动**：每个新增公共函数/路由至少一条直接测试；禁止无条件 mock 数据访问层                                                                         |
| **6 单测评审** ⚠️ | `expert-reviewer` (artifact) | `unit_test/review/test_review_v{N}.md`                | **独立 reviewer 子 agent**；每条 spec AC 能追溯到测试用例；无空跑测试                                                                     |
| **7 代码推送**    | —（直接 git）                    | commit/push；summary.md 记 SHA + 分支                     | commit message 合规；不直推 main                                                                                            |
| **8 CI 验证**   | `unit-test-ci`               | `ci_result/ci_result_v{N}.md`                         | **机械化**：`status=SUCCESS && total_tests>0 && passed==total`                                                            |
| **9 部署验证**    | `deploy-verify`              | `deployment/deploy_verify_v{N}.md`                    | verdict 非空且不为 deferred/FAIL；若 `PASS via self-attest` 必填 4 字段（理由/本机证据/跑过的命令/时间）；至少 1 条 AC 对应 spec 的 `kind: behavioral` |
| **10 用户确认**   | —                            | summary.md 末段补确认人/时间/链接                               | 用户**明确**确认；不接受沉默通过                                                                                                    |

⚠️ 标记的 stage 2 / 4 / 6 是**硬约束**：必须 spawn 独立 reviewer，禁止 self-review，否则被 `scripts/_self_check.sh` 的 `run_reviewer_lint` 硬 FAIL。

---

## 三、核心机制（流程之外的约束）

1. **Generator / Reviewer 分离**
   主会话扮演 Application Owner + Generator；评审阶段必须 `Agent(subagent_type="general-purpose", ...)` spawn 子 agent，独立上下文，避免偏袒自己产物。spawn 模板见 `application-owner.md §7.5`。

2. **版本号递增、不覆盖**
   `spec_v1.md` 不通过 → 写 `spec_v2.md` + `spec_review_v2.md`，保留历史轨迹。

3. **小变更不裁剪阶段**
   产物可以一两句话极简，但 10 个阶段都必须存在。

4. **流程缺陷反哺 harness 自身**
   发现规则/Skill 不够用，开 `harness-<改动名>-<yyyymmdd>` 变更去修 rules/skills，本身也走完整十阶段（已有 `harness-ac-behavioral-tier-20260518`、`harness-reviewer-agent-separation-20260518` 这种实例）。

5. **机械化证据 > 自然语言**
   "测试通过" 必须附 `ci_result_v*.md` 路径与 status/total/passed 字段；stage 9 self-attest 必须列文件路径和命令。

6. **典型回退路径（速查）**

   | 触发场景 | 回退到 |
   |---|---|
   | spec 不清晰 / 自相矛盾 | 阶段 1 需求分析 |
   | spec/tasks 评审不通过 | 阶段 1 需求分析 |
   | 代码评审不通过 | 阶段 3 编码 |
   | 单测为 0 或未覆盖关键路径 | 阶段 5 单测编写 |
   | 编译/类型错误 | 阶段 3 编码 |
   | 测试 mock 滥用被评审打回 | 阶段 5 单测编写 |
   | CI 失败（代码 bug） | 阶段 3 编码 |
   | CI 失败（CI 配置 bug） | 触发 `ci-generate` Skill |
   | 部署验证不通过 | 视失败位置回到阶段 3/5/8 |
   | 用户最终验收拒绝 | 视性质回到阶段 1 或开新 change |

---

## 四、典型一次变更的操作路径

```
1.  想清一句话目标 + 验收标准
2.  cp -r .harness/changes/_template .harness/changes/<slug>-<yyyymmdd>
3.  编辑 summary.md（stage=request_analysis, owner, started_at...）
4.  加载 request-analysis SKILL → 写 spec.md + tasks.md
5.  spawn reviewer 子 agent（stage 2）→ spec_review_v1.md / tasks_review_v1.md
6.  APPROVED → 加载 coding-skill → 改代码 + coding_report_v1.md
7.  spawn reviewer 子 agent（stage 4）→ code_review_v1.md
8.  APPROVED → unit-test-write → 测试 + test_report_v1.md
9.  spawn reviewer 子 agent（stage 6）→ test_review_v1.md
10. APPROVED → git commit/push → 记 SHA
11. CI 跑完 → ci_result_v1.md（机械化判定）
12. deploy-verify → deploy_verify_v1.md（含 behavioral AC 证据）
13. 用户明确确认 → summary.md 收尾，status=done
```

---

## 五、设计哲学

整套流程的设计哲学是 **Harness Engineering**：

- 把 "什么时候做什么、什么算做完、做不好怎么回退" 用**文件和门禁固化**下来；
- 不依赖会话内的临时共识；
- 每一次绕过都视为流程失败，需要把防复发机制补回 `.harness/rules` 或 `.harness/skills`，不能只在当前会话临时绕过；
- Generator / Reviewer 通过**独立 sub-agent** 物理隔离，机械化 lint 守门；
- 任何产物都有版本号 + lineage，与 dataplat 自身的版本控制价值观一致。

---

## 六、相关权威文件索引

| 你想做什么 | 去哪里 |
|---|---|
| 理解当前流程怎么跑 | `.harness/agents/application-owner.md` |
| 看十阶段流程定义 | `.harness/rules/development-process.md` |
| 看独立 reviewer 约束 | `.harness/agents/reviewer-agent.md` |
| 写代码前对齐风格 | `.harness/rules/coding-style.md` |
| 了解目录约束 | `.harness/rules/engineering-structure.md` |
| 用某个阶段的 SOP | `.harness/skills/README.md` + 各 SKILL.md |
| 看历史变更/启动新变更 | `.harness/changes/`（模板在 `_template/`） |
| 查领域术语 / 系统总体设计 | `wiki/` 与 `.harness/design.md` |
