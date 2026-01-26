# 🚀 GitHub Pages 部署指南

## 📋 前置準備

1. **GitHub 帳號**：確保您有 GitHub 帳號
2. **Git 安裝**：確認電腦已安裝 Git

---

## 🔧 部署步驟

### Step 1: 初始化 Git Repository

```powershell
# 在 travel 資料夾中執行
cd c:\python-training\travel

# 初始化 Git
git init

# 添加檔案
git add index.html README.md .gitignore

# 提交
git commit -m "Initial commit: Europe travel guide"
```

### Step 2: 創建 GitHub Repository

1. 前往 https://github.com/new
2. Repository name: `europe-travel-guide`
3. **重要**：選擇 **Private** ✅
4. **不要**勾選 "Add a README file"
5. 點擊 "Create repository"

### Step 3: 連結並推送

```powershell
# 連結到 GitHub（替換成您的用戶名）
git remote add origin https://github.com/[你的用戶名]/europe-travel-guide.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### Step 4: 啟用 GitHub Pages

1. 進入 repository 頁面
2. 點擊 "Settings"
3. 左側選單點擊 "Pages"
4. Source 選擇 "Deploy from a branch"
5. Branch 選擇 "main" 和 "/ (root)"
6. 點擊 "Save"

### Step 5: 等待部署

- 等待 1-2 分鐘
- 重新整理頁面
- 會看到綠色訊息：**"Your site is live at https://[你的用戶名].github.io/europe-travel-guide/"**

---

## 👥 邀請旅伴查看

### 方法 1：添加協作者

1. Repository → Settings → Collaborators
2. 點擊 "Add people"
3. 輸入旅伴的 GitHub 用戶名或 email
4. 旅伴會收到邀請信

### 方法 2：分享連結（需登入）

直接分享網址給旅伴：
```
https://[你的用戶名].github.io/europe-travel-guide/
```

> [!NOTE]
> 因為是 private repository，旅伴需要：
> 1. 有 GitHub 帳號
> 2. 被添加為協作者
> 3. 登入 GitHub 後才能查看

---

## 🔄 更新內容

如果之後修改了 `index.html`：

```powershell
cd c:\python-training\travel

# 添加修改
git add index.html

# 提交
git commit -m "Update travel guide"

# 推送
git push
```

等待 1-2 分鐘，網站會自動更新。

---

## 📱 手機查看

1. 在手機瀏覽器打開網址
2. 登入 GitHub 帳號
3. 即可查看（完全響應式設計）

---

## ⚠️ 常見問題

### Q: 為什麼旅伴看不到？
A: 確認：
- 旅伴有 GitHub 帳號
- 已添加為協作者
- 旅伴已登入 GitHub

### Q: 可以改成 public 嗎？
A: 可以，但建議旅行結束後再改：
- Settings → Danger Zone → Change visibility → Make public

### Q: 檔案太大怎麼辦？
A: 目前 10MB 沒問題，GitHub Pages 限制是 1GB

---

## 🎉 完成！

現在您和旅伴都可以在任何裝置上查看這份精美的旅遊指南了！
