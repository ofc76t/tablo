# -*- coding: utf-8 -*-


SHOW_FREE_SPACE = 0 #  показывать кол-во свободных мест ( 1 - показывать, 0 - не показывать)
PEFRESH_TABLO = 30 #  пауза до следующего запроса браузера к серверу
PEFRESH_PROMO = 10 #  пауза до следующего запроса браузера при показе рекламы
DEFAULT_IP = '192.168.1.96' #  
SPEED_SCROLL = 5 #  пауза милисек скрола (не меньше 1)
SPEED_JUMP_SCROLL = 1200 #  пауза милисек "прыгающего" скрола (не меньше 1)
SCROLL_HEIGHT = 46552 #  длина прокрутки
SCROLL_MODE = 1 #  режим прокрутки  0 - без прокрутки,  1 - "плавный", 2 - "прыгающий" на высоту строки таблицы
SCREEN_STR_LIMIT = 7 #  
SCHEDULE_FILE = 'schedule.tbl' #  
OUTPUT_FILE = 'result.html' #  
SECRET_KEY = b'ofc076_secret%key' #  
WORK_DIR = 'D:/' #  
PROMO_AFTER = 2 #  после скольких показов расписания показать рекламу
ON_PLATFORM = 15 #  время в минутах до отправления, когда автобус считается на платформе
PROMO_HTML_DIR = 'D:/tablo_html/' #  
PROMO_VIDEO_DIR = 'D:/tablo_video/' #  
PROMO_IMAGE_DIR = 'D:/tablo_image/' #  
PROMO_HTML_CSS_DIR = 'D:/tablo_html/css/' #  
PROMO_HTML_IMG_DIR = 'D:/tablo_html/img/' #  
PROMO_HTML_JS_DIR = 'D:/tablo_html/js/' #  
SCHEDULE_FROM_FILE = 1 #  читать расписание из файла. 1 - из файла, 0 - через сокет
IGNORE_GROUPS = () #  рейсы этих групп не выводятся на табло
BUS_NUMBER = 1 #  0 - показывать время прибытия из ДЖ, 1 - показывать гос.номер автобуса
BUY_IN_BUS_GROUP = () #  для этих групп рейсов писать "Билеты в автобусе".                    TODO
SCHEDULE_SERVER = '192.168.1.98' #  
SCHEDULE_SERVER_PORT = 1204 #  
SUPPORTED_HTML = ('html', 'shtml') #  
SUPPORTED_VIDEO = ('avi', 'mp4') #  
SUPPORTED_IMAGE = ('jpg', 'jpeg', 'bmp', 'png') #  
USER_AVAILABLE_PARAM = ('SHOW_FREE_SPACE', 'PEFRESH_TABLO', 'PEFRESH_PROMO', 'SPEED_SCROLL', 'SPEED_JUMP_SCROLL', 'SCROLL_HEIGHT', 'SCROLL_MODE', 'SCREEN_STR_LIMIT', 'SCREEN_STR_LIMIT', 'PROMO_AFTER', 'ON_PLATFORM', 'SCHEDULE_FROM_FILE', 'IGNORE_GROUPS', 'BUS_NUMBER', 'BUY_IN_BUS_GROUP') #  
SHOW_PROMO_VIDEO = 0 #  показывать рекламное видео
SHOW_PROMO_IMAGE = 1 #  показывать рекламные постеры (изображения)
PROMO_IMAGE_ALIAS = 'D:/tablo_image/' #  алиас вебсервера (apache) для папки с изображениями
PROMO_VIDEO_ALIAS = 'D:/tablo_video/' #  алиас вебсервера (apache) для папки с видео
