import os
import json
from pathvalidate import sanitize_filename
import data_extract  # 导入data_extract模块

# 使用从data_extract导入的pub_data_dict
mapping_data = data_extract.pub_data_dict

# 创建输入和输出文件夹
input_directory = "./in"
output_directory = "./out"
os.makedirs(input_directory, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)

# 遍历目录中的所有jpg文件
for root, dirs, files in os.walk(input_directory):
    for file in files:
        if file.lower().endswith(".jpg"):
            original_filename = os.path.splitext(file)[0]
            
            # 在映射数据中查找对应的SchoolID
            school_id = None
            for i, cn_name in enumerate(mapping_data["CN_Name"]):
                if cn_name == original_filename:
                    school_id = mapping_data["SchoolID"][i]
                    break
            
            if school_id:
                new_filename = sanitize_filename(school_id) + ".jpg"
                old_path = os.path.join(root, file)
                new_path = os.path.join(output_directory, new_filename)
                
                # 执行重命名操作
                os.rename(old_path, new_path)
                print(f"Renamed {file} to {new_filename}")
            else:
                print(f"Mapping not found for {original_filename}. Skipping.")

print("Batch renaming completed.")