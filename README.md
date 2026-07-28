> **中文 fork 提示：** 本仓库是 [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) 的非官方中文 fork，当前同步上游 commit 为 `7868cb9251fad80a73d26e488a5ad5f6c4a9f335`。

# Marketing Skills 中文版

这是一套面向 AI Agent 的营销 Skill 集合，覆盖转化优化、文案、SEO、付费广告、分析、增长、留存、销售赋能和市场策略。本 fork 为全部 49 个运行时 Skill 增加中文触发说明与中文执行导读，同时保留上游英文正文和 `references/` 作为精确技术契约。

## 安装中文版

使用 skills CLI 安装全部 Skill：

```bash
npx skills add oldwinter/marketingskills
```

只安装指定 Skill：

```bash
npx skills add oldwinter/marketingskills --skill cro copywriting
```

在 Claude Code 中通过 plugin marketplace 安装：

```text
/plugin marketplace add oldwinter/marketingskills
/plugin install marketing-skills
```

也可以直接 clone 中文 fork：

```bash
git clone https://github.com/oldwinter/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```

## 使用方式

安装后直接用中文描述营销任务即可，例如：“审计这个落地页为什么转化率低，并给出可验证的 A/B 测试方案。”所有 Skill 会优先读取 `.agents/product-marketing.md` 中的产品、受众与定位上下文；新项目建议先使用 `product-marketing` Skill 建立该文件。

## 中文化边界

- `name`、Skill slug、plugin 名、命令、参数、路径、URL、事件名、指标、平台字段、schema 和代码保持原样。
- 中文导读负责触发、执行顺序与边界；详细框架、模板、法规说明和平台规格仍以同一 Skill 的英文正文及 `references/` 为准。
- 本 fork 不是 Corey Haines 的官方发行；上游作者与 MIT 许可信息保持不变。
- 同步策略、许可边界与验证要求见 [`docs/translation-profile.zh-CN.md`](docs/translation-profile.zh-CN.md)。

---

下面保留上游 README，方便核对原始说明、安装方式与维护信息。

# Marketing Skills for AI Agents

A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who want AI coding agents to help with conversion optimization, copywriting, SEO, analytics, and growth engineering. Works with Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent that supports the [Agent Skills spec](https://agentskills.io).

Built by [Corey Haines](https://corey.co?ref=marketingskills). Need hands-on help? Check out [Conversion Factory](https://conversionfactory.co?ref=marketingskills) — Corey's agency for conversion optimization, landing pages, and growth strategy. Want to learn more about marketing? Subscribe to [Swipe Files](https://swipefiles.com?ref=marketingskills). Want to get dangerously good at using AI for marketing? Check out [AI Marketing Training](https://conversionfactory.co/offers/ai-marketing-training?ref=marketingskills). Want an autonomous AI agent that uses these skills to be your CMO? Try [Magister](https://magistermarketing.com?ref=marketingskills).

New to the terminal and coding agents? Check out the companion guide [Coding for Marketers](https://codingformarketers.com?ref=marketingskills).

**Contributions welcome!** Found a way to improve a skill or have a new one to add? [Open a PR](#contributing).

Run into a problem or have a question? [Open an issue](https://github.com/coreyhaines31/marketingskills/issues) — we're happy to help.

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, your agent can recognize when you're working on a marketing task and apply the right frameworks and best practices.

## How Skills Work Together

Skills reference each other and build on shared context. The `product-marketing` skill is the foundation — every other skill checks it first to understand your product, audience, and positioning before doing anything.

```
                            ┌──────────────────────────────────────┐
                            │          product-marketing           │
                            │    (read by all other skills first)  │
                            └──────────────────┬───────────────────┘
                                               │
    ┌──────────────┬─────────────┬─────────────┼─────────────┬──────────────┬──────────────┐
    ▼              ▼             ▼             ▼             ▼              ▼              ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐
│  SEO &   │ │   CRO    │ │Content & │ │  Paid &    │ │ Growth & │ │  Sales &    │ │ Strategy  │
│ Content  │ │          │ │   Copy   │ │Measurement │ │Retention │ │    GTM      │ │           │
├──────────┤ ├──────────┤ ├──────────┤ ├────────────┤ ├──────────┤ ├─────────────┤ ├───────────┤
│seo-audit │ │cro       │ │copywritng│ │ads         │ │referrals │ │revops       │ │mktg-ideas │
│ai-seo    │ │signup    │ │copy-edit │ │ad-creative │ │free-tools│ │sales-enable │ │mktg-psych │
│site-arch │ │onboarding│ │cold-email│ │ab-testing  │ │churn-    │ │launch       │ │customer-  │
│programm  │ │popups    │ │emails    │ │analytics   │ │ prevent  │ │pricing      │ │ research  │
│schema    │ │paywalls  │ │social    │ │            │ │community │ │competitors  │ │           │
│content   │ │          │ │video     │ │            │ │lead-magnt│ │comp-profile │ │           │
│aso       │ │          │ │image     │ │            │ │co-mktg   │ │directory    │ │           │
│          │ │          │ │sms       │ │            │ │          │ │prospecting  │ │           │
└────┬─────┘ └────┬─────┘ └────┬─────┘ └─────┬──────┘ └────┬─────┘ └──────┬──────┘ └─────┬─────┘
     │            │            │              │             │              │              │
     └────────────┴─────┬──────┴──────────────┴─────────────┴──────────────┴──────────────┘
                        │
         Skills cross-reference each other:
           copywriting ↔ cro ↔ ab-testing
           revops ↔ sales-enablement ↔ cold-email
           seo-audit ↔ schema ↔ ai-seo
           customer-research → copywriting, cro, competitors
```

See each skill's **Related Skills** section for the full dependency map.

## Available Skills

<!-- SKILLS:START -->
| Skill | Description |
|-------|-------------|
| [ab-testing](skills/ab-testing/) | 当用户要规划、设计或实施 A/B 测试、对照实验或增长实验体系时使用；英文触发词包括 A/B test、split test、hypothesis、statistical significance。埋点实现参见... |
| [ad-creative](skills/ad-creative/) | 当用户要生成、迭代或规模化广告标题、正文、视觉概念或完整变体时使用；英文触发词包括 ad creative、RSA headlines、Facebook ad copy、creative testing。投放策略参见... |
| [ads](skills/ads/) | 当用户要规划或优化 Google Ads、Meta、LinkedIn、X 等付费广告时使用；英文触发词包括 PPC、ROAS、CPA、retargeting、Performance Max、ABM。批量创意参见... |
| [ai-seo](skills/ai-seo/) | 当用户要提升内容在 AI 搜索和大模型答案中的可见度、引用率或品牌提及时使用；英文触发词包括 AI SEO、AEO、GEO、LLMO、AI Overviews、llms.txt。传统 SEO 参见 seo-audit，结构化数据参见... |
| [analytics](skills/analytics/) | 当用户要设置、改进或审计分析埋点与营销衡量时使用；英文触发词包括 GA4、GTM、event tracking、UTM、Mixpanel、Segment。归因模型参见 attribution，实验衡量参见 ab-testing。 Use... |
| [aso](skills/aso/) | 当用户提供 App Store 或 Google Play 页面并要审计或提升可见度、排名与下载转化时使用；英文触发词包括 ASO audit、app store optimization、listing... |
| [attribution](skills/attribution/) | 当用户要判断哪些营销活动真正带来转化与收入、选择归因模型或解释多工具数据冲突时使用；英文触发词包括 attribution、multi-touch、MMM、incrementality、dark social。埋点参见... |
| [churn-prevention](skills/churn-prevention/) | 当用户要降低主动或非主动流失、设计取消流程、挽留方案、催收或召回策略时使用；英文触发词包括 churn、cancel flow、save offer、dunning、win-back。召回邮件参见 emails，升级墙参见... |
| [co-marketing](skills/co-marketing/) | 当用户要寻找联合营销伙伴、规划共同活动或构思合作机会时使用；英文触发词包括 co-marketing、partner marketing、joint campaign、cross-promotion。客户推荐参见... |
| [cold-email](skills/cold-email/) | 当用户要撰写 B2B 冷启动邮件、销售开发邮件或多触点跟进序列时使用；英文触发词包括 cold email、outbound、prospecting email、SDR。生命周期邮件参见 emails，其他销售材料参见... |
| [community-marketing](skills/community-marketing/) | 当用户要创建或发展 Discord、Slack、论坛、subreddit、品牌倡导者或社区驱动增长体系时使用；英文触发词包括 community strategy、community-led growth、ambassador... |
| [competitor-profiling](skills/competitor-profiling/) | 当用户提供竞争对手 URL 并要研究、画像或形成竞争情报档案时使用；英文触发词包括 competitor profile、competitive intelligence、competitor dossier。比较页参见... |
| [competitors](skills/competitors/) | 当用户要创建竞品比较页、替代方案页、vs 页面或竞争定位内容时使用；英文触发词包括 alternative page、vs page、comparison page、battle card。深度画像参见... |
| [content-strategy](skills/content-strategy/) | 当用户要决定应该创作什么内容、建立主题集群、编辑日历或内容路线图时使用；英文触发词包括 content strategy、topic clusters、content pillars。单篇文案参见 copywriting，SEO 审计参见... |
| [copy-editing](skills/copy-editing/) | 当用户已有营销文案并要审阅、润色、收紧、刷新或做内容审计时使用；英文触发词包括 edit this copy、proofread、copy sweep、refresh content。新写文案参见 copywriting。 Use... |
| [copywriting](skills/copywriting/) | 当用户要撰写或改写首页、落地页、定价页、功能页、关于页或产品页文案时使用；英文触发词包括 headline、CTA、value proposition、hero copy。邮件参见 emails，弹窗参见 popups，offer... |
| [cro](skills/cro/) | 当用户要诊断或提升营销页面、落地页、定价页或表单转化时使用，即使只提供 URL 也应触发；英文触发词包括 CRO、conversion rate、form abandonment。注册参见 signup，引导参见... |
| [customer-research](skills/customer-research/) | 当用户要规划客户研究、分析访谈/评价/工单等现有资料，或从线上聚集地提炼客户语言时使用；英文触发词包括 customer research、VOC、interview analysis、pain points。相关范围参见下方正文。... |
| [directory-submissions](skills/directory-submissions/) | 当用户要把初创公司、SaaS 或 AI 产品提交到目录、榜单与发布平台时使用；英文触发词包括 directory submission、Product Hunt、startup directories、AI... |
| [emails](skills/emails/) | 当用户要设计或优化欢迎、培育、激活、促销、流失预防、召回等邮件序列时使用；英文触发词包括 email sequence、drip campaign、lifecycle email、welcome flow。冷外联参见... |
| [free-tools](skills/free-tools/) | 当用户要用计算器、生成器、检查器、模板或互动工具实现 engineering as marketing 时使用；英文触发词包括 free tool、calculator、generator、lead generation... |
| [image](skills/image/) | 当用户要生成、编辑或制作营销图像、产品图、社交图、缩略图或视觉资产时使用；英文触发词包括 AI image、image generation、product screenshot、social graphic。视频参见... |
| [influencer-marketing](skills/influencer-marketing/) | 当用户要寻找、筛选、联系或管理影响者、创作者和品牌大使合作时使用；英文触发词包括 influencer marketing、creator partnership、ambassador、UGC。联合营销参见... |
| [launch](skills/launch/) | 当用户要规划产品、功能、品牌或 Product Hunt 发布时使用；英文触发词包括 launch strategy、go-to-market launch、Product Hunt、announcement。发布合作参见... |
| [lead-magnets](skills/lead-magnets/) | 当用户要构思、创建或优化清单、模板、报告、课程、测验等 lead magnet 时使用；英文触发词包括 lead magnet、gated content、downloadable、content upgrade。表单和页面转化参见... |
| [marketing-council](skills/marketing-council/) | 当用户要用多位真实营销专家的独立视角评审策略、挑战方案或形成共识时使用；英文触发词包括 marketing council、expert panel、what would experts say。具体战术仍应参见对应营销 Skill。... |
| [marketing-ideas](skills/marketing-ideas/) | 当用户要为 SaaS 获取营销点子、渠道灵感或按目标筛选策略时使用；英文触发词包括 marketing ideas、growth ideas、ways to market、what should we try。完整计划参见... |
| [marketing-loops](skills/marketing-loops/) | 当用户要设计可重复、可调度、带反馈的营销系统，而非一次性 campaign 时使用；英文触发词包括 marketing loop、growth loop、content loop、feedback loop。分析参见... |
| [marketing-plan](skills/marketing-plan/) | 当用户需要面向客户、公司或自有产品的完整 90 天与 12 个月营销计划时使用；英文触发词包括 marketing plan、GTM plan、AARRR plan、fractional CMO。定位上下文参见... |
| [marketing-psychology](skills/marketing-psychology/) | 当用户要把心理学、行为经济学或心智模型应用于营销信息、定价和用户行为时使用；英文触发词包括 marketing psychology、cognitive bias、persuasion、behavioral... |
| [offers](skills/offers/) | 当用户要设计、评估或强化服务、课程、咨询、高客单 B2B 等完整 offer 时使用；英文触发词包括 offer design、value equation、bonuses、guarantee、risk reversal。定价参见... |
| [onboarding](skills/onboarding/) | 当用户要优化注册后的激活、首次体验、aha moment、time to value 或 onboarding flow 时使用；英文触发词包括 activation rate、first session、users sign up... |
| [paywalls](skills/paywalls/) | 当用户要创建或优化应用内付费墙、升级屏、upsell、feature gate 或试用结束页时使用；英文触发词包括 paywall、upgrade modal、freemium conversion。公开定价页参见 cro，定价策略参见... |
| [popups](skills/popups/) | 当用户要创建或优化 popup、modal、overlay、slide-in、sticky bar 或 banner 时使用；英文触发词包括 exit intent、lead capture popup、announcement... |
| [pricing](skills/pricing/) | 当用户要决定价格、套餐、价值指标、免费试用、freemium 或审计定价页时使用；英文触发词包括 pricing tiers、Van Westendorp、willingness to pay、monetization。应用内升级参见... |
| [product-marketing](skills/product-marketing/) | 当用户要创建或更新产品定位、ICP、受众、差异化和基础营销上下文时使用；英文触发词包括 positioning、product context、ideal customer profile。新项目在调用其他营销 Skill 前优先使用本... |
| [programmatic-seo](skills/programmatic-seo/) | 当用户要用模板与数据规模化生成目录页、地点页、集成页、比较页等搜索页面时使用；英文触发词包括 programmatic SEO、pSEO、template pages、pages at scale。SEO 审计参见... |
| [prospecting](skills/prospecting/) | 当用户要寻找、筛选和建立 B2B SaaS、一般 B2B 或本地商家潜客清单时使用；英文触发词包括 prospecting、lead list、target accounts、design partners。外联文案参见... |
| [public-relations](skills/public-relations/) | 当用户要获取媒体报道、寻找记者、写 pitch、新闻劫持或响应记者请求时使用；这里的 PR 指 public relations，不是 pull request。英文触发词包括 press release、earned... |
| [referrals](skills/referrals/) | 当用户要创建、优化或分析客户推荐、affiliate、ambassador 或口碑增长计划时使用；英文触发词包括 refer a friend、viral loop、affiliate payout。发布期传播参见... |
| [revops](skills/revops/) | 当用户要设计收入运营、lead lifecycle、MQL/SQL、lead scoring、routing、CRM 自动化或营销销售交接时使用；英文触发词包括 RevOps、pipeline stages、data... |
| [sales-enablement](skills/sales-enablement/) | 当用户要创建销售 deck、one-pager、异议处理、ROI 分析、demo 脚本、talk track 或 playbook 时使用；英文触发词包括 sales collateral、pitch deck、proposal... |
| [schema](skills/schema/) | 当用户要添加、修复或优化网站 schema markup 与 JSON-LD 时使用；英文触发词包括 structured data、schema.org、rich snippets、FAQ schema、Product... |
| [seo-audit](skills/seo-audit/) | 当用户要审计、诊断或修复网站技术 SEO、索引、页面排名或流量下滑时使用，即使请求很模糊也应触发；英文触发词包括 SEO audit、crawl errors、Core Web Vitals。规模化建页参见... |
| [signup](skills/signup/) | 当用户要优化注册、开户或试用激活流程并减少 dropoff 时使用；英文触发词包括 signup conversion、registration friction、trial signup、account creation。注册后体验参见... |
| [site-architecture](skills/site-architecture/) | 当用户要规划或重构页面层级、导航、URL、面包屑或内部链接时使用；英文触发词包括 sitemap、information architecture、site hierarchy。XML sitemap 属于技术 SEO，参见... |
| [sms](skills/sms/) | 当用户要规划、搭建或优化 SMS/MMS 欢迎、弃购、售后、召回、促销或事务消息时使用；英文触发词包括 SMS marketing、Klaviyo SMS、Twilio、A2P 10DLC、TCPA。邮件参见... |
| [social](skills/social/) | 当用户要为 LinkedIn、X、Instagram、TikTok、Facebook 等创建、排期、复用或优化内容，或做 social listening 时使用；英文触发词包括 content... |
| [video](skills/video/) | 当用户要用 AI 工具或程序化框架创建、生成、仿制剪辑结构或生产视频时使用；英文触发词包括 Remotion、Hyperframes、HeyGen、Veo、Sora、Runway。内容策略参见 social，视频广告参见... |
<!-- SKILLS:END -->

## Installation

### Option 1: CLI Install (Recommended)

Use [npx skills](https://github.com/vercel-labs/skills) to install skills directly:

```bash
# Install all skills
npx skills add coreyhaines31/marketingskills

# Install specific skills
npx skills add coreyhaines31/marketingskills --skill cro copywriting

# List available skills
npx skills add coreyhaines31/marketingskills --list
```

The CLI detects which agents you have installed and asks where to install. For Claude Code it installs into `.claude/skills/`; universal agents share `.agents/skills/`.

> [!TIP]
> If you run the command from **inside** an agent session (e.g., asking Claude Code to install the skills for you), the CLI runs non-interactively and may only install to the universal `.agents/skills/` directory, which Claude Code does not read. Pass the agent explicitly:
>
> ```bash
> npx skills add coreyhaines31/marketingskills -a claude-code
> ```

### Option 2: Claude Code Plugin

Install via Claude Code's built-in plugin system:

```bash
# Add the marketplace
/plugin marketplace add coreyhaines31/marketingskills

# Install all marketing skills
/plugin install marketing-skills
```

### Option 3: Clone and Copy

Clone the entire repo and copy the skills folder:

```bash
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```

### Option 4: Git Submodule

Add as a submodule for easy updates:

```bash
git submodule add https://github.com/coreyhaines31/marketingskills.git .agents/marketingskills
```

Then reference skills from `.agents/marketingskills/skills/`.

### Option 5: Fork and Customize

1. Fork this repository
2. Customize skills for your specific needs
3. Clone your fork into your projects

### Option 6: SkillKit (Multi-Agent)

Use [SkillKit](https://github.com/rohitg00/skillkit) to install skills across multiple AI agents (Claude Code, Cursor, Copilot, etc.):

```bash
# Install all skills
npx skillkit install coreyhaines31/marketingskills

# Install specific skills
npx skillkit install coreyhaines31/marketingskills --skill cro copywriting

# List available skills
npx skillkit install coreyhaines31/marketingskills --list
```

## Upgrading from v1.x to v2.0

v2.0 renames 17 skills and consolidates `page-cro` + `form-cro` into a single `cro` skill. If you installed the v1.x skills, you'll have **stale old-name folders** in your install directory after upgrading — the new skills install alongside the old ones, so you'll see both `skills/page-cro/` and `skills/cro/`, etc. Clean them up:

```bash
# From the directory where you installed the skills (e.g., .agents/skills/ or .claude/skills/)
rm -rf page-cro form-cro \
       ab-test-setup analytics-tracking aso-audit competitor-alternatives \
       email-sequence free-tool-strategy launch-strategy onboarding-cro \
       paid-ads paywall-upgrade-cro popup-cro pricing-strategy \
       product-marketing-context referral-program schema-markup \
       signup-flow-cro social-content
```

Then reinstall the v2.0 skills via your usual method (e.g., `npx skills add coreyhaines31/marketingskills`).

### Migrate the product marketing context file

In v2.0 the context file moved from `.claude/` to `.agents/` and was renamed from `product-marketing-context.md` to `product-marketing.md`. Move your existing context file:

```bash
mkdir -p .agents
# v2.0 file (or pre-v2.0 file with new name)
mv .claude/product-marketing.md .agents/product-marketing.md 2>/dev/null
# pre-v2.0 file with legacy name
mv .claude/product-marketing-context.md .agents/product-marketing.md 2>/dev/null
```

Skills will still check `.claude/` and the legacy `product-marketing-context.md` filename as fallbacks, so nothing breaks if you don't migrate.

### Full rename map

| Old | New |
|-----|-----|
| `ab-test-setup` | `ab-testing` |
| `analytics-tracking` | `analytics` |
| `aso-audit` | `aso` |
| `competitor-alternatives` | `competitors` |
| `email-sequence` | `emails` |
| `form-cro` | merged into `cro` |
| `free-tool-strategy` | `free-tools` |
| `launch-strategy` | `launch` |
| `onboarding-cro` | `onboarding` |
| `page-cro` | `cro` |
| `paid-ads` | `ads` |
| `paywall-upgrade-cro` | `paywalls` |
| `popup-cro` | `popups` |
| `pricing-strategy` | `pricing` |
| `product-marketing-context` | `product-marketing` |
| `referral-program` | `referrals` |
| `schema-markup` | `schema` |
| `signup-flow-cro` | `signup` |
| `social-content` | `social` |

## Usage

Once installed, just ask your agent to help with marketing tasks:

```
"Help me optimize this landing page for conversions"
→ Uses cro skill

"Write homepage copy for my SaaS"
→ Uses copywriting skill

"Set up GA4 tracking for signups"
→ Uses analytics skill

"Create a 5-email welcome sequence"
→ Uses emails skill
```

You can also invoke skills directly:

```
/cro
/emails
/seo-audit
```

## Skill Categories

### Conversion Optimization
- `cro` - Pages and forms
- `signup` - Registration flows
- `onboarding` - Post-signup activation
- `popups` - Modals and overlays
- `paywalls` - In-app upgrade moments

### Content & Copy
- `copywriting` - Marketing page copy
- `copy-editing` - Edit and polish existing copy
- `cold-email` - B2B cold outreach emails and sequences
- `emails` - Automated email flows
- `social` - Social media content
- `image` - AI image generation, design tools, and optimization

### SEO & Discovery
- `seo-audit` - Technical and on-page SEO
- `ai-seo` - AI search optimization (AEO, GEO, LLMO)
- `programmatic-seo` - Scaled page generation
- `site-architecture` - Page hierarchy, navigation, URL structure
- `competitors` - Comparison and alternative pages
- `schema` - Structured data

### Paid & Distribution
- `ads` - Google, Meta, LinkedIn ad campaigns
- `ad-creative` - Bulk ad creative generation and iteration
- `social` - Social media scheduling and strategy

### Measurement & Testing
- `analytics` - Event tracking setup
- `ab-testing` - Experiment design

### Retention
- `churn-prevention` - Cancel flows, save offers, dunning, payment recovery

### Growth Engineering
- `co-marketing` - Partner identification and joint campaigns
- `free-tools` - Marketing tools and calculators
- `referrals` - Referral and affiliate programs

### Strategy & Monetization
- `marketing-ideas` - 140 SaaS marketing ideas
- `marketing-psychology` - Mental models and psychology
- `launch` - Product launches and announcements
- `pricing` - Pricing, packaging, and monetization

### Sales & RevOps
- `revops` - Lead lifecycle, scoring, routing, pipeline management
- `sales-enablement` - Sales decks, one-pagers, objection docs, demo scripts

## Contributing

Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding or improving skills.

## License

[MIT](LICENSE) - Use these however you want.

<br />
<br />
<a href="https://vercel.com/open-source-program">
  <img alt="Vercel OSS Program" src="https://vercel.com/oss/program-badge-2026.svg" />
</a>
