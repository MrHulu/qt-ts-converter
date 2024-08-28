<div align="center">
  <h1>TS 文件转换器</h1>
  <p>这个工具旨在转换 Qt Linguist TS 文件，支持不同语言之间的转换，特别关注中文变体和其他语言。</p>
  <p>This tool is designed to convert Qt Linguist TS files between different languages, with a focus on Chinese variants and other languages.</p>
  <img src="./resource/image.png" alt="icon" width="50%" height="50%"/>
  <p>
    <h3><a href="./README_en.md">English</a>&emsp;|&emsp;<span>简体中文</span></h3>
  </p>
</div>


## 特性

- 支持中文变体之间的转换（简体中文、繁体中文-台湾、香港、新加坡）
- 使用 Google 翻译在各种语言之间进行翻译
- 保留 TS 文件的 XML 结构
- 支持多个文件的批量处理

## 前提条件

在开始之前，请确保您满足以下要求：

- Python 3.7+
- 所需的 Python 包：
  - `argparse`
  - `asyncio`
  - `xml`
  - `opencc`
  - `deep-translator`

您可以使用 pip 安装所需的包：

```
pip install opencc deep-translator
```

## 使用方法

要使用 TS 文件转换器，请按照以下步骤操作：

1. 克隆仓库或下载脚本。
2. 打开终端并导航到包含脚本的目录。
3. 使用以下命令运行脚本：

```
python ts_file_converter.py <file> <source_lang> <target_lang> [--src_dir <source_directory>]
```

### 参数：

- `<file>`：要转换的 TS 文件名。
- `<source_lang>`：源语言代码（例如，zh-CN、zh-HK、ja、ko、th、vi、hi）。
- `<target_lang>`：目标语言代码（例如，en、fr、de、es、it、ru、pt）。
- `--src_dir`（可选）：包含 TS 文件的源目录。默认为当前目录。

### 示例：

1. 从简体中文转换为繁体中文（台湾）：
   ```
   python ts_file_converter.py myapp_zh_CN.ts zh-CN zh-TW
   ```

2. 从日语翻译为英语：
   ```
   python ts_file_converter.py myapp_ja.ts ja en
   ```

3. 转换特定目录中的文件：
   ```
   python ts_file_converter.py myapp_zh_CN.ts zh-CN zh-TW --src_dir='/path/to/ts/files'
   ```

## 注意事项

- 此工具使用 Google 翻译 API 处理中文变体以外的语言。请注意 Google 翻译服务可能存在的使用限制或相关费用。
- 由于使用deep-translator的原因，所以翻译非中文语言时，会比较慢。

## 贡献

欢迎对 TS 文件转换器做出贡献。请随时提交 Pull Request。

## 许可证

该项目采用 MIT 许可证 - 有关详细信息，请参阅 LICENSE 文件。