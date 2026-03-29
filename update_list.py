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
    json_filenames = [f for f in os.listdir(data_dir) if f.endswith('.json')]
    
    file_list_with_count = []
    
    for filename in json_filenames:
        file_path = os.path.join(data_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 確保 JSON 是清單格式並計算長度
                count = len(data) if isinstance(data, list) else 0
                file_list_with_count.append({
                    "filename": filename,
                    "count": count
                })
        except Exception as e:
            print(f"處理檔案 {filename} 時發生錯誤: {e}")

    # 寫入清單檔 (filelist.json)
    output_path = os.path.join(current_dir, 'filelist.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(file_list_with_count, f, ensure_ascii=False, indent=4)
    
    print(f"成功！目前偵測到 {len(file_list_with_count)} 個 JSON 檔案並已計算題數。")
    print(f"輸出路徑：{output_path}")