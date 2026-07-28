# Marketing Skills 中文化档案

同步上游后先读本档案，再处理新增或变更内容。

## 项目定位

- 上游项目：`coreyhaines31/marketingskills`
- 中文 fork：`oldwinter/marketingskills`
- 当前同步上游 commit：`7868cb9251fad80a73d26e488a5ad5f6c4a9f335`
- 上游许可：MIT
- 主要安装面：skills CLI、Claude Code plugin marketplace、直接 clone
- 目标用户：使用中文与 AI Agent 完成营销工作的技术营销人员、创始人与增长团队
- 中文 runtime 入口：全部 49 个 `skills/*/SKILL.md`

## 中文化目标

本 fork 让 49 个营销 Skill 能被中文意图直接触发，并在每个运行时入口提供足以完成路由、准备、执行与边界判断的中文导读。上游英文正文、references、模板、命令和精确平台规格继续保留，避免翻译改变专业契约。

## 翻译策略

- Frontmatter `description` 使用中文说明，并保留关键英文术语和相关 Skill 边界。
- 每个 `SKILL.md` 在上游正文前增加紧凑中文执行导读；导读与正文冲突时，以同一文件的英文正文和 references 为准。
- `name`、Skill slug、plugin 名、命令、参数、路径、URL、平台名、指标、事件名、schema、代码和原始引用不翻译。
- 上游历史 README、VERSIONS 变更记录和作者归属保留原文；中文安装入口置于 README 顶部。
- 受法规影响的营销工作流只翻译操作边界，不把仓库中的说明表述为实时法律意见。

## 版本策略

- 任一 `SKILL.md` 发生可交付变更时，按上游规则提升该 Skill 的 `metadata.version`，并同步 `VERSIONS.md`。
- 中文触发与执行能力属于新能力，本次全部 49 个 Skill 提升 minor 版本；缺少 frontmatter 版本的 `marketing-plan` 依据 `VERSIONS.md` 从 `1.1.0` 提升为 `1.2.0`。
- `.claude-plugin/plugin.json` 与 `.claude-plugin/marketplace.json` 的仓库版本保持一致。
- 首次中文化发布版本为 `2.10.1`，同步基线为上游 `7868cb9251fad80a73d26e488a5ad5f6c4a9f335`。

## 安装与交付

使用 skills CLI：

```bash
npx skills add oldwinter/marketingskills
```

使用 Claude Code plugin marketplace：

```text
/plugin marketplace add oldwinter/marketingskills
/plugin install marketing-skills
```

## 同步后检查

- `git merge upstream/main` 后确认无未解决冲突，并更新本档案中的上游 commit。
- 重新检查所有上游变更的 `SKILL.md`、references、README、plugin 元数据与 `VERSIONS.md`。
- 49 个 `SKILL.md` 的 frontmatter 必须可解析，`name` 必须匹配目录，`description` 长度为 1-1024，文件不超过 500 行。
- 每个 Skill 的 `metadata.version` 必须与 `VERSIONS.md` 对应行完全一致。
- `.github/scripts/sync-skills.js` 运行后，README 技能表与 marketplace 技能数量必须保持同步。
- README 安装入口与 `plugin.json` 的 homepage/repository 必须指向 `oldwinter/marketingskills`，同时保留上游作者与 MIT 许可归属。
- 运行仓库现有的自定义、官方与 Claude plugin 校验；最后执行 JSON、diff、冲突标记和 fork/upstream 拓扑检查。
