import re
import os
import glob

def wrap_numbers_with_span(html_content):
    # 匹配内联style标签，以便跳过它们
    style_pattern = r'style="[^"]*"'
    
    # 匹配HTML标签属性，包括src、width、height等
    attr_pattern = r'\w+="[^"]*"'
    
    # 匹配表格单元格中的纯数字内容（如<td>900</td>）
    table_cell_pattern = r'<td[^>]*>\s*\d+\s*</td>'
    
    # 匹配包含font-weight样式的span标签及其内容
    font_weight_span_pattern = r'<span[^>]*style="[^"]*font-weight[^"]*"[^>]*>.*?</span>'

    # 匹配技能等级格式（如Lv.4）
    skill_level_pattern = r'Lv\.\d+'

    # 找到所有需要跳过的部分（style、属性和特定表格单元格）
    skip_pattern = f'({style_pattern}|{attr_pattern}|{table_cell_pattern}|{font_weight_span_pattern}|{skill_level_pattern})'
    skip_matches = list(re.finditer(skip_pattern, html_content, re.IGNORECASE))
    
    # 要包装的模式：包括负号、小数、百分号等完整数字格式
    number_pattern = r'[+-]?\d+\.?\d*%?|\d+(?=秒)'
    
    result = []
    last_pos = 0
    
    def wrap_match(match):
        """包装匹配到的内容"""
        return f'<b style="color: #0a2;">{match.group(0)}</b>'
    
    # 处理每个需要跳过的部分之间的内容
    for skip_match in skip_matches:
        start, end = skip_match.span()
        
        # 添加跳过部分之前的内容
        text_before_skip = html_content[last_pos:start]
        
        # 只对非跳过部分应用数字替换
        text_before_skip = re.sub(number_pattern, wrap_match, text_before_skip)
        
        result.append(text_before_skip)
        result.append(skip_match.group(0))  # 添加未修改的跳过部分
        last_pos = end
    
    # 处理最后一个跳过部分之后的内容
    text_after_last_skip = html_content[last_pos:]
    text_after_last_skip = re.sub(number_pattern, wrap_match, text_after_last_skip)
    result.append(text_after_last_skip)
    
    return ''.join(result)

def process_folder(folder_path, output_suffix='_processed'):
    """
    处理文件夹中的所有HTML文件
    """
    # 获取文件夹中所有的HTML文件
    html_files = glob.glob(os.path.join(folder_path, '*.html'))
    
    if not html_files:
        print(f"在文件夹 {folder_path} 中没有找到HTML文件")
        return
    
    processed_count = 0
    
    for file_path in html_files:
        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 处理内容
            processed_content = wrap_numbers_with_span(content)
            
            # 生成输出文件名
            file_dir, file_name = os.path.split(file_path)
            name, ext = os.path.splitext(file_name)
            output_filename = f"{name}{output_suffix}{ext}"
            output_path = os.path.join(file_dir, output_filename)
            
            # 保存处理后的内容
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(processed_content)
            
            print(f"已处理: {file_name} -> {output_filename}")
            processed_count += 1
            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {str(e)}")
    
    print(f"\n处理完成！共处理了 {processed_count} 个文件")

# 直接指定文件夹路径
folder_path = "./output_files"  # 修改为你的文件夹路径

# 检查文件夹是否存在
if not os.path.exists(folder_path):
    print(f"错误: 文件夹 '{folder_path}' 不存在")
else:
    # process_folder(folder_path)
    process_folder(folder_path, output_suffix='')