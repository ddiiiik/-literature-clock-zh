import json
import os
from pathlib import Path
from opencc import OpenCC

# 创建繁体转换器
cc = OpenCC('s2t')

def convert_to_traditional(value):
    """递归地将文本从简体转换为繁体"""
    if isinstance(value, str):
        return cc.convert(value)
    elif isinstance(value, dict):
        return {k: convert_to_traditional(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [convert_to_traditional(item) for item in value]
    return value

def merge_quotes(quotes_dir):
    """合并quotes目录下的所有json文件到两个版本的输出文件中
    
    Args:
        quotes_dir: quotes目录的路径
    """
    # 获取当前脚本所在目录
    current_dir = Path(__file__).parent
    
    # 目标文件
    output_file_hans = current_dir / "litclock_zh_hans.json"
    output_file_hant = current_dir / "litclock_zh_hant.json"
    
    # 如果输出文件不存在，创建空列表
    if not output_file_hans.exists():
        merged_data_hans = []
        merged_data_hant = []
    else:
        # 读取现有的合并文件
        with open(output_file_hans, 'r', encoding='utf-8') as f:
            merged_data_hans = json.load(f)
        # 创建繁体版本的初始数据
        merged_data_hant = [convert_to_traditional(item) for item in merged_data_hans]
    
    # 获取所有json文件
    json_files = sorted(Path(quotes_dir).glob("*.json"))
    
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
                    merged_data_hans.extend(data)
                    # 为繁体版本转换数据
                    merged_data_hant.extend([convert_to_traditional(item) for item in data])
                # 如果数据是字典，创建列表
                elif isinstance(data, dict):
                    merged_data_hans.append(data)
                    # 为繁体版本转换数据
                    merged_data_hant.append(convert_to_traditional(data))
                else:
                    print(f"Warning: {json_file} contains invalid data format")
                    continue
                    
                processed_files.add(json_file.name)
                
        except json.JSONDecodeError:
            print(f"Warning: {json_file} is not valid JSON")
            continue
    
    # 移除重复的条目（如果需要）
    merged_data_hans = list({json.dumps(d, sort_keys=True): d for d in merged_data_hans}.values())
    merged_data_hant = list({json.dumps(d, sort_keys=True): d for d in merged_data_hant}.values())
    
    # 写入合并后的数据
    with open(output_file_hans, 'w', encoding='utf-8') as f:
        json.dump(merged_data_hans, f, ensure_ascii=False, indent=2)
    with open(output_file_hant, 'w', encoding='utf-8') as f:
        json.dump(merged_data_hant, f, ensure_ascii=False, indent=2)
    
    print(f"合并完成！")
    print(f"简体版本：{len(merged_data_hans)} 条数据")
    print(f"繁体版本：{len(merged_data_hant)} 条数据")

if __name__ == "__main__":
    # 获取上一级目录中的quotes目录
    quotes_dir = Path(__file__).parent.parent / "quotes"
    merge_quotes(str(quotes_dir))
