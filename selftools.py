"""
自编写函数库
"""
from PyQt5.QtGui import QPixmap
import hashlib
import random
import base64
import cv2
import os


# 将图片bytes转成pixmap
def img2pixmap(bytes_img):
    img_data = base64.b64decode(bytes_img)  # 解码
    pixmap_data = QPixmap()  # 新建QPixmap对象
    pixmap_data.loadFromData(img_data)  # 往QPixmap中写入数据
    return pixmap_data


# 生成随机颜色（十六进制）
def random_color():
    """
    生成随机颜色（十六进制）
    :return: 十六进制色码
    """
    colors1 = '0123456789ABCDEF'
    num = "#"
    for i in range(6):
        num += random.choice(colors1)
    return num


# 获取指定文件/文件夹的大小
def get_size(f_path):
    """
    获取指定文件/文件夹的大小
    :param f_path: 文件/文件夹路径
    :return: 文件/文件夹大小，自动换算大小单位
    """
    totalSize = 0
    if not os.path.exists(f_path):  # 路径不存在返回0
        return totalSize
    if os.path.isfile(f_path):   # 路径为文件直接计算大小
        totalSize = os.path.getsize(f_path)
    elif os.path.isdir(f_path):  # 路径为文件夹计算文件夹内所有文件大小之和
        for root, dirs, files in os.walk(f_path):
            totalSize += sum([os.path.getsize(os.path.join(root, name)) for name in files])

    if totalSize/1024 < 1024:
        res = str(round(totalSize/1024, 2)) + " KB"
    elif totalSize/1024/1024 < 1024:
        res = str(round(totalSize/1024/1024, 2)) + " MB"
    else:
        res = str(round(totalSize/1024/1024/1024, 2)) + " GB"
    return res


# 计算文件哈希值
def get_md5(f_path):
    """
    计算文件哈希值
    :param f_path: 文件路径
    :return: 该文件哈希值
    """
    with open(f_path, 'rb') as f:   # 必须是'rb'模式打开
        md5obj = hashlib.md5()  # 创建一个md5算法对象
        md5obj.update(f.read())     # 更新文件对象
        md5 = md5obj.hexdigest()    # 获取这个文件的MD5值
    return md5


# 获取文件名称（不包含后缀名
def get_basename(f_path):
    """
    获取文件名称（不包含后缀名
    :param f_path: 文件完整路径
    :return: 文件名称和后缀名的元组（不含路径）
    """
    # basename = os.path.splitext(os.path.split(f_path)[1])
    basename = os.path.splitext(os.path.basename(f_path))
    return basename


# 获取指定目录下指定后缀文件列表(可选是否搜索子目录)
def get_spec_path(lib_path, suffix=None, walk=False):
    """
    获取指定目录下指定后缀文件列表(可选是否搜索子目录)
    :param lib_path: 目录路径
    :param suffix: 后缀名，可以有多个，默认为None:获取所有文件
    :param walk: 是否搜索子目录，默认False
    :return: 所有该后缀名的路径列表
    """
    f_list = []
    if walk:
        for root, dirs, files in os.walk(lib_path):
            for file_name in files:
                if suffix:
                    # if file_name.split(".")[-1].lower() in suffix:
                    if os.path.splitext(file_name)[1].lower() in suffix:
                        f_list.append(os.path.join(root, file_name))
                else:
                    f_list.append(os.path.join(root, file_name))
    else:
        for si_path in os.listdir(lib_path):
            full_path = os.path.join(lib_path, si_path)
            if os.path.isfile(full_path):
                if suffix:
                    if os.path.splitext(si_path)[1].lower() in suffix:
                        f_list.append(full_path)
                else:
                    f_list.append(full_path)
    return f_list


# 获取指定目录下所有文件夹的完整路径列表(不包含子目录
def get_dirs_list(lib_path):
    """
    获取指定目录下所有文件夹的完整路径列表(不包含子目录
    :param lib_path: 目录路径
    :return: 所有文件夹的路径列表
    """
    di_list = []
    for si in os.listdir(lib_path):
        if os.path.isdir(os.path.join(lib_path, si)):
            root_si = os.path.join(lib_path, si)
            di_list.append(root_si)
    return di_list


# 图片自适应二值化
def auto_binary(im, show=False):
    """
    图片自适应二值化
    :param im: ndarray格式的灰度图片文件
    :param show: 是否显示二值化后的图，默认False
    :return: ndarray格式的图片文件
    """
    # 高斯模糊平滑处理，(blur, blur)表示高斯矩阵的长与宽，标准差取0
    im = cv2.GaussianBlur(im, (3, 3), 0)
    # 获取自适应的阈值
    thres, _ = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 使用自适应的阈值进行二值化
    _, bina = cv2.threshold(im, thres, 255, cv2.THRESH_BINARY)
    # 简易判断图片是否需要反色
    y, x = bina.shape
    center = bina[int(y*1/5):int(y*4/5), int(x*1/5):int(x*4/5)]  # 裁剪坐标为[y0:y1, x0:x1]
    out_bla = len(bina[bina == 0]) - len(center[center == 0])   # 计算黑色像素
    out_whi = len(bina[bina == 255]) - len(center[center == 255])   # 计算白色像素
    # 如果外框黑色像素数大于白色像素，则执行反色操作
    if out_bla > out_whi:
        bina = 255 - bina
    # 是否显示预览
    if show is True:
        cv2.imshow("binary_img", bina)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return bina


# 批量多次重命名
def mul_rename(lib_path, relatuples, suffix=None):
    """
    批量多次重命名
    :param lib_path: 需要重命名的文件所在文件夹
    :param relatuples: 重命名规则，如("替换前", "替换后")
    :param suffix: 默认None，可指定后缀名进行文件筛选，元组形式
    :return: 成功匹配的次数
    """
    count = 0
    f_list = get_spec_path(lib_path, suffix)
    fNames = [os.path.basename(x) for x in f_list]
    for name in fNames:
        old = os.path.join(lib_path, name)
        for relation in relatuples:
            name = name.replace(relation[0], relation[1])
        new = os.path.join(lib_path, name)
        if old != new:
            os.rename(old, new)
            count += 1
    return count


# 弃用函数——————————————————————————————————————————

# 现被get_spec_path()替换
def get_fonts_path(lib_path):
    """
    获取指定目录下字体文件路径列表(包含子目录
    :param lib_path: 字体文件夹路径
    :return: 所有字体文件路径名列表
    """
    f_list = []
    for root, dirs, files in os.walk(lib_path):
        for file_name in files:
            if os.path.splitext(file_name)[1].lower() in (".ttf", ".otf"):
                f_path = os.path.join(root, file_name)
                f_list.append(f_path)
    return f_list


# 现被get_spec_path()替换
def get_imgs_path(lib_path):
    """
    获取指定目录下所有图片文件的列表(包含子目录
    :param lib_path: 图片文件夹路径
    :return: 所有图片文件路径名列表
    """
    im_list = []
    for root, dirs, files in os.walk(lib_path):
        for file_name in files:
            if os.path.splitext(file_name)[1].lower() in (".png", ".jpg", ".jpeg"):
                f_path = os.path.join(root, file_name)
                im_list.append(f_path)
    return im_list


# 现被get_size()替换
def get_file_size(f_path):
    """
    获取指定文件的大小（MB）
    :param f_path: 文件路径
    :return: 文件大小
    """
    size = os.path.getsize(f_path) / float(1024 * 1024)
    res = str(round(size, 2)) + " MB"
    return res
