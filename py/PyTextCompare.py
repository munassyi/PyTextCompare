import os
import sys
from typing import List

##------------------------------------------------------------------------------
##
##------------------------------------------------------------------------------
def main():
    if len(sys.argv) < 3:
        print("!!! 2 ファイル D&D してください !!!")
        input("Enter で終了…")
        return

    path1 = sys.argv[1]
    path2 = sys.argv[2]

    print("//------------------------------------------------------------------------------")
    print("// ファイルを比較します")
    print("//   File1 : " + path1)
    print("//   File2 : " + path2)
    print("//------------------------------------------------------------------------------")

    File1Data = ReadData(path1)
    File2Data = ReadData(path2)

    print(path1 + " にしかない要素")
    PrintSetDifference(File1Data, File2Data)

    print()

    print(path2 + " にしかない要素")
    PrintSetDifference(File2Data, File1Data)

    print()

    input("Enter で終了…")

##------------------------------------------------------------------------------
## ファイル読み込み
##------------------------------------------------------------------------------
def ReadData(FilePath):
    if os.path.exists(FilePath):
        with open(FilePath, 'r') as fileData:
            fileData = list(dict.fromkeys(fileData.read().splitlines()))

            # 念の為空白削除して返す
            return list(filter(None, fileData))

##------------------------------------------------------------------------------
## 差集合の表示
##------------------------------------------------------------------------------
def PrintSetDifference(File1Data : List[str], File2Data : List[str]):
    result = set(File1Data) - set(File2Data)
    for line in sorted(result):
        print(line)

##------------------------------------------------------------------------------
##
##------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

# EOF