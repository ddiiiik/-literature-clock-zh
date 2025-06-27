import json
import os
from pathlib import Path

def merge_quotes():
    # 获取当前脚本所在目录
    current_dir = Path(__file__).parent
    
    # 源目录和目标文件
    quotes_dir = current_dir
    output_file = current_dir.parent / "litclock_zh.json"
    
    # 如果输出文件不存在，创建空列表
    if not output_file.exists():
        merged_data = []
    else:
        # 读取现有的合并文件
        with open(output_file, 'r', encoding='utf-8') as f:
            merged_data = json.load(f)
    
    # 获取所有json文件
    json_files = sorted(quotes_dir.glob("*.json"))
    
    # 创建一个集合来跟踪已处理的文件
    processed_files = set()
    
    # 遍历所有json文件
    for json_file in json_files:
        # 如果文件已经在合并数据中，跳过
        if json_file.name in processed_files:
            continue
            
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # 如果数据是列表，直接添加
                if isinstance(data, list):
                    merged_data.extend(data)
                # 如果数据是字典，创建列表
                elif isinstance(data, dict):
                    merged_data.append(data)
                else:
                    print(f"Warning: {json_file} contains invalid data format")
                    continue
                    
                processed_files.add(json_file.name)
                
        except json.JSONDecodeError:
            print(f"Warning: {json_file} is not valid JSON")
            continue
    
    # 移除重复的条目（如果需要）
    merged_data = list({json.dumps(d, sort_keys=True): d for d in merged_data}.values())
    
    # 写入合并后的数据
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print(f"合并完成！总共合并了 {len(merged_data)} 条数据")

if __name__ == "__main__":
    merge_quotes()
