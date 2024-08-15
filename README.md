## 軟體

- **Python**
- **HTML**
- **CSS**
- **JavaScript**

## 功能

1. **書籍查詢介面**：根據書名、類別、狀態等關鍵字進行搜索。
2. **查看書籍明細介面**：詳細顯示書籍的相關信息。
3. **編輯、更新、刪除書籍的借閱狀態、書名、借閱人、借閱日期等信息**。

## 遇到的問題與解決方式

- **問題**：
  - 資料庫同步問題。
  - 唯讀介面可編輯。
  - 出版日期可設定超過今天。

- **解決方式**：
  1. 確保資料庫遷移是最新的。
  2. 根據 `readonly` 參數，將字段設為唯讀或禁用狀態。
  3. 使用 `if_else` 調整日期限制，防止設定超過今天的日期。

## 實作照片
<p align="center">
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/e79e5c25-8261-48fd-8d30-41586554c414">
  <br>
</p>
<p align="center">
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/381fda82-6f40-4315-8bed-763280be95be">
  <br>
  （書籍查詢介面）
</p>
<p align="center">
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/893b246a-9587-4a8f-b493-262866989e26">
  <br>
  （編輯、更新、刪除書籍的借閱狀態、書名、借閱人、借閱日期等信息）
</p>
