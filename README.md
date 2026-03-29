# 🎓 IPAS AI 應用規劃師 - 模擬練習系統

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Type](https://img.shields.io/badge/Project-Personal_Study-orange.svg)
![Purpose](https://img.shields.io/badge/Purpose-Non--Profit-green.svg)

這是一個專為 **IPAS AI 應用規劃師（初級）** 能力鑑定考試開發的網頁練習系統。透過 GitHub Pages 部署，讓你隨時隨地都能進行題庫練習、錯題複習與模擬測驗。

---

## ✨ 核心功能

- 📂 **跨分類選題**：支援同時勾選多份考卷（科目一、科目二、樣題）進行混合測驗。
- 🎯 **自訂測驗量**：可自由設定隨機抽取的題數，或挑戰全部題庫。
- 📝 **即時詳解**：提交答案後立即顯示正確選項與官方/自編詳解。
- 🧠 **專屬錯題本**：系統自動記錄答錯題目，並提供專屬複習模式（答對後自動移除）。
- 📊 **評分系統**：完整記錄答對題數與正確率，快速掌握學習進度。
- 📱 **響應式設計**：支援手機與平板，通勤時間也能輕鬆複習。

---

## 🛠️ 資料格式規範 (JSON)

本系統採動態讀檔，題庫檔案請存放於 `/data` 資料夾中，並遵循以下格式：

```json
[
  {
    "question": "題目內容文字",
    "options": ["選項 A", "選項 B", "選項 C", "選項 D"],
    "answer": 0, 
    "analysis": "這裡是該題的詳細解釋內容..."
  }
]
```
> **註：** `answer` 欄位請使用索引值（0 代表 A, 1 代表 B，依此類推）。

---

## 🚀 快速上手

1. **上傳題庫**：將符合格式的 `.json` 檔案放入 `data/` 資料夾。
2. **更新清單**：執行 `python update_list.py` 生成最新檔案索引 `filelist.json`。
3. **本地開啟**：使用 Live Server 或直接開啟 `index.html`。
4. **線上部署**：推送到 GitHub 儲存庫並在 Settings 中開啟 **GitHub Pages** 功能。

---

## ⚖️ 免責聲明與版權說明

### 📢 重要聲明
1. **個人練習用途**：本專案僅供 **個人練習** 與 **非營利學術交流** 使用。
2. **非官方系統**：本網頁為個人開發之工具，與經濟部或 iPAS 官方機構無官方關聯。
3. **資料來源**：本系統所載之題目資料來源於 [經濟部產業人才能力鑑定 (iPAS) 官方網站](https://ipd.nat.gov.tw/ipas/certification/AIAP/learning-resources)。
4. **版權歸屬**：考題著作權均歸原發行單位（經濟部產業發展署）所有。

### 🛡️ 使用規範
本專案嚴格遵循**非營利**原則：
- ❌ 禁止將此原始碼或轉製後之資料用於商業收費、補習班教材銷售。
- ❌ 禁止移除網頁內之官方來源標註。

---

## 🤝 貢獻
歡迎透過 Pull Request 貢獻更多題庫詳解或優化 UI 介面。讓我們一起順利通過 IPAS 鑑定！

---
*Made with ❤️ for AI Learners.*