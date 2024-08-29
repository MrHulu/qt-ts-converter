# Description: This script is used to test the ts_file_converter.py script.
import subprocess

def test(args=['-h']):
    result = subprocess.run(args=['python', 'ts_file_converter.py'] + args, capture_output=True, text=False)
    print("Output:\n", result.stdout.decode('utf-8'))

if __name__ == '__main__':
    test(['-h'])
    test(['test-zh_HK.ts', 'zh-CN', 'zh-HK', "--src_dir=./resource"])
    test(['test-en_US.ts', 'zh-CN', 'en', '--src_dir', './resource'])
