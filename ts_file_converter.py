import argparse
import asyncio
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from opencc import OpenCC
from deep_translator import GoogleTranslator

def get_opencc_config(source_lang, target_lang):
    config_map = {
        ('zh-CN', 'zh-TW'): 's2tw',
        ('zh-CN', 'zh-HK'): 's2hk',
        ('zh-CN', 'zh-SG'): 's2sg',
        ('zh-TW', 'zh-CN'): 't2s',
        ('zh-HK', 'zh-CN'): 't2s',
        ('zh-SG', 'zh-CN'): 't2s',
        ('zh-TW', 'zh-HK'): 't2hk',
        ('zh-TW', 'zh-SG'): 't2sg',
        # 添加其他需要的配置
    }
    return config_map.get((source_lang, target_lang))

def convert_chinese(text, conversion):
    cc = OpenCC(conversion)
    return cc.convert(text)

async def translate_text(text, source_lang, target_lang):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return await asyncio.to_thread(translator.translate, text)

async def translate_texts(texts, source_lang, target_lang):
    tasks = [translate_text(text, source_lang, target_lang) for text in texts]
    return await asyncio.gather(*tasks)

def convert_ts_file(file, source_lang, target_lang):
    # 读取文件
    tree = ET.parse(file)
    root = tree.getroot()

    # 确定使用哪种转换方法
    if source_lang.startswith('zh') and target_lang.startswith('zh'):
        opencc_config = get_opencc_config(source_lang, target_lang)
        if opencc_config:
            cc = OpenCC(opencc_config)
            convert_func = cc.convert
        else:
            raise ValueError(f"Unsupported Chinese conversion: {source_lang} to {target_lang}")
    else:
        convert_func = lambda text: asyncio.run(translate_text(text, source_lang, target_lang))

    # 遍历所有content标签
    for context in root.findall('context'):
        # 遍历所有message标签
        for message in context.findall('message'):
            # 获取message标签中的source标签
            source = message.find('source')
            # 获取source标签中的文本
            text = source.text
            if text is None:
                continue
            translation = message.find('translation')
            type = translation.get('type')
            if(type == 'unfinished'):
                # 进行转换
                text = convert_func(text)
                # 将转换后的文本赋值给translation标签
                translation.text = text
                del translation.attrib['type']
                print(f"{source_lang}: {source.text} -> {target_lang}: {translation.text}")

    # 保存文件
    ugly_xml = ET.tostring(root, encoding='utf-8').decode('utf-8')
    pretty_xml = minidom.parseString(ugly_xml).toprettyxml(indent="", newl="", encoding='utf-8')
    with open(file, "wb") as f:
        f.write(pretty_xml)

def main():
    parser = argparse.ArgumentParser(description='Convert Qt Linguist TS files between different languages.')
    parser.add_argument('file',help='TS file')
    parser.add_argument('source_lang',help='Source language code (e.g., zh-CN, zh-HK, ja, ko, th, vi, hi)', default='zh-CN')
    parser.add_argument('target_lang', help='Target language code (e.g., en, fr, de, es, it, ru, pt)')
    parser.add_argument('--src_dir', help='Source directory containing TS files', default='.')
    
    args = parser.parse_args()

    # 将脚本文件所在目录设置为当前目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    try:
        # 切换到包含TS文件的目录
        if args.src_dir:    
            os.chdir(args.src_dir)
        convert_ts_file(args.file, args.source_lang, args.target_lang)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()