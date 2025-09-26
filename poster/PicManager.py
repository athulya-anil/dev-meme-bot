# manages the list of pics and modifies them if needed
import os
from PIL import Image

class PicManager:
    def __init__(self, filepath):
        '''
        Constructor
        '''
        self.FILE = filepath
        self.picList = []
    
    def getList(self):
        """
        gets a list from the generated .txt file with the images.
        If it's empty, repopulate it from ../redditScraper/images.
        """
        with open(self.FILE, "r") as file:
            dataToList = file.read().splitlines()

        # If picList.txt is empty, rebuild it from the images folder
        if not dataToList:
            images_dir = "../redditScraper/images"
            dataToList = [
                f for f in os.listdir(images_dir) if f.lower().endswith(".jpg")
            ]
            with open(self.FILE, "w") as file:
                for pic in dataToList:
                    file.write(pic + "\n")
            print(f"🔄 picList.txt was empty, repopulated with {len(dataToList)} images")

        self.picList = dataToList
        return self.picList


    def getPics(self, num):
        '''
        gets the imageFilePath of num pics and removes them from the list
        '''
        # check if it's empty!!!
        i = 0
        retList = []
        while i < num:
            retList.append(self.picList.pop(0))
            print(i)
            i += 1
        return retList

    def rewriteFile(self):
        '''
        rewrites the file and removes image paths that have already been posted
        '''
        file = open(self.FILE, "w")
        for pic in self.picList:
            file.write(pic)
            file.write('\n')
        file.close()
    
    def resizePics(self, dir):
        thumbSize = 1080

        for pic in self.picList:
            # Ensure we only use the filename (no accidental paths)
            base = os.path.basename(pic)
            f = os.path.join(dir, base)

            if not os.path.isfile(f):
                print(f"⚠️ File not found: {f}")
                continue

            try:
                im = Image.open(f)
                im_thumb = self.expand2square(im, (255, 255, 255)).resize(
                    (thumbSize, thumbSize), Image.LANCZOS
                )
                im_thumb.save(f, quality=95)
                print(f"Resized: {f}")
            except Exception as e:
                print(f"Error resizing {f}: {e}")



        # for filename in os.listdir(dir):
        #     f = os.path.join(dir, filename)
        #     # checking if it is a file
        #     if os.path.isfile(f):
        #         print(f.path)
        #         im = Image.open(f)
        #         im_thumb = self.expand2square(im, (255, 255, 255)).resize((thumbSize, thumbSize), Image.LANCZOS)
        #         #im_thumb.save(filename, quality=95)

    def expand2square(self, pil_img, background_color):
        '''
        add padding to pil image, from https://note.nkmk.me/en/python-pillow-square-circle-thumbnail/
        '''
        width, height = pil_img.size

        if width == height:
            return pil_img
        elif width > height:
            result = Image.new(pil_img.mode, (width, width), background_color)
            result.paste(pil_img, (0, (width - height) // 2))
            return result
        else:
            result = Image.new(pil_img.mode, (height, height), background_color)
            result.paste(pil_img, ((height - width) // 2, 0))
            return result
                