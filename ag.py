import os
import sys

def search_files(pattern, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root,file)
            if file_path.endswith(('.bin', '.o', '.obj', '.a', '.dll', '.exe', '.so','.xml')):
                continue
            try:
                with open(file_path, encoding='utf-8', errors='ignore') as f:
                    #意思是打开这个路径对应的文件 并且以只读的形式
#使用 with 语句可以在代码块执行完毕后自动释放资源，而无需手动关闭打开的文件、数据库连接或其他资源。它提供了一种更优雅的方式来管理这些资源，同时还能保证在发生异常时正确地处理资源的释放。
                    # lines = f.readline()
                    line_number = 1
                    for line in f:
                        if pattern in line:
                            print(f"{file_path}:{line_number}: {line.strip()}")
# 代码 print(f"{file_path}:{line_number}: {line.strip()}") 是使用 f-string（格式化字符串）的打印语句，用于在控制台输出带有变量值的文本。
#
# 具体来说，这个代码将会输出带有文件路径、行号和去除首尾空白字符的行内容的文本。
#
# file_path 是文件路径的变量，表示文件的路径字符串。
# line_number 是行号的变量，表示文件中的行号。
# line.strip() 表示行内容去除首尾空白字符的结果。
                        line_number += 1
            except IOError:
                print(f"Error reading file: {file_path}")

def main():
    if len(sys.argv) < 2:
# 这个说明没有输入PATTERN 和 PATH

        print("Usage: python silversearcher.py PATTERN [PATH]")
        return

    pattern = sys.argv[1] # 因为第一个是运行的脚本的路径
    path = sys.argv[2] if len(sys.argv) > 2 else '.'
# 这里的意思是，如果 len(sys.argv) 大于 2（即命令行参数的数量大于 2），那么将 sys.argv[2] 的值赋给 path；否则，将 '.' （当前目录）赋给 path。
#
# 将条件放在赋值之后是因为这种语法结构是条件表达式的特定语法形式。条件表达式的一般形式是 x if condition else y，其中 x 是条件为真时的值，y 是条件为假时的值。
#
    search_files(pattern, path)
#
# 调用主函数
if __name__ == '__main__':
    main()










# import sys
#
# # 获取命令行参数
# arguments = sys.argv[1:]
#
# # 打印命令行参数
# print("命令行参数:")
# for arg in arguments:
#     print(arg)
#

# import os
#
# path = "/path/to/directory"
# print("read")
# for root, dirs, files in os.walk(path):
#     print("当前目录:", root)
#     print("子目录:", dirs)
#     print("文件:", files)
#     print()
#