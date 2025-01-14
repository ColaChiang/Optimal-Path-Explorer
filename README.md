# 臺北地標路徑規劃系統

## 簡介
本專案是一個基於Flask網頁應用的臺北地標路徑規劃系統，使用改進的貪婪演算法和Dijkstra演算法，實現以下功能：
1. 根據地標評分和距離計算最佳景點選擇。
2. 計算選定景點間的最短路徑。
3. 提供最佳路徑和總行程距離的建議。

## 功能
- 選擇參訪的景點數量，系統根據評分和距離篩選地標。
- 計算通過這些地標的最短路徑，並顯示路徑與總距離。

## 系統架構
- **後端**：使用Flask架設，整合NetworkX處理圖結構與路徑演算法。
- **前端**：HTML+JavaScript，提供使用者操作介面。
- **資料處理**：結合地標評分和距離計算收益，動態篩選最佳景點。

## 系統需求
請確認您的環境中安裝了以下軟體：
- Python3.8或更高版本

## 安裝與執行

1. **clone本專案到您的本地環境**：
   ```bash
   git clone https://github.com/ColaChiang/Optimal-Path-Explorer.git
   cd Optimal-Path-Explorer
   ```

2. **安裝所需的套件**：
   ```bash
   pip install -r requirements.txt
   ```

3. **啟動Flask伺服器**：
   ```bash
   python app.py
   ```

4. **在瀏覽器中開啟** [http://127.0.0.1:5000](http://127.0.0.1:5000)。

## 使用方式
1. 在主頁輸入您希望參訪的景點數量（1-6）。
2. 點擊「計算路徑」，查看系統推薦的最佳路徑、選定景點及總距離。
<img width="424" alt="image" src="https://github.com/user-attachments/assets/604ea8b0-bd48-428b-8b53-126a8b242d8e" />

## 項目展示
- **地圖視覺化**：顯示臺北地標的節點與連線。
- <img width="344" alt="image" src="https://github.com/user-attachments/assets/f7377435-3d0a-47dc-bfa3-156475c47391" />
- **計算結果展示**：以圖文方式顯示最佳行程規劃。

## 範例輸出
- **選擇的景點**：臺北101、中正紀念堂、北投溫泉
- **最佳路徑**：臺北101 → 中正紀念堂 → 北投溫泉
- **總距離**：15 單位

## Contributor
- **蔣哿樂** (國立臺北教育大學 數學暨資訊教育學系)
  - **指導教授**：王昱晟 助理教授

## 版權聲明
本專案為學術用途，版權所有，請勿用於商業用途。

