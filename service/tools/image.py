import io
import numpy as np
import PIL.Image


def load_image_from_bytes(fbytes: bytes, mode="RGB")->"numpy.array or None":
    """
    从bytes数据中导入图片，返回numpy数组
    """
    try:
        im = PIL.Image.open(io.BytesIO(fbytes))
        if mode:
            im = im.convert(mode)
        return np.array(im)
    except Exception as err:
        print(err)

    return None


def load_image_from_filepath(file_path, mode="RGB"):
    """
    从指定文件路径导入图片，返回numpy数组
    """
    im = PIL.Image.open(file_path)
    if mode:
        im = im.convert(mode)
    return np.array(im)


def load_image_from_request_file(req_file: "UploadedFile", mode="RGB")->"numpy.array or None":
    """
    从request.FILES中导入图片，返回numpy数组或None
    """
    fbytes = req_file.read()
    return load_image_from_bytes(fbytes)


