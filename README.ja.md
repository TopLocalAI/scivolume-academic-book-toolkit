[English](./README.md) | [简体中文](./README.zh-CN.md) | 日本語

# SciVolume Academic Book Toolkit

**SciVolume Academic Book Toolkit** は、学術専門書（モノグラフ）、大学院向け教科書、学術ノンフィクション書籍を執筆する研究者、大学教員、大学院生、技術書著者向けに構築された、Markdown テンプレート、編集チェックリスト、および外部依存ゼロの Python 製 Crossref DOI 検証スクリプトをまとめたオープンソースツールキットです。Markdown、LaTeX、Word のいずれの執筆ワークフローでも単体で利用でき、出版企画書の作成、章ごとの論証構造の設計、捏造引用や不一致引用に対する参考文献リスト全件の監査、ならびに提出前の専門用語・数式記法・図表番号・相互参照の整合性チェックを行えます。本ツールキットは SciVolume によってメンテナンスされており、公式サイトは [https://scivolume.ai](https://scivolume.ai) です。

---

## リポジトリ構成

```text
scivolume-academic-book-toolkit/
├── templates/                      # Bilingual templates (.md = EN, .zh-CN.md = ZH)
│   ├── book-proposal.md            # Academic book proposal template
│   ├── book-outline.md             # Full-book outline & chapter dependency map
│   ├── chapter-draft.md            # Single-chapter template (objectives, argument, figures, refs)
│   └── ai-disclosure.md            # Generic AI-assisted writing disclosure template
├── checklists/                     # Pre-submission editorial & citation checklists
│   ├── reference-verification.md   # 7-point per-reference anti-hallucination checklist
│   └── manuscript-consistency.md   # Full-book terminology, notation, figure & cross-ref checklist
└── tools/                          # Zero-dependency verification utilities
    ├── check_dois.py               # Pure-stdlib Crossref DOI checker (urllib)
    ├── README.md                   # Script documentation & verified sample output
    └── examples/
        └── refs-sample.bib         # Sample .bib (3 real Crossref works + 1 fabricated DOI)
```

### テンプレート（`templates/`）

| ドキュメント | English | 简体中文 | 利用場面 |
|---|---|---|---|
| **出版企画書（Book Proposal）** | [`book-proposal.md`](templates/book-proposal.md) | [`book-proposal.zh-CN.md`](templates/book-proposal.zh-CN.md) | 企画編集者への学術専門書・教科書の提案時（中心命題、想定読者層、類書比較、解説付き目次、執筆スケジュール） |
| **全章アウトライン（Full-Book Outline）** | [`book-outline.md`](templates/book-outline.md) | [`book-outline.zh-CN.md`](templates/book-outline.zh-CN.md) | 章間の依存関係、語数・図表数の配分、主要概念や記号を初出定義する章・節の計画時 |
| **単章ドラフト（Single-Chapter Draft）** | [`chapter-draft.md`](templates/chapter-draft.md) | [`chapter-draft.zh-CN.md`](templates/chapter-draft.zh-CN.md) | 章の学習・論証目標、節ごとの主張と根拠の対応関係、図表一覧、検証済み参考文献の構造化時 |
| **AI 利用開示（AI Usage Disclosure）** | [`ai-disclosure.md`](templates/ai-disclosure.md) | [`ai-disclosure.zh-CN.md`](templates/ai-disclosure.zh-CN.md) | 執筆中の AI 補助作業の記録、および前付やカバーレター向けの汎用的な開示文の作成時 |

### チェックリスト（`checklists/`）

| チェックリスト | English | 简体中文 | 監査対象 |
|---|---|---|---|
| **参考文献の検証（Reference Verification）** | [`reference-verification.md`](checklists/reference-verification.md) | [`reference-verification.zh-CN.md`](checklists/reference-verification.zh-CN.md) | 著者名、タイトル、出版年、掲載誌／出版社、巻・号・ページ、DOI の解決と一致、および本文が実際に主張を裏付けているかの確認 |
| **原稿全体の整合性（Manuscript Consistency）** | [`manuscript-consistency.md`](checklists/manuscript-consistency.md) | [`manuscript-consistency.zh-CN.md`](checklists/manuscript-consistency.zh-CN.md) | 用語の統一、数式記法と単位、図・表・数式番号の連番整合性、および章をまたぐ相互参照の確認 |

---

## クイックスタート：Crossref に対する DOI の検証

[`tools/check_dois.py`](tools/check_dois.py) は Python 3 標準ライブラリ（`urllib`）のみを使用しており、サードパーティ製パッケージは不要です。`.bib`、`.md`、`.txt`、または `.tex` ファイルから DOI を抽出し、リクエスト間に 1 秒以上の間隔を空けながら `https://api.crossref.org/works/<DOI>` へ問い合わせ、目視照合用に Crossref 側のタイトルと出版年を表示するとともに、ネットワーク／API エラー（`NETWORK_ERROR`）と存在しない DOI（`NOT_FOUND`）を区別します。

```bash
python3 tools/check_dois.py tools/examples/refs-sample.bib
```

[`tools/examples/refs-sample.bib`](tools/examples/refs-sample.bib)（実在する学術文献 3 件＋意図的に作成した架空 DOI 1 件）に対する出力例：

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

すべての CLI オプション（`--delay`、`--timeout`、`--json`、`--strict`）および完全な実行記録については [`tools/README.md`](tools/README.md) を参照してください。

---

## 引用ハルシネーションを防いで学術書を執筆するための推奨ワークフロー

1. **各章を書き始める前に書籍全体の骨格を固める**：[`templates/book-outline.md`](templates/book-outline.md) を埋め、すべての章に明確な主題、目標語数、前提知識の依存関係、および主要用語・記号を定義する担当セクションを割り当てます。
2. **すべての節を事前検証済みの文献に紐づける**：本文を書き広げる**前に**、[`templates/chapter-draft.md`](templates/chapter-draft.md) 上で各節の主張を具体的な BibTeX キーおよびページ番号と対応付けます。下書きや翻訳に AI ツールを併用する場合は、モデルの記憶から引用を生成させるのではなく、自身のノートと検証済み `.bib` レコードのみを参照範囲に制限します。
3. **自動チェックと手動の引用確認を組み合わせる**：`python3 tools/check_dois.py` を実行して架空の DOI（`NOT_FOUND`）や取り違えられた DOI（`Local` と `Crossref` のタイトルが異なるケース）を検出し、続いて [`checklists/reference-verification.md`](checklists/reference-verification.md) を用いて DOI のない書籍や本文レベルでの主張の裏付けを確認します。
4. **統合した原稿全体を統一する**：入稿前に [`checklists/manuscript-consistency.md`](checklists/manuscript-consistency.md) を一通り確認し、該当する場合は提出先出版社のガイドラインを確認したうえで [`templates/ai-disclosure.md`](templates/ai-disclosure.md) を使って透明性のある編集注記を用意します。

---

## このワークフローを自動化したい場合

個別のファイルを手作業で管理する代わりに統合されたワークスペースを利用したい場合、[SciVolume](https://scivolume.ai) は学術専門書や教科書などの本格的なノンフィクション執筆プロジェクトに対応しています。アウトラインの構築や章単位の執筆（著者が承認した参考文献およびアップロードした PDF、DOCX、BibTeX / RIS 資料のみを引用）から、引用チェック、科学イラスト作成（SciDraw API 連携）、6 言語間の書籍丸ごとの翻訳、各種エクスポートまでを一貫して扱えます。有料プラン（月額 $20 の Scholar、月額 $50 の Pro、月額 $150 の Studio、年払いオプションあり）では Word（`.docx`）、LaTeX パッケージ、EPUB 3、印刷用 PDF のエクスポートに対応しており、無料アカウントでは公開サンプル書籍や書籍全体の整合性レポート・引用チェックレポートのサンプルを閲覧できます。詳細は [https://scivolume.ai](https://scivolume.ai)、[How SciVolume Writes a Sourced Book](https://scivolume.ai/blog/how-scivolume-writes-a-sourced-book)、および [AI Academic Book Writing Tools Comparison](https://scivolume.ai/blog/ai-academic-book-writing-tools-comparison) をご覧ください。

---

## ライセンス

- **コード**（`tools/*.py`）：MIT License。
- **ドキュメント、テンプレート、チェックリスト、および画像**：Creative Commons Attribution 4.0 International（[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)）。
