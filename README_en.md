<div align="center">
  <h1>TS File Converter</h1>
  <p>这个工具旨在转换 Qt Linguist TS 文件，支持不同语言之间的转换，特别关注中文变体和其他语言。</p>
  <p>This tool is designed to convert Qt Linguist TS files between different languages, with a focus on Chinese variants and other languages.</p>
  <img src="./resource/image.png" alt="icon" width="50%" height="50%"/>
  <p>
    <h3><span>English</span>&emsp;|&emsp;<a href="./README.md">简体中文</a></h3>
  </p>
</div>

## Features

- Convert between Chinese variants (Simplified, Traditional - Taiwan, Hong Kong, Singapore)
- Translate between various languages using Google Translate
- Preserve XML structure of TS files
- Handle batch processing of multiple files

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Required Python packages:
  - `argparse`
  - `asyncio`
  - `xml`
  - `opencc`
  - `deep-translator`

You can install the required packages using pip:

```
pip install opencc deep-translator
```

## Usage

To use the TS File Converter, follow these steps:

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the following command:

```
python ts_file_converter.py <file> <source_lang> <target_lang> [--src_dir <source_directory>]
```

### Parameters:

- `<file>`: The name of the TS file to convert.
- `<source_lang>`: The source language code (e.g., zh-CN, zh-HK, ja, ko, th, vi, hi).
- `<target_lang>`: The target language code (e.g., en, fr, de, es, it, ru, pt).
- `--src_dir` (optional): The source directory containing TS files. Default is the current directory.

### Examples:

1. Convert from Simplified Chinese to Traditional Chinese (Taiwan):
   ```
   python ts_file_converter.py myapp_zh_CN.ts zh-CN zh-TW
   ```

2. Translate from Japanese to English:
   ```
   python ts_file_converter.py myapp_ja.ts ja en
   ```

3. Convert files in a specific directory:
   ```
   python ts_file_converter.py myapp_zh_CN.ts zh-CN zh-TW --src_dir='/path/to/ts/files'
   ```

## Note

- This tool uses the Google Translate API for languages other than Chinese variants. Please be aware of potential usage limitations or costs associated with the Google Translate service.
- Because of the use of deep-translator, the translation of non-Chinese languages will be slower.

## Contributing

Contributions to the TS File Converter are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.