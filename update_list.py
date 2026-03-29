import os
import json

# 取得目前腳本目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')

# 確保 data 資料夾存在
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print("已建立 'data' 資料夾，請將 .json 題目檔放進去後再執行一次。")
else:
    # 抓取所有 .json 檔案
    json_files = [f for f in os.listdir(data_dir) if f.endswith('.json')]
    
    # 寫入清單
    with open(os.path.join(current_dir, 'filelist.json'), 'w', encoding='utf-8') as f:
        json.dump(json_files, f, ensure_ascii=False, indent=4)
    
    print(f"成功！目前偵測到 {len(json_files)} 個 JSON 檔案。")
    print(f"檔案清單：{json_files}")