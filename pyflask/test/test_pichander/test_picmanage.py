from pichander import picmanage
picpath = "static/groot/grootdun.jpg"


def test_resize():
    size = 300
    img = picmanage.Picture(picpath).getcvimg()
    new_img = picmanage.resizePic(img, size)
    assert new_img.shape[0] <= size
