[English](README.md) | 简体中文

# 参考文献 DOI 核查脚本（`check_dois.py`）

`check_dois.py` 是一个零第三方依赖的纯 Python 3 标准库脚本（仅使用 `urllib` 等内置模块），可读取 `.bib`、`.md`、`.txt` 或 `.tex` 文件，自动提取其中的 DOI，并逐条请求 Crossref 公开接口（`https://api.crossref.org/works/<DOI>`）核验 DOI 是否真实存在。

对于提取出的每个唯一 DOI，脚本会输出：
- **状态分类**：`FOUND`（Crossref 中存在）、`NOT_FOUND`（HTTP 404，Crossref 未注册该 DOI）或 `NETWORK_ERROR`（网络超时、限流或接口异常，单独标出，绝不当作“不存在”处理）。
- **人工对照信息**：同时展示 Crossref 记录的**标题、出版年份、期刊/出版社**以及本地 `.bib` 条目的标题和年份，既能筛出虚构 DOI，也能一眼发现“借用真实 DOI 挂靠虚假论文标题”的张冠李戴型引文幻觉。

## 运行环境

- Python 3.8 及以上（仅用 Python 标准库，无需安装任何第三方包）
- 可访问 `https://api.crossref.org` 的网络环境

## 使用方法

在仓库根目录下运行：

```bash
# 核查 BibTeX 文献库
python3 tools/check_dois.py tools/examples/refs-sample.bib

# 核查 Markdown 章节草稿或纯文本参考文献列表
python3 tools/check_dois.py chapters/chapter-02.md

# 输出 JSON 格式结果（便于脚本或流水线处理）
python3 tools/check_dois.py tools/examples/refs-sample.bib --json

# 严格模式：若存在 NOT_FOUND 或 NETWORK_ERROR 则返回退出码 1
python3 tools/check_dois.py tools/examples/refs-sample.bib --strict
```

### 命令行参数

| 参数 | 默认值 | 说明 |
|---|---|---|
| `input_file` | *（必填）* | 待核查的 `.bib`、`.txt`、`.md` 或 `.tex` 文件路径 |
| `--delay SECONDS` | `1.0` | 相邻两次 Crossref 请求之间的间隔秒数（脚本强制不低于 `1.0` 秒） |
| `--timeout SECONDS` | `15.0` | 单次 HTTP 请求超时秒数 |
| `--json` | `false` | 以 JSON 格式输出核查结果 |
| `--strict` | `false` | 当出现 `NOT_FOUND` 或 `NETWORK_ERROR` 时以状态码 `1` 退出 |

脚本请求头携带 `User-Agent: scivolume-academic-book-toolkit/0.1`，且强制保持至少 1 秒的请求间隔。

## 实测示例（`tools/examples/refs-sample.bib`）

[`examples/refs-sample.bib`](examples/refs-sample.bib) 包含 3 条经 Crossref 实测存在的真实学术文献（1 本学术专著、1 篇期刊论文、1 篇会议论文）与 1 条故意编造的测试 DOI（`10.1038/s41586-099-99999-z`）。

运行命令：

```bash
python3 tools/check_dois.py tools/examples/refs-sample.bib
```

实测完整输出：

```text
Input file : tools/examples/refs-sample.bib
Unique DOIs: 4 (Crossref API interval: 1.0s)

[1/4] DOI: 10.7208/chicago/9780226239873.001.0001 (@booth2016craft, line 9)
      Local    : The Craft of Research, Fourth Edition (2016)
      Status   : FOUND (exists in Crossref)
      Crossref : The Craft of Research, Fourth Edition (2016)
      Venue    : University of Chicago Press

[2/4] DOI: 10.1038/nature14539 (@lecun2015deep, line 20)
      Local    : Deep learning (2015)
      Status   : FOUND (exists in Crossref)
      Crossref : Deep learning (2015)
      Venue    : Nature

[3/4] DOI: 10.1145/3442188.3445922 (@bender2021parrots, line 30)
      Local    : On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? (2021)
      Status   : FOUND (exists in Crossref)
      Crossref : On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜 (2021)
      Venue    : Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency

[4/4] DOI: 10.1038/s41586-099-99999-z (@hallucinated2024synthetic, line 42)
      Local    : Automated Synthesis of Scholarly Monographs Without Source Grounding (2024)
      Status   : NOT_FOUND (does NOT exist in Crossref)
      Detail   : HTTP 404 Not Found (DOI not registered in Crossref)

--------------------------------------------------------------------
Summary: 4 checked | 3 found | 1 not found | 0 network error(s)
```

## 脚本边界与人工复核提示

1. **DOI 存在不等于元数据无误**：`FOUND` 仅说明该 DOI 已在 Crossref 注册，请务必对照输出中的 `Local` 与 `Crossref` 标题和年份，排查“真实 DOI 指向另一篇无关文献”的错误。
2. **非 Crossref 注册机构与无 DOI 书目**：大多数国际期刊、会议与大学出版社通过 Crossref 注册 DOI，但部分数据集/预印本（DataCite 注册）、中文文献或早期纸质专著可能不在 Crossref 库中，需通过 `https://doi.org/<DOI>`、ISBN 或馆藏目录进一步人工核实。
3. **正文论点支撑度仍需阅读原文**：即使文献与元数据完全真实，也必须核对原文内容是否确实支持正文论断。交稿前请配合 [`../checklists/reference-verification.zh-CN.md`](../checklists/reference-verification.zh-CN.md) 完成全部 7 项核查。
