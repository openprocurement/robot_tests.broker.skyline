# -*- coding: utf-8 -*-
import dateutil.parser
from datetime import datetime
from pytz import timezone
import os
import urllib

def skyline_convertdate(isodate):
    date = dateutil.parser.parse(isodate)
    return date.strftime("%Y-%m-%d %H:%M")

def add_timezone_to_date(date_str):
    new_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    TZ = timezone(os.environ['TZ'] if 'TZ' in os.environ else 'Europe/Kiev')
    new_date_timezone = TZ.localize(new_date)
    return new_date_timezone.strftime("%Y-%m-%d %H:%M:%S%z")

def convert_skyline_date_to_iso_format(date_time_from_ui):
    new_timedata = datetime.strptime(date_time_from_ui, '%d-%m-%Y\n%H:%M')
    new_date_time_string = new_timedata.strftime("%Y-%m-%d %H:%M:%S.%f")
    return new_date_time_string

def convert_skyline_date_to_iso_format_with_tz(date_time_from_ui):
    new_timedata = datetime.strptime(date_time_from_ui, '%d-%m-%Y\n%H:%M')
    new_date_time_string = new_timedata.strftime("%Y-%m-%d %H:%M:%S.%f")
    return add_timezone_to_contact_date(new_date_time_string)


def convert_contract_date_to_iso(date_time_from_ui, i):
    res=date_time_from_ui.split(' - ')
    res=res[i]
    new_timedata = datetime.strptime(res, '%Y-%m-%d %H:%M')
    new_date_time_string = new_timedata.strftime("%Y-%m-%dT%H:%M:%S.%f")
    return new_date_time_string

def add_timezone_to_contact_date(date_str):
    timezone="+03:00"
    return date_str+timezone

def skyline_download_file(url, file_name, output_dir):
    urllib.urlretrieve(url, ('{}/{}'.format(output_dir, file_name)))

def convert_skyline_string(string):
    data = {
            'True':                                                   '1',
            'False':                                                  '0',
            u"Так":                                                   True,
            u"Hi":                                                    False,
            u'Очікування пропозицій':                                 'active.tendering',
            u'Період аукціону':                                       'active.auction',
            u'Кваліфікація переможця':                                'active.qualification',
            u'Пропозиції розглянуто':                                 'active.awarded',
            u'Аукціон не відбувся':                                   'unsuccessful',
            u'Аукціон завершено':                                     'complete',
            u'Аукціон відмінено':                                     'cancelled',
            u'Чорновик':                                              'draft',
            u'Майна банків':                                          'dgfOtherAssets',
            u'Прав вимоги за кредитами':                              'dgfFinancialAssets',
            u'Вперше':                                                1,
            u'Вдруге':                                                2,
            u'Втретє':                                                3,
            u'Вчетверте':                                             4,
            u'Грн.':                                                  'UAH',
            u'(включно з ПДВ)':                                       True,
            u'(без ПДВ)':                                             False,
            u'[переможець розглядається кваліфікаційною комісією]':   'pending',
            u'[Oчікування кінця кваліфікації переможця]':             'pending.waiting',
            u'[Учасник достроково забрав гарантійний внесок]':        'cancelled',
            u'[Очікується протокол]':                                 'pending.verification',
            u'[Очікується оплата]':                                   'pending.payment',
            u'[Оплачено, очікується підписання договору]':            'active',
            u'[Кваліфікаційна комісія відмовила переможцю]':          'unsuccessful',
            u'Опубліковано. Очікування інформаційного повідомлення.': 'pending',
            u'Виключено з переліку':                                  'deleted',
            u'Реєстрацію завершено':                                  'complete',
            u'Повідомлення не валідне':                               'pending.deleted',
            u'Аукціон заплановано':                                   'scheduled',
            u'Мала приватизація':                                     'sellout.english',
            u'[Очікування рішення про викуп]':                        'pending.admission',
            }
    return data.get(string, string)

def convert_skyline_lot_string(string):
    data = {
            u'Опубліковано':                     'pending',
            u'Аукціон в стадії проведення':      'active',
            u'Аукціон заплановано':              'scheduled',
            u'Реєстрацію завершено':             'complete',
            u'Перевірка коректності оголошення': 'verification',
            u'Об’єкт виключено':                 'deleted',
            u'Аукціон':                          'active.auction',
            }
    return data.get(string, string)

def convert_skyline_lot_auction_string(string):
    data = {
            u'Аукціон':                                                                                         'sellout.english',
            u'Аукціон із зниженням стартової ціни':                                                             'sellout.english',
            u'Аукціон за методом покрокового зниження стартової ціни та подальшого подання цінових пропозицій': 'sellout.insider',
            }
    return data.get(string, string)




