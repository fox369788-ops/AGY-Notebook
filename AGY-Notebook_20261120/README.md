# AGY-Notebook 教科書轉 AI 黑板微影音技能懶人包 (2026-11-20 版)

本懶人包收錄了專為 **Google Antigravity (AGY)** 與 **Google NotebookLM Video Overview** 深度調校的 4 大標準工作技能（Skills）、SOP 規範文件與片頭後製工具。

---

## 📦 懶人包目錄內容

```text
AGY-Notebook_20261120/
├── skills/                             <-- 4 大 Antigravity 核心技能目錄
│   ├── textbook-pdf-splitter/          <-- 技能 1：課本整章 PDF 依節拆解
│   ├── lesson-core-summarizer/         <-- 技能 2：課文重點摘要提煉（口語版）
│   ├── chalkboard-slides-planner/      <-- 技能 3：黑板風投影片大綱規劃（精控 3.5 分鐘）
│   └── notebooklm-video-generator/     <-- 技能 4：NotebookLM 自動化生成與片頭後製
├── tools/                              <-- 輔助後製工具
│   ├── 一鍵加入3秒無聲片頭.bat          <-- 核心後製：拖曳 MP4 立即產出 3 秒靜止收心片頭
│   └── add_3s_intro.py                 <-- FFmpeg 片頭靜音與定格無損處理腳本
├── templates/                          <-- 規範範本
│   └── SOP_教材與簡報製作懶人包.md      <-- 教師完整作業流程指南與 NotebookLM 黃金參數
├── install_skills.bat                  <-- Windows 一鍵安裝所有技能至 Antigravity
├── install_skills.py                   <-- 跨平台 Python 安裝腳本
└── README.md                           <-- 本說明文件
```

---

## 🚀 快速安裝與使用

### 1. 一鍵安裝技能到您的 Antigravity
直接雙擊執行 **`install_skills.bat`**，系統將自動把 `skills/` 下的 4 個技能複製至本機全域技能庫：
`~/.gemini/config/skills/`

安裝後即可在任何對話或專案中直接呼叫：
* 「請幫我拆解這份課本 PDF」 ➔ 自動觸發 `textbook-pdf-splitter`
* 「幫我整理這小節重點摘要」 ➔ 自動觸發 `lesson-core-summarizer`
* 「規劃 3 段手繪黑板風大綱」 ➔ 自動觸發 `chalkboard-slides-planner`
* 「上傳至 NotebookLM 啟動影片摘要」 ➔ 自動觸發 `notebooklm-video-generator`

### 2. 單一目錄存放原則
所有產出的小節課文 `.md`、重點摘要 `_摘要.md`、投影片大綱 `X-X_XX.md`，統一儲存於**與原始整章 PDF 相同的目錄下**，乾淨集中！
