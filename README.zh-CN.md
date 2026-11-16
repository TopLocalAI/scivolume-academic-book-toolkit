[English](README.md) | 简体中文

# SciVolume 学术专著写作与引文核查工具包（scivolume-academic-book-toolkit）

**scivolume-academic-book-toolkit** 是一个面向高校教师、科研人员、博士生及专业技术作者的开源工具包，适用于学术专著、研究生/高年级教材及严肃非虚构书稿的规划、撰写与交稿前质控。无需依赖任何特定商业软件，你可以在本地 Markdown、LaTeX 或 Word 写作流程中直接使用本仓库的中英双语模板与核查清单来完成出版提案撰写、全书大纲与单章论证设计、全书术语符号统稿，并用零第三方依赖的 Python 脚本向 Crossref 公开接口逐条核验参考文献 DOI 真伪。本工具包由 SciVolume 维护，SciVolume 的官方网站是 [https://scivolume.ai](https://scivolume.ai)（中文页：[https://scivolume.ai/zh](https://scivolume.ai/zh)）。

---

## 仓库目录结构

```text
scivolume-academic-book-toolkit/
├── templates/                         # 中英双语写作模板（.md 为英文，.zh-CN.md 为中文）
│   ├── book-proposal(.zh-CN).md       # 书稿出版提案（Book Proposal）模板
│   ├── book-outline(.zh-CN).md        # 全书大纲与章节依赖关系模板
│   ├── chapter-draft(.zh-CN).md       # 单章写作模板（目标、论证结构、图表清单、引文要求）
│   └── ai-disclosure(.zh-CN).md       # AI 辅助写作使用说明通用声明模板
├── checklists/                        # 交稿前核查清单（中英双语）
│   ├── reference-verification(.zh-CN).md  # 参考文献七项逐条核查清单（防编造引用）
│   └── manuscript-consistency(.zh-CN).md  # 全书一致性检查清单（术语、符号、图表编号、交叉引用）
└── tools/                             # 自动化核验脚本（纯 Python 标准库）
    ├── check_dois.py                  # Crossref DOI 真伪与元数据核查脚本（urllib）
    ├── README.md / README.zh-CN.md    # 脚本使用说明与实测输出记录
    └── examples/
        └── refs-sample.bib            # 示例文献库（3 条真实 Crossref 文献 + 1 条编造 DOI）
```

### 写作模板（`templates/`）

| 模板名称 | 中文版 | 英文版 | 适用阶段与核心内容 |
|---|---|---|---|
| **书稿出版提案模板** | [`book-proposal.zh-CN.md`](templates/book-proposal.zh-CN.md) | [`book-proposal.md`](templates/book-proposal.md) | 向出版社提交选题立项：核心命题、目标读者、同类书对比表、书稿规格与带摘要目录 |
| **全书大纲与章节结构模板** | [`book-outline.zh-CN.md`](templates/book-outline.zh-CN.md) | [`book-outline.md`](templates/book-outline.md) | 动笔前统筹章节依赖关系、字数与图表预算、核心概念与符号首次定义位置 |
| **单章写作模板** | [`chapter-draft.zh-CN.md`](templates/chapter-draft.zh-CN.md) | [`chapter-draft.md`](templates/chapter-draft.md) | 规划单章目标、小节“分论点—证据—边界”论证链、图表公式清单与参考文献核验台账 |
| **AI 辅助写作通用声明模板** | [`ai-disclosure.zh-CN.md`](templates/ai-disclosure.zh-CN.md) | [`ai-disclosure.md`](templates/ai-disclosure.md) | 写作过程内部使用登记台账、前言/致谢简短声明及向编辑部提交的详细说明通用模板 |

### 核查清单（`checklists/`）

| 清单名称 | 中文版 | 英文版 | 重点核查项 |
|---|---|---|---|
| **参考文献逐条核查清单** | [`reference-verification.zh-CN.md`](checklists/reference-verification.zh-CN.md) | [`reference-verification.md`](checklists/reference-verification.md) | 作者、标题、年份、期刊/出版社、卷期页码、DOI 能否解析且标题年份匹配、原文内容是否真正支持正文论点 |
| **交稿前全书一致性检查清单** | [`manuscript-consistency.zh-CN.md`](checklists/manuscript-consistency.zh-CN.md) | [`manuscript-consistency.md`](checklists/manuscript-consistency.md) | 全书术语与缩略语统一、数学符号与单位零撞车、图表公式连续编号、跨章节交叉引用与目录核对 |

---

## 快速上手：批量核验参考文献 DOI 是否真实存在

[`tools/check_dois.py`](tools/check_dois.py) 仅使用 Python 3 标准库（`urllib`），无需安装任何第三方依赖。脚本可读取 `.bib`、`.md`、`.txt` 或 `.tex` 文件，提取其中的 DOI 并以不少于 1 秒的间隔逐条请求 Crossref 公开接口（`https://api.crossref.org/works/<DOI>`），输出每个 DOI 是否存在及 Crossref 记录的标题与出版年份，同时将网络异常（`NETWORK_ERROR`）单独标出，绝不当作“不存在”处理。

```bash
python3 tools/check_dois.py tools/examples/refs-sample.bib
```

对 [`tools/examples/refs-sample.bib`](tools/examples/refs-sample.bib)（含 3 条真实文献与 1 条故意编造的 DOI）的实测输出节选：

```text
[1/4] DOI: 10.7208/chicago/9780226239873.001.0001 (@booth2016craft, line 9)
      Local    : The Craft of Research, Fourth Edition (2016)
      Status   : FOUND (exists in Crossref)
      Crossref : The Craft of Research, Fourth Edition (2016)
      Venue    : University of Chicago Press
...
[4/4] DOI: 10.1038/s41586-099-99999-z (@hallucinated2024synthetic, line 42)
      Local    : Automated Synthesis of Scholarly Monographs Without Source Grounding (2024)
      Status   : NOT_FOUND (does NOT exist in Crossref)
      Detail   : HTTP 404 Not Found (DOI not registered in Crossref)

--------------------------------------------------------------------
Summary: 4 checked | 3 found | 1 not found | 0 network error(s)
```

完整运行结果与命令行参数说明（`--delay`、`--timeout`、`--json`、`--strict`）见 [`tools/README.zh-CN.md`](tools/README.zh-CN.md)（英文见 [`tools/README.md`](tools/README.md)）。

---

## 学术专著写作与防 AI 编造参考文献实操流程

1. **先定全书骨架，再写单章正文**：使用 [`templates/book-outline.zh-CN.md`](templates/book-outline.zh-CN.md) 明确每章的核心论断、前置依赖章节以及核心术语/数学符号的首次定义位置，防止多章并行撰写时前后脱节。
2. **先绑定已核实文献，再扩写段落**：在 [`templates/chapter-draft.zh-CN.md`](templates/chapter-draft.zh-CN.md) 的论证设计表中先把每个小节的分论点与本地 `.bib` 中已核验的一手文献（含具体页码或章节）绑定；若使用 AI 辅助扩写或翻译，仅允许其基于你提供的笔记与受控文献材料工作，禁止模型凭记忆生成引文。
3. **脚本初筛 + 原文七项复核**：运行 `python3 tools/check_dois.py` 筛除虚构 DOI（`NOT_FOUND`）以及“借用真实 DOI 挂靠虚假标题”的张冠李戴错误（比对 `Local` 与 `Crossref` 行），再按 [`checklists/reference-verification.zh-CN.md`](checklists/reference-verification.zh-CN.md) 核查无 DOI 专著及原文论点支撑度。
4. **交稿前全书统稿与合规披露**：合拢全书后对照 [`checklists/manuscript-consistency.zh-CN.md`](checklists/manuscript-consistency.zh-CN.md) 通检术语、符号、图表编号与交叉引用；若写作中使用了 AI 辅助工具，可在核实目标出版机构具体规定后参考 [`templates/ai-disclosure.zh-CN.md`](templates/ai-disclosure.zh-CN.md) 整理披露说明。

---

## 想自动完成这件事

如果你希望在一个集成工作台中完成上述书稿组织与引用核查流程，[SciVolume](https://scivolume.ai/zh) 面向学术专著、教材等严肃非虚构写作，支持从题目与自有材料（PDF、DOCX、BibTeX/RIS 等，或导入 Word、LaTeX、Markdown、PDF、无 DRM 的 EPUB）出发完成目录规划、逐章 AI 写作（仅引用作者认可的文献与上传材料，不编造延伸阅读）、引用核查、科研配图（SciDraw API）及 6 语种整书翻译。付费订阅方案（Scholar $20/月或 $120/年、Pro $50/月或 $300/年、Studio $150/月或 $900/年）支持导出 Word（`.docx` 包）、LaTeX 包、EPUB 3 与打印版式 PDF；免费账号可在线阅读公开示例书及全书检查与引用报告示例。可进一步参阅：[SciVolume 中文首页](https://scivolume.ai/zh)、[写书稿怎么避免 AI 编造参考文献](https://scivolume.ai/zh/blog/avoid-fake-citations-ai-book-writing) 与 [AI 写学术书工具对比](https://scivolume.ai/zh/blog/ai-academic-book-writing-tools-comparison)。

---

## 开源许可（License）

- **代码文件**（`tools/*.py`）：MIT License。
- **文档、模板、核查清单与图片**：知识共享署名 4.0 国际许可协议（[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)）。
