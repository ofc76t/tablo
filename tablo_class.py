# -*- coding: utf-8 -*-


class Style:
    style_date = ' style="font-size:70%;"'
    style_time_from = ' style="font-size:200%;"'
    style_time_to = ' style="font-size:200%;"'
    style_point_from = ' style="font-size:135%;"'
    style_point_to = ' style="font-size:145%;"'
    style_hrn = ' style="font-size:130%;"'
    style_atp = ' style="font-size:105%;"'
    style_bus = ' style="font-size:115%;"'
    style_status = ' style="font-size:125%;"'
    style_free_place = ' style="font-size:195%;"'


class Route:
    routeDate = ''          # дата рейса
    routeNum = ''           # номер рейса
    routeBgn = ''           # начальный пункт
    routeEnd = ''           # конечный пункт
    routeTimeFrom = ''      # фактическое время отправления
    routeTimeTo = ''        # фактическое время прибытия
    routeTimeFromPlan = ''  # плановое время отправления
    routeTimeToPlan = ''    # плановое время прибытия в конечный
    atp = ''                # АТП
    platform = ''           # платформа
    date = ''               # дата
    price = ''              # цена до конечной станции
    freeAll = ''            # свободно мест
    group = []              # группа рейса
    bus = ''                # марка автобуса
    status = '++'           # статус ведомости
    busy = ''               # билетов продано
    timeArrivalFact = ''    # время прибытия фактическое
    busnum = ''             # гос.номер автобуса

statusRange = {'РО': 0, 'РС': 0, '--': 1, '++': 4, 'БЛ': 0, '00': 3, 'ПЛ': 2}

statusText = {'РО': 'Вiдправлено',
              'РС': 'Вiдмiнено',
              '--': 'По прибуттю',
              '++': 'В продажi',
              'БЛ': 'Затримка',
              '00': 'Кв. проданi',
              'ПЛ': '<font size=-1>На платформi</font>'}

stringColor = ('"#0d1681"', '"#1728e6"', '"#011f01"')
# stringColor[2] - цвет заголовка секции

bgColor = {'РО': '#cfcfcf',
           'РС': '#ff0f0f',
           '++': '#5fafaf',
           '--': '#0f1f0f',
           'БЛ': '#5f5f5f',
           '00': '#800f0f',
           'ПЛ': '#07aacb'
           }

frontColor = {'РО': '#ff0000',
              'РС': '#ffffff',
              '--': '#0fff0f',
              '++': '#ffffff',
              'БЛ': '#ffffff',
              '00': '#FfFf00',
              'ПЛ': '#9f0000',
              }
