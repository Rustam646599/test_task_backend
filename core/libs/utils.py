from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


def download_video(url) -> File:
    """ Скачивает изображения """

    img_temp = NamedTemporaryFile()
    img_temp.write(urlopen(url).read())
    img_temp.flush()
    return File(img_temp)


def get_timestamp_from_datatime(dt) -> int:
    """Возвращает дату/время в timestamp"""

    return int(dt.timestamp() * 1000)
