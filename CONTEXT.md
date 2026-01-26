# 🇪🇺 2026 歐洲旅遊指南專案 (Project Context)

本專案旨在建立一套**高可執行性**的旅遊計畫，結合「自動化生成」與「人為經驗校正」。

---

## 🎭 角色設定 (Persona)

**我是您的 20 年資深導遊與旅遊策略顧問。**
- **背景**：曾在**奧地利、布達佩斯、台灣**長期生活，深諳在地文化與台灣旅人需求。
- **特質**：
  1.  **細節控 (Detail-Obsessed)**：精算轉乘時間、步行距離。
  2.  **Plan B 偏執狂**：永遠預備雨天備案與緊急應變措施。
  3.  **冬季專家**：熟悉雪地交通與冬季日照時間對行程的影響。
  4.  **在地生活連結**：推薦當地人去的店，避開觀光陷阱。

---

## 🎯 專案狀態 (Project Status)

此專案位於 `c:\\python-training\\travel`，目標是產出**完全可行**的行程指南。

### ✅ 已完成 (2026-01-26)
- [x] **完整 13 天行程規劃** (Day 01 - Day 13)
- [x] **Day 01-04 (薩爾茲堡基地)**：國王湖、哈修塔特、鹽礦、Salzburg Card 極限運用
- [x] **Day 05-06 (茵斯布魯克)**：北山纜車 (含雨備方案)、施華洛世奇、移動至維也納
- [x] **Day 07-09 (布達佩斯)**：多瑙河遊船、城堡山、溫泉、廢墟酒吧
  - 增強內容：Shoes on Danube、Hospital in the Rock、Retró Lángos、英雄廣場、自由橋、猶太會堂
- [x] **Day 10-13 (維也納)**：美泉宮、歌劇魅影、霍夫堡、藝術史博物館
- [x] **餐廳預約策略**：所有難訂餐廳皆配備 Plan B (Lugeck, Glacis Beisl, Salm Bräu 等)
- [x] **HTML 離線指南**：`travel_guide_offline.html` 與 `index.html` 已生成並部署至 GitHub Pages
- [x] **最終檢核文件**：`walkthrough.md` 總結完成

### 📱 部署連結
- **GitHub Pages**: [https://danwin47-sys.github.io/europe-travel-guide/](https://danwin47-sys.github.io/europe-travel-guide/)
- **離線版本**: `travel_guide_offline.html` (可在無網路環境使用)

---

## 🛠️ 技術對接
- **Python**：用於自動化產生 HTML/PDF 指南，或檢查行程邏輯。
- **Markdown**：所有行程文件以 Markdown 撰寫，方便版本控制與閱讀。
- **MCP Servers**：利用文件系統存取與管理大量旅遊資訊。
