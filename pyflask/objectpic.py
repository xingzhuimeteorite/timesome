from base64 import b64encode
usrpath = "static"
class Pic:
    def __init__(self,dir,name):
        self.dir = dir
        self.name = name  

    def get_img(self):
        path = usrpath+"/{dir}/{name}".format(dir=self.dir,name=self.name)
        return get_img_stream(path)
    
 



def get_img_stream(path):
    '''
    依据路径返回图片流
    '''
    with open(path,"rb") as img:
        img_r = img.read()
        img_s = b64encode(img_r).decode()
    return img_s



