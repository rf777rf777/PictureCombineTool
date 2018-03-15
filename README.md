# PictureCombineTool - 照片、簽名檔合成工具
![image](https://github.com/rf777rf777/PictureCombineTool/blob/master/HomePicture.png)
## :pencil2: 概述

將簽名檔圖片與照片合成的 Terminal / Console 程式。

文章 : Medium - **[Python : 用 PIL 做影像處理(合成)](https://medium.com/@Syashin/python-%E7%85%A7%E7%89%87-%E7%B0%BD%E5%90%8D%E6%AA%94%E5%9C%96%E7%89%87%E5%90%88%E6%88%90%E5%B7%A5%E5%85%B7-e4df88f99994)**

## :closed_book: 特色
  + 使用 PIL - [Pillow](https://pypi.python.org/pypi/Pillow/5.0.0)，將已去背的簽名檔圖片與照片合成後輸出。
  + :file_folder: **Picture** : 放要進行合成的照片(可放多張)。
  + :file_folder: **SignPicture** : 放簽名檔圖片(只能放一張)。
  + :file_folder: **ResultPicture** : 結果輸出。
  + :file_folder: **Picture**、**SignPicture** 已放置範例圖片供嘗試。
  + :file_folder: **Picture**、**SignPicture** 僅接受 **'jpg'**、**'jpeg'**、**'png'**、**'gif'** 格式。
  + 本範例可在 Windows / macOS 環境下執行。
  

## :green_book: 套件安裝
1. 本程式執行的最佳環境為：[Python3.X](https://www.python.org/downloads/)，請確認自己的 Python 版本。
  
2. Clone / Download 這個專案：
    
        git clone https://github.com/rf777rf777/PictureCombineTool.git
3. 在 Terminal / Console(cmd) 輸入：
  
        pip install -r requirements.txt
    
   來安裝需要的 Packages。

## :blue_book: 使用方法
1. :file_folder: **Picture** 放入即將進行合成的照片或圖片，可放**多張**。
![image](https://upload.cc/i1/2018/03/15/ApzgBN.png)


2. :file_folder: **SignPicture** 放入即將進行合成的簽名檔圖片，只能放**一張**。
![image](https://upload.cc/i1/2018/03/15/TW5tzx.png)

3. 在 Terminal / Console(cmd) 輸入：

        python combine.py

4. :file_folder: **ResultPicture** 執行程式後結果輸出在此。
![image](https://upload.cc/i1/2018/03/15/ptkl7U.png)

5. 範例結果，其一：
![image](https://upload.cc/i1/2018/03/15/dwnqGz.jpg)

## :orange_book: 其它

應用程式版下載，內附說明，不需安裝Python即可使用：
  + macOS 版：https://nofile.io/f/baZKvwHRFCE
  + Windows 版：https://nofile.io/f/q9oVkrtYttB

## :books: Library or API Reference

[Pillow - ver5.0.0](https://pypi.python.org/pypi/Pillow/5.0.0).

## :memo: License
[MIT](https://zh.wikipedia.org/wiki/MIT%E8%A8%B1%E5%8F%AF%E8%AD%89)

