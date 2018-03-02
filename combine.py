from PIL import Image
import os
import sys

def blendPicture(pictureData,signData,resultFloder):
    print("\r=== 照片合成進行中 ===\n")

    #signData解構
    signFloder,signName = list(signData.keys())[0] , list(signData.values())[0]
    #sign圖片開啟並轉成RGBA格式
    imageB = Image.open('{0}/{1}'.format(signFloder,signName))
    imageB = imageB.convert('RGBA')
    
    #pictureData解構
    pictureFloder,pictureNameList = list(pictureData.keys())[0], list(pictureData.values())[0]
    
    #完成度參數
    complete = 0
    
    #照片開啟並轉成RGBA格式
    for image in pictureNameList:   

        imageA = Image.open('{0}/{1}'.format(pictureFloder,image))
        imageA = imageA.convert('RGBA')
        widthA , heightA = imageA.size
        
        #調整簽名檔圖片大小
        imageB_edit = resizePicture(imageA,imageB) 
        widthB , heightB = imageB_edit.size

        #建立一張新的透明圖片當底圖
        resultPicture = Image.new('RGBA', imageA.size, (0, 0, 0, 0))
        
        #把照片貼上去
        resultPicture.paste(imageA,(0,0))
        
        #照片右下角位置參數
        right_bottom = (widthA - widthB , heightA - heightB)
        
        #把簽名檔貼在照片右下角
        resultPicture.paste(imageB_edit , right_bottom , imageB_edit)
        
        #把圖片再轉成RGB好存成jpg
        resultPicture = resultPicture.convert('RGB')

        #儲存新照片
        resultPicture.save("{0}/{1}_{2}.jpg".format(resultFloder,image.split('.')[0],signName.split('.')[0]))
        
        #完成度顯示
        complete += 1
        sys.stdout.write("\r已完成 : ( %s / %s )" % (complete,len(pictureNameList)))
        sys.stdout.flush()

    print("\n\n\r=== 照片合成已完成 ===")

#調整圖片大小
def resizePicture(backImage , image):
    width_bg,height_bg = backImage.size
    width , height = image.size

    #簽名檔的寬度永遠為照片的 1/2
    newWidth = width_bg/2
    #簽名檔的高度依據新的寬度等比例縮放
    newHeight = height/width*newWidth
    image = image.resize((int(newWidth),int(newHeight)))

    return image

def main(pictureFloder = 'Picture', signFloder = 'SignPicture', resultFloder = 'ResultPicture'):
    #if執行exe檔
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        #print('系統名稱:'+os.name)
        if os.name == 'nt':
            symbol = "\\"
        else :
            symbol = "/"

        pictureFloder_path = application_path.rpartition(symbol)[0]+'/{0}'.format(pictureFloder)
        signFloder_path = application_path.rpartition(symbol)[0]+'/{0}'.format(signFloder)
        resultFloder_path = application_path.rpartition(symbol)[0]+'/{0}'.format(resultFloder)
    #if直接執行.py檔
    elif __file__:
        pictureFloder_path = pictureFloder 
        signFloder_path = signFloder
        resultFloder_path = resultFloder

    #接受的圖片格式
    acceptFormat = ('jpg','jpeg','png','gif')

    pictureList = []
    signList = []
    
    #檢查資料夾是否存在
    if not os.path.isdir(pictureFloder_path) or not os.path.isdir(signFloder_path) or not os.path.isdir(resultFloder_path):
        print("'{0}'\n'{1}'\n'{2}'\n 以上三個'資料夾'必須存在,若被移除請自行建立".format(pictureFloder_path,signFloder_path,resultFloder_path))
        return

    #巡覽照片資料夾
    for picture in os.listdir(pictureFloder_path):
        if picture.endswith(acceptFormat):
            pictureList.append(picture)
    
    #巡覽簽名檔案資料夾
    for sign in os.listdir(signFloder_path):
        if sign.endswith(acceptFormat):
            signList.append(sign)

    #找不到照片與簽名檔
    if len(pictureList) == 0 or len(signList) == 0:
        print("\r找不到要進行混合的圖片,'{0}'或'{1}'資料夾為空".format(pictureFloder_path,signFloder_path))
        return

    #簽名檔超過一張
    if len(signList) > 1:
        print("\r'{0}'內只允許一張圖片".format(signFloder_path))
        return

    pictureData = { pictureFloder_path : pictureList }
    signData = { signFloder_path : signList[0] }

    blendPicture(pictureData,signData,resultFloder_path)
    
main()

if os.name == 'nt':
    input("\n<<< 按 Enter 鍵結束 >>>")