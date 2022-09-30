import pytest 
import sys 
sys.path.append("./")
import objectpic  

def test_Pic():
    pic = objectpic.Pic("groot","grootdun.jpg")
    encode = pic.get_img()
    # assert encode == b"d7\xf6\xf5\x1f\xf9\xfe\xdf\xd1\xfe\x7f\xb7\xf6\xff\x00\x9f\xed\xfd\xbf\xeb\xfb{\x0b\xfc\xff\x00m;_\xf9\xfe\xdf\xff\xd9"
