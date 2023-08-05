# -*- coding: utf-8 -*-
# ===================================================================
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# ===================================================================
class ProviderData(object):
    JSON_CONFIG = {
        "showRowNumber": False,
        "autoSizeColumns": False,
        "config": {
            "filters": [],
            "groups": [
                {
                    "name": "catname",
                    "label": "catname",
                    "sort": {
                        "name": "commission",
                        "func": "sum",
                        "dir": "desc"
                    },
                    "limit": 10
                }
            ],
            "metrics": [
                {
                    "name": "pricepaid",
                    "func": "sum"
                }
            ],
            "fields": [],
            "exclude": []
        },
        "columns": [],
        "rows": [],
        "limit": 8,
        "offset": 0,
        "visualization": "Bars"
    }

    # region Result objects
    TS_COUNT_QUERY_RESULT = {'group': [], 'current': {'count': 172456}}
    TS_RAW_QUERY_LIMIT_RESULT = {
        'data': [
            {'rn': 1,
             'salesid': 1,
             'listid': 1,
             'sellerid': 36861,
             'buyerid': 21191,
             'eventid': 7872,
             'dateid': 1875,
             'qtysold': 4,
             'pricepaid': 728,
             'commission': 109.2,
             'saletime': '2008-02-18 02:36:00',
             'eventid.1': 7872,
             'venueid': 128,
             'catid': 9,
             'dateid.1': 1878,
             'eventname': 'Shakira',
             'starttime': '2008-02-21 15:00:00',
             'catid.1': 9,
             'catgroup': 'Concerts',
             'catname': 'Pop',
             'catdesc': 'All rock and pop music concerts',
             'venueid.1': 128.0,
             'venuename': 'E.J. Nutter Center',
             'venuecity': 'Dayton',
             'venuestate': 'OH',
             'venueseats': 0.0,
             'userid': 36861,
             'username': 'EAU72JIH',
             'firstname': 'Moses',
             'lastname': 'Arnold',
             'city': 'Geneva',
             'state': 'WI',
             'email': 'Donec.consectetuer.mauris@nunc.org',
             'phone': '(386) 197-7444',
             'likesports': None,
             'liketheatre': False,
             'likeconcerts': None,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': False,
             'likerock': True,
             'likevegas': None,
             'likebroadway': None,
             'likemusicals': None,
             'saletime_utc': '2008-02-18 02:36:00UTC',
             'saletime_min_7': '2008-02-18 02:36:00-0700',
             'saletime_plus_8': '2008-02-18 02:36:00-0800'},
            {'rn': 2,
             'salesid': 2,
             'listid': 4,
             'sellerid': 8117,
             'buyerid': 11498,
             'eventid': 4337,
             'dateid': 1983,
             'qtysold': 2,
             'pricepaid': 76,
             'commission': 11.4,
             'saletime': '2008-06-06 05:00:00',
             'eventid.1': 4337,
             'venueid': 40,
             'catid': 9,
             'dateid.1': 1994,
             'eventname': 'Kenny Wayne Shepherd',
             'starttime': '2008-06-17 15:00:00',
             'catid.1': 9,
             'catgroup': 'Concerts',
             'catname': 'Pop',
             'catdesc': 'All rock and pop music concerts',
             'venueid.1': 40.0,
             'venuename': 'American Airlines Center',
             'venuecity': 'Dallas',
             'venuestate': 'TX',
             'venueseats': 0.0,
             'userid': 8117,
             'username': 'JZQ67XSU',
             'firstname': 'Ignacia',
             'lastname': 'Buck',
             'city': 'Temple City',
             'state': 'ON',
             'email': 'mauris@enim.ca',
             'phone': '(427) 378-5329',
             'likesports': None,
             'liketheatre': False,
             'likeconcerts': True,
             'likejazz': None,
             'likeclassical': None,
             'likeopera': False,
             'likerock': None,
             'likevegas': None,
             'likebroadway': None,
             'likemusicals': None,
             'saletime_utc': '2008-06-06 05:00:00UTC',
             'saletime_min_7': '2008-06-06 05:00:00-0700',
             'saletime_plus_8': '2008-06-06 05:00:00-0800'},
            {'rn': 3,
             'salesid': 3,
             'listid': 5,
             'sellerid': 1616,
             'buyerid': 17433,
             'eventid': 8647,
             'dateid': 1983,
             'qtysold': 2,
             'pricepaid': 350,
             'commission': 52.5,
             'saletime': '2008-06-06 08:26:00',
             'eventid.1': 8647,
             'venueid': 66,
             'catid': 9,
             'dateid.1': 2000,
             'eventname': 'Good Charlotte',
             'starttime': '2008-06-23 15:00:00',
             'catid.1': 9,
             'catgroup': 'Concerts',
             'catname': 'Pop',
             'catdesc': 'All rock and pop music concerts',
             'venueid.1': 66.0,
             'venuename': 'HP Pavilion at San Jose',
             'venuecity': 'San Jose',
             'venuestate': 'CA',
             'venueseats': 0.0,
             'userid': 1616,
             'username': 'QVZ22CRT',
             'firstname': 'Drake',
             'lastname': 'Short',
             'city': 'Kettering',
             'state': 'IA',
             'email': 'erat@quama.com',
             'phone': '(880) 881-1907',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': None,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': False,
             'likerock': False,
             'likevegas': None,
             'likebroadway': None,
             'likemusicals': None,
             'saletime_utc': '2008-06-06 08:26:00UTC',
             'saletime_min_7': '2008-06-06 08:26:00-0700',
             'saletime_plus_8': '2008-06-06 08:26:00-0800'},
            {'rn': 4,
             'salesid': 4,
             'listid': 5,
             'sellerid': 1616,
             'buyerid': 19715,
             'eventid': 8647,
             'dateid': 1986,
             'qtysold': 1,
             'pricepaid': 175,
             'commission': 26.25,
             'saletime': '2008-06-09 08:38:00',
             'eventid.1': 8647,
             'venueid': 66,
             'catid': 9,
             'dateid.1': 2000,
             'eventname': 'Good Charlotte',
             'starttime': '2008-06-23 15:00:00',
             'catid.1': 9,
             'catgroup': 'Concerts',
             'catname': 'Pop',
             'catdesc': 'All rock and pop music concerts',
             'venueid.1': 66.0,
             'venuename': 'HP Pavilion at San Jose',
             'venuecity': 'San Jose',
             'venuestate': 'CA',
             'venueseats': 0.0,
             'userid': 1616,
             'username': 'QVZ22CRT',
             'firstname': 'Drake',
             'lastname': 'Short',
             'city': 'Kettering',
             'state': 'IA',
             'email': 'erat@quama.com',
             'phone': '(880) 881-1907',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': None,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': False,
             'likerock': False,
             'likevegas': None,
             'likebroadway': None,
             'likemusicals': None,
             'saletime_utc': '2008-06-09 08:38:00UTC',
             'saletime_min_7': '2008-06-09 08:38:00-0700',
             'saletime_plus_8': '2008-06-09 08:38:00-0800'},
            {'rn': 5,
             'salesid': 5,
             'listid': 6,
             'sellerid': 47402,
             'buyerid': 14115,
             'eventid': 8240,
             'dateid': 2069,
             'qtysold': 2,
             'pricepaid': 154,
             'commission': 23.1,
             'saletime': '2008-08-31 09:17:00',
             'eventid.1': 8240,
             'venueid': 51,
             'catid': 9,
             'dateid.1': 2081,
             'eventname': 'The Who',
             'starttime': '2008-09-12 19:00:00',
             'catid.1': 9,
             'catgroup': 'Concerts',
             'catname': 'Pop',
             'catdesc': 'All rock and pop music concerts',
             'venueid.1': None,
             'venuename': None,
             'venuecity': None,
             'venuestate': None,
             'venueseats': None,
             'userid': 47402,
             'username': 'YHB76KXJ',
             'firstname': 'Petra',
             'lastname': 'Avila',
             'city': 'Louisville',
             'state': 'YT',
             'email': 'fermentum@sem.edu',
             'phone': '(633) 983-9015',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': None,
             'likejazz': False,
             'likeclassical': None,
             'likeopera': None,
             'likerock': None,
             'likevegas': None,
             'likebroadway': None,
             'likemusicals': None,
             'saletime_utc': '2008-08-31 09:17:00UTC',
             'saletime_min_7': '2008-08-31 09:17:00-0700',
             'saletime_plus_8': '2008-08-31 09:17:00-0800'},
            {'rn': 6,
             'salesid': 6,
             'listid': 10,
             'sellerid': 24858,
             'buyerid': 24888,
             'eventid': 3375,
             'dateid': 2023,
             'qtysold': 2,
             'pricepaid': 394,
             'commission': 59.1,
             'saletime': '2008-07-16 11:59:00',
             'eventid.1': 3375,
             'venueid': 220,
             'catid': 7,
             'dateid.1': 2031,
             'eventname': 'Uncle Vanya',
             'starttime': '2008-07-24 19:00:00',
             'catid.1': 7,
             'catgroup': 'Shows',
             'catname': 'Plays',
             'catdesc': 'All non-musical theatre',
             'venueid.1': 220.0,
             'venuename': 'Lunt-Fontanne Theatre',
             'venuecity': 'New York City',
             'venuestate': 'NY',
             'venueseats': 0.0,
             'userid': 24858,
             'username': 'YFF20OCX',
             'firstname': 'Kalia',
             'lastname': 'Rush',
             'city': 'Lakewood',
             'state': 'DC',
             'email': 'lorem.eu@eutempor.edu',
             'phone': '(396) 106-3294',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': False,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': True,
             'likerock': None,
             'likevegas': True,
             'likebroadway': False,
             'likemusicals': True,
             'saletime_utc': '2008-07-16 11:59:00UTC',
             'saletime_min_7': '2008-07-16 11:59:00-0700',
             'saletime_plus_8': '2008-07-16 11:59:00-0800'},
            {'rn': 7,
             'salesid': 7,
             'listid': 10,
             'sellerid': 24858,
             'buyerid': 7952,
             'eventid': 3375,
             'dateid': 2003,
             'qtysold': 4,
             'pricepaid': 788,
             'commission': 118.2,
             'saletime': '2008-06-26 12:56:00',
             'eventid.1': 3375,
             'venueid': 220,
             'catid': 7,
             'dateid.1': 2031,
             'eventname': 'Uncle Vanya',
             'starttime': '2008-07-24 19:00:00',
             'catid.1': 7,
             'catgroup': 'Shows',
             'catname': 'Plays',
             'catdesc': 'All non-musical theatre',
             'venueid.1': 220.0,
             'venuename': 'Lunt-Fontanne Theatre',
             'venuecity': 'New York City',
             'venuestate': 'NY',
             'venueseats': 0.0,
             'userid': 24858,
             'username': 'YFF20OCX',
             'firstname': 'Kalia',
             'lastname': 'Rush',
             'city': 'Lakewood',
             'state': 'DC',
             'email': 'lorem.eu@eutempor.edu',
             'phone': '(396) 106-3294',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': False,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': True,
             'likerock': None,
             'likevegas': True,
             'likebroadway': False,
             'likemusicals': True,
             'saletime_utc': '2008-06-26 12:56:00UTC',
             'saletime_min_7': '2008-06-26 12:56:00-0700',
             'saletime_plus_8': '2008-06-26 12:56:00-0800'},
            {'rn': 8,
             'salesid': 8,
             'listid': 10,
             'sellerid': 24858,
             'buyerid': 19715,
             'eventid': 3375,
             'dateid': 2017,
             'qtysold': 1,
             'pricepaid': 197,
             'commission': 29.55,
             'saletime': '2008-07-10 02:12:00',
             'eventid.1': 3375,
             'venueid': 220,
             'catid': 7,
             'dateid.1': 2031,
             'eventname': 'Uncle Vanya',
             'starttime': '2008-07-24 19:00:00',
             'catid.1': 7,
             'catgroup': 'Shows',
             'catname': 'Plays',
             'catdesc': 'All non-musical theatre',
             'venueid.1': 220.0,
             'venuename': 'Lunt-Fontanne Theatre',
             'venuecity': 'New York City',
             'venuestate': 'NY',
             'venueseats': 0.0,
             'userid': 24858,
             'username': 'YFF20OCX',
             'firstname': 'Kalia',
             'lastname': 'Rush',
             'city': 'Lakewood',
             'state': 'DC',
             'email': 'lorem.eu@eutempor.edu',
             'phone': '(396) 106-3294',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': False,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': True,
             'likerock': None,
             'likevegas': True,
             'likebroadway': False,
             'likemusicals': True,
             'saletime_utc': '2008-07-10 02:12:00UTC',
             'saletime_min_7': '2008-07-10 02:12:00-0700',
             'saletime_plus_8': '2008-07-10 02:12:00-0800'
             }
        ]
    }
    TS_RAW_QUERY_OFFSET_RESULT = {
        'data': [
            {
                'rn': 1,
                'salesid': 5,
                'listid': 6,
                'sellerid': 47402,
                'buyerid': 14115,
                'eventid': 8240,
                'dateid': 2069,
                'qtysold': 2,
                'pricepaid': 154,
                'commission': 23.1,
                'saletime': '2008-08-31 09:17:00',
                'eventid.1': 8240,
                'venueid': 51,
                'catid': 9,
                'dateid.1': 2081,
                'eventname': 'The Who',
                'starttime': '2008-09-12 19:00:00',
                'catid.1': 9,
                'catgroup': 'Concerts',
                'catname': 'Pop',
                'catdesc': 'All rock and pop music concerts',
                'venueid.1': None,
                'venuename': None,
                'venuecity': None,
                'venuestate': None,
                'venueseats': None,
                'userid': 47402,
                'username': 'YHB76KXJ',
                'firstname': 'Petra',
                'lastname': 'Avila',
                'city': 'Louisville',
                'state': 'YT',
                'email': 'fermentum@sem.edu',
                'phone': '(633) 983-9015',
                'likesports': None,
                'liketheatre': None,
                'likeconcerts': None,
                'likejazz': False,
                'likeclassical': None,
                'likeopera': None,
                'likerock': None,
                'likevegas': None,
                'likebroadway': None,
                'likemusicals': None,
                'saletime_utc': '2008-08-31 09:17:00UTC',
                'saletime_min_7': '2008-08-31 09:17:00-0700',
                'saletime_plus_8': '2008-08-31 09:17:00-0800'},
            {'rn': 2,
             'salesid': 6,
             'listid': 10,
             'sellerid': 24858,
             'buyerid': 24888,
             'eventid': 3375,
             'dateid': 2023,
             'qtysold': 2,
             'pricepaid': 394,
             'commission': 59.1,
             'saletime': '2008-07-16 11:59:00',
             'eventid.1': 3375,
             'venueid': 220,
             'catid': 7,
             'dateid.1': 2031,
             'eventname': 'Uncle Vanya',
             'starttime': '2008-07-24 19:00:00',
             'catid.1': 7,
             'catgroup': 'Shows',
             'catname': 'Plays',
             'catdesc': 'All non-musical theatre',
             'venueid.1': 220.0,
             'venuename': 'Lunt-Fontanne Theatre',
             'venuecity': 'New York City',
             'venuestate': 'NY',
             'venueseats': 0.0,
             'userid': 24858,
             'username': 'YFF20OCX',
             'firstname': 'Kalia',
             'lastname': 'Rush',
             'city': 'Lakewood',
             'state': 'DC',
             'email': 'lorem.eu@eutempor.edu',
             'phone': '(396) 106-3294',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': False,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': True,
             'likerock': None,
             'likevegas': True,
             'likebroadway': False,
             'likemusicals': True,
             'saletime_utc': '2008-07-16 11:59:00UTC',
             'saletime_min_7': '2008-07-16 11:59:00-0700',
             'saletime_plus_8': '2008-07-16 11:59:00-0800'},
            {'rn': 3,
             'salesid': 7,
             'listid': 10,
             'sellerid': 24858,
             'buyerid': 7952,
             'eventid': 3375,
             'dateid': 2003,
             'qtysold': 4,
             'pricepaid': 788,
             'commission': 118.2,
             'saletime': '2008-06-26 12:56:00',
             'eventid.1': 3375,
             'venueid': 220,
             'catid': 7,
             'dateid.1': 2031,
             'eventname': 'Uncle Vanya',
             'starttime': '2008-07-24 19:00:00',
             'catid.1': 7,
             'catgroup': 'Shows',
             'catname': 'Plays',
             'catdesc': 'All non-musical theatre',
             'venueid.1': 220.0,
             'venuename': 'Lunt-Fontanne Theatre',
             'venuecity': 'New York City',
             'venuestate': 'NY',
             'venueseats': 0.0,
             'userid': 24858,
             'username': 'YFF20OCX',
             'firstname': 'Kalia',
             'lastname': 'Rush',
             'city': 'Lakewood',
             'state': 'DC',
             'email': 'lorem.eu@eutempor.edu',
             'phone': '(396) 106-3294',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': False,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': True,
             'likerock': None,
             'likevegas': True,
             'likebroadway': False,
             'likemusicals': True,
             'saletime_utc': '2008-06-26 12:56:00UTC',
             'saletime_min_7': '2008-06-26 12:56:00-0700',
             'saletime_plus_8': '2008-06-26 12:56:00-0800'},
            {'rn': 4,
             'salesid': 8,
             'listid': 10,
             'sellerid': 24858,
             'buyerid': 19715,
             'eventid': 3375,
             'dateid': 2017,
             'qtysold': 1,
             'pricepaid': 197,
             'commission': 29.55,
             'saletime': '2008-07-10 02:12:00',
             'eventid.1': 3375,
             'venueid': 220,
             'catid': 7,
             'dateid.1': 2031,
             'eventname': 'Uncle Vanya',
             'starttime': '2008-07-24 19:00:00',
             'catid.1': 7,
             'catgroup': 'Shows',
             'catname': 'Plays',
             'catdesc': 'All non-musical theatre',
             'venueid.1': 220.0,
             'venuename': 'Lunt-Fontanne Theatre',
             'venuecity': 'New York City',
             'venuestate': 'NY',
             'venueseats': 0.0,
             'userid': 24858,
             'username': 'YFF20OCX',
             'firstname': 'Kalia',
             'lastname': 'Rush',
             'city': 'Lakewood',
             'state': 'DC',
             'email': 'lorem.eu@eutempor.edu',
             'phone': '(396) 106-3294',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': False,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': True,
             'likerock': None,
             'likevegas': True,
             'likebroadway': False,
             'likemusicals': True,
             'saletime_utc': '2008-07-10 02:12:00UTC',
             'saletime_min_7': '2008-07-10 02:12:00-0700',
             'saletime_plus_8': '2008-07-10 02:12:00-0800'},
            {'rn': 5,
             'salesid': 9,
             'listid': 10,
             'sellerid': 24858,
             'buyerid': 29891,
             'eventid': 3375,
             'dateid': 2029,
             'qtysold': 3,
             'pricepaid': 591,
             'commission': 88.65,
             'saletime': '2008-07-22 02:23:00',
             'eventid.1': 3375,
             'venueid': 220,
             'catid': 7,
             'dateid.1': 2031,
             'eventname': 'Uncle Vanya',
             'starttime': '2008-07-24 19:00:00',
             'catid.1': 7,
             'catgroup': 'Shows',
             'catname': 'Plays',
             'catdesc': 'All non-musical theatre',
             'venueid.1': 220.0,
             'venuename': 'Lunt-Fontanne Theatre',
             'venuecity': 'New York City',
             'venuestate': 'NY',
             'venueseats': 0.0,
             'userid': 24858,
             'username': 'YFF20OCX',
             'firstname': 'Kalia',
             'lastname': 'Rush',
             'city': 'Lakewood',
             'state': 'DC',
             'email': 'lorem.eu@eutempor.edu',
             'phone': '(396) 106-3294',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': False,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': True,
             'likerock': None,
             'likevegas': True,
             'likebroadway': False,
             'likemusicals': True,
             'saletime_utc': '2008-07-22 02:23:00UTC',
             'saletime_min_7': '2008-07-22 02:23:00-0700',
             'saletime_plus_8': '2008-07-22 02:23:00-0800'},
            {'rn': 6,
             'salesid': 10,
             'listid': 12,
             'sellerid': 45635,
             'buyerid': 10542,
             'eventid': 4769,
             'dateid': 2044,
             'qtysold': 1,
             'pricepaid': 65,
             'commission': 9.75,
             'saletime': '2008-08-06 02:51:00',
             'eventid.1': 4769,
             'venueid': 2,
             'catid': 9,
             'dateid.1': 2075,
             'eventname': 'Neville Brothers',
             'starttime': '2008-09-06 15:00:00',
             'catid.1': 9,
             'catgroup': 'Concerts',
             'catname': 'Pop',
             'catdesc': 'All rock and pop music concerts',
             'venueid.1': 2.0,
             'venuename': 'Columbus Crew Stadium',
             'venuecity': 'Columbus',
             'venuestate': 'OH',
             'venueseats': 0.0,
             'userid': 45635,
             'username': 'BMZ94OHM',
             'firstname': 'Vaughan',
             'lastname': 'Williams',
             'city': 'Aliquippa',
             'state': 'MS',
             'email': 'nec.tempus.scelerisque@blanditatnisi.ca',
             'phone': '(781) 115-6572',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': None,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': None,
             'likerock': True,
             'likevegas': True,
             'likebroadway': None,
             'likemusicals': None,
             'saletime_utc': '2008-08-06 02:51:00UTC',
             'saletime_min_7': '2008-08-06 02:51:00-0700',
             'saletime_plus_8': '2008-08-06 02:51:00-0800'},
            {'rn': 7,
             'salesid': 11,
             'listid': 12,
             'sellerid': 45635,
             'buyerid': 8435,
             'eventid': 4769,
             'dateid': 2042,
             'qtysold': 2,
             'pricepaid': 130,
             'commission': 19.5,
             'saletime': '2008-08-04 03:06:00',
             'eventid.1': 4769,
             'venueid': 2,
             'catid': 9,
             'dateid.1': 2075,
             'eventname': 'Neville Brothers',
             'starttime': '2008-09-06 15:00:00',
             'catid.1': 9,
             'catgroup': 'Concerts',
             'catname': 'Pop',
             'catdesc': 'All rock and pop music concerts',
             'venueid.1': 2.0,
             'venuename': 'Columbus Crew Stadium',
             'venuecity': 'Columbus',
             'venuestate': 'OH',
             'venueseats': 0.0,
             'userid': 45635,
             'username': 'BMZ94OHM',
             'firstname': 'Vaughan',
             'lastname': 'Williams',
             'city': 'Aliquippa',
             'state': 'MS',
             'email': 'nec.tempus.scelerisque@blanditatnisi.ca',
             'phone': '(781) 115-6572',
             'likesports': None,
             'liketheatre': None,
             'likeconcerts': None,
             'likejazz': True,
             'likeclassical': None,
             'likeopera': None,
             'likerock': True,
             'likevegas': True,
             'likebroadway': None,
             'likemusicals': None,
             'saletime_utc': '2008-08-04 03:06:00UTC',
             'saletime_min_7': '2008-08-04 03:06:00-0700',
             'saletime_plus_8': '2008-08-04 03:06:00-0800'},
            {'rn': 8,
             'salesid': 12,
             'listid': 13,
             'sellerid': 30606,
             'buyerid': 9633,
             'eventid': 2147,
             'dateid': 1894,
             'qtysold': 2,
             'pricepaid': 344,
             'commission': 51.6,
             'saletime': '2008-03-09 03:18:00',
             'eventid.1': 2147,
             'venueid': 238,
             'catid': 7,
             'dateid.1': 1913,
             'eventname': 'Look Back in Anger',
             'starttime': '2008-03-28 15:00:00',
             'catid.1': 7,
             'catgroup': 'Shows',
             'catname': 'Plays',
             'catdesc': 'All non-musical theatre',
             'venueid.1': 238.0,
             'venuename': 'Winter Garden Theatre',
             'venuecity': 'New York City',
             'venuestate': 'NY',
             'venueseats': 0.0,
             'userid': 30606,
             'username': 'MUU02ZEH',
             'firstname': 'Shad',
             'lastname': 'Kane',
             'city': 'Chico',
             'state': 'SK',
             'email': 'sed@ametconsectetuer.edu',
             'phone': '(843) 646-6950',
             'likesports': True,
             'liketheatre': None,
             'likeconcerts': True,
             'likejazz': True,
             'likeclassical': False,
             'likeopera': None,
             'likerock': None,
             'likevegas': True,
             'likebroadway': None,
             'likemusicals': True,
             'saletime_utc': '2008-03-09 03:18:00UTC',
             'saletime_min_7': '2008-03-09 03:18:00-0700',
             'saletime_plus_8': '2008-03-09 03:18:00-0800'
             }
        ]
    }
    TS_RAW_QUERY_FIELDS_RESULT = {
        'data': [
            {'rn': 1, 'salesid': 1, 'listid': 1},
            {'rn': 2, 'salesid': 2, 'listid': 4},
            {'rn': 3, 'salesid': 3, 'listid': 5},
            {'rn': 4, 'salesid': 4, 'listid': 5},
            {'rn': 5, 'salesid': 5, 'listid': 6},
            {'rn': 6, 'salesid': 6, 'listid': 10},
            {'rn': 7, 'salesid': 7, 'listid': 10},
            {'rn': 8, 'salesid': 8, 'listid': 10}
        ]
    }
    TS_RAW_QUERY_EXCLUDE_RESULT = {
        'data': [
            {'rn': 1, 'salesid': 1},
            {'rn': 2, 'salesid': 2},
            {'rn': 3, 'salesid': 3},
            {'rn': 4, 'salesid': 4},
            {'rn': 5, 'salesid': 5},
            {'rn': 6, 'salesid': 6},
            {'rn': 7, 'salesid': 7},
            {'rn': 8, 'salesid': 8}
        ]
    }
    TS_RAW_QUERY_FILTERS_TS_RESULT = {
        'data': [
            {'rn': 1, 'catdesc': 'All rock and pop music concerts'},
            {'rn': 2, 'catdesc': 'All rock and pop music concerts'},
            {'rn': 3, 'catdesc': 'All rock and pop music concerts'},
            {'rn': 4, 'catdesc': 'All rock and pop music concerts'},
            {'rn': 5, 'catdesc': 'All rock and pop music concerts'},
            {'rn': 6, 'catdesc': 'All non-musical theatre'},
            {'rn': 7, 'catdesc': 'All non-musical theatre'},
            {'rn': 8, 'catdesc': 'All non-musical theatre'}
        ]
    }
    TS_ONE_GROUP_QUERY_RESULT = {'data': [{'group': ['Pop'], 'current': {'count': 97582, 'metrics': {'pricepaid': {'sum': 62434243.0}, 'commission': {'sum': 9365136.45}}}}, {'group': ['Plays'], 'current': {'count': 39223, 'metrics': {'pricepaid': {'sum': 25538940.0}, 'commission': {'sum': 3830841.0}}}}, {'group': ['Musicals'], 'current': {'count': 25737, 'metrics': {'pricepaid': {'sum': 16336947.0}, 'commission': {'sum': 2450542.05}}}}, {'group': ['Opera'], 'current': {'count': 9914, 'metrics': {'pricepaid': {'sum': 6455301.0}, 'commission': {'sum': 968295.15}}}}], 'visualization': 'Bars'}
    TS_TWO_GROUPS_QUERY_RESULT = {'data': [{'group': ['Pop', 'Zucchero'], 'current': {'count': 250, 'metrics': {'pricepaid': {'sum': 170070.0}, 'commission': {'sum': 25510.5}, 'eventname': {'unique': 1.0}}}}, {'group': ['Pop', 'Zombies'], 'current': {'count': 204, 'metrics': {'pricepaid': {'sum': 132719.0}, 'commission': {'sum': 19907.85}, 'eventname': {'unique': 1.0}}}}, {'group': ['Pop', 'Zappa Plays Zappa'], 'current': {'count': 217, 'metrics': {'pricepaid': {'sum': 142544.0}, 'commission': {'sum': 21381.6}, 'eventname': {'unique': 1.0}}}}, {'group': ['Pop', 'ZZ Top'], 'current': {'count': 136, 'metrics': {'pricepaid': {'sum': 102075.0}, 'commission': {'sum': 15311.25}, 'eventname': {'unique': 1.0}}}}, {'group': ['Pop', 'Yaz'], 'current': {'count': 192, 'metrics': {'pricepaid': {'sum': 106677.0}, 'commission': {'sum': 16001.55}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Young Frankenstein'], 'current': {'count': 704, 'metrics': {'pricepaid': {'sum': 507741.0}, 'commission': {'sum': 76161.15}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Woyzeck'], 'current': {'count': 698, 'metrics': {'pricepaid': {'sum': 457353.0}, 'commission': {'sum': 68602.95}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Wicked'], 'current': {'count': 709, 'metrics': {'pricepaid': {'sum': 470991.0}, 'commission': {'sum': 70648.65}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Waiting for Godot'], 'current': {'count': 861, 'metrics': {'pricepaid': {'sum': 561135.0}, 'commission': {'sum': 84170.25}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Uncle Vanya'], 'current': {'count': 799, 'metrics': {'pricepaid': {'sum': 473908.0}, 'commission': {'sum': 71086.2}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'Zumanity'], 'current': {'count': 358, 'metrics': {'pricepaid': {'sum': 201781.0}, 'commission': {'sum': 30267.15}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'White Christmas'], 'current': {'count': 20, 'metrics': {'pricepaid': {'sum': 9352.0}, 'commission': {'sum': 1402.8}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'West Side Story'], 'current': {'count': 557, 'metrics': {'pricepaid': {'sum': 327673.0}, 'commission': {'sum': 49150.95}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'The Phantom of the Opera'], 'current': {'count': 467, 'metrics': {'pricepaid': {'sum': 260787.0}, 'commission': {'sum': 39118.05}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'The Little Mermaid'], 'current': {'count': 535, 'metrics': {'pricepaid': {'sum': 360005.0}, 'commission': {'sum': 54000.75}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'Tristan und Isolde'], 'current': {'count': 368, 'metrics': {'pricepaid': {'sum': 209852.0}, 'commission': {'sum': 31477.8}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'The Queen of Spades'], 'current': {'count': 216, 'metrics': {'pricepaid': {'sum': 163686.0}, 'commission': {'sum': 24552.9}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'The Magic Flute'], 'current': {'count': 324, 'metrics': {'pricepaid': {'sum': 200965.0}, 'commission': {'sum': 30144.75}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'The Fly'], 'current': {'count': 213, 'metrics': {'pricepaid': {'sum': 169014.0}, 'commission': {'sum': 25352.1}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'The Birds (Die Vogel)'], 'current': {'count': 263, 'metrics': {'pricepaid': {'sum': 162298.0}, 'commission': {'sum': 24344.7}, 'eventname': {'unique': 1.0}}}}], 'visualization': 'Bars'}
    TS_TWO_GROUPS_QUERY_RESULT2 = {'data': [{'group': ['Pop', 'Zucchero'], 'current': {'count': 250, 'metrics': {'pricepaid': {'sum': 170070.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Pop', 'Zombies'], 'current': {'count': 204, 'metrics': {'pricepaid': {'sum': 132719.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Pop', 'Zappa Plays Zappa'], 'current': {'count': 217, 'metrics': {'pricepaid': {'sum': 142544.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Pop', 'ZZ Top'], 'current': {'count': 136, 'metrics': {'pricepaid': {'sum': 102075.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Pop', 'Yaz'], 'current': {'count': 192, 'metrics': {'pricepaid': {'sum': 106677.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Young Frankenstein'], 'current': {'count': 704, 'metrics': {'pricepaid': {'sum': 507741.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Woyzeck'], 'current': {'count': 698, 'metrics': {'pricepaid': {'sum': 457353.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Wicked'], 'current': {'count': 709, 'metrics': {'pricepaid': {'sum': 470991.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Waiting for Godot'], 'current': {'count': 861, 'metrics': {'pricepaid': {'sum': 561135.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Plays', 'Uncle Vanya'], 'current': {'count': 799, 'metrics': {'pricepaid': {'sum': 473908.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'Tristan und Isolde'], 'current': {'count': 368, 'metrics': {'pricepaid': {'sum': 209852.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'The Queen of Spades'], 'current': {'count': 216, 'metrics': {'pricepaid': {'sum': 163686.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'The Magic Flute'], 'current': {'count': 324, 'metrics': {'pricepaid': {'sum': 200965.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'The Fly'], 'current': {'count': 213, 'metrics': {'pricepaid': {'sum': 169014.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Opera', 'The Birds (Die Vogel)'], 'current': {'count': 263, 'metrics': {'pricepaid': {'sum': 162298.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'Zumanity'], 'current': {'count': 358, 'metrics': {'pricepaid': {'sum': 201781.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'White Christmas'], 'current': {'count': 20, 'metrics': {'pricepaid': {'sum': 9352.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'West Side Story'], 'current': {'count': 557, 'metrics': {'pricepaid': {'sum': 327673.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'The Phantom of the Opera'], 'current': {'count': 467, 'metrics': {'pricepaid': {'sum': 260787.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}, {'group': ['Musicals', 'The Little Mermaid'], 'current': {'count': 535, 'metrics': {'pricepaid': {'sum': 360005.0}, 'catname': {'unique': 1.0}, 'eventname': {'unique': 1.0}}}}], 'visualization': 'Bars'}
    TS_TWO_GROUPS_QUERY_RESULT3 = {'data': [{'group': ['Opera', 'The Fly'], 'current': {'count': 213, 'metrics': {'pricepaid': {'sum': 169014.0, 'avg': 793.49}, 'commission': {'sum': 25352.1}}}}, {'group': ['Opera', 'The Queen of Spades'], 'current': {'count': 216, 'metrics': {'pricepaid': {'sum': 163686.0, 'avg': 757.81}, 'commission': {'sum': 24552.9}}}}, {'group': ['Opera', 'La Boheme'], 'current': {'count': 277, 'metrics': {'pricepaid': {'sum': 206715.0, 'avg': 746.26}, 'commission': {'sum': 31007.25}}}}, {'group': ['Opera', 'L Elisir d Amore'], 'current': {'count': 343, 'metrics': {'pricepaid': {'sum': 254097.0, 'avg': 740.81}, 'commission': {'sum': 38114.55}}}}, {'group': ['Opera', 'Carmen'], 'current': {'count': 250, 'metrics': {'pricepaid': {'sum': 184851.0, 'avg': 739.4}, 'commission': {'sum': 27727.65}}}}, {'group': ['Musicals', 'High Society'], 'current': {'count': 479, 'metrics': {'pricepaid': {'sum': 343871.0, 'avg': 717.89}, 'commission': {'sum': 51580.65}}}}, {'group': ['Musicals', 'Legally Blonde'], 'current': {'count': 1121, 'metrics': {'pricepaid': {'sum': 804583.0, 'avg': 717.74}, 'commission': {'sum': 120687.45}}}}, {'group': ['Musicals', 'Kiss Me Kate'], 'current': {'count': 355, 'metrics': {'pricepaid': {'sum': 251982.0, 'avg': 709.81}, 'commission': {'sum': 37797.3}}}}, {'group': ['Musicals', 'Mystere Cirque du Soleil'], 'current': {'count': 825, 'metrics': {'pricepaid': {'sum': 583283.0, 'avg': 707.01}, 'commission': {'sum': 87492.45}}}}, {'group': ['Musicals', 'Phantom of the Opera'], 'current': {'count': 566, 'metrics': {'pricepaid': {'sum': 397067.0, 'avg': 701.53}, 'commission': {'sum': 59560.05}}}}, {'group': ['Plays', 'A Christmas Carol'], 'current': {'count': 105, 'metrics': {'pricepaid': {'sum': 87481.0, 'avg': 833.15}, 'commission': {'sum': 13122.15}}}}, {'group': ['Plays', 'Electra'], 'current': {'count': 708, 'metrics': {'pricepaid': {'sum': 529067.0, 'avg': 747.27}, 'commission': {'sum': 79360.05}}}}, {'group': ['Plays', 'The Seafarer'], 'current': {'count': 675, 'metrics': {'pricepaid': {'sum': 490500.0, 'avg': 726.67}, 'commission': {'sum': 73575.0}}}}, {'group': ['Plays', "A Doll's House"], 'current': {'count': 643, 'metrics': {'pricepaid': {'sum': 465897.0, 'avg': 724.57}, 'commission': {'sum': 69884.55}}}}, {'group': ['Plays', 'Young Frankenstein'], 'current': {'count': 704, 'metrics': {'pricepaid': {'sum': 507741.0, 'avg': 721.22}, 'commission': {'sum': 76161.15}}}}, {'group': ['Pop', 'Martina McBride'], 'current': {'count': 50, 'metrics': {'pricepaid': {'sum': 52932.0, 'avg': 1058.64}, 'commission': {'sum': 7939.8}}}}, {'group': ['Pop', 'Teena Marie'], 'current': {'count': 64, 'metrics': {'pricepaid': {'sum': 56982.0, 'avg': 890.34}, 'commission': {'sum': 8547.3}}}}, {'group': ['Pop', 'Dierks Bentley'], 'current': {'count': 214, 'metrics': {'pricepaid': {'sum': 188436.0, 'avg': 880.54}, 'commission': {'sum': 28265.4}}}}, {'group': ['Pop', 'Return To Forever'], 'current': {'count': 97, 'metrics': {'pricepaid': {'sum': 84497.0, 'avg': 871.1}, 'commission': {'sum': 12674.55}}}}, {'group': ['Pop', 'Boyz II Men'], 'current': {'count': 227, 'metrics': {'pricepaid': {'sum': 191562.0, 'avg': 843.89}, 'commission': {'sum': 28734.3}}}}], 'visualization': 'Bars'}
    TS_BOX_PLOT_RESULT = {
        'data': [
            {'group': ['Pop'],
             'current': {'metrics': {'commission': {'percentile0': 3.0,
                                                    'percentile25': 28.95,
                                                    'percentile50': 57.6,
                                                    'percentile75': 113.4,
                                                    'percentile100': 1893.6}}}},
            {'group': ['Plays'],
             'current': {'metrics': {'commission': {'percentile0': 3.0,
                                                    'percentile25': 29.85,
                                                    'percentile50': 58.5,
                                                    'percentile75': 114.6,
                                                    'percentile100': 1500.0}}}},
            {'group': ['Opera'],
             'current': {'metrics': {'commission': {'percentile0': 3.0,
                                                    'percentile25': 29.25,
                                                    'percentile50': 58.2,
                                                    'percentile75': 115.42,
                                                    'percentile100': 1477.2}}}},
            {'group': ['Musicals'],
             'current': {'metrics': {'commission': {'percentile0': 3.0,
                                                    'percentile25': 28.8,
                                                    'percentile50': 57.3,
                                                    'percentile75': 112.5,
                                                    'percentile100': 1494.0}}}}
        ],
        'visualization': 'Box Plot'
    }
    TS_TIME_RANGE_YEAR = {'data': [{'min': '2008-01-01 00:00:00', 'max': '2008-01-01 00:00:00'}],
                          'visualization': 'Time Range Picker'}
    TS_TIME_RANGE_MONTH = {'data': [{'min': '2008-01-01 00:00:00', 'max': '2008-12-01 00:00:00'}],
                           'visualization': 'Time Range Picker'}
    TS_TIME_RANGE_WEEK = {'data': [{'min': '2007-12-31 00:00:00', 'max': '2008-12-29 00:00:00'}],
                          'visualization': 'Time Range Picker'}
    TS_TIME_RANGE_DAY = {'data': [{'min': '2008-01-01 00:00:00', 'max': '2008-12-31 00:00:00'}],
                         'visualization': 'Time Range Picker'}
    TS_TIME_RANGE_HOUR = {'data': [{'min': '2008-01-01 01:00:00', 'max': '2008-12-31 12:00:00'}],
                          'visualization': 'Time Range Picker'}
    TS_TIME_RANGE_MINUTE = {'data': [{'min': '2008-01-01 01:00:00', 'max': '2008-12-31 12:58:00'}],
                            'visualization': 'Time Range Picker'}
    TS_TIME_RANGE_SECOND = {'data': [{'min': '2008-01-01 01:00:00', 'max': '2008-12-31 12:58:00'}],
                            'visualization': 'Time Range Picker'}
    TS_HISTOGRAM_DEFAULT_RESULT = {
        'data': [
            {'group': [[0.0, 1400.4444444444443]], 'current': {'count': 155362.0}},
            {'group': [[1400.4444444444443, 2800.8888888888887]],
             'current': {'count': 12322.0}},
            {'group': [[2800.8888888888887, 4201.333333333333]],
             'current': {'count': 2431.0}},
            {'group': [[4201.333333333333, 5601.777777777777]],
             'current': {'count': 1458.0}},
            {'group': [[5601.777777777777, 7002.222222222222]],
             'current': {'count': 344.0}},
            {'group': [[7002.222222222222, 8402.666666666666]],
             'current': {'count': 282.0}},
            {'group': [[8402.666666666666, 9803.11111111111]],
             'current': {'count': 227.0}},
            {'group': [[9803.11111111111, 12604.0]], 'current': {'count': 29.0}},
            {'group': [[12604.0, 14004.444444444445]], 'current': {'count': 1.0}}
        ],
        'visualization': 'Bars'
    }
    TS_HISTOGRAM_SCENARIO_1_RESULT = {
        'data': [{'group': [[20.0, 30.0]], 'current': {'count': 1570.0}},
                 {'group': [[30.0, 40.0]], 'current': {'count': 1639.0}},
                 {'group': [[40.0, 50.0]], 'current': {'count': 2332.0}},
                 {'group': [[50.0, 60.0]], 'current': {'count': 2344.0}},
                 {'group': [[60.0, 70.0]], 'current': {'count': 2464.0}},
                 {'group': [[70.0, 80.0]], 'current': {'count': 2516.0}},
                 {'group': [[80.0, 90.0]], 'current': {'count': 2655.0}},
                 {'group': [[90.0, 100.0]], 'current': {'count': 2631.0}},
                 {'group': [[100.0, 110.0]], 'current': {'count': 2643.0}},
                 {'group': [[110.0, 120.0]], 'current': {'count': 2569.0}}
                 ],
        'visualization': 'Bars'
    }
    TS_HISTOGRAM_SCENARIO_2_RESULT = {
        'data': [{'group': [[15.0, 25.0]], 'current': {'count': 777.0}},
                 {'group': [[25.0, 35.0]], 'current': {'count': 1610.0}},
                 {'group': [[35.0, 45.0]], 'current': {'count': 2085.0}},
                 {'group': [[45.0, 55.0]], 'current': {'count': 2340.0}},
                 {'group': [[55.0, 65.0]], 'current': {'count': 2428.0}},
                 {'group': [[65.0, 75.0]], 'current': {'count': 2417.0}},
                 {'group': [[75.0, 85.0]], 'current': {'count': 2644.0}},
                 {'group': [[85.0, 95.0]], 'current': {'count': 2624.0}},
                 {'group': [[95.0, 105.0]], 'current': {'count': 2662.0}},
                 {'group': [[105.0, 115.0]], 'current': {'count': 2601.0}}
                 ],
        'visualization': 'Bars'
    }
    TS_HISTOGRAM_SCENARIO_3_RESULT = {
        'data': [
            {'group': [[0.0, 600.1904761904761]], 'current': {'count': 116585.0}},
            {'group': [[600.1904761904761, 1200.3809523809523]],
             'current': {'count': 34374.0}},
            {'group': [[1200.3809523809523, 1800.5714285714284]],
             'current': {'count': 10602.0}},
            {'group': [[1800.5714285714284, 2400.7619047619046]],
             'current': {'count': 5017.0}},
            {'group': [[2400.7619047619046, 3000.9523809523807]],
             'current': {'count': 1438.0}},
            {'group': [[3000.9523809523807, 3601.142857142857]],
             'current': {'count': 1020.0}},
            {'group': [[3601.142857142857, 4201.333333333333]],
             'current': {'count': 1079.0}},
            {'group': [[4201.333333333333, 4801.523809523809]],
             'current': {'count': 977.0}},
            {'group': [[4801.523809523809, 5401.714285714285]],
             'current': {'count': 427.0}},
            {'group': [[5401.714285714285, 6001.9047619047615]],
             'current': {'count': 157.0}},
            {'group': [[6001.9047619047615, 6602.095238095238]],
             'current': {'count': 138.0}},
            {'group': [[6602.095238095238, 7202.285714285714]],
             'current': {'count': 145.0}},
            {'group': [[7202.285714285714, 7802.47619047619]],
             'current': {'count': 143.0}},
            {'group': [[7802.47619047619, 8402.666666666666]], 'current': {'count': 97.0}},
            {'group': [[8402.666666666666, 9002.857142857141]],
             'current': {'count': 95.0}},
            {'group': [[9002.857142857141, 9603.047619047618]],
             'current': {'count': 93.0}},
            {'group': [[9603.047619047618, 12604.0]], 'current': {'count': 68.0}},
            {'group': [[12604.0, 13204.190476190477]], 'current': {'count': 1.0}}
        ],
        'visualization': 'Bars'
    }
    TS_HISTOGRAM_SCENARIO_4_RESULT = {
        'data': [
            {'group': [[15.0, 25.0]], 'current': {'count': 777.0}},
            {'group': [[25.0, 35.0]], 'current': {'count': 1610.0}},
            {'group': [[35.0, 45.0]], 'current': {'count': 2085.0}},
            {'group': [[45.0, 55.0]], 'current': {'count': 2340.0}},
            {'group': [[55.0, 65.0]], 'current': {'count': 2428.0}},
            {'group': [[65.0, 75.0]], 'current': {'count': 2417.0}},
            {'group': [[75.0, 85.0]], 'current': {'count': 2644.0}},
            {'group': [[85.0, 95.0]], 'current': {'count': 2624.0}},
            {'group': [[95.0, 105.0]], 'current': {'count': 2662.0}},
            {'group': [[105.0, 115.0]], 'current': {'count': 2601.0}},
            {'group': [[115.0, 125.0]], 'current': {'count': 2691.0}},
            {'group': [[125.0, 135.0]], 'current': {'count': 2560.0}},
            {'group': [[135.0, 145.0]], 'current': {'count': 2620.0}},
            {'group': [[145.0, 155.0]], 'current': {'count': 2661.0}},
            {'group': [[155.0, 165.0]], 'current': {'count': 2659.0}},
            {'group': [[165.0, 175.0]], 'current': {'count': 2471.0}},
            {'group': [[175.0, 185.0]], 'current': {'count': 2616.0}},
            {'group': [[185.0, 195.0]], 'current': {'count': 2673.0}},
            {'group': [[195.0, 205.0]], 'current': {'count': 2612.0}},
            {'group': [[205.0, 215.0]], 'current': {'count': 2508.0}},
            {'group': [[215.0, 225.0]], 'current': {'count': 2586.0}},
            {'group': [[225.0, 235.0]], 'current': {'count': 2562.0}},
            {'group': [[235.0, 245.0]], 'current': {'count': 2622.0}},
            {'group': [[245.0, 255.0]], 'current': {'count': 2487.0}},
            {'group': [[255.0, 265.0]], 'current': {'count': 2232.0}},
            {'group': [[265.0, 275.0]], 'current': {'count': 2118.0}},
            {'group': [[275.0, 285.0]], 'current': {'count': 2207.0}},
            {'group': [[285.0, 295.0]], 'current': {'count': 2205.0}},
            {'group': [[295.0, 305.0]], 'current': {'count': 2212.0}},
            {'group': [[305.0, 315.0]], 'current': {'count': 2163.0}}
        ],
        'visualization': 'Bars'
    }
    TS_PIVOT_DEFAULT_CONFIG = {
        'data': [
            {'group': ['All non-musical theatre'], 'current': {'count': 39223, 'metrics': {}}},
            {'group': ['All opera and light opera'], 'current': {'count': 9914, 'metrics': {}}},
            {'group': ['All rock and pop music concerts'], 'current': {'count': 97582, 'metrics': {}}},
            {'group': ['Musical theatre'], 'current': {'count': 25737, 'metrics': {}}},
            {'group': ['$columnTotal'], 'current': {'count': 172456, 'metrics': {}}},
            {'group': ['$absoluteTotal'], 'current': {'count': 172456, 'metrics': {}}}
        ], 'visualization': 'Pivot Table'
    }
    TS_PIVOT_COLUMNS_ROWS_RESULT = {'data': [{'group': ['AB', 'Calgary', 'Pengrowth Saddledome', '$total'], 'current': {'count': 372, 'metrics': {}}}, {'group': ['AB', 'Edmonton', 'Rexall Place', '$total'], 'current': {'count': 1036, 'metrics': {}}}, {'group': ['AZ', 'Glendale', 'Jobing.com Arena', '$total'], 'current': {'count': 1145, 'metrics': {}}}, {'group': ['AZ', 'Glendale', 'University of Phoenix Stadium', '$total'], 'current': {'count': 698, 'metrics': {}}}, {'group': ['AZ', 'Phoenix', 'Chase Field', '$total'], 'current': {'count': 799, 'metrics': {}}}, {'group': ['AZ', 'Phoenix', 'US Airways Center', '$total'], 'current': {'count': 962, 'metrics': {}}}, {'group': ['BC', 'Vancouver', 'General Motors Place', '$total'], 'current': {'count': 741, 'metrics': {}}}, {'group': ['CA', 'Anaheim', 'Angel Stadium of Anaheim', '$total'], 'current': {'count': 746, 'metrics': {}}}, {'group': ['CA', 'Anaheim', 'Honda Center', '$total'], 'current': {'count': 647, 'metrics': {}}}, {'group': ['CA', 'Carson', 'The Home Depot Center', '$total'], 'current': {'count': 775, 'metrics': {}}}, {'group': ['CA', 'Los Angeles', 'Dodger Stadium', '$total'], 'current': {'count': 931, 'metrics': {}}}, {'group': ['CA', 'Los Angeles', 'Geffen Playhouse', '$total'], 'current': {'count': 1215, 'metrics': {}}}, {'group': ['CA', 'Los Angeles', 'Greek Theatre', '$total'], 'current': {'count': 1220, 'metrics': {}}}, {'group': ['CA', 'Los Angeles', 'Los Angeles Opera', '$total'], 'current': {'count': 869, 'metrics': {}}}, {'group': ['CA', 'Los Angeles', 'Royce Hall', '$total'], 'current': {'count': 1005, 'metrics': {}}}, {'group': ['CA', 'Los Angeles', 'Staples Center', '$total'], 'current': {'count': 782, 'metrics': {}}}, {'group': ['CA', 'Mountain View', 'Shoreline Amphitheatre', '$total'], 'current': {'count': 1008, 'metrics': {}}}, {'group': ['CA', 'Oakland', 'McAfee Coliseum', '$total'], 'current': {'count': 818, 'metrics': {}}}, {'group': ['CA', 'Oakland', 'Oracle Arena', '$total'], 'current': {'count': 802, 'metrics': {}}}, {'group': ['CA', 'Pasadena', 'Pasadena Playhouse', '$total'], 'current': {'count': 1373, 'metrics': {}}}, {'group': ['CA', 'Redwood City', 'Fox Theatre', '$total'], 'current': {'count': 727, 'metrics': {}}}, {'group': ['CA', 'Sacramento', 'ARCO Arena', '$total'], 'current': {'count': 905, 'metrics': {}}}, {'group': ['CA', 'San Diego', 'PETCO Park', '$total'], 'current': {'count': 942, 'metrics': {}}}, {'group': ['CA', 'San Diego', 'Qualcomm Stadium', '$total'], 'current': {'count': 862, 'metrics': {}}}, {'group': ['CA', 'San Francisco', 'AT&T Park', '$total'], 'current': {'count': 658, 'metrics': {}}}, {'group': ['CA', 'San Francisco', 'Curran Theatre', '$total'], 'current': {'count': 835, 'metrics': {}}}, {'group': ['CA', 'San Francisco', 'Monster Park', '$total'], 'current': {'count': 523, 'metrics': {}}}, {'group': ['CA', 'San Francisco', 'San Francisco Opera', '$total'], 'current': {'count': 1042, 'metrics': {}}}, {'group': ['CA', 'San Francisco', 'War Memorial Opera House', '$total'], 'current': {'count': 830, 'metrics': {}}}, {'group': ['CA', 'San Jose', 'HP Pavilion at San Jose', '$total'], 'current': {'count': 861, 'metrics': {}}}, {'group': ['CA', 'San Jose', 'San Jose Repertory Theatre', '$total'], 'current': {'count': 1027, 'metrics': {}}}, {'group': ['CA', 'Santa Clara', 'Buck Shaw Stadium', '$total'], 'current': {'count': 933, 'metrics': {}}}, {'group': ['CA', 'Saratoga', 'Mountain Winery', '$total'], 'current': {'count': 648, 'metrics': {}}}, {'group': ['CA', 'Saratoga', 'Villa Montalvo', '$total'], 'current': {'count': 719, 'metrics': {}}}, {'group': ['CO', 'Commerce City', "Dick's Sporting Goods Park", '$total'], 'current': {'count': 930, 'metrics': {}}}, {'group': ['CO', 'Denver', 'Coors Field', '$total'], 'current': {'count': 536, 'metrics': {}}}, {'group': ['CO', 'Denver', 'Ellie Caulkins Opera House', '$total'], 'current': {'count': 748, 'metrics': {}}}, {'group': ['CO', 'Denver', 'INVESCO Field', '$total'], 'current': {'count': 679, 'metrics': {}}}, {'group': ['CO', 'Denver', 'Pepsi Center', '$total'], 'current': {'count': 689, 'metrics': {}}}, {'group': ['DC', 'Washington', 'Kennedy Center Opera House', '$total'], 'current': {'count': 1085, 'metrics': {}}}, {'group': ['DC', 'Washington', 'Nationals Park', '$total'], 'current': {'count': 668, 'metrics': {}}}, {'group': ['DC', 'Washington', 'RFK Stadium', '$total'], 'current': {'count': 708, 'metrics': {}}}, {'group': ['DC', 'Washington', 'Verizon Center', '$total'], 'current': {'count': 921, 'metrics': {}}}, {'group': ['FL', 'Jacksonville', 'Jacksonville Municipal Stadium', '$total'], 'current': {'count': 657, 'metrics': {}}}, {'group': ['FL', 'Miami', 'American Airlines Arena', '$total'], 'current': {'count': 792, 'metrics': {}}}, {'group': ['FL', 'Miami Gardens', 'Dolphin Stadium', '$total'], 'current': {'count': 871, 'metrics': {}}}, {'group': ['FL', 'Orlando', 'Amway Arena', '$total'], 'current': {'count': 784, 'metrics': {}}}, {'group': ['FL', 'St. Petersburg', 'Tropicana Field', '$total'], 'current': {'count': 730, 'metrics': {}}}, {'group': ['FL', 'Sunrise', 'BankAtlantic Center', '$total'], 'current': {'count': 445, 'metrics': {}}}, {'group': ['FL', 'Tampa', 'Raymond James Stadium', '$total'], 'current': {'count': 581, 'metrics': {}}}, {'group': ['FL', 'Tampa', 'St. Pete Times Forum', '$total'], 'current': {'count': 579, 'metrics': {}}}, {'group': ['GA', 'Atlanta', 'Georgia Dome', '$total'], 'current': {'count': 763, 'metrics': {}}}, {'group': ['GA', 'Atlanta', 'Philips Arena', '$total'], 'current': {'count': 568, 'metrics': {}}}, {'group': ['GA', 'Atlanta', 'Turner Field', '$total'], 'current': {'count': 745, 'metrics': {}}}, {'group': ['IL', 'Bridgeview', 'Toyota Park', '$total'], 'current': {'count': 857, 'metrics': {}}}, {'group': ['IL', 'Chicago', 'Lyric Opera House', '$total'], 'current': {'count': 1013, 'metrics': {}}}, {'group': ['IL', 'Chicago', 'Soldier Field', '$total'], 'current': {'count': 673, 'metrics': {}}}, {'group': ['IL', 'Chicago', 'U.S. Cellular Field', '$total'], 'current': {'count': 794, 'metrics': {}}}, {'group': ['IL', 'Chicago', 'United Center', '$total'], 'current': {'count': 753, 'metrics': {}}}, {'group': ['IL', 'Chicago', 'Wrigley Field', '$total'], 'current': {'count': 653, 'metrics': {}}}, {'group': ['IN', 'Indianapolis', 'Conseco Fieldhouse', '$total'], 'current': {'count': 534, 'metrics': {}}}, {'group': ['IN', 'Indianapolis', 'Lucas Oil Stadium', '$total'], 'current': {'count': 656, 'metrics': {}}}, {'group': ['KS', 'Kansas City', 'CommunityAmerica Ballpark', '$total'], 'current': {'count': 555, 'metrics': {}}}, {'group': ['LA', 'New Orleans', 'Louisiana Superdome', '$total'], 'current': {'count': 829, 'metrics': {}}}, {'group': ['LA', 'New Orleans', 'New Orleans Arena', '$total'], 'current': {'count': 681, 'metrics': {}}}, {'group': ['MA', 'Boston', 'Charles Playhouse', '$total'], 'current': {'count': 1244, 'metrics': {}}}, {'group': ['MA', 'Boston', 'Fenway Park', '$total'], 'current': {'count': 727, 'metrics': {}}}, {'group': ['MA', 'Boston', 'TD Banknorth Garden', '$total'], 'current': {'count': 829, 'metrics': {}}}, {'group': ['MA', 'Foxborough', 'Gillette Stadium', '$total'], 'current': {'count': 562, 'metrics': {}}}, {'group': ['MD', 'Baltimore', 'Lyric Opera House', '$total'], 'current': {'count': 1154, 'metrics': {}}}, {'group': ['MD', 'Baltimore', 'M&T Bank Stadium', '$total'], 'current': {'count': 836, 'metrics': {}}}, {'group': ['MD', 'Baltimore', 'Oriole Park at Camden Yards', '$total'], 'current': {'count': 941, 'metrics': {}}}, {'group': ['MD', 'Landover', 'FedExField', '$total'], 'current': {'count': 858, 'metrics': {}}}, {'group': ['MI', 'Auburn Hills', 'The Palace of Auburn Hills', '$total'], 'current': {'count': 858, 'metrics': {}}}, {'group': ['MI', 'Detroit', 'Comerica Park', '$total'], 'current': {'count': 568, 'metrics': {}}}, {'group': ['MI', 'Detroit', 'Detroit Opera House', '$total'], 'current': {'count': 1003, 'metrics': {}}}, {'group': ['MI', 'Detroit', 'Ford Field', '$total'], 'current': {'count': 624, 'metrics': {}}}, {'group': ['MI', 'Detroit', 'Joe Louis Arena', '$total'], 'current': {'count': 736, 'metrics': {}}}, {'group': ['MN', 'Minneapolis', 'Hubert H. Humphrey Metrodome', '$total'], 'current': {'count': 651, 'metrics': {}}}, {'group': ['MN', 'Minneapolis', 'Target Center', '$total'], 'current': {'count': 758, 'metrics': {}}}, {'group': ['MN', 'Minneapolis', 'The Guthrie Theater', '$total'], 'current': {'count': 943, 'metrics': {}}}, {'group': ['MN', 'St. Paul', 'Xcel Energy Center', '$total'], 'current': {'count': 828, 'metrics': {}}}, {'group': ['MO', 'Kansas City', 'Arrowhead Stadium', '$total'], 'current': {'count': 603, 'metrics': {}}}, {'group': ['MO', 'Kansas City', 'Kauffman Stadium', '$total'], 'current': {'count': 554, 'metrics': {}}}, {'group': ['MO', 'St. Louis', 'Busch Stadium', '$total'], 'current': {'count': 737, 'metrics': {}}}, {'group': ['MO', 'St. Louis', 'Edward Jones Dome', '$total'], 'current': {'count': 895, 'metrics': {}}}, {'group': ['MO', 'St. Louis', 'Scottrade Center', '$total'], 'current': {'count': 803, 'metrics': {}}}, {'group': ['NC', 'Charlotte', 'Bank of America Stadium', '$total'], 'current': {'count': 711, 'metrics': {}}}, {'group': ['NC', 'Charlotte', 'Time Warner Cable Arena', '$total'], 'current': {'count': 599, 'metrics': {}}}, {'group': ['NC', 'Raleigh', 'RBC Center', '$total'], 'current': {'count': 714, 'metrics': {}}}, {'group': ['NJ', 'East Rutherford', 'Izod Center', '$total'], 'current': {'count': 826, 'metrics': {}}}, {'group': ['NJ', 'East Rutherford', 'New York Giants Stadium', '$total'], 'current': {'count': 805, 'metrics': {}}}, {'group': ['NJ', 'Newark', 'Prudential Center', '$total'], 'current': {'count': 525, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Ballys Hotel', '$total'], 'current': {'count': 398, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Bellagio Hotel', '$total'], 'current': {'count': 465, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Caesars Palace', '$total'], 'current': {'count': 427, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Harrahs Hotel', '$total'], 'current': {'count': 518, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Hilton Hotel', '$total'], 'current': {'count': 418, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Luxor Hotel', '$total'], 'current': {'count': 671, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Mandalay Bay Hotel', '$total'], 'current': {'count': 332, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Mirage Hotel', '$total'], 'current': {'count': 432, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Paris Hotel', '$total'], 'current': {'count': 309, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Paris MGM Grand', '$total'], 'current': {'count': 378, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Sahara Hotel', '$total'], 'current': {'count': 378, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Tropicana Hotel', '$total'], 'current': {'count': 443, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Venetian Hotel', '$total'], 'current': {'count': 589, 'metrics': {}}}, {'group': ['NV', 'Las Vegas', 'Wynn Hotel', '$total'], 'current': {'count': 327, 'metrics': {}}}, {'group': ['NY', 'Buffalo', 'HSBC Arena', '$total'], 'current': {'count': 732, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Al Hirschfeld Theatre', '$total'], 'current': {'count': 1191, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Ambassador Theatre', '$total'], 'current': {'count': 1168, 'metrics': {}}}, {'group': ['NY', 'New York City', 'American Airlines Theatre', '$total'], 'current': {'count': 929, 'metrics': {}}}, {'group': ['NY', 'New York City', 'August Wilson Theatre', '$total'], 'current': {'count': 1583, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Belasco Theatre', '$total'], 'current': {'count': 1217, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Bernard B. Jacobs Theatre', '$total'], 'current': {'count': 1217, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Biltmore Theatre', '$total'], 'current': {'count': 1305, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Booth Theatre', '$total'], 'current': {'count': 1210, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Broadhurst Theatre', '$total'], 'current': {'count': 1055, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Brooks Atkinson Theatre', '$total'], 'current': {'count': 1013, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Carnegie Hall', '$total'], 'current': {'count': 1211, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Circle in the Square Theatre', '$total'], 'current': {'count': 1047, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Cort Theatre', '$total'], 'current': {'count': 1082, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Ethel Barrymore Theatre', '$total'], 'current': {'count': 1413, 'metrics': {}}}, {'group': ['NY', 'New York City', "Eugene O'Neill Theatre", '$total'], 'current': {'count': 1239, 'metrics': {}}}, {'group': ['NY', 'New York City', 'George Gershwin Theatre', '$total'], 'current': {'count': 1137, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Gerald Schoenfeld Theatre', '$total'], 'current': {'count': 1132, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Helen Hayes Theatre', '$total'], 'current': {'count': 1456, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Hilton Theatre', '$total'], 'current': {'count': 1488, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Imperial Theatre', '$total'], 'current': {'count': 1357, 'metrics': {}}}, {'group': ['NY', 'New York City', 'John Golden Theatre', '$total'], 'current': {'count': 1208, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Lincoln Center for the Performing Arts', '$total'], 'current': {'count': 1082, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Longacre Theatre', '$total'], 'current': {'count': 1143, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Lunt-Fontanne Theatre', '$total'], 'current': {'count': 1672, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Lyceum Theatre', '$total'], 'current': {'count': 1221, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Madison Square Garden', '$total'], 'current': {'count': 923, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Majestic Theatre', '$total'], 'current': {'count': 1265, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Marquis Theatre', '$total'], 'current': {'count': 1023, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Metropolitan Opera', '$total'], 'current': {'count': 1088, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Minskoff Theatre', '$total'], 'current': {'count': 1185, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Music Box Theatre', '$total'], 'current': {'count': 963, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Nederlander Theatre', '$total'], 'current': {'count': 1465, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Neil Simon Theatre', '$total'], 'current': {'count': 1107, 'metrics': {}}}, {'group': ['NY', 'New York City', 'New Amsterdam Theatre', '$total'], 'current': {'count': 1016, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Palace Theatre', '$total'], 'current': {'count': 1039, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Richard Rodgers Theatre', '$total'], 'current': {'count': 1099, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Shea Stadium', '$total'], 'current': {'count': 539, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Shubert Theatre', '$total'], 'current': {'count': 992, 'metrics': {}}}, {'group': ['NY', 'New York City', 'St. James Theatre', '$total'], 'current': {'count': 958, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Studio 54', '$total'], 'current': {'count': 1146, 'metrics': {}}}, {'group': ['NY', 'New York City', 'The Broadway Theatre', '$total'], 'current': {'count': 1118, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Vivian Beaumont Theatre', '$total'], 'current': {'count': 1055, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Walter Kerr Theatre', '$total'], 'current': {'count': 1208, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Winter Garden Theatre', '$total'], 'current': {'count': 1451, 'metrics': {}}}, {'group': ['NY', 'New York City', 'Yankee Stadium', '$total'], 'current': {'count': 869, 'metrics': {}}}, {'group': ['NY', 'Orchard Park', 'Ralph Wilson Stadium', '$total'], 'current': {'count': 661, 'metrics': {}}}, {'group': ['NY', 'Saratoga Springs', 'Saratoga Springs Performing Arts Center', '$total'], 'current': {'count': 782, 'metrics': {}}}, {'group': ['NY', 'Uniondale', 'Nassau Veterans Memorial Coliseum', '$total'], 'current': {'count': 713, 'metrics': {}}}, {'group': [None, None, None, '$total'], 'current': {'count': 2777, 'metrics': {}}}, {'group': ['OH', 'Cincinnati', 'Great American Ball Park', '$total'], 'current': {'count': 879, 'metrics': {}}}, {'group': ['OH', 'Cincinnati', 'Paul Brown Stadium', '$total'], 'current': {'count': 880, 'metrics': {}}}, {'group': ['OH', 'Cleveland', 'Cleveland Browns Stadium', '$total'], 'current': {'count': 617, 'metrics': {}}}, {'group': ['OH', 'Cleveland', 'Progressive Field', '$total'], 'current': {'count': 742, 'metrics': {}}}, {'group': ['OH', 'Cleveland', 'Quicken Loans Arena', '$total'], 'current': {'count': 778, 'metrics': {}}}, {'group': ['OH', 'Columbus', 'Columbus Crew Stadium', '$total'], 'current': {'count': 686, 'metrics': {}}}, {'group': ['OH', 'Columbus', 'Nationwide Arena', '$total'], 'current': {'count': 865, 'metrics': {}}}, {'group': ['OH', 'Dayton', 'E.J. Nutter Center', '$total'], 'current': {'count': 797, 'metrics': {}}}, {'group': ['OK', 'Oklahoma City', 'Ford Center', '$total'], 'current': {'count': 761, 'metrics': {}}}, {'group': ['ON', 'Ottawa', 'Scotiabank Place', '$total'], 'current': {'count': 789, 'metrics': {}}}, {'group': ['ON', 'Toronto', 'Air Canada Centre', '$total'], 'current': {'count': 882, 'metrics': {}}}, {'group': ['ON', 'Toronto', 'BMO Field', '$total'], 'current': {'count': 756, 'metrics': {}}}, {'group': ['ON', 'Toronto', 'Rogers Centre', '$total'], 'current': {'count': 682, 'metrics': {}}}, {'group': ['OR', 'Portland', 'Rose Garden', '$total'], 'current': {'count': 849, 'metrics': {}}}, {'group': ['PA', 'Hershey', 'Hersheypark Stadium', '$total'], 'current': {'count': 794, 'metrics': {}}}, {'group': ['PA', 'Philadelphia', 'Citizens Bank Park', '$total'], 'current': {'count': 788, 'metrics': {}}}, {'group': ['PA', 'Philadelphia', 'Lincoln Financial Field', '$total'], 'current': {'count': 694, 'metrics': {}}}, {'group': ['PA', 'Philadelphia', 'Wachovia Center', '$total'], 'current': {'count': 791, 'metrics': {}}}, {'group': ['PA', 'Pittsburgh', 'Heinz Field', '$total'], 'current': {'count': 538, 'metrics': {}}}, {'group': ['PA', 'Pittsburgh', 'Mellon Arena', '$total'], 'current': {'count': 593, 'metrics': {}}}, {'group': ['PA', 'Pittsburgh', 'PNC Park', '$total'], 'current': {'count': 813, 'metrics': {}}}, {'group': ['QC', 'Montreal', 'Bell Centre', '$total'], 'current': {'count': 555, 'metrics': {}}}, {'group': ['SC', 'Charleston', 'North Charleston Coliseum', '$total'], 'current': {'count': 837, 'metrics': {}}}, {'group': ['TN', 'Memphis', 'FedExForum', '$total'], 'current': {'count': 882, 'metrics': {}}}, {'group': ['TN', 'Nashville', 'LP Field', '$total'], 'current': {'count': 666, 'metrics': {}}}, {'group': ['TN', 'Nashville', 'Sommet Center', '$total'], 'current': {'count': 626, 'metrics': {}}}, {'group': ['TX', 'Arlington', 'Rangers BallPark in Arlington', '$total'], 'current': {'count': 711, 'metrics': {}}}, {'group': ['TX', 'Dallas', 'American Airlines Center', '$total'], 'current': {'count': 682, 'metrics': {}}}, {'group': ['TX', 'Dallas', 'Superpages.com Center', '$total'], 'current': {'count': 742, 'metrics': {}}}, {'group': ['TX', 'Frisco', 'Pizza Hut Park', '$total'], 'current': {'count': 866, 'metrics': {}}}, {'group': ['TX', 'Galveston', 'Grand 1894 Opera House', '$total'], 'current': {'count': 1082, 'metrics': {}}}, {'group': ['TX', 'Houston', 'Minute Maid Park', '$total'], 'current': {'count': 780, 'metrics': {}}}, {'group': ['TX', 'Houston', 'Reliant Stadium', '$total'], 'current': {'count': 829, 'metrics': {}}}, {'group': ['TX', 'Houston', 'Robertson Stadium', '$total'], 'current': {'count': 817, 'metrics': {}}}, {'group': ['TX', 'Houston', 'Toyota Center', '$total'], 'current': {'count': 628, 'metrics': {}}}, {'group': ['TX', 'Irving', 'Texas Stadium', '$total'], 'current': {'count': 516, 'metrics': {}}}, {'group': ['TX', 'San Antonio', 'AT&T Center', '$total'], 'current': {'count': 708, 'metrics': {}}}, {'group': ['UT', 'Salt Lake City', 'EnergySolutions Arena', '$total'], 'current': {'count': 602, 'metrics': {}}}, {'group': ['UT', 'Salt Lake City', 'Rice-Eccles Stadium', '$total'], 'current': {'count': 768, 'metrics': {}}}, {'group': ['WA', 'Seattle', 'Paramount Theatre', '$total'], 'current': {'count': 1147, 'metrics': {}}}, {'group': ['WA', 'Seattle', 'Qwest Field', '$total'], 'current': {'count': 770, 'metrics': {}}}, {'group': ['WA', 'Seattle', 'Safeco Field', '$total'], 'current': {'count': 682, 'metrics': {}}}, {'group': ['WI', 'Green Bay', 'Lambeau Field', '$total'], 'current': {'count': 921, 'metrics': {}}}, {'group': ['WI', 'Milwaukee', 'Bradley Center', '$total'], 'current': {'count': 705, 'metrics': {}}}, {'group': ['WI', 'Milwaukee', 'Miller Park', '$total'], 'current': {'count': 1100, 'metrics': {}}}, {'group': ['Concerts', 'Pop', '$columnTotal'], 'current': {'count': 97582, 'metrics': {}}}, {'group': ['Shows', 'Musicals', '$columnTotal'], 'current': {'count': 25737, 'metrics': {}}}, {'group': ['Shows', 'Opera', '$columnTotal'], 'current': {'count': 9914, 'metrics': {}}}, {'group': ['Shows', 'Plays', '$columnTotal'], 'current': {'count': 39223, 'metrics': {}}}, {'group': ['$absoluteTotal'], 'current': {'count': 172456, 'metrics': {}}}], 'visualization': 'Pivot Table'}
    TS_PIVOT_ROWS_METRICS_NO_COLUMNS_RESULT = {'data': [{'group': ['AB', 'Calgary', 'Pengrowth Saddledome'], 'current': {'count': 372, 'metrics': {'commission': {'avg': 105.68185483870968}, 'qtysold': {'sum': 728.0}}}}, {'group': ['AB', 'Edmonton', 'Rexall Place'], 'current': {'count': 1036, 'metrics': {'commission': {'avg': 92.30777027027028}, 'qtysold': {'sum': 2021.0}}}}, {'group': ['AZ', 'Glendale', 'Jobing.com Arena'], 'current': {'count': 1145, 'metrics': {'commission': {'avg': 95.21174672489083}, 'qtysold': {'sum': 2308.0}}}}, {'group': ['AZ', 'Glendale', 'University of Phoenix Stadium'], 'current': {'count': 698, 'metrics': {'commission': {'avg': 103.21719197707738}, 'qtysold': {'sum': 1408.0}}}}, {'group': ['AZ', 'Phoenix', 'Chase Field'], 'current': {'count': 799, 'metrics': {'commission': {'avg': 88.26683354192741}, 'qtysold': {'sum': 1582.0}}}}, {'group': ['AZ', 'Phoenix', 'US Airways Center'], 'current': {'count': 962, 'metrics': {'commission': {'avg': 92.2864864864865}, 'qtysold': {'sum': 1949.0}}}}, {'group': ['BC', 'Vancouver', 'General Motors Place'], 'current': {'count': 741, 'metrics': {'commission': {'avg': 93.04291497975709}, 'qtysold': {'sum': 1456.0}}}}, {'group': ['CA', 'Anaheim', 'Angel Stadium of Anaheim'], 'current': {'count': 746, 'metrics': {'commission': {'avg': 96.92754691689008}, 'qtysold': {'sum': 1507.0}}}}, {'group': ['CA', 'Anaheim', 'Honda Center'], 'current': {'count': 647, 'metrics': {'commission': {'avg': 87.79428129829985}, 'qtysold': {'sum': 1293.0}}}}, {'group': ['CA', 'Carson', 'The Home Depot Center'], 'current': {'count': 775, 'metrics': {'commission': {'avg': 97.25264516129033}, 'qtysold': {'sum': 1558.0}}}}, {'group': ['CA', 'Los Angeles', 'Dodger Stadium'], 'current': {'count': 931, 'metrics': {'commission': {'avg': 92.84436090225564}, 'qtysold': {'sum': 1822.0}}}}, {'group': ['CA', 'Los Angeles', 'Geffen Playhouse'], 'current': {'count': 1215, 'metrics': {'commission': {'avg': 92.70777777777778}, 'qtysold': {'sum': 2437.0}}}}, {'group': ['CA', 'Los Angeles', 'Greek Theatre'], 'current': {'count': 1220, 'metrics': {'commission': {'avg': 103.14565573770491}, 'qtysold': {'sum': 2445.0}}}}, {'group': ['CA', 'Los Angeles', 'Los Angeles Opera'], 'current': {'count': 869, 'metrics': {'commission': {'avg': 98.50581127733027}, 'qtysold': {'sum': 1756.0}}}}, {'group': ['CA', 'Los Angeles', 'Royce Hall'], 'current': {'count': 1005, 'metrics': {'commission': {'avg': 103.88014925373135}, 'qtysold': {'sum': 1992.0}}}}, {'group': ['CA', 'Los Angeles', 'Staples Center'], 'current': {'count': 782, 'metrics': {'commission': {'avg': 91.09047314578005}, 'qtysold': {'sum': 1548.0}}}}, {'group': ['CA', 'Mountain View', 'Shoreline Amphitheatre'], 'current': {'count': 1008, 'metrics': {'commission': {'avg': 99.87961309523808}, 'qtysold': {'sum': 1987.0}}}}, {'group': ['CA', 'Oakland', 'McAfee Coliseum'], 'current': {'count': 818, 'metrics': {'commission': {'avg': 92.2809902200489}, 'qtysold': {'sum': 1648.0}}}}, {'group': ['CA', 'Oakland', 'Oracle Arena'], 'current': {'count': 802, 'metrics': {'commission': {'avg': 93.68472568578552}, 'qtysold': {'sum': 1594.0}}}}, {'group': ['CA', 'Pasadena', 'Pasadena Playhouse'], 'current': {'count': 1373, 'metrics': {'commission': {'avg': 89.6323743627094}, 'qtysold': {'sum': 2739.0}}}}, {'group': ['CA', 'Redwood City', 'Fox Theatre'], 'current': {'count': 727, 'metrics': {'commission': {'avg': 93.09759284731774}, 'qtysold': {'sum': 1463.0}}}}, {'group': ['CA', 'Sacramento', 'ARCO Arena'], 'current': {'count': 905, 'metrics': {'commission': {'avg': 97.46834254143647}, 'qtysold': {'sum': 1789.0}}}}, {'group': ['CA', 'San Diego', 'PETCO Park'], 'current': {'count': 942, 'metrics': {'commission': {'avg': 104.73550955414014}, 'qtysold': {'sum': 1907.0}}}}, {'group': ['CA', 'San Diego', 'Qualcomm Stadium'], 'current': {'count': 862, 'metrics': {'commission': {'avg': 102.51073085846868}, 'qtysold': {'sum': 1774.0}}}}, {'group': ['CA', 'San Francisco', 'AT&T Park'], 'current': {'count': 658, 'metrics': {'commission': {'avg': 101.76041033434652}, 'qtysold': {'sum': 1315.0}}}}, {'group': ['CA', 'San Francisco', 'Curran Theatre'], 'current': {'count': 835, 'metrics': {'commission': {'avg': 110.12586826347307}, 'qtysold': {'sum': 1641.0}}}}, {'group': ['CA', 'San Francisco', 'Monster Park'], 'current': {'count': 523, 'metrics': {'commission': {'avg': 100.1586998087954}, 'qtysold': {'sum': 1050.0}}}}, {'group': ['CA', 'San Francisco', 'San Francisco Opera'], 'current': {'count': 1042, 'metrics': {'commission': {'avg': 95.43627639155471}, 'qtysold': {'sum': 2075.0}}}}, {'group': ['CA', 'San Francisco', 'War Memorial Opera House'], 'current': {'count': 830, 'metrics': {'commission': {'avg': 100.95939759036145}, 'qtysold': {'sum': 1691.0}}}}, {'group': ['CA', 'San Jose', 'HP Pavilion at San Jose'], 'current': {'count': 861, 'metrics': {'commission': {'avg': 95.11707317073171}, 'qtysold': {'sum': 1727.0}}}}, {'group': ['CA', 'San Jose', 'San Jose Repertory Theatre'], 'current': {'count': 1027, 'metrics': {'commission': {'avg': 94.4807205452775}, 'qtysold': {'sum': 2068.0}}}}, {'group': ['CA', 'Santa Clara', 'Buck Shaw Stadium'], 'current': {'count': 933, 'metrics': {'commission': {'avg': 94.80514469453377}, 'qtysold': {'sum': 1898.0}}}}, {'group': ['CA', 'Saratoga', 'Mountain Winery'], 'current': {'count': 648, 'metrics': {'commission': {'avg': 100.4099537037037}, 'qtysold': {'sum': 1337.0}}}}, {'group': ['CA', 'Saratoga', 'Villa Montalvo'], 'current': {'count': 719, 'metrics': {'commission': {'avg': 85.92642559109875}, 'qtysold': {'sum': 1407.0}}}}, {'group': ['CO', 'Commerce City', "Dick's Sporting Goods Park"], 'current': {'count': 930, 'metrics': {'commission': {'avg': 85.69935483870967}, 'qtysold': {'sum': 1879.0}}}}, {'group': ['CO', 'Denver', 'Coors Field'], 'current': {'count': 536, 'metrics': {'commission': {'avg': 89.23348880597015}, 'qtysold': {'sum': 1029.0}}}}, {'group': ['CO', 'Denver', 'Ellie Caulkins Opera House'], 'current': {'count': 748, 'metrics': {'commission': {'avg': 95.38997326203209}, 'qtysold': {'sum': 1497.0}}}}, {'group': ['CO', 'Denver', 'INVESCO Field'], 'current': {'count': 679, 'metrics': {'commission': {'avg': 93.91745213549336}, 'qtysold': {'sum': 1373.0}}}}, {'group': ['CO', 'Denver', 'Pepsi Center'], 'current': {'count': 689, 'metrics': {'commission': {'avg': 107.05907111756169}, 'qtysold': {'sum': 1367.0}}}}, {'group': ['DC', 'Washington', 'Kennedy Center Opera House'], 'current': {'count': 1085, 'metrics': {'commission': {'avg': 107.63958525345622}, 'qtysold': {'sum': 2175.0}}}}, {'group': ['DC', 'Washington', 'Nationals Park'], 'current': {'count': 668, 'metrics': {'commission': {'avg': 91.04303892215569}, 'qtysold': {'sum': 1305.0}}}}, {'group': ['DC', 'Washington', 'RFK Stadium'], 'current': {'count': 708, 'metrics': {'commission': {'avg': 91.33940677966102}, 'qtysold': {'sum': 1402.0}}}}, {'group': ['DC', 'Washington', 'Verizon Center'], 'current': {'count': 921, 'metrics': {'commission': {'avg': 97.7270358306189}, 'qtysold': {'sum': 1855.0}}}}, {'group': ['FL', 'Jacksonville', 'Jacksonville Municipal Stadium'], 'current': {'count': 657, 'metrics': {'commission': {'avg': 102.01141552511416}, 'qtysold': {'sum': 1350.0}}}}, {'group': ['FL', 'Miami', 'American Airlines Arena'], 'current': {'count': 792, 'metrics': {'commission': {'avg': 93.41856060606061}, 'qtysold': {'sum': 1579.0}}}}, {'group': ['FL', 'Miami Gardens', 'Dolphin Stadium'], 'current': {'count': 871, 'metrics': {'commission': {'avg': 93.74018369690012}, 'qtysold': {'sum': 1753.0}}}}, {'group': ['FL', 'Orlando', 'Amway Arena'], 'current': {'count': 784, 'metrics': {'commission': {'avg': 95.54713010204081}, 'qtysold': {'sum': 1567.0}}}}, {'group': ['FL', 'St. Petersburg', 'Tropicana Field'], 'current': {'count': 730, 'metrics': {'commission': {'avg': 88.69849315068494}, 'qtysold': {'sum': 1431.0}}}}, {'group': ['FL', 'Sunrise', 'BankAtlantic Center'], 'current': {'count': 445, 'metrics': {'commission': {'avg': 96.68595505617978}, 'qtysold': {'sum': 879.0}}}}, {'group': ['FL', 'Tampa', 'Raymond James Stadium'], 'current': {'count': 581, 'metrics': {'commission': {'avg': 103.36368330464717}, 'qtysold': {'sum': 1187.0}}}}, {'group': ['FL', 'Tampa', 'St. Pete Times Forum'], 'current': {'count': 579, 'metrics': {'commission': {'avg': 101.31554404145078}, 'qtysold': {'sum': 1201.0}}}}, {'group': ['GA', 'Atlanta', 'Georgia Dome'], 'current': {'count': 763, 'metrics': {'commission': {'avg': 97.29082568807338}, 'qtysold': {'sum': 1559.0}}}}, {'group': ['GA', 'Atlanta', 'Philips Arena'], 'current': {'count': 568, 'metrics': {'commission': {'avg': 98.17896126760563}, 'qtysold': {'sum': 1136.0}}}}, {'group': ['GA', 'Atlanta', 'Turner Field'], 'current': {'count': 745, 'metrics': {'commission': {'avg': 97.60530201342281}, 'qtysold': {'sum': 1473.0}}}}, {'group': ['IL', 'Bridgeview', 'Toyota Park'], 'current': {'count': 857, 'metrics': {'commission': {'avg': 90.58162193698949}, 'qtysold': {'sum': 1699.0}}}}, {'group': ['IL', 'Chicago', 'Lyric Opera House'], 'current': {'count': 1013, 'metrics': {'commission': {'avg': 103.63682132280356}, 'qtysold': {'sum': 2006.0}}}}, {'group': ['IL', 'Chicago', 'Soldier Field'], 'current': {'count': 673, 'metrics': {'commission': {'avg': 99.65839524517088}, 'qtysold': {'sum': 1349.0}}}}, {'group': ['IL', 'Chicago', 'U.S. Cellular Field'], 'current': {'count': 794, 'metrics': {'commission': {'avg': 97.20717884130983}, 'qtysold': {'sum': 1602.0}}}}, {'group': ['IL', 'Chicago', 'United Center'], 'current': {'count': 753, 'metrics': {'commission': {'avg': 102.1272908366534}, 'qtysold': {'sum': 1537.0}}}}, {'group': ['IL', 'Chicago', 'Wrigley Field'], 'current': {'count': 653, 'metrics': {'commission': {'avg': 102.08705972434916}, 'qtysold': {'sum': 1331.0}}}}, {'group': ['IN', 'Indianapolis', 'Conseco Fieldhouse'], 'current': {'count': 534, 'metrics': {'commission': {'avg': 90.48932584269663}, 'qtysold': {'sum': 1095.0}}}}, {'group': ['IN', 'Indianapolis', 'Lucas Oil Stadium'], 'current': {'count': 656, 'metrics': {'commission': {'avg': 93.69146341463414}, 'qtysold': {'sum': 1293.0}}}}, {'group': ['KS', 'Kansas City', 'CommunityAmerica Ballpark'], 'current': {'count': 555, 'metrics': {'commission': {'avg': 93.23297297297297}, 'qtysold': {'sum': 1151.0}}}}, {'group': ['LA', 'New Orleans', 'Louisiana Superdome'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 90.66821471652594}, 'qtysold': {'sum': 1677.0}}}}, {'group': ['LA', 'New Orleans', 'New Orleans Arena'], 'current': {'count': 681, 'metrics': {'commission': {'avg': 95.7057268722467}, 'qtysold': {'sum': 1377.0}}}}, {'group': ['MA', 'Boston', 'Charles Playhouse'], 'current': {'count': 1244, 'metrics': {'commission': {'avg': 103.33975080385852}, 'qtysold': {'sum': 2502.0}}}}, {'group': ['MA', 'Boston', 'Fenway Park'], 'current': {'count': 727, 'metrics': {'commission': {'avg': 85.51733149931223}, 'qtysold': {'sum': 1404.0}}}}, {'group': ['MA', 'Boston', 'TD Banknorth Garden'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 84.86019300361882}, 'qtysold': {'sum': 1667.0}}}}, {'group': ['MA', 'Foxborough', 'Gillette Stadium'], 'current': {'count': 562, 'metrics': {'commission': {'avg': 101.1894128113879}, 'qtysold': {'sum': 1094.0}}}}, {'group': ['MD', 'Baltimore', 'Lyric Opera House'], 'current': {'count': 1154, 'metrics': {'commission': {'avg': 97.08925476603119}, 'qtysold': {'sum': 2305.0}}}}, {'group': ['MD', 'Baltimore', 'M&T Bank Stadium'], 'current': {'count': 836, 'metrics': {'commission': {'avg': 107.96232057416267}, 'qtysold': {'sum': 1688.0}}}}, {'group': ['MD', 'Baltimore', 'Oriole Park at Camden Yards'], 'current': {'count': 941, 'metrics': {'commission': {'avg': 96.13071200850159}, 'qtysold': {'sum': 1878.0}}}}, {'group': ['MD', 'Landover', 'FedExField'], 'current': {'count': 858, 'metrics': {'commission': {'avg': 96.0340909090909}, 'qtysold': {'sum': 1730.0}}}}, {'group': ['MI', 'Auburn Hills', 'The Palace of Auburn Hills'], 'current': {'count': 858, 'metrics': {'commission': {'avg': 94.67115384615386}, 'qtysold': {'sum': 1717.0}}}}, {'group': ['MI', 'Detroit', 'Comerica Park'], 'current': {'count': 568, 'metrics': {'commission': {'avg': 96.39110915492958}, 'qtysold': {'sum': 1124.0}}}}, {'group': ['MI', 'Detroit', 'Detroit Opera House'], 'current': {'count': 1003, 'metrics': {'commission': {'avg': 90.81550348953141}, 'qtysold': {'sum': 2008.0}}}}, {'group': ['MI', 'Detroit', 'Ford Field'], 'current': {'count': 624, 'metrics': {'commission': {'avg': 93.95745192307692}, 'qtysold': {'sum': 1222.0}}}}, {'group': ['MI', 'Detroit', 'Joe Louis Arena'], 'current': {'count': 736, 'metrics': {'commission': {'avg': 104.90176630434782}, 'qtysold': {'sum': 1485.0}}}}, {'group': ['MN', 'Minneapolis', 'Hubert H. Humphrey Metrodome'], 'current': {'count': 651, 'metrics': {'commission': {'avg': 88.21958525345622}, 'qtysold': {'sum': 1311.0}}}}, {'group': ['MN', 'Minneapolis', 'Target Center'], 'current': {'count': 758, 'metrics': {'commission': {'avg': 99.10092348284961}, 'qtysold': {'sum': 1514.0}}}}, {'group': ['MN', 'Minneapolis', 'The Guthrie Theater'], 'current': {'count': 943, 'metrics': {'commission': {'avg': 103.7475079533404}, 'qtysold': {'sum': 1883.0}}}}, {'group': ['MN', 'St. Paul', 'Xcel Energy Center'], 'current': {'count': 828, 'metrics': {'commission': {'avg': 103.17409420289854}, 'qtysold': {'sum': 1663.0}}}}, {'group': ['MO', 'Kansas City', 'Arrowhead Stadium'], 'current': {'count': 603, 'metrics': {'commission': {'avg': 83.18134328358208}, 'qtysold': {'sum': 1160.0}}}}, {'group': ['MO', 'Kansas City', 'Kauffman Stadium'], 'current': {'count': 554, 'metrics': {'commission': {'avg': 101.24485559566787}, 'qtysold': {'sum': 1125.0}}}}, {'group': ['MO', 'St. Louis', 'Busch Stadium'], 'current': {'count': 737, 'metrics': {'commission': {'avg': 93.25257801899592}, 'qtysold': {'sum': 1449.0}}}}, {'group': ['MO', 'St. Louis', 'Edward Jones Dome'], 'current': {'count': 895, 'metrics': {'commission': {'avg': 104.81916201117318}, 'qtysold': {'sum': 1798.0}}}}, {'group': ['MO', 'St. Louis', 'Scottrade Center'], 'current': {'count': 803, 'metrics': {'commission': {'avg': 96.8194894146949}, 'qtysold': {'sum': 1608.0}}}}, {'group': ['NC', 'Charlotte', 'Bank of America Stadium'], 'current': {'count': 711, 'metrics': {'commission': {'avg': 92.35063291139241}, 'qtysold': {'sum': 1412.0}}}}, {'group': ['NC', 'Charlotte', 'Time Warner Cable Arena'], 'current': {'count': 599, 'metrics': {'commission': {'avg': 85.6915692821369}, 'qtysold': {'sum': 1221.0}}}}, {'group': ['NC', 'Raleigh', 'RBC Center'], 'current': {'count': 714, 'metrics': {'commission': {'avg': 96.1623949579832}, 'qtysold': {'sum': 1417.0}}}}, {'group': ['NJ', 'East Rutherford', 'Izod Center'], 'current': {'count': 826, 'metrics': {'commission': {'avg': 97.1115617433414}, 'qtysold': {'sum': 1702.0}}}}, {'group': ['NJ', 'East Rutherford', 'New York Giants Stadium'], 'current': {'count': 805, 'metrics': {'commission': {'avg': 89.8039751552795}, 'qtysold': {'sum': 1609.0}}}}, {'group': ['NJ', 'Newark', 'Prudential Center'], 'current': {'count': 525, 'metrics': {'commission': {'avg': 92.902}, 'qtysold': {'sum': 1066.0}}}}, {'group': ['NV', 'Las Vegas', 'Ballys Hotel'], 'current': {'count': 398, 'metrics': {'commission': {'avg': 98.10000000000001}, 'qtysold': {'sum': 787.0}}}}, {'group': ['NV', 'Las Vegas', 'Bellagio Hotel'], 'current': {'count': 465, 'metrics': {'commission': {'avg': 92.73967741935483}, 'qtysold': {'sum': 951.0}}}}, {'group': ['NV', 'Las Vegas', 'Caesars Palace'], 'current': {'count': 427, 'metrics': {'commission': {'avg': 89.00620608899298}, 'qtysold': {'sum': 862.0}}}}, {'group': ['NV', 'Las Vegas', 'Harrahs Hotel'], 'current': {'count': 518, 'metrics': {'commission': {'avg': 93.98918918918919}, 'qtysold': {'sum': 1066.0}}}}, {'group': ['NV', 'Las Vegas', 'Hilton Hotel'], 'current': {'count': 418, 'metrics': {'commission': {'avg': 98.68205741626794}, 'qtysold': {'sum': 862.0}}}}, {'group': ['NV', 'Las Vegas', 'Luxor Hotel'], 'current': {'count': 671, 'metrics': {'commission': {'avg': 100.90953800298063}, 'qtysold': {'sum': 1363.0}}}}, {'group': ['NV', 'Las Vegas', 'Mandalay Bay Hotel'], 'current': {'count': 332, 'metrics': {'commission': {'avg': 88.73765060240964}, 'qtysold': {'sum': 658.0}}}}, {'group': ['NV', 'Las Vegas', 'Mirage Hotel'], 'current': {'count': 432, 'metrics': {'commission': {'avg': 107.42291666666667}, 'qtysold': {'sum': 913.0}}}}, {'group': ['NV', 'Las Vegas', 'Paris Hotel'], 'current': {'count': 309, 'metrics': {'commission': {'avg': 93.64029126213592}, 'qtysold': {'sum': 634.0}}}}, {'group': ['NV', 'Las Vegas', 'Paris MGM Grand'], 'current': {'count': 378, 'metrics': {'commission': {'avg': 92.47698412698414}, 'qtysold': {'sum': 758.0}}}}, {'group': ['NV', 'Las Vegas', 'Sahara Hotel'], 'current': {'count': 378, 'metrics': {'commission': {'avg': 96.11111111111111}, 'qtysold': {'sum': 751.0}}}}, {'group': ['NV', 'Las Vegas', 'Tropicana Hotel'], 'current': {'count': 443, 'metrics': {'commission': {'avg': 95.37799097065462}, 'qtysold': {'sum': 905.0}}}}, {'group': ['NV', 'Las Vegas', 'Venetian Hotel'], 'current': {'count': 589, 'metrics': {'commission': {'avg': 100.2455857385399}, 'qtysold': {'sum': 1158.0}}}}, {'group': ['NV', 'Las Vegas', 'Wynn Hotel'], 'current': {'count': 327, 'metrics': {'commission': {'avg': 107.62752293577981}, 'qtysold': {'sum': 660.0}}}}, {'group': ['NY', 'Buffalo', 'HSBC Arena'], 'current': {'count': 732, 'metrics': {'commission': {'avg': 95.04282786885247}, 'qtysold': {'sum': 1453.0}}}}, {'group': ['NY', 'New York City', 'Al Hirschfeld Theatre'], 'current': {'count': 1191, 'metrics': {'commission': {'avg': 97.23211586901763}, 'qtysold': {'sum': 2361.0}}}}, {'group': ['NY', 'New York City', 'Ambassador Theatre'], 'current': {'count': 1168, 'metrics': {'commission': {'avg': 101.56142979452055}, 'qtysold': {'sum': 2321.0}}}}, {'group': ['NY', 'New York City', 'American Airlines Theatre'], 'current': {'count': 929, 'metrics': {'commission': {'avg': 99.22475780409042}, 'qtysold': {'sum': 1889.0}}}}, {'group': ['NY', 'New York City', 'August Wilson Theatre'], 'current': {'count': 1583, 'metrics': {'commission': {'avg': 97.80379027163613}, 'qtysold': {'sum': 3187.0}}}}, {'group': ['NY', 'New York City', 'Belasco Theatre'], 'current': {'count': 1217, 'metrics': {'commission': {'avg': 87.27534921939196}, 'qtysold': {'sum': 2394.0}}}}, {'group': ['NY', 'New York City', 'Bernard B. Jacobs Theatre'], 'current': {'count': 1217, 'metrics': {'commission': {'avg': 96.05398520953163}, 'qtysold': {'sum': 2412.0}}}}, {'group': ['NY', 'New York City', 'Biltmore Theatre'], 'current': {'count': 1305, 'metrics': {'commission': {'avg': 95.2851724137931}, 'qtysold': {'sum': 2629.0}}}}, {'group': ['NY', 'New York City', 'Booth Theatre'], 'current': {'count': 1210, 'metrics': {'commission': {'avg': 97.16082644628099}, 'qtysold': {'sum': 2447.0}}}}, {'group': ['NY', 'New York City', 'Broadhurst Theatre'], 'current': {'count': 1055, 'metrics': {'commission': {'avg': 101.01042654028436}, 'qtysold': {'sum': 2131.0}}}}, {'group': ['NY', 'New York City', 'Brooks Atkinson Theatre'], 'current': {'count': 1013, 'metrics': {'commission': {'avg': 100.29787759131293}, 'qtysold': {'sum': 2049.0}}}}, {'group': ['NY', 'New York City', 'Carnegie Hall'], 'current': {'count': 1211, 'metrics': {'commission': {'avg': 84.96515276630883}, 'qtysold': {'sum': 2390.0}}}}, {'group': ['NY', 'New York City', 'Circle in the Square Theatre'], 'current': {'count': 1047, 'metrics': {'commission': {'avg': 93.35444126074499}, 'qtysold': {'sum': 2127.0}}}}, {'group': ['NY', 'New York City', 'Cort Theatre'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 100.08507393715342}, 'qtysold': {'sum': 2152.0}}}}, {'group': ['NY', 'New York City', 'Ethel Barrymore Theatre'], 'current': {'count': 1413, 'metrics': {'commission': {'avg': 94.60424628450106}, 'qtysold': {'sum': 2828.0}}}}, {'group': ['NY', 'New York City', "Eugene O'Neill Theatre"], 'current': {'count': 1239, 'metrics': {'commission': {'avg': 100.35714285714286}, 'qtysold': {'sum': 2488.0}}}}, {'group': ['NY', 'New York City', 'George Gershwin Theatre'], 'current': {'count': 1137, 'metrics': {'commission': {'avg': 96.40316622691293}, 'qtysold': {'sum': 2284.0}}}}, {'group': ['NY', 'New York City', 'Gerald Schoenfeld Theatre'], 'current': {'count': 1132, 'metrics': {'commission': {'avg': 91.84730565371024}, 'qtysold': {'sum': 2275.0}}}}, {'group': ['NY', 'New York City', 'Helen Hayes Theatre'], 'current': {'count': 1456, 'metrics': {'commission': {'avg': 100.83430631868131}, 'qtysold': {'sum': 2948.0}}}}, {'group': ['NY', 'New York City', 'Hilton Theatre'], 'current': {'count': 1488, 'metrics': {'commission': {'avg': 89.2828629032258}, 'qtysold': {'sum': 2999.0}}}}, {'group': ['NY', 'New York City', 'Imperial Theatre'], 'current': {'count': 1357, 'metrics': {'commission': {'avg': 97.0515475313191}, 'qtysold': {'sum': 2702.0}}}}, {'group': ['NY', 'New York City', 'John Golden Theatre'], 'current': {'count': 1208, 'metrics': {'commission': {'avg': 91.7873344370861}, 'qtysold': {'sum': 2388.0}}}}, {'group': ['NY', 'New York City', 'Lincoln Center for the Performing Arts'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 92.61959334565618}, 'qtysold': {'sum': 2155.0}}}}, {'group': ['NY', 'New York City', 'Longacre Theatre'], 'current': {'count': 1143, 'metrics': {'commission': {'avg': 102.5251968503937}, 'qtysold': {'sum': 2268.0}}}}, {'group': ['NY', 'New York City', 'Lunt-Fontanne Theatre'], 'current': {'count': 1672, 'metrics': {'commission': {'avg': 100.04623205741626}, 'qtysold': {'sum': 3326.0}}}}, {'group': ['NY', 'New York City', 'Lyceum Theatre'], 'current': {'count': 1221, 'metrics': {'commission': {'avg': 94.2}, 'qtysold': {'sum': 2470.0}}}}, {'group': ['NY', 'New York City', 'Madison Square Garden'], 'current': {'count': 923, 'metrics': {'commission': {'avg': 96.59106175514627}, 'qtysold': {'sum': 1847.0}}}}, {'group': ['NY', 'New York City', 'Majestic Theatre'], 'current': {'count': 1265, 'metrics': {'commission': {'avg': 106.0405138339921}, 'qtysold': {'sum': 2549.0}}}}, {'group': ['NY', 'New York City', 'Marquis Theatre'], 'current': {'count': 1023, 'metrics': {'commission': {'avg': 98.0991202346041}, 'qtysold': {'sum': 2027.0}}}}, {'group': ['NY', 'New York City', 'Metropolitan Opera'], 'current': {'count': 1088, 'metrics': {'commission': {'avg': 96.12973345588235}, 'qtysold': {'sum': 2132.0}}}}, {'group': ['NY', 'New York City', 'Minskoff Theatre'], 'current': {'count': 1185, 'metrics': {'commission': {'avg': 100.19949367088607}, 'qtysold': {'sum': 2329.0}}}}, {'group': ['NY', 'New York City', 'Music Box Theatre'], 'current': {'count': 963, 'metrics': {'commission': {'avg': 92.48333333333333}, 'qtysold': {'sum': 1923.0}}}}, {'group': ['NY', 'New York City', 'Nederlander Theatre'], 'current': {'count': 1465, 'metrics': {'commission': {'avg': 95.8681228668942}, 'qtysold': {'sum': 2934.0}}}}, {'group': ['NY', 'New York City', 'Neil Simon Theatre'], 'current': {'count': 1107, 'metrics': {'commission': {'avg': 96.67615176151762}, 'qtysold': {'sum': 2243.0}}}}, {'group': ['NY', 'New York City', 'New Amsterdam Theatre'], 'current': {'count': 1016, 'metrics': {'commission': {'avg': 98.37563976377952}, 'qtysold': {'sum': 2055.0}}}}, {'group': ['NY', 'New York City', 'Palace Theatre'], 'current': {'count': 1039, 'metrics': {'commission': {'avg': 94.59889316650626}, 'qtysold': {'sum': 2089.0}}}}, {'group': ['NY', 'New York City', 'Richard Rodgers Theatre'], 'current': {'count': 1099, 'metrics': {'commission': {'avg': 93.30832575068244}, 'qtysold': {'sum': 2208.0}}}}, {'group': ['NY', 'New York City', 'Shea Stadium'], 'current': {'count': 539, 'metrics': {'commission': {'avg': 99.38738404452691}, 'qtysold': {'sum': 1099.0}}}}, {'group': ['NY', 'New York City', 'Shubert Theatre'], 'current': {'count': 992, 'metrics': {'commission': {'avg': 95.96915322580645}, 'qtysold': {'sum': 1987.0}}}}, {'group': ['NY', 'New York City', 'St. James Theatre'], 'current': {'count': 958, 'metrics': {'commission': {'avg': 90.2776096033403}, 'qtysold': {'sum': 1947.0}}}}, {'group': ['NY', 'New York City', 'Studio 54'], 'current': {'count': 1146, 'metrics': {'commission': {'avg': 90.83023560209423}, 'qtysold': {'sum': 2304.0}}}}, {'group': ['NY', 'New York City', 'The Broadway Theatre'], 'current': {'count': 1118, 'metrics': {'commission': {'avg': 93.95232558139534}, 'qtysold': {'sum': 2215.0}}}}, {'group': ['NY', 'New York City', 'Vivian Beaumont Theatre'], 'current': {'count': 1055, 'metrics': {'commission': {'avg': 102.36341232227488}, 'qtysold': {'sum': 2088.0}}}}, {'group': ['NY', 'New York City', 'Walter Kerr Theatre'], 'current': {'count': 1208, 'metrics': {'commission': {'avg': 95.24031456953642}, 'qtysold': {'sum': 2401.0}}}}, {'group': ['NY', 'New York City', 'Winter Garden Theatre'], 'current': {'count': 1451, 'metrics': {'commission': {'avg': 97.09755341144037}, 'qtysold': {'sum': 2838.0}}}}, {'group': ['NY', 'New York City', 'Yankee Stadium'], 'current': {'count': 869, 'metrics': {'commission': {'avg': 109.60978135788261}, 'qtysold': {'sum': 1765.0}}}}, {'group': ['NY', 'Orchard Park', 'Ralph Wilson Stadium'], 'current': {'count': 661, 'metrics': {'commission': {'avg': 102.43888048411499}, 'qtysold': {'sum': 1327.0}}}}, {'group': ['NY', 'Saratoga Springs', 'Saratoga Springs Performing Arts Center'], 'current': {'count': 782, 'metrics': {'commission': {'avg': 95.82717391304348}, 'qtysold': {'sum': 1542.0}}}}, {'group': ['NY', 'Uniondale', 'Nassau Veterans Memorial Coliseum'], 'current': {'count': 713, 'metrics': {'commission': {'avg': 93.24635343618513}, 'qtysold': {'sum': 1451.0}}}}, {'group': [None, None, None], 'current': {'count': 2777, 'metrics': {'commission': {'avg': 96.69927979834354}, 'qtysold': {'sum': 5553.0}}}}, {'group': ['OH', 'Cincinnati', 'Great American Ball Park'], 'current': {'count': 879, 'metrics': {'commission': {'avg': 111.43105802047782}, 'qtysold': {'sum': 1758.0}}}}, {'group': ['OH', 'Cincinnati', 'Paul Brown Stadium'], 'current': {'count': 880, 'metrics': {'commission': {'avg': 88.91454545454546}, 'qtysold': {'sum': 1787.0}}}}, {'group': ['OH', 'Cleveland', 'Cleveland Browns Stadium'], 'current': {'count': 617, 'metrics': {'commission': {'avg': 106.50097244732578}, 'qtysold': {'sum': 1239.0}}}}, {'group': ['OH', 'Cleveland', 'Progressive Field'], 'current': {'count': 742, 'metrics': {'commission': {'avg': 107.71314016172506}, 'qtysold': {'sum': 1486.0}}}}, {'group': ['OH', 'Cleveland', 'Quicken Loans Arena'], 'current': {'count': 778, 'metrics': {'commission': {'avg': 90.58284061696658}, 'qtysold': {'sum': 1543.0}}}}, {'group': ['OH', 'Columbus', 'Columbus Crew Stadium'], 'current': {'count': 686, 'metrics': {'commission': {'avg': 97.54395043731778}, 'qtysold': {'sum': 1366.0}}}}, {'group': ['OH', 'Columbus', 'Nationwide Arena'], 'current': {'count': 865, 'metrics': {'commission': {'avg': 93.1864161849711}, 'qtysold': {'sum': 1700.0}}}}, {'group': ['OH', 'Dayton', 'E.J. Nutter Center'], 'current': {'count': 797, 'metrics': {'commission': {'avg': 86.60250941028858}, 'qtysold': {'sum': 1540.0}}}}, {'group': ['OK', 'Oklahoma City', 'Ford Center'], 'current': {'count': 761, 'metrics': {'commission': {'avg': 94.14086727989488}, 'qtysold': {'sum': 1502.0}}}}, {'group': ['ON', 'Ottawa', 'Scotiabank Place'], 'current': {'count': 789, 'metrics': {'commission': {'avg': 90.74182509505704}, 'qtysold': {'sum': 1598.0}}}}, {'group': ['ON', 'Toronto', 'Air Canada Centre'], 'current': {'count': 882, 'metrics': {'commission': {'avg': 100.60510204081632}, 'qtysold': {'sum': 1798.0}}}}, {'group': ['ON', 'Toronto', 'BMO Field'], 'current': {'count': 756, 'metrics': {'commission': {'avg': 92.62718253968254}, 'qtysold': {'sum': 1552.0}}}}, {'group': ['ON', 'Toronto', 'Rogers Centre'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 83.99956011730205}, 'qtysold': {'sum': 1329.0}}}}, {'group': ['OR', 'Portland', 'Rose Garden'], 'current': {'count': 849, 'metrics': {'commission': {'avg': 87.40053003533569}, 'qtysold': {'sum': 1711.0}}}}, {'group': ['PA', 'Hershey', 'Hersheypark Stadium'], 'current': {'count': 794, 'metrics': {'commission': {'avg': 96.34609571788414}, 'qtysold': {'sum': 1554.0}}}}, {'group': ['PA', 'Philadelphia', 'Citizens Bank Park'], 'current': {'count': 788, 'metrics': {'commission': {'avg': 109.20989847715735}, 'qtysold': {'sum': 1620.0}}}}, {'group': ['PA', 'Philadelphia', 'Lincoln Financial Field'], 'current': {'count': 694, 'metrics': {'commission': {'avg': 93.15410662824208}, 'qtysold': {'sum': 1390.0}}}}, {'group': ['PA', 'Philadelphia', 'Wachovia Center'], 'current': {'count': 791, 'metrics': {'commission': {'avg': 96.54481668773704}, 'qtysold': {'sum': 1593.0}}}}, {'group': ['PA', 'Pittsburgh', 'Heinz Field'], 'current': {'count': 538, 'metrics': {'commission': {'avg': 89.25920074349442}, 'qtysold': {'sum': 1040.0}}}}, {'group': ['PA', 'Pittsburgh', 'Mellon Arena'], 'current': {'count': 593, 'metrics': {'commission': {'avg': 109.46964586846543}, 'qtysold': {'sum': 1176.0}}}}, {'group': ['PA', 'Pittsburgh', 'PNC Park'], 'current': {'count': 813, 'metrics': {'commission': {'avg': 100.03911439114391}, 'qtysold': {'sum': 1649.0}}}}, {'group': ['QC', 'Montreal', 'Bell Centre'], 'current': {'count': 555, 'metrics': {'commission': {'avg': 99.7481081081081}, 'qtysold': {'sum': 1123.0}}}}, {'group': ['SC', 'Charleston', 'North Charleston Coliseum'], 'current': {'count': 837, 'metrics': {'commission': {'avg': 101.26290322580645}, 'qtysold': {'sum': 1719.0}}}}, {'group': ['TN', 'Memphis', 'FedExForum'], 'current': {'count': 882, 'metrics': {'commission': {'avg': 95.33401360544218}, 'qtysold': {'sum': 1764.0}}}}, {'group': ['TN', 'Nashville', 'LP Field'], 'current': {'count': 666, 'metrics': {'commission': {'avg': 101.55202702702702}, 'qtysold': {'sum': 1330.0}}}}, {'group': ['TN', 'Nashville', 'Sommet Center'], 'current': {'count': 626, 'metrics': {'commission': {'avg': 92.69712460063899}, 'qtysold': {'sum': 1288.0}}}}, {'group': ['TX', 'Arlington', 'Rangers BallPark in Arlington'], 'current': {'count': 711, 'metrics': {'commission': {'avg': 89.17257383966245}, 'qtysold': {'sum': 1428.0}}}}, {'group': ['TX', 'Dallas', 'American Airlines Center'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 90.375}, 'qtysold': {'sum': 1347.0}}}}, {'group': ['TX', 'Dallas', 'Superpages.com Center'], 'current': {'count': 742, 'metrics': {'commission': {'avg': 90.65033692722372}, 'qtysold': {'sum': 1481.0}}}}, {'group': ['TX', 'Frisco', 'Pizza Hut Park'], 'current': {'count': 866, 'metrics': {'commission': {'avg': 99.03412240184758}, 'qtysold': {'sum': 1735.0}}}}, {'group': ['TX', 'Galveston', 'Grand 1894 Opera House'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 91.13664510166359}, 'qtysold': {'sum': 2142.0}}}}, {'group': ['TX', 'Houston', 'Minute Maid Park'], 'current': {'count': 780, 'metrics': {'commission': {'avg': 97.1546153846154}, 'qtysold': {'sum': 1553.0}}}}, {'group': ['TX', 'Houston', 'Reliant Stadium'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 95.29270205066344}, 'qtysold': {'sum': 1684.0}}}}, {'group': ['TX', 'Houston', 'Robertson Stadium'], 'current': {'count': 817, 'metrics': {'commission': {'avg': 99.72576499388005}, 'qtysold': {'sum': 1637.0}}}}, {'group': ['TX', 'Houston', 'Toyota Center'], 'current': {'count': 628, 'metrics': {'commission': {'avg': 97.96074840764331}, 'qtysold': {'sum': 1269.0}}}}, {'group': ['TX', 'Irving', 'Texas Stadium'], 'current': {'count': 516, 'metrics': {'commission': {'avg': 101.7392441860465}, 'qtysold': {'sum': 1028.0}}}}, {'group': ['TX', 'San Antonio', 'AT&T Center'], 'current': {'count': 708, 'metrics': {'commission': {'avg': 100.4489406779661}, 'qtysold': {'sum': 1426.0}}}}, {'group': ['UT', 'Salt Lake City', 'EnergySolutions Arena'], 'current': {'count': 602, 'metrics': {'commission': {'avg': 93.53421926910299}, 'qtysold': {'sum': 1158.0}}}}, {'group': ['UT', 'Salt Lake City', 'Rice-Eccles Stadium'], 'current': {'count': 768, 'metrics': {'commission': {'avg': 92.0978515625}, 'qtysold': {'sum': 1534.0}}}}, {'group': ['WA', 'Seattle', 'Paramount Theatre'], 'current': {'count': 1147, 'metrics': {'commission': {'avg': 93.5312118570183}, 'qtysold': {'sum': 2326.0}}}}, {'group': ['WA', 'Seattle', 'Qwest Field'], 'current': {'count': 770, 'metrics': {'commission': {'avg': 93.83571428571429}, 'qtysold': {'sum': 1543.0}}}}, {'group': ['WA', 'Seattle', 'Safeco Field'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 90.6050586510264}, 'qtysold': {'sum': 1373.0}}}}, {'group': ['WI', 'Green Bay', 'Lambeau Field'], 'current': {'count': 921, 'metrics': {'commission': {'avg': 92.20684039087948}, 'qtysold': {'sum': 1845.0}}}}, {'group': ['WI', 'Milwaukee', 'Bradley Center'], 'current': {'count': 705, 'metrics': {'commission': {'avg': 100.02914893617022}, 'qtysold': {'sum': 1428.0}}}}, {'group': ['WI', 'Milwaukee', 'Miller Park'], 'current': {'count': 1100, 'metrics': {'commission': {'avg': 96.67936363636363}, 'qtysold': {'sum': 2207.0}}}}, {'group': ['$columnTotal'], 'current': {'count': 172456, 'metrics': {'commission': {'avg': 96.34234036507864}, 'qtysold': {'sum': 345349.0}}}}, {'group': ['$absoluteTotal'], 'current': {'count': 172456, 'metrics': {'commission': {'avg': 96.34234036507864}, 'qtysold': {'sum': 345349.0}}}}], 'visualization': 'Pivot Table'}
    TS_PIVOT_COLUMNS_ROWS_METRICS_RESULT = {'data': [{'group': ['AB', 'Calgary', 'Pengrowth Saddledome', 'Concerts', 'Pop'], 'current': {'count': 372, 'metrics': {'commission': {'avg': 105.68185483870968}, 'qtysold': {'sum': 728.0}}}}, {'group': ['AB', 'Edmonton', 'Rexall Place', 'Concerts', 'Pop'], 'current': {'count': 1036, 'metrics': {'commission': {'avg': 92.30777027027028}, 'qtysold': {'sum': 2021.0}}}}, {'group': ['AZ', 'Glendale', 'Jobing.com Arena', 'Concerts', 'Pop'], 'current': {'count': 1145, 'metrics': {'commission': {'avg': 95.21174672489083}, 'qtysold': {'sum': 2308.0}}}}, {'group': ['AZ', 'Glendale', 'University of Phoenix Stadium', 'Concerts', 'Pop'], 'current': {'count': 698, 'metrics': {'commission': {'avg': 103.21719197707738}, 'qtysold': {'sum': 1408.0}}}}, {'group': ['AZ', 'Phoenix', 'Chase Field', 'Concerts', 'Pop'], 'current': {'count': 799, 'metrics': {'commission': {'avg': 88.26683354192741}, 'qtysold': {'sum': 1582.0}}}}, {'group': ['AZ', 'Phoenix', 'US Airways Center', 'Concerts', 'Pop'], 'current': {'count': 962, 'metrics': {'commission': {'avg': 92.2864864864865}, 'qtysold': {'sum': 1949.0}}}}, {'group': ['BC', 'Vancouver', 'General Motors Place', 'Concerts', 'Pop'], 'current': {'count': 741, 'metrics': {'commission': {'avg': 93.04291497975709}, 'qtysold': {'sum': 1456.0}}}}, {'group': ['CA', 'Anaheim', 'Angel Stadium of Anaheim', 'Concerts', 'Pop'], 'current': {'count': 746, 'metrics': {'commission': {'avg': 96.92754691689008}, 'qtysold': {'sum': 1507.0}}}}, {'group': ['CA', 'Anaheim', 'Honda Center', 'Concerts', 'Pop'], 'current': {'count': 647, 'metrics': {'commission': {'avg': 87.79428129829985}, 'qtysold': {'sum': 1293.0}}}}, {'group': ['CA', 'Carson', 'The Home Depot Center', 'Concerts', 'Pop'], 'current': {'count': 775, 'metrics': {'commission': {'avg': 97.25264516129033}, 'qtysold': {'sum': 1558.0}}}}, {'group': ['CA', 'Los Angeles', 'Dodger Stadium', 'Concerts', 'Pop'], 'current': {'count': 931, 'metrics': {'commission': {'avg': 92.84436090225564}, 'qtysold': {'sum': 1822.0}}}}, {'group': ['CA', 'Los Angeles', 'Staples Center', 'Concerts', 'Pop'], 'current': {'count': 782, 'metrics': {'commission': {'avg': 91.09047314578005}, 'qtysold': {'sum': 1548.0}}}}, {'group': ['CA', 'Mountain View', 'Shoreline Amphitheatre', 'Concerts', 'Pop'], 'current': {'count': 1008, 'metrics': {'commission': {'avg': 99.87961309523808}, 'qtysold': {'sum': 1987.0}}}}, {'group': ['CA', 'Oakland', 'McAfee Coliseum', 'Concerts', 'Pop'], 'current': {'count': 818, 'metrics': {'commission': {'avg': 92.2809902200489}, 'qtysold': {'sum': 1648.0}}}}, {'group': ['CA', 'Oakland', 'Oracle Arena', 'Concerts', 'Pop'], 'current': {'count': 802, 'metrics': {'commission': {'avg': 93.68472568578552}, 'qtysold': {'sum': 1594.0}}}}, {'group': ['CA', 'Redwood City', 'Fox Theatre', 'Concerts', 'Pop'], 'current': {'count': 727, 'metrics': {'commission': {'avg': 93.09759284731774}, 'qtysold': {'sum': 1463.0}}}}, {'group': ['CA', 'Sacramento', 'ARCO Arena', 'Concerts', 'Pop'], 'current': {'count': 905, 'metrics': {'commission': {'avg': 97.46834254143647}, 'qtysold': {'sum': 1789.0}}}}, {'group': ['CA', 'San Diego', 'PETCO Park', 'Concerts', 'Pop'], 'current': {'count': 942, 'metrics': {'commission': {'avg': 104.73550955414014}, 'qtysold': {'sum': 1907.0}}}}, {'group': ['CA', 'San Diego', 'Qualcomm Stadium', 'Concerts', 'Pop'], 'current': {'count': 862, 'metrics': {'commission': {'avg': 102.51073085846868}, 'qtysold': {'sum': 1774.0}}}}, {'group': ['CA', 'San Francisco', 'AT&T Park', 'Concerts', 'Pop'], 'current': {'count': 658, 'metrics': {'commission': {'avg': 101.76041033434652}, 'qtysold': {'sum': 1315.0}}}}, {'group': ['CA', 'San Francisco', 'Monster Park', 'Concerts', 'Pop'], 'current': {'count': 523, 'metrics': {'commission': {'avg': 100.1586998087954}, 'qtysold': {'sum': 1050.0}}}}, {'group': ['CA', 'San Jose', 'HP Pavilion at San Jose', 'Concerts', 'Pop'], 'current': {'count': 861, 'metrics': {'commission': {'avg': 95.11707317073171}, 'qtysold': {'sum': 1727.0}}}}, {'group': ['CA', 'Santa Clara', 'Buck Shaw Stadium', 'Concerts', 'Pop'], 'current': {'count': 933, 'metrics': {'commission': {'avg': 94.80514469453377}, 'qtysold': {'sum': 1898.0}}}}, {'group': ['CA', 'Saratoga', 'Mountain Winery', 'Concerts', 'Pop'], 'current': {'count': 648, 'metrics': {'commission': {'avg': 100.4099537037037}, 'qtysold': {'sum': 1337.0}}}}, {'group': ['CA', 'Saratoga', 'Villa Montalvo', 'Concerts', 'Pop'], 'current': {'count': 719, 'metrics': {'commission': {'avg': 85.92642559109875}, 'qtysold': {'sum': 1407.0}}}}, {'group': ['CO', 'Commerce City', "Dick's Sporting Goods Park", 'Concerts', 'Pop'], 'current': {'count': 930, 'metrics': {'commission': {'avg': 85.69935483870967}, 'qtysold': {'sum': 1879.0}}}}, {'group': ['CO', 'Denver', 'Coors Field', 'Concerts', 'Pop'], 'current': {'count': 536, 'metrics': {'commission': {'avg': 89.23348880597015}, 'qtysold': {'sum': 1029.0}}}}, {'group': ['CO', 'Denver', 'INVESCO Field', 'Concerts', 'Pop'], 'current': {'count': 679, 'metrics': {'commission': {'avg': 93.91745213549336}, 'qtysold': {'sum': 1373.0}}}}, {'group': ['CO', 'Denver', 'Pepsi Center', 'Concerts', 'Pop'], 'current': {'count': 689, 'metrics': {'commission': {'avg': 107.05907111756169}, 'qtysold': {'sum': 1367.0}}}}, {'group': ['DC', 'Washington', 'Nationals Park', 'Concerts', 'Pop'], 'current': {'count': 668, 'metrics': {'commission': {'avg': 91.04303892215569}, 'qtysold': {'sum': 1305.0}}}}, {'group': ['DC', 'Washington', 'RFK Stadium', 'Concerts', 'Pop'], 'current': {'count': 708, 'metrics': {'commission': {'avg': 91.33940677966102}, 'qtysold': {'sum': 1402.0}}}}, {'group': ['DC', 'Washington', 'Verizon Center', 'Concerts', 'Pop'], 'current': {'count': 921, 'metrics': {'commission': {'avg': 97.7270358306189}, 'qtysold': {'sum': 1855.0}}}}, {'group': ['FL', 'Jacksonville', 'Jacksonville Municipal Stadium', 'Concerts', 'Pop'], 'current': {'count': 657, 'metrics': {'commission': {'avg': 102.01141552511416}, 'qtysold': {'sum': 1350.0}}}}, {'group': ['FL', 'Miami', 'American Airlines Arena', 'Concerts', 'Pop'], 'current': {'count': 792, 'metrics': {'commission': {'avg': 93.41856060606061}, 'qtysold': {'sum': 1579.0}}}}, {'group': ['FL', 'Miami Gardens', 'Dolphin Stadium', 'Concerts', 'Pop'], 'current': {'count': 871, 'metrics': {'commission': {'avg': 93.74018369690012}, 'qtysold': {'sum': 1753.0}}}}, {'group': ['FL', 'Orlando', 'Amway Arena', 'Concerts', 'Pop'], 'current': {'count': 784, 'metrics': {'commission': {'avg': 95.54713010204081}, 'qtysold': {'sum': 1567.0}}}}, {'group': ['FL', 'St. Petersburg', 'Tropicana Field', 'Concerts', 'Pop'], 'current': {'count': 730, 'metrics': {'commission': {'avg': 88.69849315068494}, 'qtysold': {'sum': 1431.0}}}}, {'group': ['FL', 'Sunrise', 'BankAtlantic Center', 'Concerts', 'Pop'], 'current': {'count': 445, 'metrics': {'commission': {'avg': 96.68595505617978}, 'qtysold': {'sum': 879.0}}}}, {'group': ['FL', 'Tampa', 'Raymond James Stadium', 'Concerts', 'Pop'], 'current': {'count': 581, 'metrics': {'commission': {'avg': 103.36368330464717}, 'qtysold': {'sum': 1187.0}}}}, {'group': ['FL', 'Tampa', 'St. Pete Times Forum', 'Concerts', 'Pop'], 'current': {'count': 579, 'metrics': {'commission': {'avg': 101.31554404145078}, 'qtysold': {'sum': 1201.0}}}}, {'group': ['GA', 'Atlanta', 'Georgia Dome', 'Concerts', 'Pop'], 'current': {'count': 763, 'metrics': {'commission': {'avg': 97.29082568807338}, 'qtysold': {'sum': 1559.0}}}}, {'group': ['GA', 'Atlanta', 'Philips Arena', 'Concerts', 'Pop'], 'current': {'count': 568, 'metrics': {'commission': {'avg': 98.17896126760563}, 'qtysold': {'sum': 1136.0}}}}, {'group': ['GA', 'Atlanta', 'Turner Field', 'Concerts', 'Pop'], 'current': {'count': 745, 'metrics': {'commission': {'avg': 97.60530201342281}, 'qtysold': {'sum': 1473.0}}}}, {'group': ['IL', 'Bridgeview', 'Toyota Park', 'Concerts', 'Pop'], 'current': {'count': 857, 'metrics': {'commission': {'avg': 90.58162193698949}, 'qtysold': {'sum': 1699.0}}}}, {'group': ['IL', 'Chicago', 'Soldier Field', 'Concerts', 'Pop'], 'current': {'count': 673, 'metrics': {'commission': {'avg': 99.65839524517088}, 'qtysold': {'sum': 1349.0}}}}, {'group': ['IL', 'Chicago', 'U.S. Cellular Field', 'Concerts', 'Pop'], 'current': {'count': 794, 'metrics': {'commission': {'avg': 97.20717884130983}, 'qtysold': {'sum': 1602.0}}}}, {'group': ['IL', 'Chicago', 'United Center', 'Concerts', 'Pop'], 'current': {'count': 753, 'metrics': {'commission': {'avg': 102.1272908366534}, 'qtysold': {'sum': 1537.0}}}}, {'group': ['IL', 'Chicago', 'Wrigley Field', 'Concerts', 'Pop'], 'current': {'count': 653, 'metrics': {'commission': {'avg': 102.08705972434916}, 'qtysold': {'sum': 1331.0}}}}, {'group': ['IN', 'Indianapolis', 'Conseco Fieldhouse', 'Concerts', 'Pop'], 'current': {'count': 534, 'metrics': {'commission': {'avg': 90.48932584269663}, 'qtysold': {'sum': 1095.0}}}}, {'group': ['IN', 'Indianapolis', 'Lucas Oil Stadium', 'Concerts', 'Pop'], 'current': {'count': 656, 'metrics': {'commission': {'avg': 93.69146341463414}, 'qtysold': {'sum': 1293.0}}}}, {'group': ['KS', 'Kansas City', 'CommunityAmerica Ballpark', 'Concerts', 'Pop'], 'current': {'count': 555, 'metrics': {'commission': {'avg': 93.23297297297297}, 'qtysold': {'sum': 1151.0}}}}, {'group': ['LA', 'New Orleans', 'Louisiana Superdome', 'Concerts', 'Pop'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 90.66821471652594}, 'qtysold': {'sum': 1677.0}}}}, {'group': ['LA', 'New Orleans', 'New Orleans Arena', 'Concerts', 'Pop'], 'current': {'count': 681, 'metrics': {'commission': {'avg': 95.7057268722467}, 'qtysold': {'sum': 1377.0}}}}, {'group': ['MA', 'Boston', 'Fenway Park', 'Concerts', 'Pop'], 'current': {'count': 727, 'metrics': {'commission': {'avg': 85.51733149931223}, 'qtysold': {'sum': 1404.0}}}}, {'group': ['MA', 'Boston', 'TD Banknorth Garden', 'Concerts', 'Pop'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 84.86019300361882}, 'qtysold': {'sum': 1667.0}}}}, {'group': ['MA', 'Foxborough', 'Gillette Stadium', 'Concerts', 'Pop'], 'current': {'count': 562, 'metrics': {'commission': {'avg': 101.1894128113879}, 'qtysold': {'sum': 1094.0}}}}, {'group': ['MD', 'Baltimore', 'M&T Bank Stadium', 'Concerts', 'Pop'], 'current': {'count': 836, 'metrics': {'commission': {'avg': 107.96232057416267}, 'qtysold': {'sum': 1688.0}}}}, {'group': ['MD', 'Baltimore', 'Oriole Park at Camden Yards', 'Concerts', 'Pop'], 'current': {'count': 941, 'metrics': {'commission': {'avg': 96.13071200850159}, 'qtysold': {'sum': 1878.0}}}}, {'group': ['MD', 'Landover', 'FedExField', 'Concerts', 'Pop'], 'current': {'count': 858, 'metrics': {'commission': {'avg': 96.0340909090909}, 'qtysold': {'sum': 1730.0}}}}, {'group': ['MI', 'Auburn Hills', 'The Palace of Auburn Hills', 'Concerts', 'Pop'], 'current': {'count': 858, 'metrics': {'commission': {'avg': 94.67115384615386}, 'qtysold': {'sum': 1717.0}}}}, {'group': ['MI', 'Detroit', 'Comerica Park', 'Concerts', 'Pop'], 'current': {'count': 568, 'metrics': {'commission': {'avg': 96.39110915492958}, 'qtysold': {'sum': 1124.0}}}}, {'group': ['MI', 'Detroit', 'Ford Field', 'Concerts', 'Pop'], 'current': {'count': 624, 'metrics': {'commission': {'avg': 93.95745192307692}, 'qtysold': {'sum': 1222.0}}}}, {'group': ['MI', 'Detroit', 'Joe Louis Arena', 'Concerts', 'Pop'], 'current': {'count': 736, 'metrics': {'commission': {'avg': 104.90176630434782}, 'qtysold': {'sum': 1485.0}}}}, {'group': ['MN', 'Minneapolis', 'Hubert H. Humphrey Metrodome', 'Concerts', 'Pop'], 'current': {'count': 651, 'metrics': {'commission': {'avg': 88.21958525345622}, 'qtysold': {'sum': 1311.0}}}}, {'group': ['MN', 'Minneapolis', 'Target Center', 'Concerts', 'Pop'], 'current': {'count': 758, 'metrics': {'commission': {'avg': 99.10092348284961}, 'qtysold': {'sum': 1514.0}}}}, {'group': ['MN', 'St. Paul', 'Xcel Energy Center', 'Concerts', 'Pop'], 'current': {'count': 828, 'metrics': {'commission': {'avg': 103.17409420289854}, 'qtysold': {'sum': 1663.0}}}}, {'group': ['MO', 'Kansas City', 'Arrowhead Stadium', 'Concerts', 'Pop'], 'current': {'count': 603, 'metrics': {'commission': {'avg': 83.18134328358208}, 'qtysold': {'sum': 1160.0}}}}, {'group': ['MO', 'Kansas City', 'Kauffman Stadium', 'Concerts', 'Pop'], 'current': {'count': 554, 'metrics': {'commission': {'avg': 101.24485559566787}, 'qtysold': {'sum': 1125.0}}}}, {'group': ['MO', 'St. Louis', 'Busch Stadium', 'Concerts', 'Pop'], 'current': {'count': 737, 'metrics': {'commission': {'avg': 93.25257801899592}, 'qtysold': {'sum': 1449.0}}}}, {'group': ['MO', 'St. Louis', 'Edward Jones Dome', 'Concerts', 'Pop'], 'current': {'count': 895, 'metrics': {'commission': {'avg': 104.81916201117318}, 'qtysold': {'sum': 1798.0}}}}, {'group': ['MO', 'St. Louis', 'Scottrade Center', 'Concerts', 'Pop'], 'current': {'count': 803, 'metrics': {'commission': {'avg': 96.8194894146949}, 'qtysold': {'sum': 1608.0}}}}, {'group': ['NC', 'Charlotte', 'Bank of America Stadium', 'Concerts', 'Pop'], 'current': {'count': 711, 'metrics': {'commission': {'avg': 92.35063291139241}, 'qtysold': {'sum': 1412.0}}}}, {'group': ['NC', 'Charlotte', 'Time Warner Cable Arena', 'Concerts', 'Pop'], 'current': {'count': 599, 'metrics': {'commission': {'avg': 85.6915692821369}, 'qtysold': {'sum': 1221.0}}}}, {'group': ['NC', 'Raleigh', 'RBC Center', 'Concerts', 'Pop'], 'current': {'count': 714, 'metrics': {'commission': {'avg': 96.1623949579832}, 'qtysold': {'sum': 1417.0}}}}, {'group': ['NJ', 'East Rutherford', 'Izod Center', 'Concerts', 'Pop'], 'current': {'count': 826, 'metrics': {'commission': {'avg': 97.1115617433414}, 'qtysold': {'sum': 1702.0}}}}, {'group': ['NJ', 'East Rutherford', 'New York Giants Stadium', 'Concerts', 'Pop'], 'current': {'count': 805, 'metrics': {'commission': {'avg': 89.8039751552795}, 'qtysold': {'sum': 1609.0}}}}, {'group': ['NJ', 'Newark', 'Prudential Center', 'Concerts', 'Pop'], 'current': {'count': 525, 'metrics': {'commission': {'avg': 92.902}, 'qtysold': {'sum': 1066.0}}}}, {'group': ['NY', 'Buffalo', 'HSBC Arena', 'Concerts', 'Pop'], 'current': {'count': 732, 'metrics': {'commission': {'avg': 95.04282786885247}, 'qtysold': {'sum': 1453.0}}}}, {'group': ['NY', 'New York City', 'Madison Square Garden', 'Concerts', 'Pop'], 'current': {'count': 923, 'metrics': {'commission': {'avg': 96.59106175514627}, 'qtysold': {'sum': 1847.0}}}}, {'group': ['NY', 'New York City', 'Shea Stadium', 'Concerts', 'Pop'], 'current': {'count': 539, 'metrics': {'commission': {'avg': 99.38738404452691}, 'qtysold': {'sum': 1099.0}}}}, {'group': ['NY', 'New York City', 'Yankee Stadium', 'Concerts', 'Pop'], 'current': {'count': 869, 'metrics': {'commission': {'avg': 109.60978135788261}, 'qtysold': {'sum': 1765.0}}}}, {'group': ['NY', 'Orchard Park', 'Ralph Wilson Stadium', 'Concerts', 'Pop'], 'current': {'count': 661, 'metrics': {'commission': {'avg': 102.43888048411499}, 'qtysold': {'sum': 1327.0}}}}, {'group': ['NY', 'Saratoga Springs', 'Saratoga Springs Performing Arts Center', 'Concerts', 'Pop'], 'current': {'count': 782, 'metrics': {'commission': {'avg': 95.82717391304348}, 'qtysold': {'sum': 1542.0}}}}, {'group': ['NY', 'Uniondale', 'Nassau Veterans Memorial Coliseum', 'Concerts', 'Pop'], 'current': {'count': 713, 'metrics': {'commission': {'avg': 93.24635343618513}, 'qtysold': {'sum': 1451.0}}}}, {'group': [None, None, None, 'Concerts', 'Pop'], 'current': {'count': 2777, 'metrics': {'commission': {'avg': 96.69927979834354}, 'qtysold': {'sum': 5553.0}}}}, {'group': ['OH', 'Cincinnati', 'Great American Ball Park', 'Concerts', 'Pop'], 'current': {'count': 879, 'metrics': {'commission': {'avg': 111.43105802047782}, 'qtysold': {'sum': 1758.0}}}}, {'group': ['OH', 'Cincinnati', 'Paul Brown Stadium', 'Concerts', 'Pop'], 'current': {'count': 880, 'metrics': {'commission': {'avg': 88.91454545454546}, 'qtysold': {'sum': 1787.0}}}}, {'group': ['OH', 'Cleveland', 'Cleveland Browns Stadium', 'Concerts', 'Pop'], 'current': {'count': 617, 'metrics': {'commission': {'avg': 106.50097244732578}, 'qtysold': {'sum': 1239.0}}}}, {'group': ['OH', 'Cleveland', 'Progressive Field', 'Concerts', 'Pop'], 'current': {'count': 742, 'metrics': {'commission': {'avg': 107.71314016172506}, 'qtysold': {'sum': 1486.0}}}}, {'group': ['OH', 'Cleveland', 'Quicken Loans Arena', 'Concerts', 'Pop'], 'current': {'count': 778, 'metrics': {'commission': {'avg': 90.58284061696658}, 'qtysold': {'sum': 1543.0}}}}, {'group': ['OH', 'Columbus', 'Columbus Crew Stadium', 'Concerts', 'Pop'], 'current': {'count': 686, 'metrics': {'commission': {'avg': 97.54395043731778}, 'qtysold': {'sum': 1366.0}}}}, {'group': ['OH', 'Columbus', 'Nationwide Arena', 'Concerts', 'Pop'], 'current': {'count': 865, 'metrics': {'commission': {'avg': 93.1864161849711}, 'qtysold': {'sum': 1700.0}}}}, {'group': ['OH', 'Dayton', 'E.J. Nutter Center', 'Concerts', 'Pop'], 'current': {'count': 797, 'metrics': {'commission': {'avg': 86.60250941028858}, 'qtysold': {'sum': 1540.0}}}}, {'group': ['OK', 'Oklahoma City', 'Ford Center', 'Concerts', 'Pop'], 'current': {'count': 761, 'metrics': {'commission': {'avg': 94.14086727989488}, 'qtysold': {'sum': 1502.0}}}}, {'group': ['ON', 'Ottawa', 'Scotiabank Place', 'Concerts', 'Pop'], 'current': {'count': 789, 'metrics': {'commission': {'avg': 90.74182509505704}, 'qtysold': {'sum': 1598.0}}}}, {'group': ['ON', 'Toronto', 'Air Canada Centre', 'Concerts', 'Pop'], 'current': {'count': 882, 'metrics': {'commission': {'avg': 100.60510204081632}, 'qtysold': {'sum': 1798.0}}}}, {'group': ['ON', 'Toronto', 'BMO Field', 'Concerts', 'Pop'], 'current': {'count': 756, 'metrics': {'commission': {'avg': 92.62718253968254}, 'qtysold': {'sum': 1552.0}}}}, {'group': ['ON', 'Toronto', 'Rogers Centre', 'Concerts', 'Pop'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 83.99956011730205}, 'qtysold': {'sum': 1329.0}}}}, {'group': ['OR', 'Portland', 'Rose Garden', 'Concerts', 'Pop'], 'current': {'count': 849, 'metrics': {'commission': {'avg': 87.40053003533569}, 'qtysold': {'sum': 1711.0}}}}, {'group': ['PA', 'Hershey', 'Hersheypark Stadium', 'Concerts', 'Pop'], 'current': {'count': 794, 'metrics': {'commission': {'avg': 96.34609571788414}, 'qtysold': {'sum': 1554.0}}}}, {'group': ['PA', 'Philadelphia', 'Citizens Bank Park', 'Concerts', 'Pop'], 'current': {'count': 788, 'metrics': {'commission': {'avg': 109.20989847715735}, 'qtysold': {'sum': 1620.0}}}}, {'group': ['PA', 'Philadelphia', 'Lincoln Financial Field', 'Concerts', 'Pop'], 'current': {'count': 694, 'metrics': {'commission': {'avg': 93.15410662824208}, 'qtysold': {'sum': 1390.0}}}}, {'group': ['PA', 'Philadelphia', 'Wachovia Center', 'Concerts', 'Pop'], 'current': {'count': 791, 'metrics': {'commission': {'avg': 96.54481668773704}, 'qtysold': {'sum': 1593.0}}}}, {'group': ['PA', 'Pittsburgh', 'Heinz Field', 'Concerts', 'Pop'], 'current': {'count': 538, 'metrics': {'commission': {'avg': 89.25920074349442}, 'qtysold': {'sum': 1040.0}}}}, {'group': ['PA', 'Pittsburgh', 'Mellon Arena', 'Concerts', 'Pop'], 'current': {'count': 593, 'metrics': {'commission': {'avg': 109.46964586846543}, 'qtysold': {'sum': 1176.0}}}}, {'group': ['PA', 'Pittsburgh', 'PNC Park', 'Concerts', 'Pop'], 'current': {'count': 813, 'metrics': {'commission': {'avg': 100.03911439114391}, 'qtysold': {'sum': 1649.0}}}}, {'group': ['QC', 'Montreal', 'Bell Centre', 'Concerts', 'Pop'], 'current': {'count': 555, 'metrics': {'commission': {'avg': 99.7481081081081}, 'qtysold': {'sum': 1123.0}}}}, {'group': ['SC', 'Charleston', 'North Charleston Coliseum', 'Concerts', 'Pop'], 'current': {'count': 837, 'metrics': {'commission': {'avg': 101.26290322580645}, 'qtysold': {'sum': 1719.0}}}}, {'group': ['TN', 'Memphis', 'FedExForum', 'Concerts', 'Pop'], 'current': {'count': 882, 'metrics': {'commission': {'avg': 95.33401360544218}, 'qtysold': {'sum': 1764.0}}}}, {'group': ['TN', 'Nashville', 'LP Field', 'Concerts', 'Pop'], 'current': {'count': 666, 'metrics': {'commission': {'avg': 101.55202702702702}, 'qtysold': {'sum': 1330.0}}}}, {'group': ['TN', 'Nashville', 'Sommet Center', 'Concerts', 'Pop'], 'current': {'count': 626, 'metrics': {'commission': {'avg': 92.69712460063899}, 'qtysold': {'sum': 1288.0}}}}, {'group': ['TX', 'Arlington', 'Rangers BallPark in Arlington', 'Concerts', 'Pop'], 'current': {'count': 711, 'metrics': {'commission': {'avg': 89.17257383966245}, 'qtysold': {'sum': 1428.0}}}}, {'group': ['TX', 'Dallas', 'American Airlines Center', 'Concerts', 'Pop'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 90.375}, 'qtysold': {'sum': 1347.0}}}}, {'group': ['TX', 'Dallas', 'Superpages.com Center', 'Concerts', 'Pop'], 'current': {'count': 742, 'metrics': {'commission': {'avg': 90.65033692722372}, 'qtysold': {'sum': 1481.0}}}}, {'group': ['TX', 'Frisco', 'Pizza Hut Park', 'Concerts', 'Pop'], 'current': {'count': 866, 'metrics': {'commission': {'avg': 99.03412240184758}, 'qtysold': {'sum': 1735.0}}}}, {'group': ['TX', 'Houston', 'Minute Maid Park', 'Concerts', 'Pop'], 'current': {'count': 780, 'metrics': {'commission': {'avg': 97.1546153846154}, 'qtysold': {'sum': 1553.0}}}}, {'group': ['TX', 'Houston', 'Reliant Stadium', 'Concerts', 'Pop'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 95.29270205066344}, 'qtysold': {'sum': 1684.0}}}}, {'group': ['TX', 'Houston', 'Robertson Stadium', 'Concerts', 'Pop'], 'current': {'count': 817, 'metrics': {'commission': {'avg': 99.72576499388005}, 'qtysold': {'sum': 1637.0}}}}, {'group': ['TX', 'Houston', 'Toyota Center', 'Concerts', 'Pop'], 'current': {'count': 628, 'metrics': {'commission': {'avg': 97.96074840764331}, 'qtysold': {'sum': 1269.0}}}}, {'group': ['TX', 'Irving', 'Texas Stadium', 'Concerts', 'Pop'], 'current': {'count': 516, 'metrics': {'commission': {'avg': 101.7392441860465}, 'qtysold': {'sum': 1028.0}}}}, {'group': ['TX', 'San Antonio', 'AT&T Center', 'Concerts', 'Pop'], 'current': {'count': 708, 'metrics': {'commission': {'avg': 100.4489406779661}, 'qtysold': {'sum': 1426.0}}}}, {'group': ['UT', 'Salt Lake City', 'EnergySolutions Arena', 'Concerts', 'Pop'], 'current': {'count': 602, 'metrics': {'commission': {'avg': 93.53421926910299}, 'qtysold': {'sum': 1158.0}}}}, {'group': ['UT', 'Salt Lake City', 'Rice-Eccles Stadium', 'Concerts', 'Pop'], 'current': {'count': 768, 'metrics': {'commission': {'avg': 92.0978515625}, 'qtysold': {'sum': 1534.0}}}}, {'group': ['WA', 'Seattle', 'Qwest Field', 'Concerts', 'Pop'], 'current': {'count': 770, 'metrics': {'commission': {'avg': 93.83571428571429}, 'qtysold': {'sum': 1543.0}}}}, {'group': ['WA', 'Seattle', 'Safeco Field', 'Concerts', 'Pop'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 90.6050586510264}, 'qtysold': {'sum': 1373.0}}}}, {'group': ['WI', 'Green Bay', 'Lambeau Field', 'Concerts', 'Pop'], 'current': {'count': 921, 'metrics': {'commission': {'avg': 92.20684039087948}, 'qtysold': {'sum': 1845.0}}}}, {'group': ['WI', 'Milwaukee', 'Bradley Center', 'Concerts', 'Pop'], 'current': {'count': 705, 'metrics': {'commission': {'avg': 100.02914893617022}, 'qtysold': {'sum': 1428.0}}}}, {'group': ['WI', 'Milwaukee', 'Miller Park', 'Concerts', 'Pop'], 'current': {'count': 1100, 'metrics': {'commission': {'avg': 96.67936363636363}, 'qtysold': {'sum': 2207.0}}}}, {'group': ['CA', 'Los Angeles', 'Geffen Playhouse', 'Shows', 'Musicals'], 'current': {'count': 1215, 'metrics': {'commission': {'avg': 95.62787723785166}, 'qtysold': {'sum': 767.0}}}}, {'group': ['CA', 'Los Angeles', 'Greek Theatre', 'Shows', 'Musicals'], 'current': {'count': 1220, 'metrics': {'commission': {'avg': 88.99517647058823}, 'qtysold': {'sum': 873.0}}}}, {'group': ['CA', 'Los Angeles', 'Royce Hall', 'Shows', 'Musicals'], 'current': {'count': 1005, 'metrics': {'commission': {'avg': 98.3053738317757}, 'qtysold': {'sum': 438.0}}}}, {'group': ['CA', 'Pasadena', 'Pasadena Playhouse', 'Shows', 'Musicals'], 'current': {'count': 1373, 'metrics': {'commission': {'avg': 88.8359872611465}, 'qtysold': {'sum': 928.0}}}}, {'group': ['CA', 'San Francisco', 'Curran Theatre', 'Shows', 'Musicals'], 'current': {'count': 835, 'metrics': {'commission': {'avg': 107.85783582089553}, 'qtysold': {'sum': 536.0}}}}, {'group': ['CA', 'San Jose', 'San Jose Repertory Theatre', 'Shows', 'Musicals'], 'current': {'count': 1027, 'metrics': {'commission': {'avg': 99.40576496674058}, 'qtysold': {'sum': 892.0}}}}, {'group': ['MA', 'Boston', 'Charles Playhouse', 'Shows', 'Musicals'], 'current': {'count': 1244, 'metrics': {'commission': {'avg': 78.92688679245283}, 'qtysold': {'sum': 632.0}}}}, {'group': ['MN', 'Minneapolis', 'The Guthrie Theater', 'Shows', 'Musicals'], 'current': {'count': 943, 'metrics': {'commission': {'avg': 106.43808724832215}, 'qtysold': {'sum': 599.0}}}}, {'group': ['NV', 'Las Vegas', 'Ballys Hotel', 'Shows', 'Musicals'], 'current': {'count': 398, 'metrics': {'commission': {'avg': 98.10000000000001}, 'qtysold': {'sum': 787.0}}}}, {'group': ['NV', 'Las Vegas', 'Bellagio Hotel', 'Shows', 'Musicals'], 'current': {'count': 465, 'metrics': {'commission': {'avg': 92.73967741935483}, 'qtysold': {'sum': 951.0}}}}, {'group': ['NV', 'Las Vegas', 'Caesars Palace', 'Shows', 'Musicals'], 'current': {'count': 427, 'metrics': {'commission': {'avg': 89.00620608899298}, 'qtysold': {'sum': 862.0}}}}, {'group': ['NV', 'Las Vegas', 'Harrahs Hotel', 'Shows', 'Musicals'], 'current': {'count': 518, 'metrics': {'commission': {'avg': 93.98918918918919}, 'qtysold': {'sum': 1066.0}}}}, {'group': ['NV', 'Las Vegas', 'Hilton Hotel', 'Shows', 'Musicals'], 'current': {'count': 418, 'metrics': {'commission': {'avg': 98.68205741626794}, 'qtysold': {'sum': 862.0}}}}, {'group': ['NV', 'Las Vegas', 'Luxor Hotel', 'Shows', 'Musicals'], 'current': {'count': 671, 'metrics': {'commission': {'avg': 100.90953800298063}, 'qtysold': {'sum': 1363.0}}}}, {'group': ['NV', 'Las Vegas', 'Mandalay Bay Hotel', 'Shows', 'Musicals'], 'current': {'count': 332, 'metrics': {'commission': {'avg': 88.73765060240964}, 'qtysold': {'sum': 658.0}}}}, {'group': ['NV', 'Las Vegas', 'Mirage Hotel', 'Shows', 'Musicals'], 'current': {'count': 432, 'metrics': {'commission': {'avg': 107.42291666666667}, 'qtysold': {'sum': 913.0}}}}, {'group': ['NV', 'Las Vegas', 'Paris Hotel', 'Shows', 'Musicals'], 'current': {'count': 309, 'metrics': {'commission': {'avg': 93.64029126213592}, 'qtysold': {'sum': 634.0}}}}, {'group': ['NV', 'Las Vegas', 'Paris MGM Grand', 'Shows', 'Musicals'], 'current': {'count': 378, 'metrics': {'commission': {'avg': 92.47698412698414}, 'qtysold': {'sum': 758.0}}}}, {'group': ['NV', 'Las Vegas', 'Sahara Hotel', 'Shows', 'Musicals'], 'current': {'count': 378, 'metrics': {'commission': {'avg': 96.11111111111111}, 'qtysold': {'sum': 751.0}}}}, {'group': ['NV', 'Las Vegas', 'Tropicana Hotel', 'Shows', 'Musicals'], 'current': {'count': 443, 'metrics': {'commission': {'avg': 95.37799097065462}, 'qtysold': {'sum': 905.0}}}}, {'group': ['NV', 'Las Vegas', 'Venetian Hotel', 'Shows', 'Musicals'], 'current': {'count': 589, 'metrics': {'commission': {'avg': 100.2455857385399}, 'qtysold': {'sum': 1158.0}}}}, {'group': ['NV', 'Las Vegas', 'Wynn Hotel', 'Shows', 'Musicals'], 'current': {'count': 327, 'metrics': {'commission': {'avg': 107.62752293577981}, 'qtysold': {'sum': 660.0}}}}, {'group': ['NY', 'New York City', 'Al Hirschfeld Theatre', 'Shows', 'Musicals'], 'current': {'count': 1191, 'metrics': {'commission': {'avg': 93.78791946308723}, 'qtysold': {'sum': 885.0}}}}, {'group': ['NY', 'New York City', 'Ambassador Theatre', 'Shows', 'Musicals'], 'current': {'count': 1168, 'metrics': {'commission': {'avg': 98.46315789473684}, 'qtysold': {'sum': 777.0}}}}, {'group': ['NY', 'New York City', 'American Airlines Theatre', 'Shows', 'Musicals'], 'current': {'count': 929, 'metrics': {'commission': {'avg': 98.68423423423422}, 'qtysold': {'sum': 649.0}}}}, {'group': ['NY', 'New York City', 'August Wilson Theatre', 'Shows', 'Musicals'], 'current': {'count': 1583, 'metrics': {'commission': {'avg': 93.34921874999999}, 'qtysold': {'sum': 875.0}}}}, {'group': ['NY', 'New York City', 'Belasco Theatre', 'Shows', 'Musicals'], 'current': {'count': 1217, 'metrics': {'commission': {'avg': 81.05150602409638}, 'qtysold': {'sum': 648.0}}}}, {'group': ['NY', 'New York City', 'Bernard B. Jacobs Theatre', 'Shows', 'Musicals'], 'current': {'count': 1217, 'metrics': {'commission': {'avg': 97.1421357615894}, 'qtysold': {'sum': 1206.0}}}}, {'group': ['NY', 'New York City', 'Biltmore Theatre', 'Shows', 'Musicals'], 'current': {'count': 1305, 'metrics': {'commission': {'avg': 94.47768052516412}, 'qtysold': {'sum': 928.0}}}}, {'group': ['NY', 'New York City', 'Booth Theatre', 'Shows', 'Musicals'], 'current': {'count': 1210, 'metrics': {'commission': {'avg': 89.12098445595853}, 'qtysold': {'sum': 771.0}}}}, {'group': ['NY', 'New York City', 'Broadhurst Theatre', 'Shows', 'Musicals'], 'current': {'count': 1055, 'metrics': {'commission': {'avg': 96.75598006644518}, 'qtysold': {'sum': 614.0}}}}, {'group': ['NY', 'New York City', 'Brooks Atkinson Theatre', 'Shows', 'Musicals'], 'current': {'count': 1013, 'metrics': {'commission': {'avg': 105.10513392857142}, 'qtysold': {'sum': 451.0}}}}, {'group': ['NY', 'New York City', 'Carnegie Hall', 'Shows', 'Musicals'], 'current': {'count': 1211, 'metrics': {'commission': {'avg': 84.76658767772511}, 'qtysold': {'sum': 1258.0}}}}, {'group': ['NY', 'New York City', 'Circle in the Square Theatre', 'Shows', 'Musicals'], 'current': {'count': 1047, 'metrics': {'commission': {'avg': 94.33041543026705}, 'qtysold': {'sum': 669.0}}}}, {'group': ['NY', 'New York City', 'Cort Theatre', 'Shows', 'Musicals'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 100.54730113636364}, 'qtysold': {'sum': 699.0}}}}, {'group': ['NY', 'New York City', 'Ethel Barrymore Theatre', 'Shows', 'Musicals'], 'current': {'count': 1413, 'metrics': {'commission': {'avg': 85.82558823529412}, 'qtysold': {'sum': 676.0}}}}, {'group': ['NY', 'New York City', "Eugene O'Neill Theatre", 'Shows', 'Musicals'], 'current': {'count': 1239, 'metrics': {'commission': {'avg': 109.61712846347606}, 'qtysold': {'sum': 815.0}}}}, {'group': ['NY', 'New York City', 'George Gershwin Theatre', 'Shows', 'Musicals'], 'current': {'count': 1137, 'metrics': {'commission': {'avg': 123.83423645320197}, 'qtysold': {'sum': 419.0}}}}, {'group': ['NY', 'New York City', 'Gerald Schoenfeld Theatre', 'Shows', 'Musicals'], 'current': {'count': 1132, 'metrics': {'commission': {'avg': 79.25374707259952}, 'qtysold': {'sum': 857.0}}}}, {'group': ['NY', 'New York City', 'Helen Hayes Theatre', 'Shows', 'Musicals'], 'current': {'count': 1456, 'metrics': {'commission': {'avg': 96.50718562874252}, 'qtysold': {'sum': 1007.0}}}}, {'group': ['NY', 'New York City', 'Hilton Theatre', 'Shows', 'Musicals'], 'current': {'count': 1488, 'metrics': {'commission': {'avg': 86.72583170254403}, 'qtysold': {'sum': 1016.0}}}}, {'group': ['NY', 'New York City', 'Imperial Theatre', 'Shows', 'Musicals'], 'current': {'count': 1357, 'metrics': {'commission': {'avg': 99.16940928270041}, 'qtysold': {'sum': 1423.0}}}}, {'group': ['NY', 'New York City', 'John Golden Theatre', 'Shows', 'Musicals'], 'current': {'count': 1208, 'metrics': {'commission': {'avg': 84.1924}, 'qtysold': {'sum': 734.0}}}}, {'group': ['NY', 'New York City', 'Lincoln Center for the Performing Arts', 'Shows', 'Musicals'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 99.23439635535308}, 'qtysold': {'sum': 879.0}}}}, {'group': ['NY', 'New York City', 'Longacre Theatre', 'Shows', 'Musicals'], 'current': {'count': 1143, 'metrics': {'commission': {'avg': 87.61441441441441}, 'qtysold': {'sum': 645.0}}}}, {'group': ['NY', 'New York City', 'Lunt-Fontanne Theatre', 'Shows', 'Musicals'], 'current': {'count': 1672, 'metrics': {'commission': {'avg': 103.93170103092784}, 'qtysold': {'sum': 1184.0}}}}, {'group': ['NY', 'New York City', 'Lyceum Theatre', 'Shows', 'Musicals'], 'current': {'count': 1221, 'metrics': {'commission': {'avg': 90.35502183406113}, 'qtysold': {'sum': 907.0}}}}, {'group': ['NY', 'New York City', 'Majestic Theatre', 'Shows', 'Musicals'], 'current': {'count': 1265, 'metrics': {'commission': {'avg': 99.0501246882793}, 'qtysold': {'sum': 824.0}}}}, {'group': ['NY', 'New York City', 'Marquis Theatre', 'Shows', 'Musicals'], 'current': {'count': 1023, 'metrics': {'commission': {'avg': 96.12258064516129}, 'qtysold': {'sum': 554.0}}}}, {'group': ['NY', 'New York City', 'Minskoff Theatre', 'Shows', 'Musicals'], 'current': {'count': 1185, 'metrics': {'commission': {'avg': 101.47782608695651}, 'qtysold': {'sum': 666.0}}}}, {'group': ['NY', 'New York City', 'Music Box Theatre', 'Shows', 'Musicals'], 'current': {'count': 963, 'metrics': {'commission': {'avg': 86.22769857433809}, 'qtysold': {'sum': 992.0}}}}, {'group': ['NY', 'New York City', 'Nederlander Theatre', 'Shows', 'Musicals'], 'current': {'count': 1465, 'metrics': {'commission': {'avg': 105.15431415929204}, 'qtysold': {'sum': 924.0}}}}, {'group': ['NY', 'New York City', 'Neil Simon Theatre', 'Shows', 'Musicals'], 'current': {'count': 1107, 'metrics': {'commission': {'avg': 102.94105263157896}, 'qtysold': {'sum': 560.0}}}}, {'group': ['NY', 'New York City', 'New Amsterdam Theatre', 'Shows', 'Musicals'], 'current': {'count': 1016, 'metrics': {'commission': {'avg': 99.04119170984457}, 'qtysold': {'sum': 777.0}}}}, {'group': ['NY', 'New York City', 'Palace Theatre', 'Shows', 'Musicals'], 'current': {'count': 1039, 'metrics': {'commission': {'avg': 97.08377723970943}, 'qtysold': {'sum': 841.0}}}}, {'group': ['NY', 'New York City', 'Richard Rodgers Theatre', 'Shows', 'Musicals'], 'current': {'count': 1099, 'metrics': {'commission': {'avg': 93.9996}, 'qtysold': {'sum': 509.0}}}}, {'group': ['NY', 'New York City', 'Shubert Theatre', 'Shows', 'Musicals'], 'current': {'count': 992, 'metrics': {'commission': {'avg': 93.07608695652173}, 'qtysold': {'sum': 400.0}}}}, {'group': ['NY', 'New York City', 'St. James Theatre', 'Shows', 'Musicals'], 'current': {'count': 958, 'metrics': {'commission': {'avg': 81.38834355828222}, 'qtysold': {'sum': 345.0}}}}, {'group': ['NY', 'New York City', 'Studio 54', 'Shows', 'Musicals'], 'current': {'count': 1146, 'metrics': {'commission': {'avg': 89.75992555831266}, 'qtysold': {'sum': 793.0}}}}, {'group': ['NY', 'New York City', 'The Broadway Theatre', 'Shows', 'Musicals'], 'current': {'count': 1118, 'metrics': {'commission': {'avg': 96.11916243654822}, 'qtysold': {'sum': 770.0}}}}, {'group': ['NY', 'New York City', 'Vivian Beaumont Theatre', 'Shows', 'Musicals'], 'current': {'count': 1055, 'metrics': {'commission': {'avg': 102.96085918854415}, 'qtysold': {'sum': 819.0}}}}, {'group': ['NY', 'New York City', 'Walter Kerr Theatre', 'Shows', 'Musicals'], 'current': {'count': 1208, 'metrics': {'commission': {'avg': 81.98680387409202}, 'qtysold': {'sum': 808.0}}}}, {'group': ['NY', 'New York City', 'Winter Garden Theatre', 'Shows', 'Musicals'], 'current': {'count': 1451, 'metrics': {'commission': {'avg': 93.44814487632509}, 'qtysold': {'sum': 1110.0}}}}, {'group': ['WA', 'Seattle', 'Paramount Theatre', 'Shows', 'Musicals'], 'current': {'count': 1147, 'metrics': {'commission': {'avg': 92.97157534246575}, 'qtysold': {'sum': 896.0}}}}, {'group': ['CA', 'Los Angeles', 'Los Angeles Opera', 'Shows', 'Opera'], 'current': {'count': 869, 'metrics': {'commission': {'avg': 98.50581127733027}, 'qtysold': {'sum': 1756.0}}}}, {'group': ['CA', 'San Francisco', 'San Francisco Opera', 'Shows', 'Opera'], 'current': {'count': 1042, 'metrics': {'commission': {'avg': 95.43627639155471}, 'qtysold': {'sum': 2075.0}}}}, {'group': ['CA', 'San Francisco', 'War Memorial Opera House', 'Shows', 'Opera'], 'current': {'count': 830, 'metrics': {'commission': {'avg': 100.95939759036145}, 'qtysold': {'sum': 1691.0}}}}, {'group': ['CO', 'Denver', 'Ellie Caulkins Opera House', 'Shows', 'Opera'], 'current': {'count': 748, 'metrics': {'commission': {'avg': 95.38997326203209}, 'qtysold': {'sum': 1497.0}}}}, {'group': ['DC', 'Washington', 'Kennedy Center Opera House', 'Shows', 'Opera'], 'current': {'count': 1085, 'metrics': {'commission': {'avg': 107.63958525345622}, 'qtysold': {'sum': 2175.0}}}}, {'group': ['IL', 'Chicago', 'Lyric Opera House', 'Shows', 'Opera'], 'current': {'count': 1013, 'metrics': {'commission': {'avg': 103.63682132280356}, 'qtysold': {'sum': 2006.0}}}}, {'group': ['MD', 'Baltimore', 'Lyric Opera House', 'Shows', 'Opera'], 'current': {'count': 1154, 'metrics': {'commission': {'avg': 97.08925476603119}, 'qtysold': {'sum': 2305.0}}}}, {'group': ['MI', 'Detroit', 'Detroit Opera House', 'Shows', 'Opera'], 'current': {'count': 1003, 'metrics': {'commission': {'avg': 90.81550348953141}, 'qtysold': {'sum': 2008.0}}}}, {'group': ['NY', 'New York City', 'Metropolitan Opera', 'Shows', 'Opera'], 'current': {'count': 1088, 'metrics': {'commission': {'avg': 96.12973345588235}, 'qtysold': {'sum': 2132.0}}}}, {'group': ['TX', 'Galveston', 'Grand 1894 Opera House', 'Shows', 'Opera'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 91.13664510166359}, 'qtysold': {'sum': 2142.0}}}}, {'group': ['CA', 'Los Angeles', 'Geffen Playhouse', 'Shows', 'Plays'], 'current': {'count': 1215, 'metrics': {'commission': {'avg': 91.32214805825242}, 'qtysold': {'sum': 1670.0}}}}, {'group': ['CA', 'Los Angeles', 'Greek Theatre', 'Shows', 'Plays'], 'current': {'count': 1220, 'metrics': {'commission': {'avg': 110.71037735849056}, 'qtysold': {'sum': 1572.0}}}}, {'group': ['CA', 'Los Angeles', 'Royce Hall', 'Shows', 'Plays'], 'current': {'count': 1005, 'metrics': {'commission': {'avg': 105.38836915297092}, 'qtysold': {'sum': 1554.0}}}}, {'group': ['CA', 'Pasadena', 'Pasadena Playhouse', 'Shows', 'Plays'], 'current': {'count': 1373, 'metrics': {'commission': {'avg': 90.04822616407982}, 'qtysold': {'sum': 1811.0}}}}, {'group': ['CA', 'San Francisco', 'Curran Theatre', 'Shows', 'Plays'], 'current': {'count': 835, 'metrics': {'commission': {'avg': 111.19788359788359}, 'qtysold': {'sum': 1105.0}}}}, {'group': ['CA', 'San Jose', 'San Jose Repertory Theatre', 'Shows', 'Plays'], 'current': {'count': 1027, 'metrics': {'commission': {'avg': 90.62447916666666}, 'qtysold': {'sum': 1176.0}}}}, {'group': ['MA', 'Boston', 'Charles Playhouse', 'Shows', 'Plays'], 'current': {'count': 1244, 'metrics': {'commission': {'avg': 111.72343412526997}, 'qtysold': {'sum': 1870.0}}}}, {'group': ['MN', 'Minneapolis', 'The Guthrie Theater', 'Shows', 'Plays'], 'current': {'count': 943, 'metrics': {'commission': {'avg': 102.50441860465118}, 'qtysold': {'sum': 1284.0}}}}, {'group': ['NY', 'New York City', 'Al Hirschfeld Theatre', 'Shows', 'Plays'], 'current': {'count': 1191, 'metrics': {'commission': {'avg': 99.30141129032258}, 'qtysold': {'sum': 1476.0}}}}, {'group': ['NY', 'New York City', 'Ambassador Theatre', 'Shows', 'Plays'], 'current': {'count': 1168, 'metrics': {'commission': {'avg': 103.05552030456853}, 'qtysold': {'sum': 1544.0}}}}, {'group': ['NY', 'New York City', 'American Airlines Theatre', 'Shows', 'Plays'], 'current': {'count': 929, 'metrics': {'commission': {'avg': 99.52676174496644}, 'qtysold': {'sum': 1240.0}}}}, {'group': ['NY', 'New York City', 'August Wilson Theatre', 'Shows', 'Plays'], 'current': {'count': 1583, 'metrics': {'commission': {'avg': 99.5620704845815}, 'qtysold': {'sum': 2312.0}}}}, {'group': ['NY', 'New York City', 'Belasco Theatre', 'Shows', 'Plays'], 'current': {'count': 1217, 'metrics': {'commission': {'avg': 89.61016949152543}, 'qtysold': {'sum': 1746.0}}}}, {'group': ['NY', 'New York City', 'Bernard B. Jacobs Theatre', 'Shows', 'Plays'], 'current': {'count': 1217, 'metrics': {'commission': {'avg': 94.98181076672104}, 'qtysold': {'sum': 1206.0}}}}, {'group': ['NY', 'New York City', 'Biltmore Theatre', 'Shows', 'Plays'], 'current': {'count': 1305, 'metrics': {'commission': {'avg': 95.72034198113208}, 'qtysold': {'sum': 1701.0}}}}, {'group': ['NY', 'New York City', 'Booth Theatre', 'Shows', 'Plays'], 'current': {'count': 1210, 'metrics': {'commission': {'avg': 100.92706310679611}, 'qtysold': {'sum': 1676.0}}}}, {'group': ['NY', 'New York City', 'Broadhurst Theatre', 'Shows', 'Plays'], 'current': {'count': 1055, 'metrics': {'commission': {'avg': 102.7088196286472}, 'qtysold': {'sum': 1517.0}}}}, {'group': ['NY', 'New York City', 'Brooks Atkinson Theatre', 'Shows', 'Plays'], 'current': {'count': 1013, 'metrics': {'commission': {'avg': 98.93307984790874}, 'qtysold': {'sum': 1598.0}}}}, {'group': ['NY', 'New York City', 'Carnegie Hall', 'Shows', 'Plays'], 'current': {'count': 1211, 'metrics': {'commission': {'avg': 85.1826124567474}, 'qtysold': {'sum': 1132.0}}}}, {'group': ['NY', 'New York City', 'Circle in the Square Theatre', 'Shows', 'Plays'], 'current': {'count': 1047, 'metrics': {'commission': {'avg': 92.8911971830986}, 'qtysold': {'sum': 1458.0}}}}, {'group': ['NY', 'New York City', 'Cort Theatre', 'Shows', 'Plays'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 99.86219178082192}, 'qtysold': {'sum': 1453.0}}}}, {'group': ['NY', 'New York City', 'Ethel Barrymore Theatre', 'Shows', 'Plays'], 'current': {'count': 1413, 'metrics': {'commission': {'avg': 97.38592730661696}, 'qtysold': {'sum': 2152.0}}}}, {'group': ['NY', 'New York City', "Eugene O'Neill Theatre", 'Shows', 'Plays'], 'current': {'count': 1239, 'metrics': {'commission': {'avg': 95.99109263657957}, 'qtysold': {'sum': 1673.0}}}}, {'group': ['NY', 'New York City', 'George Gershwin Theatre', 'Shows', 'Plays'], 'current': {'count': 1137, 'metrics': {'commission': {'avg': 90.44116702355461}, 'qtysold': {'sum': 1865.0}}}}, {'group': ['NY', 'New York City', 'Gerald Schoenfeld Theatre', 'Shows', 'Plays'], 'current': {'count': 1132, 'metrics': {'commission': {'avg': 99.47489361702128}, 'qtysold': {'sum': 1418.0}}}}, {'group': ['NY', 'New York City', 'Helen Hayes Theatre', 'Shows', 'Plays'], 'current': {'count': 1456, 'metrics': {'commission': {'avg': 103.10434554973821}, 'qtysold': {'sum': 1941.0}}}}, {'group': ['NY', 'New York City', 'Hilton Theatre', 'Shows', 'Plays'], 'current': {'count': 1488, 'metrics': {'commission': {'avg': 90.62026612077788}, 'qtysold': {'sum': 1983.0}}}}, {'group': ['NY', 'New York City', 'Imperial Theatre', 'Shows', 'Plays'], 'current': {'count': 1357, 'metrics': {'commission': {'avg': 94.72058823529412}, 'qtysold': {'sum': 1279.0}}}}, {'group': ['NY', 'New York City', 'John Golden Theatre', 'Shows', 'Plays'], 'current': {'count': 1208, 'metrics': {'commission': {'avg': 95.20642256902761}, 'qtysold': {'sum': 1654.0}}}}, {'group': ['NY', 'New York City', 'Lincoln Center for the Performing Arts', 'Shows', 'Plays'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 88.10342146189736}, 'qtysold': {'sum': 1276.0}}}}, {'group': ['NY', 'New York City', 'Longacre Theatre', 'Shows', 'Plays'], 'current': {'count': 1143, 'metrics': {'commission': {'avg': 108.65518518518518}, 'qtysold': {'sum': 1623.0}}}}, {'group': ['NY', 'New York City', 'Lunt-Fontanne Theatre', 'Shows', 'Plays'], 'current': {'count': 1672, 'metrics': {'commission': {'avg': 97.97160550458716}, 'qtysold': {'sum': 2142.0}}}}, {'group': ['NY', 'New York City', 'Lyceum Theatre', 'Shows', 'Plays'], 'current': {'count': 1221, 'metrics': {'commission': {'avg': 96.50799475753605}, 'qtysold': {'sum': 1563.0}}}}, {'group': ['NY', 'New York City', 'Majestic Theatre', 'Shows', 'Plays'], 'current': {'count': 1265, 'metrics': {'commission': {'avg': 109.28489583333332}, 'qtysold': {'sum': 1725.0}}}}, {'group': ['NY', 'New York City', 'Marquis Theatre', 'Shows', 'Plays'], 'current': {'count': 1023, 'metrics': {'commission': {'avg': 98.84032258064516}, 'qtysold': {'sum': 1473.0}}}}, {'group': ['NY', 'New York City', 'Minskoff Theatre', 'Shows', 'Plays'], 'current': {'count': 1185, 'metrics': {'commission': {'avg': 99.6744642857143}, 'qtysold': {'sum': 1663.0}}}}, {'group': ['NY', 'New York City', 'Music Box Theatre', 'Shows', 'Plays'], 'current': {'count': 963, 'metrics': {'commission': {'avg': 98.99078389830508}, 'qtysold': {'sum': 931.0}}}}, {'group': ['NY', 'New York City', 'Nederlander Theatre', 'Shows', 'Plays'], 'current': {'count': 1465, 'metrics': {'commission': {'avg': 91.72462981243831}, 'qtysold': {'sum': 2010.0}}}}, {'group': ['NY', 'New York City', 'Neil Simon Theatre', 'Shows', 'Plays'], 'current': {'count': 1107, 'metrics': {'commission': {'avg': 94.50401459854015}, 'qtysold': {'sum': 1683.0}}}}, {'group': ['NY', 'New York City', 'New Amsterdam Theatre', 'Shows', 'Plays'], 'current': {'count': 1016, 'metrics': {'commission': {'avg': 97.96785714285714}, 'qtysold': {'sum': 1278.0}}}}, {'group': ['NY', 'New York City', 'Palace Theatre', 'Shows', 'Plays'], 'current': {'count': 1039, 'metrics': {'commission': {'avg': 92.95950479233227}, 'qtysold': {'sum': 1248.0}}}}, {'group': ['NY', 'New York City', 'Richard Rodgers Theatre', 'Shows', 'Plays'], 'current': {'count': 1099, 'metrics': {'commission': {'avg': 93.1047703180212}, 'qtysold': {'sum': 1699.0}}}}, {'group': ['NY', 'New York City', 'Shubert Theatre', 'Shows', 'Plays'], 'current': {'count': 992, 'metrics': {'commission': {'avg': 96.7320382165605}, 'qtysold': {'sum': 1587.0}}}}, {'group': ['NY', 'New York City', 'St. James Theatre', 'Shows', 'Plays'], 'current': {'count': 958, 'metrics': {'commission': {'avg': 92.10018867924528}, 'qtysold': {'sum': 1602.0}}}}, {'group': ['NY', 'New York City', 'Studio 54', 'Shows', 'Plays'], 'current': {'count': 1146, 'metrics': {'commission': {'avg': 91.4107671601615}, 'qtysold': {'sum': 1511.0}}}}, {'group': ['NY', 'New York City', 'The Broadway Theatre', 'Shows', 'Plays'], 'current': {'count': 1118, 'metrics': {'commission': {'avg': 92.77313535911603}, 'qtysold': {'sum': 1445.0}}}}, {'group': ['NY', 'New York City', 'Vivian Beaumont Theatre', 'Shows', 'Plays'], 'current': {'count': 1055, 'metrics': {'commission': {'avg': 101.96981132075472}, 'qtysold': {'sum': 1269.0}}}}, {'group': ['NY', 'New York City', 'Walter Kerr Theatre', 'Shows', 'Plays'], 'current': {'count': 1208, 'metrics': {'commission': {'avg': 102.1254716981132}, 'qtysold': {'sum': 1593.0}}}}, {'group': ['NY', 'New York City', 'Winter Garden Theatre', 'Shows', 'Plays'], 'current': {'count': 1451, 'metrics': {'commission': {'avg': 99.4315254237288}, 'qtysold': {'sum': 1728.0}}}}, {'group': ['WA', 'Seattle', 'Paramount Theatre', 'Shows', 'Plays'], 'current': {'count': 1147, 'metrics': {'commission': {'avg': 93.87693935119887}, 'qtysold': {'sum': 1430.0}}}}, {'group': ['AB', 'Calgary', 'Pengrowth Saddledome', '$total'], 'current': {'count': 372, 'metrics': {'commission': {'avg': 105.68185483870968}, 'qtysold': {'sum': 728.0}}}}, {'group': ['AB', 'Edmonton', 'Rexall Place', '$total'], 'current': {'count': 1036, 'metrics': {'commission': {'avg': 92.30777027027028}, 'qtysold': {'sum': 2021.0}}}}, {'group': ['AZ', 'Glendale', 'Jobing.com Arena', '$total'], 'current': {'count': 1145, 'metrics': {'commission': {'avg': 95.21174672489083}, 'qtysold': {'sum': 2308.0}}}}, {'group': ['AZ', 'Glendale', 'University of Phoenix Stadium', '$total'], 'current': {'count': 698, 'metrics': {'commission': {'avg': 103.21719197707738}, 'qtysold': {'sum': 1408.0}}}}, {'group': ['AZ', 'Phoenix', 'Chase Field', '$total'], 'current': {'count': 799, 'metrics': {'commission': {'avg': 88.26683354192741}, 'qtysold': {'sum': 1582.0}}}}, {'group': ['AZ', 'Phoenix', 'US Airways Center', '$total'], 'current': {'count': 962, 'metrics': {'commission': {'avg': 92.2864864864865}, 'qtysold': {'sum': 1949.0}}}}, {'group': ['BC', 'Vancouver', 'General Motors Place', '$total'], 'current': {'count': 741, 'metrics': {'commission': {'avg': 93.04291497975709}, 'qtysold': {'sum': 1456.0}}}}, {'group': ['CA', 'Anaheim', 'Angel Stadium of Anaheim', '$total'], 'current': {'count': 746, 'metrics': {'commission': {'avg': 96.92754691689008}, 'qtysold': {'sum': 1507.0}}}}, {'group': ['CA', 'Anaheim', 'Honda Center', '$total'], 'current': {'count': 647, 'metrics': {'commission': {'avg': 87.79428129829985}, 'qtysold': {'sum': 1293.0}}}}, {'group': ['CA', 'Carson', 'The Home Depot Center', '$total'], 'current': {'count': 775, 'metrics': {'commission': {'avg': 97.25264516129033}, 'qtysold': {'sum': 1558.0}}}}, {'group': ['CA', 'Los Angeles', 'Dodger Stadium', '$total'], 'current': {'count': 931, 'metrics': {'commission': {'avg': 92.84436090225564}, 'qtysold': {'sum': 1822.0}}}}, {'group': ['CA', 'Los Angeles', 'Geffen Playhouse', '$total'], 'current': {'count': 1215, 'metrics': {'commission': {'avg': 92.70777777777778}, 'qtysold': {'sum': 2437.0}}}}, {'group': ['CA', 'Los Angeles', 'Greek Theatre', '$total'], 'current': {'count': 1220, 'metrics': {'commission': {'avg': 103.14565573770491}, 'qtysold': {'sum': 2445.0}}}}, {'group': ['CA', 'Los Angeles', 'Los Angeles Opera', '$total'], 'current': {'count': 869, 'metrics': {'commission': {'avg': 98.50581127733027}, 'qtysold': {'sum': 1756.0}}}}, {'group': ['CA', 'Los Angeles', 'Royce Hall', '$total'], 'current': {'count': 1005, 'metrics': {'commission': {'avg': 103.88014925373135}, 'qtysold': {'sum': 1992.0}}}}, {'group': ['CA', 'Los Angeles', 'Staples Center', '$total'], 'current': {'count': 782, 'metrics': {'commission': {'avg': 91.09047314578005}, 'qtysold': {'sum': 1548.0}}}}, {'group': ['CA', 'Mountain View', 'Shoreline Amphitheatre', '$total'], 'current': {'count': 1008, 'metrics': {'commission': {'avg': 99.87961309523808}, 'qtysold': {'sum': 1987.0}}}}, {'group': ['CA', 'Oakland', 'McAfee Coliseum', '$total'], 'current': {'count': 818, 'metrics': {'commission': {'avg': 92.2809902200489}, 'qtysold': {'sum': 1648.0}}}}, {'group': ['CA', 'Oakland', 'Oracle Arena', '$total'], 'current': {'count': 802, 'metrics': {'commission': {'avg': 93.68472568578552}, 'qtysold': {'sum': 1594.0}}}}, {'group': ['CA', 'Pasadena', 'Pasadena Playhouse', '$total'], 'current': {'count': 1373, 'metrics': {'commission': {'avg': 89.6323743627094}, 'qtysold': {'sum': 2739.0}}}}, {'group': ['CA', 'Redwood City', 'Fox Theatre', '$total'], 'current': {'count': 727, 'metrics': {'commission': {'avg': 93.09759284731774}, 'qtysold': {'sum': 1463.0}}}}, {'group': ['CA', 'Sacramento', 'ARCO Arena', '$total'], 'current': {'count': 905, 'metrics': {'commission': {'avg': 97.46834254143647}, 'qtysold': {'sum': 1789.0}}}}, {'group': ['CA', 'San Diego', 'PETCO Park', '$total'], 'current': {'count': 942, 'metrics': {'commission': {'avg': 104.73550955414014}, 'qtysold': {'sum': 1907.0}}}}, {'group': ['CA', 'San Diego', 'Qualcomm Stadium', '$total'], 'current': {'count': 862, 'metrics': {'commission': {'avg': 102.51073085846868}, 'qtysold': {'sum': 1774.0}}}}, {'group': ['CA', 'San Francisco', 'AT&T Park', '$total'], 'current': {'count': 658, 'metrics': {'commission': {'avg': 101.76041033434652}, 'qtysold': {'sum': 1315.0}}}}, {'group': ['CA', 'San Francisco', 'Curran Theatre', '$total'], 'current': {'count': 835, 'metrics': {'commission': {'avg': 110.12586826347307}, 'qtysold': {'sum': 1641.0}}}}, {'group': ['CA', 'San Francisco', 'Monster Park', '$total'], 'current': {'count': 523, 'metrics': {'commission': {'avg': 100.1586998087954}, 'qtysold': {'sum': 1050.0}}}}, {'group': ['CA', 'San Francisco', 'San Francisco Opera', '$total'], 'current': {'count': 1042, 'metrics': {'commission': {'avg': 95.43627639155471}, 'qtysold': {'sum': 2075.0}}}}, {'group': ['CA', 'San Francisco', 'War Memorial Opera House', '$total'], 'current': {'count': 830, 'metrics': {'commission': {'avg': 100.95939759036145}, 'qtysold': {'sum': 1691.0}}}}, {'group': ['CA', 'San Jose', 'HP Pavilion at San Jose', '$total'], 'current': {'count': 861, 'metrics': {'commission': {'avg': 95.11707317073171}, 'qtysold': {'sum': 1727.0}}}}, {'group': ['CA', 'San Jose', 'San Jose Repertory Theatre', '$total'], 'current': {'count': 1027, 'metrics': {'commission': {'avg': 94.4807205452775}, 'qtysold': {'sum': 2068.0}}}}, {'group': ['CA', 'Santa Clara', 'Buck Shaw Stadium', '$total'], 'current': {'count': 933, 'metrics': {'commission': {'avg': 94.80514469453377}, 'qtysold': {'sum': 1898.0}}}}, {'group': ['CA', 'Saratoga', 'Mountain Winery', '$total'], 'current': {'count': 648, 'metrics': {'commission': {'avg': 100.4099537037037}, 'qtysold': {'sum': 1337.0}}}}, {'group': ['CA', 'Saratoga', 'Villa Montalvo', '$total'], 'current': {'count': 719, 'metrics': {'commission': {'avg': 85.92642559109875}, 'qtysold': {'sum': 1407.0}}}}, {'group': ['CO', 'Commerce City', "Dick's Sporting Goods Park", '$total'], 'current': {'count': 930, 'metrics': {'commission': {'avg': 85.69935483870967}, 'qtysold': {'sum': 1879.0}}}}, {'group': ['CO', 'Denver', 'Coors Field', '$total'], 'current': {'count': 536, 'metrics': {'commission': {'avg': 89.23348880597015}, 'qtysold': {'sum': 1029.0}}}}, {'group': ['CO', 'Denver', 'Ellie Caulkins Opera House', '$total'], 'current': {'count': 748, 'metrics': {'commission': {'avg': 95.38997326203209}, 'qtysold': {'sum': 1497.0}}}}, {'group': ['CO', 'Denver', 'INVESCO Field', '$total'], 'current': {'count': 679, 'metrics': {'commission': {'avg': 93.91745213549336}, 'qtysold': {'sum': 1373.0}}}}, {'group': ['CO', 'Denver', 'Pepsi Center', '$total'], 'current': {'count': 689, 'metrics': {'commission': {'avg': 107.05907111756169}, 'qtysold': {'sum': 1367.0}}}}, {'group': ['DC', 'Washington', 'Kennedy Center Opera House', '$total'], 'current': {'count': 1085, 'metrics': {'commission': {'avg': 107.63958525345622}, 'qtysold': {'sum': 2175.0}}}}, {'group': ['DC', 'Washington', 'Nationals Park', '$total'], 'current': {'count': 668, 'metrics': {'commission': {'avg': 91.04303892215569}, 'qtysold': {'sum': 1305.0}}}}, {'group': ['DC', 'Washington', 'RFK Stadium', '$total'], 'current': {'count': 708, 'metrics': {'commission': {'avg': 91.33940677966102}, 'qtysold': {'sum': 1402.0}}}}, {'group': ['DC', 'Washington', 'Verizon Center', '$total'], 'current': {'count': 921, 'metrics': {'commission': {'avg': 97.7270358306189}, 'qtysold': {'sum': 1855.0}}}}, {'group': ['FL', 'Jacksonville', 'Jacksonville Municipal Stadium', '$total'], 'current': {'count': 657, 'metrics': {'commission': {'avg': 102.01141552511416}, 'qtysold': {'sum': 1350.0}}}}, {'group': ['FL', 'Miami', 'American Airlines Arena', '$total'], 'current': {'count': 792, 'metrics': {'commission': {'avg': 93.41856060606061}, 'qtysold': {'sum': 1579.0}}}}, {'group': ['FL', 'Miami Gardens', 'Dolphin Stadium', '$total'], 'current': {'count': 871, 'metrics': {'commission': {'avg': 93.74018369690012}, 'qtysold': {'sum': 1753.0}}}}, {'group': ['FL', 'Orlando', 'Amway Arena', '$total'], 'current': {'count': 784, 'metrics': {'commission': {'avg': 95.54713010204081}, 'qtysold': {'sum': 1567.0}}}}, {'group': ['FL', 'St. Petersburg', 'Tropicana Field', '$total'], 'current': {'count': 730, 'metrics': {'commission': {'avg': 88.69849315068494}, 'qtysold': {'sum': 1431.0}}}}, {'group': ['FL', 'Sunrise', 'BankAtlantic Center', '$total'], 'current': {'count': 445, 'metrics': {'commission': {'avg': 96.68595505617978}, 'qtysold': {'sum': 879.0}}}}, {'group': ['FL', 'Tampa', 'Raymond James Stadium', '$total'], 'current': {'count': 581, 'metrics': {'commission': {'avg': 103.36368330464717}, 'qtysold': {'sum': 1187.0}}}}, {'group': ['FL', 'Tampa', 'St. Pete Times Forum', '$total'], 'current': {'count': 579, 'metrics': {'commission': {'avg': 101.31554404145078}, 'qtysold': {'sum': 1201.0}}}}, {'group': ['GA', 'Atlanta', 'Georgia Dome', '$total'], 'current': {'count': 763, 'metrics': {'commission': {'avg': 97.29082568807338}, 'qtysold': {'sum': 1559.0}}}}, {'group': ['GA', 'Atlanta', 'Philips Arena', '$total'], 'current': {'count': 568, 'metrics': {'commission': {'avg': 98.17896126760563}, 'qtysold': {'sum': 1136.0}}}}, {'group': ['GA', 'Atlanta', 'Turner Field', '$total'], 'current': {'count': 745, 'metrics': {'commission': {'avg': 97.60530201342281}, 'qtysold': {'sum': 1473.0}}}}, {'group': ['IL', 'Bridgeview', 'Toyota Park', '$total'], 'current': {'count': 857, 'metrics': {'commission': {'avg': 90.58162193698949}, 'qtysold': {'sum': 1699.0}}}}, {'group': ['IL', 'Chicago', 'Lyric Opera House', '$total'], 'current': {'count': 1013, 'metrics': {'commission': {'avg': 103.63682132280356}, 'qtysold': {'sum': 2006.0}}}}, {'group': ['IL', 'Chicago', 'Soldier Field', '$total'], 'current': {'count': 673, 'metrics': {'commission': {'avg': 99.65839524517088}, 'qtysold': {'sum': 1349.0}}}}, {'group': ['IL', 'Chicago', 'U.S. Cellular Field', '$total'], 'current': {'count': 794, 'metrics': {'commission': {'avg': 97.20717884130983}, 'qtysold': {'sum': 1602.0}}}}, {'group': ['IL', 'Chicago', 'United Center', '$total'], 'current': {'count': 753, 'metrics': {'commission': {'avg': 102.1272908366534}, 'qtysold': {'sum': 1537.0}}}}, {'group': ['IL', 'Chicago', 'Wrigley Field', '$total'], 'current': {'count': 653, 'metrics': {'commission': {'avg': 102.08705972434916}, 'qtysold': {'sum': 1331.0}}}}, {'group': ['IN', 'Indianapolis', 'Conseco Fieldhouse', '$total'], 'current': {'count': 534, 'metrics': {'commission': {'avg': 90.48932584269663}, 'qtysold': {'sum': 1095.0}}}}, {'group': ['IN', 'Indianapolis', 'Lucas Oil Stadium', '$total'], 'current': {'count': 656, 'metrics': {'commission': {'avg': 93.69146341463414}, 'qtysold': {'sum': 1293.0}}}}, {'group': ['KS', 'Kansas City', 'CommunityAmerica Ballpark', '$total'], 'current': {'count': 555, 'metrics': {'commission': {'avg': 93.23297297297297}, 'qtysold': {'sum': 1151.0}}}}, {'group': ['LA', 'New Orleans', 'Louisiana Superdome', '$total'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 90.66821471652594}, 'qtysold': {'sum': 1677.0}}}}, {'group': ['LA', 'New Orleans', 'New Orleans Arena', '$total'], 'current': {'count': 681, 'metrics': {'commission': {'avg': 95.7057268722467}, 'qtysold': {'sum': 1377.0}}}}, {'group': ['MA', 'Boston', 'Charles Playhouse', '$total'], 'current': {'count': 1244, 'metrics': {'commission': {'avg': 103.33975080385852}, 'qtysold': {'sum': 2502.0}}}}, {'group': ['MA', 'Boston', 'Fenway Park', '$total'], 'current': {'count': 727, 'metrics': {'commission': {'avg': 85.51733149931223}, 'qtysold': {'sum': 1404.0}}}}, {'group': ['MA', 'Boston', 'TD Banknorth Garden', '$total'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 84.86019300361882}, 'qtysold': {'sum': 1667.0}}}}, {'group': ['MA', 'Foxborough', 'Gillette Stadium', '$total'], 'current': {'count': 562, 'metrics': {'commission': {'avg': 101.1894128113879}, 'qtysold': {'sum': 1094.0}}}}, {'group': ['MD', 'Baltimore', 'Lyric Opera House', '$total'], 'current': {'count': 1154, 'metrics': {'commission': {'avg': 97.08925476603119}, 'qtysold': {'sum': 2305.0}}}}, {'group': ['MD', 'Baltimore', 'M&T Bank Stadium', '$total'], 'current': {'count': 836, 'metrics': {'commission': {'avg': 107.96232057416267}, 'qtysold': {'sum': 1688.0}}}}, {'group': ['MD', 'Baltimore', 'Oriole Park at Camden Yards', '$total'], 'current': {'count': 941, 'metrics': {'commission': {'avg': 96.13071200850159}, 'qtysold': {'sum': 1878.0}}}}, {'group': ['MD', 'Landover', 'FedExField', '$total'], 'current': {'count': 858, 'metrics': {'commission': {'avg': 96.0340909090909}, 'qtysold': {'sum': 1730.0}}}}, {'group': ['MI', 'Auburn Hills', 'The Palace of Auburn Hills', '$total'], 'current': {'count': 858, 'metrics': {'commission': {'avg': 94.67115384615386}, 'qtysold': {'sum': 1717.0}}}}, {'group': ['MI', 'Detroit', 'Comerica Park', '$total'], 'current': {'count': 568, 'metrics': {'commission': {'avg': 96.39110915492958}, 'qtysold': {'sum': 1124.0}}}}, {'group': ['MI', 'Detroit', 'Detroit Opera House', '$total'], 'current': {'count': 1003, 'metrics': {'commission': {'avg': 90.81550348953141}, 'qtysold': {'sum': 2008.0}}}}, {'group': ['MI', 'Detroit', 'Ford Field', '$total'], 'current': {'count': 624, 'metrics': {'commission': {'avg': 93.95745192307692}, 'qtysold': {'sum': 1222.0}}}}, {'group': ['MI', 'Detroit', 'Joe Louis Arena', '$total'], 'current': {'count': 736, 'metrics': {'commission': {'avg': 104.90176630434782}, 'qtysold': {'sum': 1485.0}}}}, {'group': ['MN', 'Minneapolis', 'Hubert H. Humphrey Metrodome', '$total'], 'current': {'count': 651, 'metrics': {'commission': {'avg': 88.21958525345622}, 'qtysold': {'sum': 1311.0}}}}, {'group': ['MN', 'Minneapolis', 'Target Center', '$total'], 'current': {'count': 758, 'metrics': {'commission': {'avg': 99.10092348284961}, 'qtysold': {'sum': 1514.0}}}}, {'group': ['MN', 'Minneapolis', 'The Guthrie Theater', '$total'], 'current': {'count': 943, 'metrics': {'commission': {'avg': 103.7475079533404}, 'qtysold': {'sum': 1883.0}}}}, {'group': ['MN', 'St. Paul', 'Xcel Energy Center', '$total'], 'current': {'count': 828, 'metrics': {'commission': {'avg': 103.17409420289854}, 'qtysold': {'sum': 1663.0}}}}, {'group': ['MO', 'Kansas City', 'Arrowhead Stadium', '$total'], 'current': {'count': 603, 'metrics': {'commission': {'avg': 83.18134328358208}, 'qtysold': {'sum': 1160.0}}}}, {'group': ['MO', 'Kansas City', 'Kauffman Stadium', '$total'], 'current': {'count': 554, 'metrics': {'commission': {'avg': 101.24485559566787}, 'qtysold': {'sum': 1125.0}}}}, {'group': ['MO', 'St. Louis', 'Busch Stadium', '$total'], 'current': {'count': 737, 'metrics': {'commission': {'avg': 93.25257801899592}, 'qtysold': {'sum': 1449.0}}}}, {'group': ['MO', 'St. Louis', 'Edward Jones Dome', '$total'], 'current': {'count': 895, 'metrics': {'commission': {'avg': 104.81916201117318}, 'qtysold': {'sum': 1798.0}}}}, {'group': ['MO', 'St. Louis', 'Scottrade Center', '$total'], 'current': {'count': 803, 'metrics': {'commission': {'avg': 96.8194894146949}, 'qtysold': {'sum': 1608.0}}}}, {'group': ['NC', 'Charlotte', 'Bank of America Stadium', '$total'], 'current': {'count': 711, 'metrics': {'commission': {'avg': 92.35063291139241}, 'qtysold': {'sum': 1412.0}}}}, {'group': ['NC', 'Charlotte', 'Time Warner Cable Arena', '$total'], 'current': {'count': 599, 'metrics': {'commission': {'avg': 85.6915692821369}, 'qtysold': {'sum': 1221.0}}}}, {'group': ['NC', 'Raleigh', 'RBC Center', '$total'], 'current': {'count': 714, 'metrics': {'commission': {'avg': 96.1623949579832}, 'qtysold': {'sum': 1417.0}}}}, {'group': ['NJ', 'East Rutherford', 'Izod Center', '$total'], 'current': {'count': 826, 'metrics': {'commission': {'avg': 97.1115617433414}, 'qtysold': {'sum': 1702.0}}}}, {'group': ['NJ', 'East Rutherford', 'New York Giants Stadium', '$total'], 'current': {'count': 805, 'metrics': {'commission': {'avg': 89.8039751552795}, 'qtysold': {'sum': 1609.0}}}}, {'group': ['NJ', 'Newark', 'Prudential Center', '$total'], 'current': {'count': 525, 'metrics': {'commission': {'avg': 92.902}, 'qtysold': {'sum': 1066.0}}}}, {'group': ['NV', 'Las Vegas', 'Ballys Hotel', '$total'], 'current': {'count': 398, 'metrics': {'commission': {'avg': 98.10000000000001}, 'qtysold': {'sum': 787.0}}}}, {'group': ['NV', 'Las Vegas', 'Bellagio Hotel', '$total'], 'current': {'count': 465, 'metrics': {'commission': {'avg': 92.73967741935483}, 'qtysold': {'sum': 951.0}}}}, {'group': ['NV', 'Las Vegas', 'Caesars Palace', '$total'], 'current': {'count': 427, 'metrics': {'commission': {'avg': 89.00620608899298}, 'qtysold': {'sum': 862.0}}}}, {'group': ['NV', 'Las Vegas', 'Harrahs Hotel', '$total'], 'current': {'count': 518, 'metrics': {'commission': {'avg': 93.98918918918919}, 'qtysold': {'sum': 1066.0}}}}, {'group': ['NV', 'Las Vegas', 'Hilton Hotel', '$total'], 'current': {'count': 418, 'metrics': {'commission': {'avg': 98.68205741626794}, 'qtysold': {'sum': 862.0}}}}, {'group': ['NV', 'Las Vegas', 'Luxor Hotel', '$total'], 'current': {'count': 671, 'metrics': {'commission': {'avg': 100.90953800298063}, 'qtysold': {'sum': 1363.0}}}}, {'group': ['NV', 'Las Vegas', 'Mandalay Bay Hotel', '$total'], 'current': {'count': 332, 'metrics': {'commission': {'avg': 88.73765060240964}, 'qtysold': {'sum': 658.0}}}}, {'group': ['NV', 'Las Vegas', 'Mirage Hotel', '$total'], 'current': {'count': 432, 'metrics': {'commission': {'avg': 107.42291666666667}, 'qtysold': {'sum': 913.0}}}}, {'group': ['NV', 'Las Vegas', 'Paris Hotel', '$total'], 'current': {'count': 309, 'metrics': {'commission': {'avg': 93.64029126213592}, 'qtysold': {'sum': 634.0}}}}, {'group': ['NV', 'Las Vegas', 'Paris MGM Grand', '$total'], 'current': {'count': 378, 'metrics': {'commission': {'avg': 92.47698412698414}, 'qtysold': {'sum': 758.0}}}}, {'group': ['NV', 'Las Vegas', 'Sahara Hotel', '$total'], 'current': {'count': 378, 'metrics': {'commission': {'avg': 96.11111111111111}, 'qtysold': {'sum': 751.0}}}}, {'group': ['NV', 'Las Vegas', 'Tropicana Hotel', '$total'], 'current': {'count': 443, 'metrics': {'commission': {'avg': 95.37799097065462}, 'qtysold': {'sum': 905.0}}}}, {'group': ['NV', 'Las Vegas', 'Venetian Hotel', '$total'], 'current': {'count': 589, 'metrics': {'commission': {'avg': 100.2455857385399}, 'qtysold': {'sum': 1158.0}}}}, {'group': ['NV', 'Las Vegas', 'Wynn Hotel', '$total'], 'current': {'count': 327, 'metrics': {'commission': {'avg': 107.62752293577981}, 'qtysold': {'sum': 660.0}}}}, {'group': ['NY', 'Buffalo', 'HSBC Arena', '$total'], 'current': {'count': 732, 'metrics': {'commission': {'avg': 95.04282786885247}, 'qtysold': {'sum': 1453.0}}}}, {'group': ['NY', 'New York City', 'Al Hirschfeld Theatre', '$total'], 'current': {'count': 1191, 'metrics': {'commission': {'avg': 97.23211586901763}, 'qtysold': {'sum': 2361.0}}}}, {'group': ['NY', 'New York City', 'Ambassador Theatre', '$total'], 'current': {'count': 1168, 'metrics': {'commission': {'avg': 101.56142979452055}, 'qtysold': {'sum': 2321.0}}}}, {'group': ['NY', 'New York City', 'American Airlines Theatre', '$total'], 'current': {'count': 929, 'metrics': {'commission': {'avg': 99.22475780409042}, 'qtysold': {'sum': 1889.0}}}}, {'group': ['NY', 'New York City', 'August Wilson Theatre', '$total'], 'current': {'count': 1583, 'metrics': {'commission': {'avg': 97.80379027163613}, 'qtysold': {'sum': 3187.0}}}}, {'group': ['NY', 'New York City', 'Belasco Theatre', '$total'], 'current': {'count': 1217, 'metrics': {'commission': {'avg': 87.27534921939196}, 'qtysold': {'sum': 2394.0}}}}, {'group': ['NY', 'New York City', 'Bernard B. Jacobs Theatre', '$total'], 'current': {'count': 1217, 'metrics': {'commission': {'avg': 96.05398520953163}, 'qtysold': {'sum': 2412.0}}}}, {'group': ['NY', 'New York City', 'Biltmore Theatre', '$total'], 'current': {'count': 1305, 'metrics': {'commission': {'avg': 95.2851724137931}, 'qtysold': {'sum': 2629.0}}}}, {'group': ['NY', 'New York City', 'Booth Theatre', '$total'], 'current': {'count': 1210, 'metrics': {'commission': {'avg': 97.16082644628099}, 'qtysold': {'sum': 2447.0}}}}, {'group': ['NY', 'New York City', 'Broadhurst Theatre', '$total'], 'current': {'count': 1055, 'metrics': {'commission': {'avg': 101.01042654028436}, 'qtysold': {'sum': 2131.0}}}}, {'group': ['NY', 'New York City', 'Brooks Atkinson Theatre', '$total'], 'current': {'count': 1013, 'metrics': {'commission': {'avg': 100.29787759131293}, 'qtysold': {'sum': 2049.0}}}}, {'group': ['NY', 'New York City', 'Carnegie Hall', '$total'], 'current': {'count': 1211, 'metrics': {'commission': {'avg': 84.96515276630883}, 'qtysold': {'sum': 2390.0}}}}, {'group': ['NY', 'New York City', 'Circle in the Square Theatre', '$total'], 'current': {'count': 1047, 'metrics': {'commission': {'avg': 93.35444126074499}, 'qtysold': {'sum': 2127.0}}}}, {'group': ['NY', 'New York City', 'Cort Theatre', '$total'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 100.08507393715342}, 'qtysold': {'sum': 2152.0}}}}, {'group': ['NY', 'New York City', 'Ethel Barrymore Theatre', '$total'], 'current': {'count': 1413, 'metrics': {'commission': {'avg': 94.60424628450106}, 'qtysold': {'sum': 2828.0}}}}, {'group': ['NY', 'New York City', "Eugene O'Neill Theatre", '$total'], 'current': {'count': 1239, 'metrics': {'commission': {'avg': 100.35714285714286}, 'qtysold': {'sum': 2488.0}}}}, {'group': ['NY', 'New York City', 'George Gershwin Theatre', '$total'], 'current': {'count': 1137, 'metrics': {'commission': {'avg': 96.40316622691293}, 'qtysold': {'sum': 2284.0}}}}, {'group': ['NY', 'New York City', 'Gerald Schoenfeld Theatre', '$total'], 'current': {'count': 1132, 'metrics': {'commission': {'avg': 91.84730565371024}, 'qtysold': {'sum': 2275.0}}}}, {'group': ['NY', 'New York City', 'Helen Hayes Theatre', '$total'], 'current': {'count': 1456, 'metrics': {'commission': {'avg': 100.83430631868131}, 'qtysold': {'sum': 2948.0}}}}, {'group': ['NY', 'New York City', 'Hilton Theatre', '$total'], 'current': {'count': 1488, 'metrics': {'commission': {'avg': 89.2828629032258}, 'qtysold': {'sum': 2999.0}}}}, {'group': ['NY', 'New York City', 'Imperial Theatre', '$total'], 'current': {'count': 1357, 'metrics': {'commission': {'avg': 97.0515475313191}, 'qtysold': {'sum': 2702.0}}}}, {'group': ['NY', 'New York City', 'John Golden Theatre', '$total'], 'current': {'count': 1208, 'metrics': {'commission': {'avg': 91.7873344370861}, 'qtysold': {'sum': 2388.0}}}}, {'group': ['NY', 'New York City', 'Lincoln Center for the Performing Arts', '$total'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 92.61959334565618}, 'qtysold': {'sum': 2155.0}}}}, {'group': ['NY', 'New York City', 'Longacre Theatre', '$total'], 'current': {'count': 1143, 'metrics': {'commission': {'avg': 102.5251968503937}, 'qtysold': {'sum': 2268.0}}}}, {'group': ['NY', 'New York City', 'Lunt-Fontanne Theatre', '$total'], 'current': {'count': 1672, 'metrics': {'commission': {'avg': 100.04623205741626}, 'qtysold': {'sum': 3326.0}}}}, {'group': ['NY', 'New York City', 'Lyceum Theatre', '$total'], 'current': {'count': 1221, 'metrics': {'commission': {'avg': 94.2}, 'qtysold': {'sum': 2470.0}}}}, {'group': ['NY', 'New York City', 'Madison Square Garden', '$total'], 'current': {'count': 923, 'metrics': {'commission': {'avg': 96.59106175514627}, 'qtysold': {'sum': 1847.0}}}}, {'group': ['NY', 'New York City', 'Majestic Theatre', '$total'], 'current': {'count': 1265, 'metrics': {'commission': {'avg': 106.0405138339921}, 'qtysold': {'sum': 2549.0}}}}, {'group': ['NY', 'New York City', 'Marquis Theatre', '$total'], 'current': {'count': 1023, 'metrics': {'commission': {'avg': 98.0991202346041}, 'qtysold': {'sum': 2027.0}}}}, {'group': ['NY', 'New York City', 'Metropolitan Opera', '$total'], 'current': {'count': 1088, 'metrics': {'commission': {'avg': 96.12973345588235}, 'qtysold': {'sum': 2132.0}}}}, {'group': ['NY', 'New York City', 'Minskoff Theatre', '$total'], 'current': {'count': 1185, 'metrics': {'commission': {'avg': 100.19949367088607}, 'qtysold': {'sum': 2329.0}}}}, {'group': ['NY', 'New York City', 'Music Box Theatre', '$total'], 'current': {'count': 963, 'metrics': {'commission': {'avg': 92.48333333333333}, 'qtysold': {'sum': 1923.0}}}}, {'group': ['NY', 'New York City', 'Nederlander Theatre', '$total'], 'current': {'count': 1465, 'metrics': {'commission': {'avg': 95.8681228668942}, 'qtysold': {'sum': 2934.0}}}}, {'group': ['NY', 'New York City', 'Neil Simon Theatre', '$total'], 'current': {'count': 1107, 'metrics': {'commission': {'avg': 96.67615176151762}, 'qtysold': {'sum': 2243.0}}}}, {'group': ['NY', 'New York City', 'New Amsterdam Theatre', '$total'], 'current': {'count': 1016, 'metrics': {'commission': {'avg': 98.37563976377952}, 'qtysold': {'sum': 2055.0}}}}, {'group': ['NY', 'New York City', 'Palace Theatre', '$total'], 'current': {'count': 1039, 'metrics': {'commission': {'avg': 94.59889316650626}, 'qtysold': {'sum': 2089.0}}}}, {'group': ['NY', 'New York City', 'Richard Rodgers Theatre', '$total'], 'current': {'count': 1099, 'metrics': {'commission': {'avg': 93.30832575068244}, 'qtysold': {'sum': 2208.0}}}}, {'group': ['NY', 'New York City', 'Shea Stadium', '$total'], 'current': {'count': 539, 'metrics': {'commission': {'avg': 99.38738404452691}, 'qtysold': {'sum': 1099.0}}}}, {'group': ['NY', 'New York City', 'Shubert Theatre', '$total'], 'current': {'count': 992, 'metrics': {'commission': {'avg': 95.96915322580645}, 'qtysold': {'sum': 1987.0}}}}, {'group': ['NY', 'New York City', 'St. James Theatre', '$total'], 'current': {'count': 958, 'metrics': {'commission': {'avg': 90.2776096033403}, 'qtysold': {'sum': 1947.0}}}}, {'group': ['NY', 'New York City', 'Studio 54', '$total'], 'current': {'count': 1146, 'metrics': {'commission': {'avg': 90.83023560209423}, 'qtysold': {'sum': 2304.0}}}}, {'group': ['NY', 'New York City', 'The Broadway Theatre', '$total'], 'current': {'count': 1118, 'metrics': {'commission': {'avg': 93.95232558139534}, 'qtysold': {'sum': 2215.0}}}}, {'group': ['NY', 'New York City', 'Vivian Beaumont Theatre', '$total'], 'current': {'count': 1055, 'metrics': {'commission': {'avg': 102.36341232227488}, 'qtysold': {'sum': 2088.0}}}}, {'group': ['NY', 'New York City', 'Walter Kerr Theatre', '$total'], 'current': {'count': 1208, 'metrics': {'commission': {'avg': 95.24031456953642}, 'qtysold': {'sum': 2401.0}}}}, {'group': ['NY', 'New York City', 'Winter Garden Theatre', '$total'], 'current': {'count': 1451, 'metrics': {'commission': {'avg': 97.09755341144037}, 'qtysold': {'sum': 2838.0}}}}, {'group': ['NY', 'New York City', 'Yankee Stadium', '$total'], 'current': {'count': 869, 'metrics': {'commission': {'avg': 109.60978135788261}, 'qtysold': {'sum': 1765.0}}}}, {'group': ['NY', 'Orchard Park', 'Ralph Wilson Stadium', '$total'], 'current': {'count': 661, 'metrics': {'commission': {'avg': 102.43888048411499}, 'qtysold': {'sum': 1327.0}}}}, {'group': ['NY', 'Saratoga Springs', 'Saratoga Springs Performing Arts Center', '$total'], 'current': {'count': 782, 'metrics': {'commission': {'avg': 95.82717391304348}, 'qtysold': {'sum': 1542.0}}}}, {'group': ['NY', 'Uniondale', 'Nassau Veterans Memorial Coliseum', '$total'], 'current': {'count': 713, 'metrics': {'commission': {'avg': 93.24635343618513}, 'qtysold': {'sum': 1451.0}}}}, {'group': [None, None, None, '$total'], 'current': {'count': 2777, 'metrics': {'commission': {'avg': 96.69927979834354}, 'qtysold': {'sum': 5553.0}}}}, {'group': ['OH', 'Cincinnati', 'Great American Ball Park', '$total'], 'current': {'count': 879, 'metrics': {'commission': {'avg': 111.43105802047782}, 'qtysold': {'sum': 1758.0}}}}, {'group': ['OH', 'Cincinnati', 'Paul Brown Stadium', '$total'], 'current': {'count': 880, 'metrics': {'commission': {'avg': 88.91454545454546}, 'qtysold': {'sum': 1787.0}}}}, {'group': ['OH', 'Cleveland', 'Cleveland Browns Stadium', '$total'], 'current': {'count': 617, 'metrics': {'commission': {'avg': 106.50097244732578}, 'qtysold': {'sum': 1239.0}}}}, {'group': ['OH', 'Cleveland', 'Progressive Field', '$total'], 'current': {'count': 742, 'metrics': {'commission': {'avg': 107.71314016172506}, 'qtysold': {'sum': 1486.0}}}}, {'group': ['OH', 'Cleveland', 'Quicken Loans Arena', '$total'], 'current': {'count': 778, 'metrics': {'commission': {'avg': 90.58284061696658}, 'qtysold': {'sum': 1543.0}}}}, {'group': ['OH', 'Columbus', 'Columbus Crew Stadium', '$total'], 'current': {'count': 686, 'metrics': {'commission': {'avg': 97.54395043731778}, 'qtysold': {'sum': 1366.0}}}}, {'group': ['OH', 'Columbus', 'Nationwide Arena', '$total'], 'current': {'count': 865, 'metrics': {'commission': {'avg': 93.1864161849711}, 'qtysold': {'sum': 1700.0}}}}, {'group': ['OH', 'Dayton', 'E.J. Nutter Center', '$total'], 'current': {'count': 797, 'metrics': {'commission': {'avg': 86.60250941028858}, 'qtysold': {'sum': 1540.0}}}}, {'group': ['OK', 'Oklahoma City', 'Ford Center', '$total'], 'current': {'count': 761, 'metrics': {'commission': {'avg': 94.14086727989488}, 'qtysold': {'sum': 1502.0}}}}, {'group': ['ON', 'Ottawa', 'Scotiabank Place', '$total'], 'current': {'count': 789, 'metrics': {'commission': {'avg': 90.74182509505704}, 'qtysold': {'sum': 1598.0}}}}, {'group': ['ON', 'Toronto', 'Air Canada Centre', '$total'], 'current': {'count': 882, 'metrics': {'commission': {'avg': 100.60510204081632}, 'qtysold': {'sum': 1798.0}}}}, {'group': ['ON', 'Toronto', 'BMO Field', '$total'], 'current': {'count': 756, 'metrics': {'commission': {'avg': 92.62718253968254}, 'qtysold': {'sum': 1552.0}}}}, {'group': ['ON', 'Toronto', 'Rogers Centre', '$total'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 83.99956011730205}, 'qtysold': {'sum': 1329.0}}}}, {'group': ['OR', 'Portland', 'Rose Garden', '$total'], 'current': {'count': 849, 'metrics': {'commission': {'avg': 87.40053003533569}, 'qtysold': {'sum': 1711.0}}}}, {'group': ['PA', 'Hershey', 'Hersheypark Stadium', '$total'], 'current': {'count': 794, 'metrics': {'commission': {'avg': 96.34609571788414}, 'qtysold': {'sum': 1554.0}}}}, {'group': ['PA', 'Philadelphia', 'Citizens Bank Park', '$total'], 'current': {'count': 788, 'metrics': {'commission': {'avg': 109.20989847715735}, 'qtysold': {'sum': 1620.0}}}}, {'group': ['PA', 'Philadelphia', 'Lincoln Financial Field', '$total'], 'current': {'count': 694, 'metrics': {'commission': {'avg': 93.15410662824208}, 'qtysold': {'sum': 1390.0}}}}, {'group': ['PA', 'Philadelphia', 'Wachovia Center', '$total'], 'current': {'count': 791, 'metrics': {'commission': {'avg': 96.54481668773704}, 'qtysold': {'sum': 1593.0}}}}, {'group': ['PA', 'Pittsburgh', 'Heinz Field', '$total'], 'current': {'count': 538, 'metrics': {'commission': {'avg': 89.25920074349442}, 'qtysold': {'sum': 1040.0}}}}, {'group': ['PA', 'Pittsburgh', 'Mellon Arena', '$total'], 'current': {'count': 593, 'metrics': {'commission': {'avg': 109.46964586846543}, 'qtysold': {'sum': 1176.0}}}}, {'group': ['PA', 'Pittsburgh', 'PNC Park', '$total'], 'current': {'count': 813, 'metrics': {'commission': {'avg': 100.03911439114391}, 'qtysold': {'sum': 1649.0}}}}, {'group': ['QC', 'Montreal', 'Bell Centre', '$total'], 'current': {'count': 555, 'metrics': {'commission': {'avg': 99.7481081081081}, 'qtysold': {'sum': 1123.0}}}}, {'group': ['SC', 'Charleston', 'North Charleston Coliseum', '$total'], 'current': {'count': 837, 'metrics': {'commission': {'avg': 101.26290322580645}, 'qtysold': {'sum': 1719.0}}}}, {'group': ['TN', 'Memphis', 'FedExForum', '$total'], 'current': {'count': 882, 'metrics': {'commission': {'avg': 95.33401360544218}, 'qtysold': {'sum': 1764.0}}}}, {'group': ['TN', 'Nashville', 'LP Field', '$total'], 'current': {'count': 666, 'metrics': {'commission': {'avg': 101.55202702702702}, 'qtysold': {'sum': 1330.0}}}}, {'group': ['TN', 'Nashville', 'Sommet Center', '$total'], 'current': {'count': 626, 'metrics': {'commission': {'avg': 92.69712460063899}, 'qtysold': {'sum': 1288.0}}}}, {'group': ['TX', 'Arlington', 'Rangers BallPark in Arlington', '$total'], 'current': {'count': 711, 'metrics': {'commission': {'avg': 89.17257383966245}, 'qtysold': {'sum': 1428.0}}}}, {'group': ['TX', 'Dallas', 'American Airlines Center', '$total'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 90.375}, 'qtysold': {'sum': 1347.0}}}}, {'group': ['TX', 'Dallas', 'Superpages.com Center', '$total'], 'current': {'count': 742, 'metrics': {'commission': {'avg': 90.65033692722372}, 'qtysold': {'sum': 1481.0}}}}, {'group': ['TX', 'Frisco', 'Pizza Hut Park', '$total'], 'current': {'count': 866, 'metrics': {'commission': {'avg': 99.03412240184758}, 'qtysold': {'sum': 1735.0}}}}, {'group': ['TX', 'Galveston', 'Grand 1894 Opera House', '$total'], 'current': {'count': 1082, 'metrics': {'commission': {'avg': 91.13664510166359}, 'qtysold': {'sum': 2142.0}}}}, {'group': ['TX', 'Houston', 'Minute Maid Park', '$total'], 'current': {'count': 780, 'metrics': {'commission': {'avg': 97.1546153846154}, 'qtysold': {'sum': 1553.0}}}}, {'group': ['TX', 'Houston', 'Reliant Stadium', '$total'], 'current': {'count': 829, 'metrics': {'commission': {'avg': 95.29270205066344}, 'qtysold': {'sum': 1684.0}}}}, {'group': ['TX', 'Houston', 'Robertson Stadium', '$total'], 'current': {'count': 817, 'metrics': {'commission': {'avg': 99.72576499388005}, 'qtysold': {'sum': 1637.0}}}}, {'group': ['TX', 'Houston', 'Toyota Center', '$total'], 'current': {'count': 628, 'metrics': {'commission': {'avg': 97.96074840764331}, 'qtysold': {'sum': 1269.0}}}}, {'group': ['TX', 'Irving', 'Texas Stadium', '$total'], 'current': {'count': 516, 'metrics': {'commission': {'avg': 101.7392441860465}, 'qtysold': {'sum': 1028.0}}}}, {'group': ['TX', 'San Antonio', 'AT&T Center', '$total'], 'current': {'count': 708, 'metrics': {'commission': {'avg': 100.4489406779661}, 'qtysold': {'sum': 1426.0}}}}, {'group': ['UT', 'Salt Lake City', 'EnergySolutions Arena', '$total'], 'current': {'count': 602, 'metrics': {'commission': {'avg': 93.53421926910299}, 'qtysold': {'sum': 1158.0}}}}, {'group': ['UT', 'Salt Lake City', 'Rice-Eccles Stadium', '$total'], 'current': {'count': 768, 'metrics': {'commission': {'avg': 92.0978515625}, 'qtysold': {'sum': 1534.0}}}}, {'group': ['WA', 'Seattle', 'Paramount Theatre', '$total'], 'current': {'count': 1147, 'metrics': {'commission': {'avg': 93.5312118570183}, 'qtysold': {'sum': 2326.0}}}}, {'group': ['WA', 'Seattle', 'Qwest Field', '$total'], 'current': {'count': 770, 'metrics': {'commission': {'avg': 93.83571428571429}, 'qtysold': {'sum': 1543.0}}}}, {'group': ['WA', 'Seattle', 'Safeco Field', '$total'], 'current': {'count': 682, 'metrics': {'commission': {'avg': 90.6050586510264}, 'qtysold': {'sum': 1373.0}}}}, {'group': ['WI', 'Green Bay', 'Lambeau Field', '$total'], 'current': {'count': 921, 'metrics': {'commission': {'avg': 92.20684039087948}, 'qtysold': {'sum': 1845.0}}}}, {'group': ['WI', 'Milwaukee', 'Bradley Center', '$total'], 'current': {'count': 705, 'metrics': {'commission': {'avg': 100.02914893617022}, 'qtysold': {'sum': 1428.0}}}}, {'group': ['WI', 'Milwaukee', 'Miller Park', '$total'], 'current': {'count': 1100, 'metrics': {'commission': {'avg': 96.67936363636363}, 'qtysold': {'sum': 2207.0}}}}, {'group': ['Concerts', 'Pop', '$columnTotal'], 'current': {'count': 97582, 'metrics': {'commission': {'avg': 95.97196665368612}, 'qtysold': {'sum': 195444.0}}}}, {'group': ['Shows', 'Musicals', '$columnTotal'], 'current': {'count': 25737, 'metrics': {'commission': {'avg': 95.21475113649609}, 'qtysold': {'sum': 51573.0}}}}, {'group': ['Shows', 'Opera', '$columnTotal'], 'current': {'count': 9914, 'metrics': {'commission': {'avg': 97.66947246318338}, 'qtysold': {'sum': 19787.0}}}}, {'group': ['Shows', 'Plays', '$columnTotal'], 'current': {'count': 39223, 'metrics': {'commission': {'avg': 97.66823037503505}, 'qtysold': {'sum': 78545.0}}}}, {'group': ['$absoluteTotal'], 'current': {'count': 172456, 'metrics': {'commission': {'avg': 96.34234036507864}, 'qtysold': {'sum': 345349.0}}}}], 'visualization': 'Pivot Table'}
    TS_GEO_HASH_PRECISION_1_RESULT = {
        'data': [{'geohash': 'd', 'count': 9680, 'extras+avg': 0.6941745867413923, 'fare+sum': 111869.35001929477},
                 {'geohash': '7', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}],
        'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_2_RESULT = {'data': [{'geohash': 'dp', 'count': 9680, 'extras+avg': 0.6941745867413923, 'fare+sum': 111869.35001929477}, {'geohash': '7z', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_3_RESULT = {'data': [{'geohash': 'dp3', 'count': 9680, 'extras+avg': 0.6941745867413923, 'fare+sum': 111869.35001929477}, {'geohash': '7zz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_4_RESULT = {'data': [{'geohash': 'dp3w', 'count': 9039, 'extras+avg': 0.6135479588070226, 'fare+sum': 93054.5300100632}, {'geohash': 'dp3q', 'count': 348, 'extras+avg': 2.305316091954023, 'fare+sum': 11415.440001249313}, {'geohash': '7zzz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}, {'geohash': 'dp3t', 'count': 293, 'extras+avg': 1.2679180887372015, 'fare+sum': 7399.380007982254}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_5_RESULT = {'data': [{'geohash': 'dp3wm', 'count': 3346, 'extras+avg': 0.5692618051404662, 'fare+sum': 30136.430019387975}, {'geohash': 'dp3wq', 'count': 1981, 'extras+avg': 0.7115093387178193, 'fare+sum': 19008.350019762293}, {'geohash': 'dp3wt', 'count': 1012, 'extras+avg': 0.6078162051943451, 'fare+sum': 11932.079979896544}, {'geohash': 'dp3wn', 'count': 759, 'extras+avg': 0.6637022397891963, 'fare+sum': 8941.939994335175}, {'geohash': 'dp3wj', 'count': 728, 'extras+avg': 0.5336538461538461, 'fare+sum': 7238.269993305206}, {'geohash': 'dp3wk', 'count': 482, 'extras+avg': 0.6545643153526971, 'fare+sum': 5639.330008506775}, {'geohash': 'dp3qz', 'count': 348, 'extras+avg': 2.305316091954023, 'fare+sum': 11415.440001249313}, {'geohash': '7zzzz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}, {'geohash': 'dp3wv', 'count': 187, 'extras+avg': 0.45989304812834225, 'fare+sum': 2609.9899983406067}, {'geohash': 'dp3ws', 'count': 165, 'extras+avg': 0.4575757575757576, 'fare+sum': 2011.979993343353}, {'geohash': 'dp3wu', 'count': 122, 'extras+avg': 0.5, 'fare+sum': 1795.7000045776367}, {'geohash': 'dp3te', 'count': 99, 'extras+avg': 1.8838383838383839, 'fare+sum': 2832.1400027275085}, {'geohash': 'dp3ty', 'count': 95, 'extras+avg': 0.8789473684210526, 'fare+sum': 2037.1000037193303}, {'geohash': 'dp3we', 'count': 71, 'extras+avg': 0.6408450704225352, 'fare+sum': 989.3500008583067}, {'geohash': 'dp3wh', 'count': 50, 'extras+avg': 0.56, 'fare+sum': 593.0399999618529}, {'geohash': 'dp3wg', 'count': 41, 'extras+avg': 0.4878048780487805, 'fare+sum': 529.6299977302549}, {'geohash': 'dp3tf', 'count': 29, 'extras+avg': 1.9137931034482758, 'fare+sum': 889.6900062561035}, {'geohash': 'dp3wd', 'count': 21, 'extras+avg': 0.35714285714285715, 'fare+sum': 404.59999990463245}, {'geohash': 'dp3tw', 'count': 21, 'extras+avg': 0.7857142857142857, 'fare+sum': 456.49999618530273}, {'geohash': 'dp3wc', 'count': 20, 'extras+avg': 0.825, 'fare+sum': 357.5900006294249}, {'geohash': 'dp3wb', 'count': 19, 'extras+avg': 2.236842105263158, 'fare+sum': 320.6000003814697}, {'geohash': 'dp3tu', 'count': 17, 'extras+avg': 0.4117647058823529, 'fare+sum': 316.7499990463257}, {'geohash': 'dp3w7', 'count': 16, 'extras+avg': 1.015625, 'fare+sum': 224.04999780654896}, {'geohash': 'dp3wf', 'count': 11, 'extras+avg': 0.2727272727272727, 'fare+sum': 166.75000190734872}, {'geohash': 'dp3w5', 'count': 6, 'extras+avg': 1.1666666666666667, 'fare+sum': 109.7499990463257}, {'geohash': 'dp3tv', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 119.2500000000001}, {'geohash': 'dp3tx', 'count': 5, 'extras+avg': 0.5, 'fare+sum': 87.85000085830691}, {'geohash': 'dp3tq', 'count': 4, 'extras+avg': 0.5, 'fare+sum': 140.7999982833862}, {'geohash': 'dp3tk', 'count': 4, 'extras+avg': 2.75, 'fare+sum': 141.10000157356262}, {'geohash': 'dp3w9', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 45.1000003814698}, {'geohash': 'dp3tj', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 72.5999984741211}, {'geohash': 'dp3tg', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 30.3000001907348}, {'geohash': 'dp3ts', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3td', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 71.6500015258789}, {'geohash': 'dp3tm', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 28.2999992370605}, {'geohash': 'dp3th', 'count': 1, 'extras+avg': 3.0, 'fare+sum': 68.25}, {'geohash': 'dp3tt', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.25}, {'geohash': 'dp3tr', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 46.0}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_6_RESULT = {'data': [{'geohash': 'dp3wmb', 'count': 895, 'extras+avg': 0.43435754189944137, 'fare+sum': 7642.2900059223175}, {'geohash': 'dp3wq4', 'count': 885, 'extras+avg': 0.711864406779661, 'fare+sum': 8915.880015680566}, {'geohash': 'dp3wmf', 'count': 825, 'extras+avg': 0.6924242424242424, 'fare+sum': 6900.74999714829}, {'geohash': 'dp3wq0', 'count': 500, 'extras+avg': 0.806, 'fare+sum': 4521.259998083115}, {'geohash': 'dp3wt7', 'count': 394, 'extras+avg': 0.5624619280626325, 'fare+sum': 4414.839994430542}, {'geohash': 'dp3wmg', 'count': 390, 'extras+avg': 0.4948717948717949, 'fare+sum': 4125.78000497818}, {'geohash': 'dp3wq5', 'count': 373, 'extras+avg': 0.6179624664879356, 'fare+sum': 3581.7200043201447}, {'geohash': 'dp3wnp', 'count': 329, 'extras+avg': 0.5083586626139818, 'fare+sum': 3693.2199988365173}, {'geohash': '7zzzzz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}, {'geohash': 'dp3wjx', 'count': 312, 'extras+avg': 0.6121794871794872, 'fare+sum': 2575.690001010895}, {'geohash': 'dp3qzd', 'count': 277, 'extras+avg': 2.4521660649819497, 'fare+sum': 9363.659996271133}, {'geohash': 'dp3wkg', 'count': 236, 'extras+avg': 0.6038135593220338, 'fare+sum': 2616.9000017642975}, {'geohash': 'dp3wmr', 'count': 236, 'extras+avg': 0.7902542372881356, 'fare+sum': 2532.230007171631}, {'geohash': 'dp3wnh', 'count': 212, 'extras+avg': 0.660377358490566, 'fare+sum': 2430.589998722077}, {'geohash': 'dp3wm8', 'count': 199, 'extras+avg': 0.41708542713567837, 'fare+sum': 1629.880003452301}, {'geohash': 'dp3wjn', 'count': 172, 'extras+avg': 0.37209302325581395, 'fare+sum': 2094.479995727539}, {'geohash': 'dp3wm2', 'count': 137, 'extras+avg': 0.5218978102189781, 'fare+sum': 1092.809996843338}, {'geohash': 'dp3wtr', 'count': 122, 'extras+avg': 0.5368852459016393, 'fare+sum': 1586.1799941062923}, {'geohash': 'dp3wv5', 'count': 113, 'extras+avg': 0.5132743362831859, 'fare+sum': 1488.1499972343447}, {'geohash': 'dp3wkr', 'count': 111, 'extras+avg': 0.6576576576576577, 'fare+sum': 1426.979999303818}, {'geohash': 'dp3wmy', 'count': 110, 'extras+avg': 0.6772727272727272, 'fare+sum': 1076.3400044441225}, {'geohash': 'dp3wnn', 'count': 107, 'extras+avg': 0.9112149532710281, 'fare+sum': 1241.1899988651276}, {'geohash': 'dp3ten', 'count': 97, 'extras+avg': 1.922680412371134, 'fare+sum': 2773.190001964569}, {'geohash': 'dp3wmv', 'count': 96, 'extras+avg': 0.453125, 'fare+sum': 858.42999958992}, {'geohash': 'dp3wq6', 'count': 93, 'extras+avg': 0.7419354838709677, 'fare+sum': 853.4499983787537}, {'geohash': 'dp3wjr', 'count': 72, 'extras+avg': 0.4583333333333333, 'fare+sum': 570.0500001907349}, {'geohash': 'dp3wn4', 'count': 71, 'extras+avg': 0.823943661971831, 'fare+sum': 1019.849999666214}, {'geohash': 'dp3qz6', 'count': 70, 'extras+avg': 1.7285714285714286, 'fare+sum': 2008.1300034523015}, {'geohash': 'dp3wqj', 'count': 66, 'extras+avg': 0.4772727272727273, 'fare+sum': 561.7000007629395}, {'geohash': 'dp3wss', 'count': 65, 'extras+avg': 0.34615384615384615, 'fare+sum': 814.0499963760374}, {'geohash': 'dp3wqh', 'count': 64, 'extras+avg': 0.7109375, 'fare+sum': 574.3400025367737}, {'geohash': 'dp3wtk', 'count': 63, 'extras+avg': 0.753968253968254, 'fare+sum': 809.1799993515014}, {'geohash': 'dp3wmk', 'count': 62, 'extras+avg': 0.49193548387096775, 'fare+sum': 655.4200019836427}, {'geohash': 'dp3wu9', 'count': 61, 'extras+avg': 0.5081967213114754, 'fare+sum': 909.520004272461}, {'geohash': 'dp3wev', 'count': 58, 'extras+avg': 0.5344827586206896, 'fare+sum': 829.9500012397764}, {'geohash': 'dp3wt9', 'count': 56, 'extras+avg': 0.5089285714285714, 'fare+sum': 622.7500035762787}, {'geohash': 'dp3wmu', 'count': 55, 'extras+avg': 0.6454545454545455, 'fare+sum': 492.84000062942505}, {'geohash': 'dp3wm7', 'count': 55, 'extras+avg': 0.6590909090909091, 'fare+sum': 430.49000048637396}, {'geohash': 'dp3tyb', 'count': 52, 'extras+avg': 1.0480769230769231, 'fare+sum': 1270.749999523163}, {'geohash': 'dp3wku', 'count': 50, 'extras+avg': 0.77, 'fare+sum': 516.8000001907346}, {'geohash': 'dp3wjt', 'count': 50, 'extras+avg': 0.72, 'fare+sum': 545.8399968147276}, {'geohash': 'dp3wmz', 'count': 49, 'extras+avg': 0.5612244897959183, 'fare+sum': 516.3499989509581}, {'geohash': 'dp3wvp', 'count': 48, 'extras+avg': 0.3333333333333333, 'fare+sum': 757.5900006294248}, {'geohash': 'dp3wjy', 'count': 47, 'extras+avg': 0.5212765957446809, 'fare+sum': 341.0399994850159}, {'geohash': 'dp3wmx', 'count': 43, 'extras+avg': 0.5465116279069767, 'fare+sum': 360.33999776840204}, {'geohash': 'dp3wm6', 'count': 43, 'extras+avg': 0.7674418604651163, 'fare+sum': 423.1999988555908}, {'geohash': 'dp3wte', 'count': 43, 'extras+avg': 0.7674418604651163, 'fare+sum': 515.9400010108948}, {'geohash': 'dp3wt2', 'count': 43, 'extras+avg': 0.8837209302325582, 'fare+sum': 518.449996471405}, {'geohash': 'dp3wt6', 'count': 41, 'extras+avg': 0.7439024390243902, 'fare+sum': 418.8999998569488}, {'geohash': 'dp3ws4', 'count': 41, 'extras+avg': 0.4268292682926829, 'fare+sum': 508.1399979591372}, {'geohash': 'dp3wuq', 'count': 41, 'extras+avg': 0.5, 'fare+sum': 650.9400033950803}, {'geohash': 'dp3wt8', 'count': 40, 'extras+avg': 0.8375, 'fare+sum': 468.99999761581404}, {'geohash': 'dp3wn5', 'count': 39, 'extras+avg': 1.0384615384615385, 'fare+sum': 557.0899982452393}, {'geohash': 'dp3wm5', 'count': 38, 'extras+avg': 1.1710526315789473, 'fare+sum': 404.5900011062622}, {'geohash': 'dp3wtd', 'count': 33, 'extras+avg': 0.5303030303030303, 'fare+sum': 383.78999900817877}, {'geohash': 'dp3wmq', 'count': 31, 'extras+avg': 0.5, 'fare+sum': 302.10000085830694}, {'geohash': 'dp3wgb', 'count': 30, 'extras+avg': 0.5, 'fare+sum': 425.1499981880186}, {'geohash': 'dp3tfb', 'count': 29, 'extras+avg': 1.9137931034482758, 'fare+sum': 889.6900062561035}, {'geohash': 'dp3wj4', 'count': 28, 'extras+avg': 0.2857142857142857, 'fare+sum': 355.3799991607667}, {'geohash': 'dp3whz', 'count': 23, 'extras+avg': 0.8260869565217391, 'fare+sum': 247.85000085830683}, {'geohash': 'dp3wkv', 'count': 22, 'extras+avg': 0.9772727272727273, 'fare+sum': 251.8000025749208}, {'geohash': 'dp3wts', 'count': 22, 'extras+avg': 0.5681818181818182, 'fare+sum': 267.62999963760376}, {'geohash': 'dp3wt4', 'count': 22, 'extras+avg': 0.6590909090909091, 'fare+sum': 289.94999885559076}, {'geohash': 'dp3wmw', 'count': 21, 'extras+avg': 0.6904761904761905, 'fare+sum': 203.49999952316284}, {'geohash': 'dp3wtb', 'count': 20, 'extras+avg': 0.575, 'fare+sum': 252.5000004768371}, {'geohash': 'dp3wb6', 'count': 19, 'extras+avg': 2.236842105263158, 'fare+sum': 320.6000003814697}, {'geohash': 'dp3typ', 'count': 19, 'extras+avg': 0.6842105263157895, 'fare+sum': 261.8500003814699}, {'geohash': 'dp3wt5', 'count': 18, 'extras+avg': 0.6111111111111112, 'fare+sum': 179.89999914169314}, {'geohash': 'dp3wtw', 'count': 18, 'extras+avg': 0.16666666666666666, 'fare+sum': 233.08999872207642}, {'geohash': 'dp3why', 'count': 17, 'extras+avg': 0.4117647058823529, 'fare+sum': 192.2899985313415}, {'geohash': 'dp3wme', 'count': 17, 'extras+avg': 0.4117647058823529, 'fare+sum': 128.15000009536746}, {'geohash': 'dp3wj8', 'count': 17, 'extras+avg': 0.7941176470588235, 'fare+sum': 322.1999998092651}, {'geohash': 'dp3wcg', 'count': 17, 'extras+avg': 0.8529411764705882, 'fare+sum': 277.4400010108947}, {'geohash': 'dp3wmp', 'count': 15, 'extras+avg': 0.9333333333333333, 'fare+sum': 142.7399997711182}, {'geohash': 'dp3wtn', 'count': 15, 'extras+avg': 0.23333333333333334, 'fare+sum': 174.34999942779535}, {'geohash': 'dp3wkz', 'count': 15, 'extras+avg': 0.5, 'fare+sum': 216.15000438690186}, {'geohash': 'dp3wdv', 'count': 15, 'extras+avg': 0.5, 'fare+sum': 298.20000123977655}, {'geohash': 'dp3wjc', 'count': 15, 'extras+avg': 0.5333333333333333, 'fare+sum': 242.0000004768371}, {'geohash': 'dp3wtq', 'count': 14, 'extras+avg': 0.6785714285714286, 'fare+sum': 183.70000171661368}, {'geohash': 'dp3tye', 'count': 13, 'extras+avg': 0.6153846153846154, 'fare+sum': 245.2000007629395}, {'geohash': 'dp3wth', 'count': 12, 'extras+avg': 1.4166666666666667, 'fare+sum': 216.09999752044664}, {'geohash': 'dp3wmt', 'count': 12, 'extras+avg': 0.16666666666666666, 'fare+sum': 85.99999952316283}, {'geohash': 'dp3wm4', 'count': 12, 'extras+avg': 0.4166666666666667, 'fare+sum': 91.35000038146968}, {'geohash': 'dp3wtt', 'count': 12, 'extras+avg': 0.4166666666666667, 'fare+sum': 119.43999767303464}, {'geohash': 'dp3wfd', 'count': 11, 'extras+avg': 0.2727272727272727, 'fare+sum': 166.75000190734872}, {'geohash': 'dp3w7g', 'count': 11, 'extras+avg': 1.0454545454545454, 'fare+sum': 150.6999988555908}, {'geohash': 'dp3wv2', 'count': 9, 'extras+avg': 0.2222222222222222, 'fare+sum': 117.25000000000006}, {'geohash': 'dp3wv0', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 132.80000114440915}, {'geohash': 'dp3wkt', 'count': 9, 'extras+avg': 0.8888888888888888, 'fare+sum': 107.8500003814697}, {'geohash': 'dp3wt0', 'count': 9, 'extras+avg': 0.5555555555555556, 'fare+sum': 110.89999961853025}, {'geohash': 'dp3wsg', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 97.24999952316278}, {'geohash': 'dp3tuk', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 204.09999847412115}, {'geohash': 'dp3wkx', 'count': 8, 'extras+avg': 0.9375, 'fare+sum': 109.99999952316286}, {'geohash': 'dp3wky', 'count': 8, 'extras+avg': 0.5, 'fare+sum': 104.24999904632563}, {'geohash': 'dp3wtp', 'count': 8, 'extras+avg': 0.75, 'fare+sum': 109.54000139236452}, {'geohash': 'dp3ty5', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 126.9500007629395}, {'geohash': 'dp3twz', 'count': 7, 'extras+avg': 1.1428571428571428, 'fare+sum': 128.9999971389769}, {'geohash': 'dp3twx', 'count': 7, 'extras+avg': 0.6428571428571429, 'fare+sum': 142.75000000000009}, {'geohash': 'dp3wsb', 'count': 7, 'extras+avg': 0.7857142857142857, 'fare+sum': 92.34999847412101}, {'geohash': 'dp3wsu', 'count': 7, 'extras+avg': 0.42857142857142855, 'fare+sum': 67.14999961853036}, {'geohash': 'dp3wjf', 'count': 7, 'extras+avg': 0.8571428571428571, 'fare+sum': 99.14000082016}, {'geohash': 'dp3wub', 'count': 7, 'extras+avg': 0.14285714285714285, 'fare+sum': 77.39999914169312}, {'geohash': 'dp3tv7', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 119.2500000000001}, {'geohash': 'dp3twt', 'count': 6, 'extras+avg': 0.6666666666666666, 'fare+sum': 178.2999992370606}, {'geohash': 'dp3w5u', 'count': 6, 'extras+avg': 1.1666666666666667, 'fare+sum': 109.7499990463257}, {'geohash': 'dp3weg', 'count': 6, 'extras+avg': 0.5, 'fare+sum': 70.29999923706049}, {'geohash': 'dp3wgf', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 37.34999942779544}, {'geohash': 'dp3wh0', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 115.70000076293942}, {'geohash': 'dp3wse', 'count': 5, 'extras+avg': 0.6, 'fare+sum': 51.650000572204604}, {'geohash': 'dp3wks', 'count': 5, 'extras+avg': 0.0, 'fare+sum': 58.25}, {'geohash': 'dp3wsw', 'count': 5, 'extras+avg': 0.6, 'fare+sum': 60.24000024795523}, {'geohash': 'dp3wdb', 'count': 5, 'extras+avg': 0.0, 'fare+sum': 70.6499986648559}, {'geohash': 'dp3wtm', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.650000095367446}, {'geohash': 'dp3tx4', 'count': 5, 'extras+avg': 0.5, 'fare+sum': 87.85000085830691}, {'geohash': 'dp3ws8', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w71', 'count': 5, 'extras+avg': 0.95, 'fare+sum': 73.34999895095817}, {'geohash': 'dp3wgh', 'count': 5, 'extras+avg': 1.0, 'fare+sum': 67.13000011444086}, {'geohash': 'dp3wju', 'count': 4, 'extras+avg': 0.875, 'fare+sum': 59.65000009536743}, {'geohash': 'dp3wmh', 'count': 4, 'extras+avg': 1.0, 'fare+sum': 31.20000028610233}, {'geohash': 'dp3we8', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 61.0500001907349}, {'geohash': 'dp3whp', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 37.19999980926511}, {'geohash': 'dp3wkf', 'count': 4, 'extras+avg': 0.5, 'fare+sum': 32.40000009536743}, {'geohash': 'dp3wsf', 'count': 4, 'extras+avg': 1.5, 'fare+sum': 82.24999904632564}, {'geohash': 'dp3wuf', 'count': 4, 'extras+avg': 1.125, 'fare+sum': 50.38999986648564}, {'geohash': 'dp3wke', 'count': 3, 'extras+avg': 0.16666666666666666, 'fare+sum': 40.70000076293943}, {'geohash': 'dp3tuy', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 32.55000019073486}, {'geohash': 'dp3wsx', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 42.3500003814697}, {'geohash': 'dp3wk7', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 31.350000381469762}, {'geohash': 'dp3wsr', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 38.550000190734906}, {'geohash': 'dp3wsz', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 40.950000286102274}, {'geohash': 'dp3ws2', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 35.7500009536743}, {'geohash': 'dp3tu2', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 58.2000007629394}, {'geohash': 'dp3tkc', 'count': 3, 'extras+avg': 2.3333333333333335, 'fare+sum': 69.10000157356262}, {'geohash': 'dp3wcx', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 80.1499996185302}, {'geohash': 'dp3tsk', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3wv4', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 29.10000038146977}, {'geohash': 'dp3wtc', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 14.3000001907349}, {'geohash': 'dp3tmr', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 28.2999992370605}, {'geohash': 'dp3tee', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 58.950000762939496}, {'geohash': 'dp3tdv', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 71.6500015258789}, {'geohash': 'dp3wu2', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wvh', 'count': 2, 'extras+avg': 1.25, 'fare+sum': 20.29999971389773}, {'geohash': 'dp3wuy', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.899999618530302}, {'geohash': 'dp3wvq', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3ty0', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 64.4500007629395}, {'geohash': 'dp3wjq', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 21.29999971389773}, {'geohash': 'dp3ws1', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.30000019073486}, {'geohash': 'dp3tuz', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 21.8999996185303}, {'geohash': 'dp3wkw', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 26.100000381469698}, {'geohash': 'dp3w9u', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 45.1000003814698}, {'geohash': 'dp3tyc', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 67.9000015258789}, {'geohash': 'dp3wu8', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3tgb', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3wj2', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wug', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 21.0499992370605}, {'geohash': 'dp3wjm', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 8.25}, {'geohash': 'dp3wus', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wuu', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.25}, {'geohash': 'dp3wsn', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3wey', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkp', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.8500003814697}, {'geohash': 'dp3wkn', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 15.8500003814697}, {'geohash': 'dp3wkm', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 18.0499992370605}, {'geohash': 'dp3wkc', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.44999980926514}, {'geohash': 'dp3wv6', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.25}, {'geohash': 'dp3wv7', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 26.25}, {'geohash': 'dp3wk8', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3qzw', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 43.6500015258789}, {'geohash': 'dp3wu6', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3thn', 'count': 1, 'extras+avg': 3.0, 'fare+sum': 68.25}, {'geohash': 'dp3tge', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 17.8500003814697}, {'geohash': 'dp3tq0', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.25}, {'geohash': 'dp3ws0', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3ttt', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.25}, {'geohash': 'dp3tw4', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.44999980926514}, {'geohash': 'dp3trh', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 46.0}, {'geohash': 'dp3tqz', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 57.25}, {'geohash': 'dp3tqn', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.4499998092651}, {'geohash': 'dp3tq8', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 32.8499984741211}, {'geohash': 'dp3tkp', 'count': 1, 'extras+avg': 4.0, 'fare+sum': 72.0}, {'geohash': 'dp3wew', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 20.75}, {'geohash': 'dp3wn1', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 0.0}, {'geohash': 'dp3wd0', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.75}, {'geohash': 'dp3tjj', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.8499984741211}, {'geohash': 'dp3wmj', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 9.64999961853027}, {'geohash': 'dp3weu', 'count': 1, 'extras+avg': 9.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3tjf', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.75}, {'geohash': 'dp3wsy', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 6.84999990463257}, {'geohash': 'dp3wk0', 'count': 1, 'extras+avg': 5.0, 'fare+sum': 39.75}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_7_RESULT = {'data': [{'geohash': 'dp3wmb5', 'count': 895, 'extras+avg': 0.43435754189944137, 'fare+sum': 7642.2900059223175}, {'geohash': 'dp3wq0u', 'count': 500, 'extras+avg': 0.806, 'fare+sum': 4521.259998083115}, {'geohash': 'dp3wq42', 'count': 386, 'extras+avg': 0.8018134715025906, 'fare+sum': 4033.2300107479095}, {'geohash': 'dp3wmfh', 'count': 374, 'extras+avg': 0.6778074866310161, 'fare+sum': 3112.0099957082425}, {'geohash': 'dp3wt7d', 'count': 358, 'extras+avg': 0.5519832392644615, 'fare+sum': 4049.5199956893925}, {'geohash': '7zzzzzz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}, {'geohash': 'dp3wjxu', 'count': 312, 'extras+avg': 0.6121794871794872, 'fare+sum': 2575.690001010895}, {'geohash': 'dp3wq4j', 'count': 301, 'extras+avg': 0.707641196013289, 'fare+sum': 3094.2200043890625}, {'geohash': 'dp3wmf2', 'count': 299, 'extras+avg': 0.6337792642140468, 'fare+sum': 2514.6099982261658}, {'geohash': 'dp3wmge', 'count': 282, 'extras+avg': 0.44148936170212766, 'fare+sum': 3214.6300044059753}, {'geohash': 'dp3qzdn', 'count': 277, 'extras+avg': 2.4521660649819497, 'fare+sum': 9363.659996271133}, {'geohash': 'dp3wq58', 'count': 224, 'extras+avg': 0.5714285714285714, 'fare+sum': 2129.800005197525}, {'geohash': 'dp3wkgu', 'count': 218, 'extras+avg': 0.5871559633027523, 'fare+sum': 2422.8500015735626}, {'geohash': 'dp3wnhq', 'count': 212, 'extras+avg': 0.660377358490566, 'fare+sum': 2430.589998722077}, {'geohash': 'dp3wmrz', 'count': 202, 'extras+avg': 0.5841584158415841, 'fare+sum': 2192.4400038719177}, {'geohash': 'dp3wm8u', 'count': 199, 'extras+avg': 0.41708542713567837, 'fare+sum': 1629.880003452301}, {'geohash': 'dp3wq4v', 'count': 198, 'extras+avg': 0.5429292929292929, 'fare+sum': 1788.4300005435944}, {'geohash': 'dp3wnpe', 'count': 176, 'extras+avg': 0.7130681818181818, 'fare+sum': 1527.6799974441528}, {'geohash': 'dp3wjnv', 'count': 170, 'extras+avg': 0.37058823529411766, 'fare+sum': 2066.3799953460693}, {'geohash': 'dp3wnpc', 'count': 153, 'extras+avg': 0.272875816993464, 'fare+sum': 2165.5400013923645}, {'geohash': 'dp3wmfn', 'count': 152, 'extras+avg': 0.84375, 'fare+sum': 1274.1300032138824}, {'geohash': 'dp3wq5k', 'count': 149, 'extras+avg': 0.6879194630872483, 'fare+sum': 1451.9199991226196}, {'geohash': 'dp3wm2c', 'count': 137, 'extras+avg': 0.5218978102189781, 'fare+sum': 1092.809996843338}, {'geohash': 'dp3wtrd', 'count': 118, 'extras+avg': 0.5550847457627118, 'fare+sum': 1521.6299939155574}, {'geohash': 'dp3wv5m', 'count': 111, 'extras+avg': 0.5045045045045045, 'fare+sum': 1464.2499966621401}, {'geohash': 'dp3wmyk', 'count': 110, 'extras+avg': 0.6772727272727272, 'fare+sum': 1076.3400044441225}, {'geohash': 'dp3wkrg', 'count': 108, 'extras+avg': 0.6435185185185185, 'fare+sum': 1392.8299996852877}, {'geohash': 'dp3wnn7', 'count': 107, 'extras+avg': 0.9112149532710281, 'fare+sum': 1241.1899988651276}, {'geohash': 'dp3tenv', 'count': 97, 'extras+avg': 1.922680412371134, 'fare+sum': 2773.190001964569}, {'geohash': 'dp3wq64', 'count': 93, 'extras+avg': 0.7419354838709677, 'fare+sum': 853.4499983787537}, {'geohash': 'dp3wmv1', 'count': 73, 'extras+avg': 0.4863013698630137, 'fare+sum': 644.2300004959106}, {'geohash': 'dp3wjrf', 'count': 72, 'extras+avg': 0.4583333333333333, 'fare+sum': 570.0500001907349}, {'geohash': 'dp3wn46', 'count': 71, 'extras+avg': 0.823943661971831, 'fare+sum': 1019.849999666214}, {'geohash': 'dp3qz6r', 'count': 70, 'extras+avg': 1.7285714285714286, 'fare+sum': 2008.1300034523015}, {'geohash': 'dp3wqj0', 'count': 66, 'extras+avg': 0.4772727272727273, 'fare+sum': 561.7000007629395}, {'geohash': 'dp3wqh0', 'count': 64, 'extras+avg': 0.7109375, 'fare+sum': 574.3400025367737}, {'geohash': 'dp3wssq', 'count': 63, 'extras+avg': 0.3253968253968254, 'fare+sum': 770.3499956130979}, {'geohash': 'dp3wmkx', 'count': 62, 'extras+avg': 0.49193548387096775, 'fare+sum': 655.4200019836427}, {'geohash': 'dp3wu97', 'count': 61, 'extras+avg': 0.5081967213114754, 'fare+sum': 909.520004272461}, {'geohash': 'dp3wmgs', 'count': 59, 'extras+avg': 0.576271186440678, 'fare+sum': 543.9500012397766}, {'geohash': 'dp3wev3', 'count': 58, 'extras+avg': 0.5344827586206896, 'fare+sum': 829.9500012397764}, {'geohash': 'dp3wmut', 'count': 55, 'extras+avg': 0.6454545454545455, 'fare+sum': 492.84000062942505}, {'geohash': 'dp3wm7k', 'count': 55, 'extras+avg': 0.6590909090909091, 'fare+sum': 430.49000048637396}, {'geohash': 'dp3tyb3', 'count': 52, 'extras+avg': 1.0480769230769231, 'fare+sum': 1270.749999523163}, {'geohash': 'dp3wjtu', 'count': 50, 'extras+avg': 0.72, 'fare+sum': 545.8399968147276}, {'geohash': 'dp3wmgw', 'count': 49, 'extras+avg': 0.7040816326530612, 'fare+sum': 367.1999993324279}, {'geohash': 'dp3wmzd', 'count': 49, 'extras+avg': 0.5612244897959183, 'fare+sum': 516.3499989509581}, {'geohash': 'dp3wvp8', 'count': 47, 'extras+avg': 0.3191489361702128, 'fare+sum': 745.7400002479551}, {'geohash': 'dp3wjyk', 'count': 47, 'extras+avg': 0.5212765957446809, 'fare+sum': 341.0399994850159}, {'geohash': 'dp3wkuu', 'count': 47, 'extras+avg': 0.776595744680851, 'fare+sum': 467.9999995231626}, {'geohash': 'dp3ws4d', 'count': 41, 'extras+avg': 0.4268292682926829, 'fare+sum': 508.1399979591372}, {'geohash': 'dp3wuqn', 'count': 39, 'extras+avg': 0.5256410256410257, 'fare+sum': 644.4400033950803}, {'geohash': 'dp3wn5u', 'count': 39, 'extras+avg': 1.0384615384615385, 'fare+sum': 557.0899982452393}, {'geohash': 'dp3wm6m', 'count': 37, 'extras+avg': 0.7567567567567568, 'fare+sum': 372.6999988555908}, {'geohash': 'dp3wtkh', 'count': 35, 'extras+avg': 0.8857142857142857, 'fare+sum': 426.19000148773176}, {'geohash': 'dp3wt2y', 'count': 33, 'extras+avg': 0.8636363636363636, 'fare+sum': 416.8499965667726}, {'geohash': 'dp3wt8c', 'count': 33, 'extras+avg': 0.9393939393939394, 'fare+sum': 414.24999713897694}, {'geohash': 'dp3wmqk', 'count': 31, 'extras+avg': 0.5, 'fare+sum': 302.10000085830694}, {'geohash': 'dp3wgb5', 'count': 30, 'extras+avg': 0.5, 'fare+sum': 425.1499981880186}, {'geohash': 'dp3tfb0', 'count': 29, 'extras+avg': 1.9137931034482758, 'fare+sum': 889.6900062561035}, {'geohash': 'dp3wj4d', 'count': 28, 'extras+avg': 0.2857142857142857, 'fare+sum': 355.3799991607667}, {'geohash': 'dp3wt7m', 'count': 27, 'extras+avg': 0.6666666666666666, 'fare+sum': 272.27999830245966}, {'geohash': 'dp3wmvm', 'count': 23, 'extras+avg': 0.34782608695652173, 'fare+sum': 214.19999909400934}, {'geohash': 'dp3wt9y', 'count': 23, 'extras+avg': 0.6086956521739131, 'fare+sum': 250.60000228881842}, {'geohash': 'dp3wmxt', 'count': 22, 'extras+avg': 0.25, 'fare+sum': 188.48999881744376}, {'geohash': 'dp3wtse', 'count': 22, 'extras+avg': 0.5681818181818182, 'fare+sum': 267.62999963760376}, {'geohash': 'dp3wtdx', 'count': 21, 'extras+avg': 0.5, 'fare+sum': 252.9399991035461}, {'geohash': 'dp3wt6q', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 245.3500015735625}, {'geohash': 'dp3wm5s', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 208.59999990463248}, {'geohash': 'dp3wmx9', 'count': 21, 'extras+avg': 0.8571428571428571, 'fare+sum': 171.84999895095828}, {'geohash': 'dp3wtbc', 'count': 20, 'extras+avg': 0.575, 'fare+sum': 252.5000004768371}, {'geohash': 'dp3whzz', 'count': 20, 'extras+avg': 0.8, 'fare+sum': 222.50000047683713}, {'geohash': 'dp3wt66', 'count': 20, 'extras+avg': 0.875, 'fare+sum': 173.5499982833863}, {'geohash': 'dp3wte3', 'count': 20, 'extras+avg': 1.075, 'fare+sum': 256.6000008583069}, {'geohash': 'dp3wmrw', 'count': 20, 'extras+avg': 0.7, 'fare+sum': 207.5000023841858}, {'geohash': 'dp3wb69', 'count': 19, 'extras+avg': 2.236842105263158, 'fare+sum': 320.6000003814697}, {'geohash': 'dp3typy', 'count': 19, 'extras+avg': 0.6842105263157895, 'fare+sum': 261.8500003814699}, {'geohash': 'dp3wtwf', 'count': 18, 'extras+avg': 0.16666666666666666, 'fare+sum': 233.08999872207642}, {'geohash': 'dp3wj80', 'count': 17, 'extras+avg': 0.7941176470588235, 'fare+sum': 322.1999998092651}, {'geohash': 'dp3whyk', 'count': 17, 'extras+avg': 0.4117647058823529, 'fare+sum': 192.2899985313415}, {'geohash': 'dp3wm58', 'count': 17, 'extras+avg': 1.8529411764705883, 'fare+sum': 195.9900012016297}, {'geohash': 'dp3wcgn', 'count': 17, 'extras+avg': 0.8529411764705882, 'fare+sum': 277.4400010108947}, {'geohash': 'dp3wmw6', 'count': 16, 'extras+avg': 0.90625, 'fare+sum': 156.7999997138977}, {'geohash': 'dp3wtkt', 'count': 16, 'extras+avg': 0.78125, 'fare+sum': 238.1399984359742}, {'geohash': 'dp3wmps', 'count': 15, 'extras+avg': 0.9333333333333333, 'fare+sum': 142.7399997711182}, {'geohash': 'dp3wdvk', 'count': 15, 'extras+avg': 0.5, 'fare+sum': 298.20000123977655}, {'geohash': 'dp3wjc4', 'count': 15, 'extras+avg': 0.5333333333333333, 'fare+sum': 242.0000004768371}, {'geohash': 'dp3wkvp', 'count': 14, 'extras+avg': 0.6428571428571429, 'fare+sum': 150.40000104904186}, {'geohash': 'dp3wtqj', 'count': 14, 'extras+avg': 0.6785714285714286, 'fare+sum': 183.70000171661368}, {'geohash': 'dp3wmrd', 'count': 14, 'extras+avg': 3.892857142857143, 'fare+sum': 132.29000091552737}, {'geohash': 'dp3wtet', 'count': 14, 'extras+avg': 0.42857142857142855, 'fare+sum': 157.30000066757194}, {'geohash': 'dp3wkgt', 'count': 13, 'extras+avg': 0.9615384615384616, 'fare+sum': 145.6999998092651}, {'geohash': 'dp3wt4p', 'count': 13, 'extras+avg': 0.7692307692307693, 'fare+sum': 207.29999971389762}, {'geohash': 'dp3wt9h', 'count': 13, 'extras+avg': 0.11538461538461539, 'fare+sum': 126.45000052452089}, {'geohash': 'dp3tyen', 'count': 13, 'extras+avg': 0.6153846153846154, 'fare+sum': 245.2000007629395}, {'geohash': 'dp3wtt6', 'count': 12, 'extras+avg': 0.4166666666666667, 'fare+sum': 119.43999767303464}, {'geohash': 'dp3wmtj', 'count': 12, 'extras+avg': 0.16666666666666666, 'fare+sum': 85.99999952316283}, {'geohash': 'dp3wtd9', 'count': 12, 'extras+avg': 0.5833333333333334, 'fare+sum': 130.84999990463263}, {'geohash': 'dp3wtkd', 'count': 12, 'extras+avg': 0.3333333333333333, 'fare+sum': 144.84999942779535}, {'geohash': 'dp3wt9c', 'count': 12, 'extras+avg': 0.5416666666666666, 'fare+sum': 126.49999904632557}, {'geohash': 'dp3wfdn', 'count': 11, 'extras+avg': 0.2727272727272727, 'fare+sum': 166.75000190734872}, {'geohash': 'dp3wkzp', 'count': 11, 'extras+avg': 0.6818181818181818, 'fare+sum': 174.95000457763675}, {'geohash': 'dp3w7ge', 'count': 11, 'extras+avg': 1.0454545454545454, 'fare+sum': 150.6999988555908}, {'geohash': 'dp3wtnp', 'count': 10, 'extras+avg': 0.25, 'fare+sum': 115.89999914169309}, {'geohash': 'dp3wt2f', 'count': 10, 'extras+avg': 0.95, 'fare+sum': 101.59999990463251}, {'geohash': 'dp3wt45', 'count': 9, 'extras+avg': 0.5, 'fare+sum': 82.64999914169313}, {'geohash': 'dp3tuke', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 204.09999847412115}, {'geohash': 'dp3wtee', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 102.03999948501597}, {'geohash': 'dp3wv0v', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 132.80000114440915}, {'geohash': 'dp3wt76', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 93.04000043869009}, {'geohash': 'dp3wmem', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 64.95000076293945}, {'geohash': 'dp3wthg', 'count': 8, 'extras+avg': 1.3125, 'fare+sum': 142.09999752044666}, {'geohash': 'dp3wt9u', 'count': 8, 'extras+avg': 0.8125, 'fare+sum': 119.2000017166138}, {'geohash': 'dp3wkty', 'count': 8, 'extras+avg': 0.75, 'fare+sum': 101.80000019073483}, {'geohash': 'dp3wmez', 'count': 8, 'extras+avg': 0.125, 'fare+sum': 63.199999332428}, {'geohash': 'dp3wkvu', 'count': 8, 'extras+avg': 1.5625, 'fare+sum': 101.40000152587892}, {'geohash': 'dp3wm4k', 'count': 8, 'extras+avg': 0.0, 'fare+sum': 53.95000028610228}, {'geohash': 'dp3wkys', 'count': 8, 'extras+avg': 0.5, 'fare+sum': 104.24999904632563}, {'geohash': 'dp3wtpt', 'count': 7, 'extras+avg': 0.7142857142857143, 'fare+sum': 105.49000120162967}, {'geohash': 'dp3wsbv', 'count': 7, 'extras+avg': 0.7857142857142857, 'fare+sum': 92.34999847412101}, {'geohash': 'dp3wt8s', 'count': 7, 'extras+avg': 0.35714285714285715, 'fare+sum': 54.75000047683715}, {'geohash': 'dp3wjfd', 'count': 7, 'extras+avg': 0.8571428571428571, 'fare+sum': 99.14000082016}, {'geohash': 'dp3wsgp', 'count': 7, 'extras+avg': 0.42857142857142855, 'fare+sum': 55.55000066757199}, {'geohash': 'dp3ty5y', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 126.9500007629395}, {'geohash': 'dp3wt5c', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 82.74999999999991}, {'geohash': 'dp3twzx', 'count': 7, 'extras+avg': 1.1428571428571428, 'fare+sum': 128.9999971389769}, {'geohash': 'dp3wt0g', 'count': 7, 'extras+avg': 0.2857142857142857, 'fare+sum': 74.79999923706055}, {'geohash': 'dp3wv2z', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 74.10000038146975}, {'geohash': 'dp3twtx', 'count': 6, 'extras+avg': 0.6666666666666666, 'fare+sum': 178.2999992370606}, {'geohash': 'dp3w5uq', 'count': 6, 'extras+avg': 1.1666666666666667, 'fare+sum': 109.7499990463257}, {'geohash': 'dp3tv70', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 119.2500000000001}, {'geohash': 'dp3wkxt', 'count': 6, 'extras+avg': 1.0833333333333333, 'fare+sum': 83.89999914169313}, {'geohash': 'dp3wegq', 'count': 6, 'extras+avg': 0.5, 'fare+sum': 70.29999923706049}, {'geohash': 'dp3wgfc', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 37.34999942779544}, {'geohash': 'dp3wh08', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 115.70000076293942}, {'geohash': 'dp3wm62', 'count': 6, 'extras+avg': 0.8333333333333334, 'fare+sum': 50.5}, {'geohash': 'dp3wubf', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 62.74999952316281}, {'geohash': 'dp3wtn5', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 58.45000028610226}, {'geohash': 'dp3wt5y', 'count': 5, 'extras+avg': 0.8, 'fare+sum': 53.64999961853038}, {'geohash': 'dp3wtmk', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.650000095367446}, {'geohash': 'dp3twxd', 'count': 5, 'extras+avg': 0.7, 'fare+sum': 105.2500000000001}, {'geohash': 'dp3wghb', 'count': 5, 'extras+avg': 1.0, 'fare+sum': 67.13000011444086}, {'geohash': 'dp3tx4r', 'count': 5, 'extras+avg': 0.5, 'fare+sum': 87.85000085830691}, {'geohash': 'dp3ws8v', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w71c', 'count': 5, 'extras+avg': 0.95, 'fare+sum': 73.34999895095817}, {'geohash': 'dp3wdbe', 'count': 5, 'extras+avg': 0.0, 'fare+sum': 70.6499986648559}, {'geohash': 'dp3wkg9', 'count': 5, 'extras+avg': 0.4, 'fare+sum': 48.35000038146973}, {'geohash': 'dp3wtrj', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 64.5500001907349}, {'geohash': 'dp3wufp', 'count': 4, 'extras+avg': 1.125, 'fare+sum': 50.38999986648564}, {'geohash': 'dp3wsuu', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.59999990463259}, {'geohash': 'dp3wswn', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 56.99000024795523}, {'geohash': 'dp3wthw', 'count': 4, 'extras+avg': 1.625, 'fare+sum': 73.99999999999997}, {'geohash': 'dp3wt55', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.39999961853028}, {'geohash': 'dp3wmhu', 'count': 4, 'extras+avg': 1.0, 'fare+sum': 31.20000028610233}, {'geohash': 'dp3whpy', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 37.19999980926511}, {'geohash': 'dp3wjut', 'count': 4, 'extras+avg': 0.875, 'fare+sum': 59.65000009536743}, {'geohash': 'dp3wkf3', 'count': 4, 'extras+avg': 0.5, 'fare+sum': 32.40000009536743}, {'geohash': 'dp3wm42', 'count': 4, 'extras+avg': 1.25, 'fare+sum': 37.40000009536741}, {'geohash': 'dp3wkz3', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 41.1999998092651}, {'geohash': 'dp3we81', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 61.0500001907349}, {'geohash': 'dp3wsfp', 'count': 3, 'extras+avg': 1.3333333333333333, 'fare+sum': 53.19999980926514}, {'geohash': 'dp3whz8', 'count': 3, 'extras+avg': 1.0, 'fare+sum': 25.350000381469698}, {'geohash': 'dp3wmwt', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 25.75}, {'geohash': 'dp3wsze', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 40.950000286102274}, {'geohash': 'dp3wsxy', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 42.3500003814697}, {'geohash': 'dp3wcxr', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 80.1499996185302}, {'geohash': 'dp3wsuz', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 34.54999971389777}, {'geohash': 'dp3wsrz', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 38.550000190734906}, {'geohash': 'dp3tuyy', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 32.55000019073486}, {'geohash': 'dp3wk7z', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 31.350000381469762}, {'geohash': 'dp3tu2t', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 58.2000007629394}, {'geohash': 'dp3tkcs', 'count': 3, 'extras+avg': 2.3333333333333335, 'fare+sum': 69.10000157356262}, {'geohash': 'dp3wksv', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 38.75}, {'geohash': 'dp3wkub', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 48.80000066757207}, {'geohash': 'dp3wv2c', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 43.1499996185303}, {'geohash': 'dp3ws2f', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 35.7500009536743}, {'geohash': 'dp3tmr6', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 28.2999992370605}, {'geohash': 'dp3wtcf', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 14.3000001907349}, {'geohash': 'dp3wvhu', 'count': 2, 'extras+avg': 1.25, 'fare+sum': 20.29999971389773}, {'geohash': 'dp3wjqs', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 21.29999971389773}, {'geohash': 'dp3wv5s', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 23.90000057220464}, {'geohash': 'dp3tdv8', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 71.6500015258789}, {'geohash': 'dp3wv4h', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 29.10000038146977}, {'geohash': 'dp3teez', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 58.950000762939496}, {'geohash': 'dp3wuyn', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.899999618530302}, {'geohash': 'dp3tskm', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w9uj', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 45.1000003814698}, {'geohash': 'dp3tyc5', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 67.9000015258789}, {'geohash': 'dp3ty0n', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 64.4500007629395}, {'geohash': 'dp3twxx', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 37.5}, {'geohash': 'dp3tuz8', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 21.8999996185303}, {'geohash': 'dp3wuqp', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 6.5}, {'geohash': 'dp3wu2z', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wt5n', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 11.09999990463257}, {'geohash': 'dp3wvq8', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wkxd', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 26.10000038146973}, {'geohash': 'dp3wt0z', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 36.1000003814697}, {'geohash': 'dp3wssy', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 43.700000762939396}, {'geohash': 'dp3wksf', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 19.5}, {'geohash': 'dp3ws14', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.30000019073486}, {'geohash': 'dp3wkw8', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 26.100000381469698}, {'geohash': 'dp3wkrd', 'count': 2, 'extras+avg': 1.75, 'fare+sum': 28.0999994277954}, {'geohash': 'dp3wsec', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 24.300000190734842}, {'geohash': 'dp3wmwj', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 20.94999980926514}, {'geohash': 'dp3wkew', 'count': 2, 'extras+avg': 0.25, 'fare+sum': 20.85000038146973}, {'geohash': 'dp3wsej', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 20.100000381469762}, {'geohash': 'dp3wu6p', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wu8u', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3tger', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 17.8500003814697}, {'geohash': 'dp3tjj3', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.8499984741211}, {'geohash': 'dp3tjf3', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.75}, {'geohash': 'dp3wubz', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 14.6499996185303}, {'geohash': 'dp3thn3', 'count': 1, 'extras+avg': 3.0, 'fare+sum': 68.25}, {'geohash': 'dp3wugr', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 21.0499992370605}, {'geohash': 'dp3tkps', 'count': 1, 'extras+avg': 4.0, 'fare+sum': 72.0}, {'geohash': 'dp3wk8y', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3wuuy', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.25}, {'geohash': 'dp3wusu', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3tq06', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.25}, {'geohash': 'dp3wktf', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3tgb1', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3ws0z', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3wmjb', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 9.64999961853027}, {'geohash': 'dp3wv6m', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.25}, {'geohash': 'dp3wv7h', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 26.25}, {'geohash': 'dp3wvp4', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 11.8500003814697}, {'geohash': 'dp3qzwz', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 43.6500015258789}, {'geohash': 'dp3wsev', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.25}, {'geohash': 'dp3tqnx', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.4499998092651}, {'geohash': 'dp3tq8k', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 32.8499984741211}, {'geohash': 'dp3wkcp', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.44999980926514}, {'geohash': 'dp3wk0b', 'count': 1, 'extras+avg': 5.0, 'fare+sum': 39.75}, {'geohash': 'dp3wked', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.8500003814697}, {'geohash': 'dp3wjny', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 9.25}, {'geohash': 'dp3wjnh', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.8500003814697}, {'geohash': 'dp3wjmh', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 8.25}, {'geohash': 'dp3wj2h', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkmn', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 18.0499992370605}, {'geohash': 'dp3wey4', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wewh', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 20.75}, {'geohash': 'dp3weuf', 'count': 1, 'extras+avg': 9.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3wsyh', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 6.84999990463257}, {'geohash': 'dp3wknx', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 15.8500003814697}, {'geohash': 'dp3wd0g', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.75}, {'geohash': 'dp3wsw0', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkpx', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.8500003814697}, {'geohash': 'dp3wsn3', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3tw4z', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.44999980926514}, {'geohash': 'dp3wsgu', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 28.0499992370605}, {'geohash': 'dp3wkrq', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3wsgh', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 13.6499996185303}, {'geohash': 'dp3tttk', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.25}, {'geohash': 'dp3wsfh', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 29.0499992370605}, {'geohash': 'dp3trhx', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 46.0}, {'geohash': 'dp3wtp0', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3tqzm', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 57.25}, {'geohash': 'dp3wn15', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 0.0}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_8_RESULT = {'data': [{'geohash': 'dp3wmb5y', 'count': 895, 'extras+avg': 0.43435754189944137, 'fare+sum': 7642.2900059223175}, {'geohash': 'dp3wq0um', 'count': 500, 'extras+avg': 0.806, 'fare+sum': 4521.259998083115}, {'geohash': 'dp3wq429', 'count': 386, 'extras+avg': 0.8018134715025906, 'fare+sum': 4033.2300107479095}, {'geohash': 'dp3wmfhq', 'count': 374, 'extras+avg': 0.6778074866310161, 'fare+sum': 3112.0099957082425}, {'geohash': 'dp3wt7dy', 'count': 358, 'extras+avg': 0.5519832392644615, 'fare+sum': 4049.5199956893925}, {'geohash': '7zzzzzzz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}, {'geohash': 'dp3wjxus', 'count': 312, 'extras+avg': 0.6121794871794872, 'fare+sum': 2575.690001010895}, {'geohash': 'dp3wq4jb', 'count': 301, 'extras+avg': 0.707641196013289, 'fare+sum': 3094.2200043890625}, {'geohash': 'dp3wmf2j', 'count': 299, 'extras+avg': 0.6337792642140468, 'fare+sum': 2514.6099982261658}, {'geohash': 'dp3wmge6', 'count': 282, 'extras+avg': 0.44148936170212766, 'fare+sum': 3214.6300044059753}, {'geohash': 'dp3qzdnc', 'count': 277, 'extras+avg': 2.4521660649819497, 'fare+sum': 9363.659996271133}, {'geohash': 'dp3wq588', 'count': 224, 'extras+avg': 0.5714285714285714, 'fare+sum': 2129.800005197525}, {'geohash': 'dp3wkguh', 'count': 218, 'extras+avg': 0.5871559633027523, 'fare+sum': 2422.8500015735626}, {'geohash': 'dp3wnhqb', 'count': 212, 'extras+avg': 0.660377358490566, 'fare+sum': 2430.589998722077}, {'geohash': 'dp3wmrz9', 'count': 202, 'extras+avg': 0.5841584158415841, 'fare+sum': 2192.4400038719177}, {'geohash': 'dp3wm8ur', 'count': 199, 'extras+avg': 0.41708542713567837, 'fare+sum': 1629.880003452301}, {'geohash': 'dp3wq4v2', 'count': 198, 'extras+avg': 0.5429292929292929, 'fare+sum': 1788.4300005435944}, {'geohash': 'dp3wnpe9', 'count': 176, 'extras+avg': 0.7130681818181818, 'fare+sum': 1527.6799974441528}, {'geohash': 'dp3wjnvm', 'count': 170, 'extras+avg': 0.37058823529411766, 'fare+sum': 2066.3799953460693}, {'geohash': 'dp3wnpc6', 'count': 153, 'extras+avg': 0.272875816993464, 'fare+sum': 2165.5400013923645}, {'geohash': 'dp3wmfnx', 'count': 152, 'extras+avg': 0.84375, 'fare+sum': 1274.1300032138824}, {'geohash': 'dp3wq5ke', 'count': 149, 'extras+avg': 0.6879194630872483, 'fare+sum': 1451.9199991226196}, {'geohash': 'dp3wm2cz', 'count': 137, 'extras+avg': 0.5218978102189781, 'fare+sum': 1092.809996843338}, {'geohash': 'dp3wtrdu', 'count': 118, 'extras+avg': 0.5550847457627118, 'fare+sum': 1521.6299939155574}, {'geohash': 'dp3wv5mq', 'count': 111, 'extras+avg': 0.5045045045045045, 'fare+sum': 1464.2499966621401}, {'geohash': 'dp3wmykd', 'count': 110, 'extras+avg': 0.6772727272727272, 'fare+sum': 1076.3400044441225}, {'geohash': 'dp3wkrg3', 'count': 108, 'extras+avg': 0.6435185185185185, 'fare+sum': 1392.8299996852877}, {'geohash': 'dp3wnn73', 'count': 107, 'extras+avg': 0.9112149532710281, 'fare+sum': 1241.1899988651276}, {'geohash': 'dp3tenvt', 'count': 97, 'extras+avg': 1.922680412371134, 'fare+sum': 2773.190001964569}, {'geohash': 'dp3wq64n', 'count': 93, 'extras+avg': 0.7419354838709677, 'fare+sum': 853.4499983787537}, {'geohash': 'dp3wmv18', 'count': 73, 'extras+avg': 0.4863013698630137, 'fare+sum': 644.2300004959106}, {'geohash': 'dp3wjrf5', 'count': 72, 'extras+avg': 0.4583333333333333, 'fare+sum': 570.0500001907349}, {'geohash': 'dp3wn46j', 'count': 71, 'extras+avg': 0.823943661971831, 'fare+sum': 1019.849999666214}, {'geohash': 'dp3qz6r2', 'count': 70, 'extras+avg': 1.7285714285714286, 'fare+sum': 2008.1300034523015}, {'geohash': 'dp3wqj00', 'count': 66, 'extras+avg': 0.4772727272727273, 'fare+sum': 561.7000007629395}, {'geohash': 'dp3wqh0t', 'count': 64, 'extras+avg': 0.7109375, 'fare+sum': 574.3400025367737}, {'geohash': 'dp3wssqe', 'count': 63, 'extras+avg': 0.3253968253968254, 'fare+sum': 770.3499956130979}, {'geohash': 'dp3wmkx3', 'count': 62, 'extras+avg': 0.49193548387096775, 'fare+sum': 655.4200019836427}, {'geohash': 'dp3wu97g', 'count': 61, 'extras+avg': 0.5081967213114754, 'fare+sum': 909.520004272461}, {'geohash': 'dp3wmgsn', 'count': 59, 'extras+avg': 0.576271186440678, 'fare+sum': 543.9500012397766}, {'geohash': 'dp3wev3t', 'count': 58, 'extras+avg': 0.5344827586206896, 'fare+sum': 829.9500012397764}, {'geohash': 'dp3wmutp', 'count': 55, 'extras+avg': 0.6454545454545455, 'fare+sum': 492.84000062942505}, {'geohash': 'dp3wm7ke', 'count': 55, 'extras+avg': 0.6590909090909091, 'fare+sum': 430.49000048637396}, {'geohash': 'dp3tyb3h', 'count': 52, 'extras+avg': 1.0480769230769231, 'fare+sum': 1270.749999523163}, {'geohash': 'dp3wjtu6', 'count': 50, 'extras+avg': 0.72, 'fare+sum': 545.8399968147276}, {'geohash': 'dp3wmgwq', 'count': 49, 'extras+avg': 0.7040816326530612, 'fare+sum': 367.1999993324279}, {'geohash': 'dp3wmzdv', 'count': 49, 'extras+avg': 0.5612244897959183, 'fare+sum': 516.3499989509581}, {'geohash': 'dp3wvp8e', 'count': 47, 'extras+avg': 0.3191489361702128, 'fare+sum': 745.7400002479551}, {'geohash': 'dp3wjyku', 'count': 47, 'extras+avg': 0.5212765957446809, 'fare+sum': 341.0399994850159}, {'geohash': 'dp3wkuub', 'count': 47, 'extras+avg': 0.776595744680851, 'fare+sum': 467.9999995231626}, {'geohash': 'dp3ws4dw', 'count': 41, 'extras+avg': 0.4268292682926829, 'fare+sum': 508.1399979591372}, {'geohash': 'dp3wuqnk', 'count': 39, 'extras+avg': 0.5256410256410257, 'fare+sum': 644.4400033950803}, {'geohash': 'dp3wn5ug', 'count': 39, 'extras+avg': 1.0384615384615385, 'fare+sum': 557.0899982452393}, {'geohash': 'dp3wm6m6', 'count': 37, 'extras+avg': 0.7567567567567568, 'fare+sum': 372.6999988555908}, {'geohash': 'dp3wtkh4', 'count': 35, 'extras+avg': 0.8857142857142857, 'fare+sum': 426.19000148773176}, {'geohash': 'dp3wt2yq', 'count': 33, 'extras+avg': 0.8636363636363636, 'fare+sum': 416.8499965667726}, {'geohash': 'dp3wt8cy', 'count': 33, 'extras+avg': 0.9393939393939394, 'fare+sum': 414.24999713897694}, {'geohash': 'dp3wmqk7', 'count': 31, 'extras+avg': 0.5, 'fare+sum': 302.10000085830694}, {'geohash': 'dp3wgb51', 'count': 30, 'extras+avg': 0.5, 'fare+sum': 425.1499981880186}, {'geohash': 'dp3tfb05', 'count': 29, 'extras+avg': 1.9137931034482758, 'fare+sum': 889.6900062561035}, {'geohash': 'dp3wj4d7', 'count': 28, 'extras+avg': 0.2857142857142857, 'fare+sum': 355.3799991607667}, {'geohash': 'dp3wt7mv', 'count': 27, 'extras+avg': 0.6666666666666666, 'fare+sum': 272.27999830245966}, {'geohash': 'dp3wmvmh', 'count': 23, 'extras+avg': 0.34782608695652173, 'fare+sum': 214.19999909400934}, {'geohash': 'dp3wt9yx', 'count': 23, 'extras+avg': 0.6086956521739131, 'fare+sum': 250.60000228881842}, {'geohash': 'dp3wmxtk', 'count': 22, 'extras+avg': 0.25, 'fare+sum': 188.48999881744376}, {'geohash': 'dp3wtsex', 'count': 22, 'extras+avg': 0.5681818181818182, 'fare+sum': 267.62999963760376}, {'geohash': 'dp3wtdxs', 'count': 21, 'extras+avg': 0.5, 'fare+sum': 252.9399991035461}, {'geohash': 'dp3wt6q0', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 245.3500015735625}, {'geohash': 'dp3wm5s7', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 208.59999990463248}, {'geohash': 'dp3wmx9u', 'count': 21, 'extras+avg': 0.8571428571428571, 'fare+sum': 171.84999895095828}, {'geohash': 'dp3wtbcr', 'count': 20, 'extras+avg': 0.575, 'fare+sum': 252.5000004768371}, {'geohash': 'dp3whzz2', 'count': 20, 'extras+avg': 0.8, 'fare+sum': 222.50000047683713}, {'geohash': 'dp3wt668', 'count': 20, 'extras+avg': 0.875, 'fare+sum': 173.5499982833863}, {'geohash': 'dp3wte3m', 'count': 20, 'extras+avg': 1.075, 'fare+sum': 256.6000008583069}, {'geohash': 'dp3wmrwk', 'count': 20, 'extras+avg': 0.7, 'fare+sum': 207.5000023841858}, {'geohash': 'dp3wb69x', 'count': 19, 'extras+avg': 2.236842105263158, 'fare+sum': 320.6000003814697}, {'geohash': 'dp3typy5', 'count': 19, 'extras+avg': 0.6842105263157895, 'fare+sum': 261.8500003814699}, {'geohash': 'dp3wtwfx', 'count': 18, 'extras+avg': 0.16666666666666666, 'fare+sum': 233.08999872207642}, {'geohash': 'dp3wj801', 'count': 17, 'extras+avg': 0.7941176470588235, 'fare+sum': 322.1999998092651}, {'geohash': 'dp3whykb', 'count': 17, 'extras+avg': 0.4117647058823529, 'fare+sum': 192.2899985313415}, {'geohash': 'dp3wm58g', 'count': 17, 'extras+avg': 1.8529411764705883, 'fare+sum': 195.9900012016297}, {'geohash': 'dp3wcgns', 'count': 17, 'extras+avg': 0.8529411764705882, 'fare+sum': 277.4400010108947}, {'geohash': 'dp3wmw64', 'count': 16, 'extras+avg': 0.90625, 'fare+sum': 156.7999997138977}, {'geohash': 'dp3wtktg', 'count': 16, 'extras+avg': 0.78125, 'fare+sum': 238.1399984359742}, {'geohash': 'dp3wmpsu', 'count': 15, 'extras+avg': 0.9333333333333333, 'fare+sum': 142.7399997711182}, {'geohash': 'dp3wdvkx', 'count': 15, 'extras+avg': 0.5, 'fare+sum': 298.20000123977655}, {'geohash': 'dp3wjc4g', 'count': 15, 'extras+avg': 0.5333333333333333, 'fare+sum': 242.0000004768371}, {'geohash': 'dp3wkvpy', 'count': 14, 'extras+avg': 0.6428571428571429, 'fare+sum': 150.40000104904186}, {'geohash': 'dp3wtqjp', 'count': 14, 'extras+avg': 0.6785714285714286, 'fare+sum': 183.70000171661368}, {'geohash': 'dp3wmrdg', 'count': 14, 'extras+avg': 3.892857142857143, 'fare+sum': 132.29000091552737}, {'geohash': 'dp3wtetb', 'count': 14, 'extras+avg': 0.42857142857142855, 'fare+sum': 157.30000066757194}, {'geohash': 'dp3wkgt4', 'count': 13, 'extras+avg': 0.9615384615384616, 'fare+sum': 145.6999998092651}, {'geohash': 'dp3wt4pp', 'count': 13, 'extras+avg': 0.7692307692307693, 'fare+sum': 207.29999971389762}, {'geohash': 'dp3wt9hz', 'count': 13, 'extras+avg': 0.11538461538461539, 'fare+sum': 126.45000052452089}, {'geohash': 'dp3tyen6', 'count': 13, 'extras+avg': 0.6153846153846154, 'fare+sum': 245.2000007629395}, {'geohash': 'dp3wtt6h', 'count': 12, 'extras+avg': 0.4166666666666667, 'fare+sum': 119.43999767303464}, {'geohash': 'dp3wmtjb', 'count': 12, 'extras+avg': 0.16666666666666666, 'fare+sum': 85.99999952316283}, {'geohash': 'dp3wtd9e', 'count': 12, 'extras+avg': 0.5833333333333334, 'fare+sum': 130.84999990463263}, {'geohash': 'dp3wtkd7', 'count': 12, 'extras+avg': 0.3333333333333333, 'fare+sum': 144.84999942779535}, {'geohash': 'dp3wt9cx', 'count': 12, 'extras+avg': 0.5416666666666666, 'fare+sum': 126.49999904632557}, {'geohash': 'dp3wfdnb', 'count': 11, 'extras+avg': 0.2727272727272727, 'fare+sum': 166.75000190734872}, {'geohash': 'dp3wkzpt', 'count': 11, 'extras+avg': 0.6818181818181818, 'fare+sum': 174.95000457763675}, {'geohash': 'dp3w7get', 'count': 11, 'extras+avg': 1.0454545454545454, 'fare+sum': 150.6999988555908}, {'geohash': 'dp3wtnpx', 'count': 10, 'extras+avg': 0.25, 'fare+sum': 115.89999914169309}, {'geohash': 'dp3wt2ft', 'count': 10, 'extras+avg': 0.95, 'fare+sum': 101.59999990463251}, {'geohash': 'dp3wt45r', 'count': 9, 'extras+avg': 0.5, 'fare+sum': 82.64999914169313}, {'geohash': 'dp3tukee', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 204.09999847412115}, {'geohash': 'dp3wteec', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 102.03999948501597}, {'geohash': 'dp3wv0vh', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 132.80000114440915}, {'geohash': 'dp3wt76m', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 93.04000043869009}, {'geohash': 'dp3wmem3', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 64.95000076293945}, {'geohash': 'dp3wthgh', 'count': 8, 'extras+avg': 1.3125, 'fare+sum': 142.09999752044666}, {'geohash': 'dp3wt9uq', 'count': 8, 'extras+avg': 0.8125, 'fare+sum': 119.2000017166138}, {'geohash': 'dp3wktyd', 'count': 8, 'extras+avg': 0.75, 'fare+sum': 101.80000019073483}, {'geohash': 'dp3wmezw', 'count': 8, 'extras+avg': 0.125, 'fare+sum': 63.199999332428}, {'geohash': 'dp3wkvuv', 'count': 8, 'extras+avg': 1.5625, 'fare+sum': 101.40000152587892}, {'geohash': 'dp3wm4k3', 'count': 8, 'extras+avg': 0.0, 'fare+sum': 53.95000028610228}, {'geohash': 'dp3wkysf', 'count': 8, 'extras+avg': 0.5, 'fare+sum': 104.24999904632563}, {'geohash': 'dp3wtptd', 'count': 7, 'extras+avg': 0.7142857142857143, 'fare+sum': 105.49000120162967}, {'geohash': 'dp3wsbvz', 'count': 7, 'extras+avg': 0.7857142857142857, 'fare+sum': 92.34999847412101}, {'geohash': 'dp3wt8s9', 'count': 7, 'extras+avg': 0.35714285714285715, 'fare+sum': 54.75000047683715}, {'geohash': 'dp3wjfdp', 'count': 7, 'extras+avg': 0.8571428571428571, 'fare+sum': 99.14000082016}, {'geohash': 'dp3wsgpy', 'count': 7, 'extras+avg': 0.42857142857142855, 'fare+sum': 55.55000066757199}, {'geohash': 'dp3ty5yd', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 126.9500007629395}, {'geohash': 'dp3wt5cs', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 82.74999999999991}, {'geohash': 'dp3twzxz', 'count': 7, 'extras+avg': 1.1428571428571428, 'fare+sum': 128.9999971389769}, {'geohash': 'dp3wt0gu', 'count': 7, 'extras+avg': 0.2857142857142857, 'fare+sum': 74.79999923706055}, {'geohash': 'dp3wv2zn', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 74.10000038146975}, {'geohash': 'dp3twtx7', 'count': 6, 'extras+avg': 0.6666666666666666, 'fare+sum': 178.2999992370606}, {'geohash': 'dp3w5uqm', 'count': 6, 'extras+avg': 1.1666666666666667, 'fare+sum': 109.7499990463257}, {'geohash': 'dp3tv70e', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 119.2500000000001}, {'geohash': 'dp3wkxt9', 'count': 6, 'extras+avg': 1.0833333333333333, 'fare+sum': 83.89999914169313}, {'geohash': 'dp3wegqn', 'count': 6, 'extras+avg': 0.5, 'fare+sum': 70.29999923706049}, {'geohash': 'dp3wgfcs', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 37.34999942779544}, {'geohash': 'dp3wh08d', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 115.70000076293942}, {'geohash': 'dp3wm621', 'count': 6, 'extras+avg': 0.8333333333333334, 'fare+sum': 50.5}, {'geohash': 'dp3wubf5', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 62.74999952316281}, {'geohash': 'dp3wtn5h', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 58.45000028610226}, {'geohash': 'dp3wt5yu', 'count': 5, 'extras+avg': 0.8, 'fare+sum': 53.64999961853038}, {'geohash': 'dp3wtmkb', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.650000095367446}, {'geohash': 'dp3twxdx', 'count': 5, 'extras+avg': 0.7, 'fare+sum': 105.2500000000001}, {'geohash': 'dp3wghb2', 'count': 5, 'extras+avg': 1.0, 'fare+sum': 67.13000011444086}, {'geohash': 'dp3tx4rq', 'count': 5, 'extras+avg': 0.5, 'fare+sum': 87.85000085830691}, {'geohash': 'dp3ws8v7', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w71cy', 'count': 5, 'extras+avg': 0.95, 'fare+sum': 73.34999895095817}, {'geohash': 'dp3wdbe5', 'count': 5, 'extras+avg': 0.0, 'fare+sum': 70.6499986648559}, {'geohash': 'dp3wkg9d', 'count': 5, 'extras+avg': 0.4, 'fare+sum': 48.35000038146973}, {'geohash': 'dp3wtrjr', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 64.5500001907349}, {'geohash': 'dp3wufpw', 'count': 4, 'extras+avg': 1.125, 'fare+sum': 50.38999986648564}, {'geohash': 'dp3wsuu5', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.59999990463259}, {'geohash': 'dp3wswnt', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 56.99000024795523}, {'geohash': 'dp3wthwd', 'count': 4, 'extras+avg': 1.625, 'fare+sum': 73.99999999999997}, {'geohash': 'dp3wt55r', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.39999961853028}, {'geohash': 'dp3wmhu5', 'count': 4, 'extras+avg': 1.0, 'fare+sum': 31.20000028610233}, {'geohash': 'dp3whpyd', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 37.19999980926511}, {'geohash': 'dp3wjut7', 'count': 4, 'extras+avg': 0.875, 'fare+sum': 59.65000009536743}, {'geohash': 'dp3wkf3b', 'count': 4, 'extras+avg': 0.5, 'fare+sum': 32.40000009536743}, {'geohash': 'dp3wm42c', 'count': 4, 'extras+avg': 1.25, 'fare+sum': 37.40000009536741}, {'geohash': 'dp3wkz3k', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 41.1999998092651}, {'geohash': 'dp3we81e', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 61.0500001907349}, {'geohash': 'dp3wsfpy', 'count': 3, 'extras+avg': 1.3333333333333333, 'fare+sum': 53.19999980926514}, {'geohash': 'dp3whz8c', 'count': 3, 'extras+avg': 1.0, 'fare+sum': 25.350000381469698}, {'geohash': 'dp3wmwtt', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 25.75}, {'geohash': 'dp3wszeb', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 40.950000286102274}, {'geohash': 'dp3wsxy6', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 42.3500003814697}, {'geohash': 'dp3wcxrb', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 80.1499996185302}, {'geohash': 'dp3wsuze', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 34.54999971389777}, {'geohash': 'dp3wsrz4', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 38.550000190734906}, {'geohash': 'dp3tuyyu', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 32.55000019073486}, {'geohash': 'dp3wk7z0', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 31.350000381469762}, {'geohash': 'dp3tu2tk', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 58.2000007629394}, {'geohash': 'dp3tkcsu', 'count': 3, 'extras+avg': 2.3333333333333335, 'fare+sum': 69.10000157356262}, {'geohash': 'dp3wksvu', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 38.75}, {'geohash': 'dp3wkubs', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 48.80000066757207}, {'geohash': 'dp3wv2cu', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 43.1499996185303}, {'geohash': 'dp3ws2ff', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 35.7500009536743}, {'geohash': 'dp3tmr69', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 28.2999992370605}, {'geohash': 'dp3wtcfr', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 14.3000001907349}, {'geohash': 'dp3wvhu5', 'count': 2, 'extras+avg': 1.25, 'fare+sum': 20.29999971389773}, {'geohash': 'dp3wjqs0', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 21.29999971389773}, {'geohash': 'dp3wv5s3', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 23.90000057220464}, {'geohash': 'dp3tdv8z', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 71.6500015258789}, {'geohash': 'dp3wv4hy', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 29.10000038146977}, {'geohash': 'dp3teezn', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 58.950000762939496}, {'geohash': 'dp3wuynj', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.899999618530302}, {'geohash': 'dp3tskmf', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w9ujs', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 45.1000003814698}, {'geohash': 'dp3tyc54', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 67.9000015258789}, {'geohash': 'dp3ty0nd', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 64.4500007629395}, {'geohash': 'dp3twxxz', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 37.5}, {'geohash': 'dp3tuz83', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 21.8999996185303}, {'geohash': 'dp3wuqp7', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 6.5}, {'geohash': 'dp3wu2zh', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wt5nz', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 11.09999990463257}, {'geohash': 'dp3wvq8x', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wkxd5', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 26.10000038146973}, {'geohash': 'dp3wt0zm', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 36.1000003814697}, {'geohash': 'dp3wssyg', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 43.700000762939396}, {'geohash': 'dp3wksf7', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 19.5}, {'geohash': 'dp3ws140', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.30000019073486}, {'geohash': 'dp3wkw82', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 26.100000381469698}, {'geohash': 'dp3wkrdb', 'count': 2, 'extras+avg': 1.75, 'fare+sum': 28.0999994277954}, {'geohash': 'dp3wsecd', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 24.300000190734842}, {'geohash': 'dp3wmwj8', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 20.94999980926514}, {'geohash': 'dp3wkew1', 'count': 2, 'extras+avg': 0.25, 'fare+sum': 20.85000038146973}, {'geohash': 'dp3wsejm', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 20.100000381469762}, {'geohash': 'dp3wu6pn', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wu8ub', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3tgerw', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 17.8500003814697}, {'geohash': 'dp3tjj3k', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.8499984741211}, {'geohash': 'dp3tjf3x', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.75}, {'geohash': 'dp3wubzg', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 14.6499996185303}, {'geohash': 'dp3thn34', 'count': 1, 'extras+avg': 3.0, 'fare+sum': 68.25}, {'geohash': 'dp3wugrp', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 21.0499992370605}, {'geohash': 'dp3tkpsd', 'count': 1, 'extras+avg': 4.0, 'fare+sum': 72.0}, {'geohash': 'dp3wk8yk', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3wuuyg', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.25}, {'geohash': 'dp3wusuf', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3tq06w', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.25}, {'geohash': 'dp3wktf7', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3tgb1j', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3ws0z4', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3wmjbt', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 9.64999961853027}, {'geohash': 'dp3wv6m8', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.25}, {'geohash': 'dp3wv7hr', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 26.25}, {'geohash': 'dp3wvp42', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 11.8500003814697}, {'geohash': 'dp3qzwzu', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 43.6500015258789}, {'geohash': 'dp3wsev5', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.25}, {'geohash': 'dp3tqnxf', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.4499998092651}, {'geohash': 'dp3tq8kg', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 32.8499984741211}, {'geohash': 'dp3wkcp7', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.44999980926514}, {'geohash': 'dp3wk0bw', 'count': 1, 'extras+avg': 5.0, 'fare+sum': 39.75}, {'geohash': 'dp3wked9', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.8500003814697}, {'geohash': 'dp3wjnyw', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 9.25}, {'geohash': 'dp3wjnhf', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.8500003814697}, {'geohash': 'dp3wjmh2', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 8.25}, {'geohash': 'dp3wj2hg', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkmng', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 18.0499992370605}, {'geohash': 'dp3wey45', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wewh6', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 20.75}, {'geohash': 'dp3weuf2', 'count': 1, 'extras+avg': 9.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3wsyhn', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 6.84999990463257}, {'geohash': 'dp3wknx8', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 15.8500003814697}, {'geohash': 'dp3wd0gr', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.75}, {'geohash': 'dp3wsw0v', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkpx2', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.8500003814697}, {'geohash': 'dp3wsn3q', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3tw4zb', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.44999980926514}, {'geohash': 'dp3wsgu5', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 28.0499992370605}, {'geohash': 'dp3wkrqy', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3wsghq', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 13.6499996185303}, {'geohash': 'dp3tttk9', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.25}, {'geohash': 'dp3wsfhq', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 29.0499992370605}, {'geohash': 'dp3trhxk', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 46.0}, {'geohash': 'dp3wtp0w', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3tqzm9', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 57.25}, {'geohash': 'dp3wn15e', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 0.0}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_9_RESULT = {'data': [{'geohash': 'dp3wmb5y3', 'count': 895, 'extras+avg': 0.43435754189944137, 'fare+sum': 7642.2900059223175}, {'geohash': 'dp3wq0umd', 'count': 500, 'extras+avg': 0.806, 'fare+sum': 4521.259998083115}, {'geohash': 'dp3wq4299', 'count': 386, 'extras+avg': 0.8018134715025906, 'fare+sum': 4033.2300107479095}, {'geohash': 'dp3wmfhqv', 'count': 374, 'extras+avg': 0.6778074866310161, 'fare+sum': 3112.0099957082425}, {'geohash': 'dp3wt7dyg', 'count': 358, 'extras+avg': 0.5519832392644615, 'fare+sum': 4049.5199956893925}, {'geohash': '7zzzzzzzz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}, {'geohash': 'dp3wjxus6', 'count': 312, 'extras+avg': 0.6121794871794872, 'fare+sum': 2575.690001010895}, {'geohash': 'dp3wq4jbk', 'count': 301, 'extras+avg': 0.707641196013289, 'fare+sum': 3094.2200043890625}, {'geohash': 'dp3wmf2jd', 'count': 299, 'extras+avg': 0.6337792642140468, 'fare+sum': 2514.6099982261658}, {'geohash': 'dp3wmge6g', 'count': 282, 'extras+avg': 0.44148936170212766, 'fare+sum': 3214.6300044059753}, {'geohash': 'dp3qzdncy', 'count': 277, 'extras+avg': 2.4521660649819497, 'fare+sum': 9363.659996271133}, {'geohash': 'dp3wq5883', 'count': 224, 'extras+avg': 0.5714285714285714, 'fare+sum': 2129.800005197525}, {'geohash': 'dp3wkguh0', 'count': 218, 'extras+avg': 0.5871559633027523, 'fare+sum': 2422.8500015735626}, {'geohash': 'dp3wnhqbr', 'count': 212, 'extras+avg': 0.660377358490566, 'fare+sum': 2430.589998722077}, {'geohash': 'dp3wmrz96', 'count': 202, 'extras+avg': 0.5841584158415841, 'fare+sum': 2192.4400038719177}, {'geohash': 'dp3wm8urw', 'count': 199, 'extras+avg': 0.41708542713567837, 'fare+sum': 1629.880003452301}, {'geohash': 'dp3wq4v22', 'count': 198, 'extras+avg': 0.5429292929292929, 'fare+sum': 1788.4300005435944}, {'geohash': 'dp3wnpe9s', 'count': 176, 'extras+avg': 0.7130681818181818, 'fare+sum': 1527.6799974441528}, {'geohash': 'dp3wjnvmg', 'count': 170, 'extras+avg': 0.37058823529411766, 'fare+sum': 2066.3799953460693}, {'geohash': 'dp3wnpc61', 'count': 153, 'extras+avg': 0.272875816993464, 'fare+sum': 2165.5400013923645}, {'geohash': 'dp3wmfnx5', 'count': 152, 'extras+avg': 0.84375, 'fare+sum': 1274.1300032138824}, {'geohash': 'dp3wq5ke2', 'count': 149, 'extras+avg': 0.6879194630872483, 'fare+sum': 1451.9199991226196}, {'geohash': 'dp3wm2czq', 'count': 137, 'extras+avg': 0.5218978102189781, 'fare+sum': 1092.809996843338}, {'geohash': 'dp3wtrdut', 'count': 118, 'extras+avg': 0.5550847457627118, 'fare+sum': 1521.6299939155574}, {'geohash': 'dp3wv5mqq', 'count': 111, 'extras+avg': 0.5045045045045045, 'fare+sum': 1464.2499966621401}, {'geohash': 'dp3wmykd2', 'count': 110, 'extras+avg': 0.6772727272727272, 'fare+sum': 1076.3400044441225}, {'geohash': 'dp3wkrg3v', 'count': 108, 'extras+avg': 0.6435185185185185, 'fare+sum': 1392.8299996852877}, {'geohash': 'dp3wnn73z', 'count': 107, 'extras+avg': 0.9112149532710281, 'fare+sum': 1241.1899988651276}, {'geohash': 'dp3tenvtp', 'count': 97, 'extras+avg': 1.922680412371134, 'fare+sum': 2773.190001964569}, {'geohash': 'dp3wq64nq', 'count': 93, 'extras+avg': 0.7419354838709677, 'fare+sum': 853.4499983787537}, {'geohash': 'dp3wmv18f', 'count': 73, 'extras+avg': 0.4863013698630137, 'fare+sum': 644.2300004959106}, {'geohash': 'dp3wjrf55', 'count': 72, 'extras+avg': 0.4583333333333333, 'fare+sum': 570.0500001907349}, {'geohash': 'dp3wn46j9', 'count': 71, 'extras+avg': 0.823943661971831, 'fare+sum': 1019.849999666214}, {'geohash': 'dp3qz6r2b', 'count': 70, 'extras+avg': 1.7285714285714286, 'fare+sum': 2008.1300034523015}, {'geohash': 'dp3wqj00y', 'count': 66, 'extras+avg': 0.4772727272727273, 'fare+sum': 561.7000007629395}, {'geohash': 'dp3wqh0t6', 'count': 64, 'extras+avg': 0.7109375, 'fare+sum': 574.3400025367737}, {'geohash': 'dp3wssqed', 'count': 63, 'extras+avg': 0.3253968253968254, 'fare+sum': 770.3499956130979}, {'geohash': 'dp3wmkx3c', 'count': 62, 'extras+avg': 0.49193548387096775, 'fare+sum': 655.4200019836427}, {'geohash': 'dp3wu97gh', 'count': 61, 'extras+avg': 0.5081967213114754, 'fare+sum': 909.520004272461}, {'geohash': 'dp3wmgsnx', 'count': 59, 'extras+avg': 0.576271186440678, 'fare+sum': 543.9500012397766}, {'geohash': 'dp3wev3tr', 'count': 58, 'extras+avg': 0.5344827586206896, 'fare+sum': 829.9500012397764}, {'geohash': 'dp3wmutpk', 'count': 55, 'extras+avg': 0.6454545454545455, 'fare+sum': 492.84000062942505}, {'geohash': 'dp3wm7ke6', 'count': 55, 'extras+avg': 0.6590909090909091, 'fare+sum': 430.49000048637396}, {'geohash': 'dp3tyb3hp', 'count': 52, 'extras+avg': 1.0480769230769231, 'fare+sum': 1270.749999523163}, {'geohash': 'dp3wjtu65', 'count': 50, 'extras+avg': 0.72, 'fare+sum': 545.8399968147276}, {'geohash': 'dp3wmgwqm', 'count': 49, 'extras+avg': 0.7040816326530612, 'fare+sum': 367.1999993324279}, {'geohash': 'dp3wmzdvb', 'count': 49, 'extras+avg': 0.5612244897959183, 'fare+sum': 516.3499989509581}, {'geohash': 'dp3wvp8ec', 'count': 47, 'extras+avg': 0.3191489361702128, 'fare+sum': 745.7400002479551}, {'geohash': 'dp3wjyku2', 'count': 47, 'extras+avg': 0.5212765957446809, 'fare+sum': 341.0399994850159}, {'geohash': 'dp3wkuub3', 'count': 47, 'extras+avg': 0.776595744680851, 'fare+sum': 467.9999995231626}, {'geohash': 'dp3ws4dwk', 'count': 41, 'extras+avg': 0.4268292682926829, 'fare+sum': 508.1399979591372}, {'geohash': 'dp3wuqnky', 'count': 39, 'extras+avg': 0.5256410256410257, 'fare+sum': 644.4400033950803}, {'geohash': 'dp3wn5ugf', 'count': 39, 'extras+avg': 1.0384615384615385, 'fare+sum': 557.0899982452393}, {'geohash': 'dp3wm6m67', 'count': 37, 'extras+avg': 0.7567567567567568, 'fare+sum': 372.6999988555908}, {'geohash': 'dp3wtkh4f', 'count': 35, 'extras+avg': 0.8857142857142857, 'fare+sum': 426.19000148773176}, {'geohash': 'dp3wt2yq2', 'count': 33, 'extras+avg': 0.8636363636363636, 'fare+sum': 416.8499965667726}, {'geohash': 'dp3wt8cyt', 'count': 33, 'extras+avg': 0.9393939393939394, 'fare+sum': 414.24999713897694}, {'geohash': 'dp3wmqk71', 'count': 31, 'extras+avg': 0.5, 'fare+sum': 302.10000085830694}, {'geohash': 'dp3wgb51e', 'count': 30, 'extras+avg': 0.5, 'fare+sum': 425.1499981880186}, {'geohash': 'dp3tfb057', 'count': 29, 'extras+avg': 1.9137931034482758, 'fare+sum': 889.6900062561035}, {'geohash': 'dp3wj4d7m', 'count': 28, 'extras+avg': 0.2857142857142857, 'fare+sum': 355.3799991607667}, {'geohash': 'dp3wt7mvv', 'count': 27, 'extras+avg': 0.6666666666666666, 'fare+sum': 272.27999830245966}, {'geohash': 'dp3wmvmhd', 'count': 23, 'extras+avg': 0.34782608695652173, 'fare+sum': 214.19999909400934}, {'geohash': 'dp3wt9yxe', 'count': 23, 'extras+avg': 0.6086956521739131, 'fare+sum': 250.60000228881842}, {'geohash': 'dp3wmxtkj', 'count': 22, 'extras+avg': 0.25, 'fare+sum': 188.48999881744376}, {'geohash': 'dp3wtsex7', 'count': 22, 'extras+avg': 0.5681818181818182, 'fare+sum': 267.62999963760376}, {'geohash': 'dp3wtdxsc', 'count': 21, 'extras+avg': 0.5, 'fare+sum': 252.9399991035461}, {'geohash': 'dp3wt6q0d', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 245.3500015735625}, {'geohash': 'dp3wm5s7d', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 208.59999990463248}, {'geohash': 'dp3wmx9ux', 'count': 21, 'extras+avg': 0.8571428571428571, 'fare+sum': 171.84999895095828}, {'geohash': 'dp3wtbcrx', 'count': 20, 'extras+avg': 0.575, 'fare+sum': 252.5000004768371}, {'geohash': 'dp3whzz2y', 'count': 20, 'extras+avg': 0.8, 'fare+sum': 222.50000047683713}, {'geohash': 'dp3wt6683', 'count': 20, 'extras+avg': 0.875, 'fare+sum': 173.5499982833863}, {'geohash': 'dp3wte3m5', 'count': 20, 'extras+avg': 1.075, 'fare+sum': 256.6000008583069}, {'geohash': 'dp3wmrwkn', 'count': 20, 'extras+avg': 0.7, 'fare+sum': 207.5000023841858}, {'geohash': 'dp3wb69xq', 'count': 19, 'extras+avg': 2.236842105263158, 'fare+sum': 320.6000003814697}, {'geohash': 'dp3typy50', 'count': 19, 'extras+avg': 0.6842105263157895, 'fare+sum': 261.8500003814699}, {'geohash': 'dp3wtwfx6', 'count': 18, 'extras+avg': 0.16666666666666666, 'fare+sum': 233.08999872207642}, {'geohash': 'dp3wj8015', 'count': 17, 'extras+avg': 0.7941176470588235, 'fare+sum': 322.1999998092651}, {'geohash': 'dp3whykby', 'count': 17, 'extras+avg': 0.4117647058823529, 'fare+sum': 192.2899985313415}, {'geohash': 'dp3wm58g2', 'count': 17, 'extras+avg': 1.8529411764705883, 'fare+sum': 195.9900012016297}, {'geohash': 'dp3wcgnsq', 'count': 17, 'extras+avg': 0.8529411764705882, 'fare+sum': 277.4400010108947}, {'geohash': 'dp3wmw64h', 'count': 16, 'extras+avg': 0.90625, 'fare+sum': 156.7999997138977}, {'geohash': 'dp3wtktgc', 'count': 16, 'extras+avg': 0.78125, 'fare+sum': 238.1399984359742}, {'geohash': 'dp3wmpsuw', 'count': 15, 'extras+avg': 0.9333333333333333, 'fare+sum': 142.7399997711182}, {'geohash': 'dp3wdvkxu', 'count': 15, 'extras+avg': 0.5, 'fare+sum': 298.20000123977655}, {'geohash': 'dp3wjc4gu', 'count': 15, 'extras+avg': 0.5333333333333333, 'fare+sum': 242.0000004768371}, {'geohash': 'dp3wkvpyn', 'count': 14, 'extras+avg': 0.6428571428571429, 'fare+sum': 150.40000104904186}, {'geohash': 'dp3wtqjpb', 'count': 14, 'extras+avg': 0.6785714285714286, 'fare+sum': 183.70000171661368}, {'geohash': 'dp3wmrdgt', 'count': 14, 'extras+avg': 3.892857142857143, 'fare+sum': 132.29000091552737}, {'geohash': 'dp3wtetbx', 'count': 14, 'extras+avg': 0.42857142857142855, 'fare+sum': 157.30000066757194}, {'geohash': 'dp3wkgt4y', 'count': 13, 'extras+avg': 0.9615384615384616, 'fare+sum': 145.6999998092651}, {'geohash': 'dp3wt4ppb', 'count': 13, 'extras+avg': 0.7692307692307693, 'fare+sum': 207.29999971389762}, {'geohash': 'dp3wt9hzk', 'count': 13, 'extras+avg': 0.11538461538461539, 'fare+sum': 126.45000052452089}, {'geohash': 'dp3tyen6s', 'count': 13, 'extras+avg': 0.6153846153846154, 'fare+sum': 245.2000007629395}, {'geohash': 'dp3wtt6hk', 'count': 12, 'extras+avg': 0.4166666666666667, 'fare+sum': 119.43999767303464}, {'geohash': 'dp3wmtjb6', 'count': 12, 'extras+avg': 0.16666666666666666, 'fare+sum': 85.99999952316283}, {'geohash': 'dp3wtd9ec', 'count': 12, 'extras+avg': 0.5833333333333334, 'fare+sum': 130.84999990463263}, {'geohash': 'dp3wtkd72', 'count': 12, 'extras+avg': 0.3333333333333333, 'fare+sum': 144.84999942779535}, {'geohash': 'dp3wt9cx5', 'count': 12, 'extras+avg': 0.5416666666666666, 'fare+sum': 126.49999904632557}, {'geohash': 'dp3wfdnbr', 'count': 11, 'extras+avg': 0.2727272727272727, 'fare+sum': 166.75000190734872}, {'geohash': 'dp3wkzpt5', 'count': 11, 'extras+avg': 0.6818181818181818, 'fare+sum': 174.95000457763675}, {'geohash': 'dp3w7getd', 'count': 11, 'extras+avg': 1.0454545454545454, 'fare+sum': 150.6999988555908}, {'geohash': 'dp3wtnpxk', 'count': 10, 'extras+avg': 0.25, 'fare+sum': 115.89999914169309}, {'geohash': 'dp3wt2ftz', 'count': 10, 'extras+avg': 0.95, 'fare+sum': 101.59999990463251}, {'geohash': 'dp3wt45rr', 'count': 9, 'extras+avg': 0.5, 'fare+sum': 82.64999914169313}, {'geohash': 'dp3tukeeu', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 204.09999847412115}, {'geohash': 'dp3wteecp', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 102.03999948501597}, {'geohash': 'dp3wv0vhe', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 132.80000114440915}, {'geohash': 'dp3wt76mk', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 93.04000043869009}, {'geohash': 'dp3wmem3m', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 64.95000076293945}, {'geohash': 'dp3wthghm', 'count': 8, 'extras+avg': 1.3125, 'fare+sum': 142.09999752044666}, {'geohash': 'dp3wt9uq3', 'count': 8, 'extras+avg': 0.8125, 'fare+sum': 119.2000017166138}, {'geohash': 'dp3wktydz', 'count': 8, 'extras+avg': 0.75, 'fare+sum': 101.80000019073483}, {'geohash': 'dp3wmezwm', 'count': 8, 'extras+avg': 0.125, 'fare+sum': 63.199999332428}, {'geohash': 'dp3wkvuvn', 'count': 8, 'extras+avg': 1.5625, 'fare+sum': 101.40000152587892}, {'geohash': 'dp3wm4k3r', 'count': 8, 'extras+avg': 0.0, 'fare+sum': 53.95000028610228}, {'geohash': 'dp3wkysfq', 'count': 8, 'extras+avg': 0.5, 'fare+sum': 104.24999904632563}, {'geohash': 'dp3wtptd7', 'count': 7, 'extras+avg': 0.7142857142857143, 'fare+sum': 105.49000120162967}, {'geohash': 'dp3wsbvzs', 'count': 7, 'extras+avg': 0.7857142857142857, 'fare+sum': 92.34999847412101}, {'geohash': 'dp3wt8s97', 'count': 7, 'extras+avg': 0.35714285714285715, 'fare+sum': 54.75000047683715}, {'geohash': 'dp3wjfdpf', 'count': 7, 'extras+avg': 0.8571428571428571, 'fare+sum': 99.14000082016}, {'geohash': 'dp3wsgpyg', 'count': 7, 'extras+avg': 0.42857142857142855, 'fare+sum': 55.55000066757199}, {'geohash': 'dp3ty5yd5', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 126.9500007629395}, {'geohash': 'dp3wt5cs3', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 82.74999999999991}, {'geohash': 'dp3twzxzk', 'count': 7, 'extras+avg': 1.1428571428571428, 'fare+sum': 128.9999971389769}, {'geohash': 'dp3wt0gu9', 'count': 7, 'extras+avg': 0.2857142857142857, 'fare+sum': 74.79999923706055}, {'geohash': 'dp3wv2zn0', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 74.10000038146975}, {'geohash': 'dp3twtx7d', 'count': 6, 'extras+avg': 0.6666666666666666, 'fare+sum': 178.2999992370606}, {'geohash': 'dp3w5uqm2', 'count': 6, 'extras+avg': 1.1666666666666667, 'fare+sum': 109.7499990463257}, {'geohash': 'dp3tv70e1', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 119.2500000000001}, {'geohash': 'dp3wkxt9j', 'count': 6, 'extras+avg': 1.0833333333333333, 'fare+sum': 83.89999914169313}, {'geohash': 'dp3wegqnf', 'count': 6, 'extras+avg': 0.5, 'fare+sum': 70.29999923706049}, {'geohash': 'dp3wgfcsk', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 37.34999942779544}, {'geohash': 'dp3wh08d7', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 115.70000076293942}, {'geohash': 'dp3wm6219', 'count': 6, 'extras+avg': 0.8333333333333334, 'fare+sum': 50.5}, {'geohash': 'dp3wubf5y', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 62.74999952316281}, {'geohash': 'dp3wtn5h7', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 58.45000028610226}, {'geohash': 'dp3wt5yuc', 'count': 5, 'extras+avg': 0.8, 'fare+sum': 53.64999961853038}, {'geohash': 'dp3wtmkbg', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.650000095367446}, {'geohash': 'dp3twxdxn', 'count': 5, 'extras+avg': 0.7, 'fare+sum': 105.2500000000001}, {'geohash': 'dp3wghb26', 'count': 5, 'extras+avg': 1.0, 'fare+sum': 67.13000011444086}, {'geohash': 'dp3tx4rqy', 'count': 5, 'extras+avg': 0.5, 'fare+sum': 87.85000085830691}, {'geohash': 'dp3ws8v7y', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w71cyr', 'count': 5, 'extras+avg': 0.95, 'fare+sum': 73.34999895095817}, {'geohash': 'dp3wdbe5g', 'count': 5, 'extras+avg': 0.0, 'fare+sum': 70.6499986648559}, {'geohash': 'dp3wkg9dm', 'count': 5, 'extras+avg': 0.4, 'fare+sum': 48.35000038146973}, {'geohash': 'dp3wtrjrz', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 64.5500001907349}, {'geohash': 'dp3wufpw5', 'count': 4, 'extras+avg': 1.125, 'fare+sum': 50.38999986648564}, {'geohash': 'dp3wsuu5s', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.59999990463259}, {'geohash': 'dp3wswntt', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 56.99000024795523}, {'geohash': 'dp3wthwdz', 'count': 4, 'extras+avg': 1.625, 'fare+sum': 73.99999999999997}, {'geohash': 'dp3wt55r7', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.39999961853028}, {'geohash': 'dp3wmhu5c', 'count': 4, 'extras+avg': 1.0, 'fare+sum': 31.20000028610233}, {'geohash': 'dp3whpyd2', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 37.19999980926511}, {'geohash': 'dp3wjut7e', 'count': 4, 'extras+avg': 0.875, 'fare+sum': 59.65000009536743}, {'geohash': 'dp3wkf3b1', 'count': 4, 'extras+avg': 0.5, 'fare+sum': 32.40000009536743}, {'geohash': 'dp3wm42cj', 'count': 4, 'extras+avg': 1.25, 'fare+sum': 37.40000009536741}, {'geohash': 'dp3wkz3kk', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 41.1999998092651}, {'geohash': 'dp3we81e0', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 61.0500001907349}, {'geohash': 'dp3wsfpyy', 'count': 3, 'extras+avg': 1.3333333333333333, 'fare+sum': 53.19999980926514}, {'geohash': 'dp3whz8ck', 'count': 3, 'extras+avg': 1.0, 'fare+sum': 25.350000381469698}, {'geohash': 'dp3wmwtth', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 25.75}, {'geohash': 'dp3wszebe', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 40.950000286102274}, {'geohash': 'dp3wsxy6w', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 42.3500003814697}, {'geohash': 'dp3wcxrbn', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 80.1499996185302}, {'geohash': 'dp3wsuzev', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 34.54999971389777}, {'geohash': 'dp3wsrz4m', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 38.550000190734906}, {'geohash': 'dp3tuyyuf', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 32.55000019073486}, {'geohash': 'dp3wk7z03', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 31.350000381469762}, {'geohash': 'dp3tu2tkh', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 58.2000007629394}, {'geohash': 'dp3tkcsuw', 'count': 3, 'extras+avg': 2.3333333333333335, 'fare+sum': 69.10000157356262}, {'geohash': 'dp3wksvuq', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 38.75}, {'geohash': 'dp3wkubss', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 48.80000066757207}, {'geohash': 'dp3wv2cug', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 43.1499996185303}, {'geohash': 'dp3ws2fff', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 35.7500009536743}, {'geohash': 'dp3tmr69s', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 28.2999992370605}, {'geohash': 'dp3wtcfrh', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 14.3000001907349}, {'geohash': 'dp3wvhu5k', 'count': 2, 'extras+avg': 1.25, 'fare+sum': 20.29999971389773}, {'geohash': 'dp3wjqs0r', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 21.29999971389773}, {'geohash': 'dp3wv5s36', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 23.90000057220464}, {'geohash': 'dp3tdv8zt', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 71.6500015258789}, {'geohash': 'dp3wv4hys', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 29.10000038146977}, {'geohash': 'dp3teeznw', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 58.950000762939496}, {'geohash': 'dp3wuynj9', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.899999618530302}, {'geohash': 'dp3tskmfw', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w9ujs5', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 45.1000003814698}, {'geohash': 'dp3tyc54y', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 67.9000015258789}, {'geohash': 'dp3ty0nd4', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 64.4500007629395}, {'geohash': 'dp3twxxzx', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 37.5}, {'geohash': 'dp3tuz83u', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 21.8999996185303}, {'geohash': 'dp3wuqp7q', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 6.5}, {'geohash': 'dp3wu2zhj', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wt5nzs', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 11.09999990463257}, {'geohash': 'dp3wvq8x6', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wkxd5k', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 26.10000038146973}, {'geohash': 'dp3wt0zmc', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 36.1000003814697}, {'geohash': 'dp3wssyg4', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 43.700000762939396}, {'geohash': 'dp3wksf7u', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 19.5}, {'geohash': 'dp3ws1404', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.30000019073486}, {'geohash': 'dp3wkw82y', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 26.100000381469698}, {'geohash': 'dp3wkrdbr', 'count': 2, 'extras+avg': 1.75, 'fare+sum': 28.0999994277954}, {'geohash': 'dp3wsecd2', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 24.300000190734842}, {'geohash': 'dp3wmwj8p', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 20.94999980926514}, {'geohash': 'dp3wkew1g', 'count': 2, 'extras+avg': 0.25, 'fare+sum': 20.85000038146973}, {'geohash': 'dp3wsejmc', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 20.100000381469762}, {'geohash': 'dp3wu6pn7', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wu8ubv', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3tgerw5', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 17.8500003814697}, {'geohash': 'dp3tjj3k6', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.8499984741211}, {'geohash': 'dp3tjf3xe', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.75}, {'geohash': 'dp3wubzg5', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 14.6499996185303}, {'geohash': 'dp3thn34q', 'count': 1, 'extras+avg': 3.0, 'fare+sum': 68.25}, {'geohash': 'dp3wugrps', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 21.0499992370605}, {'geohash': 'dp3tkpsdw', 'count': 1, 'extras+avg': 4.0, 'fare+sum': 72.0}, {'geohash': 'dp3wk8yk7', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3wuuyg1', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.25}, {'geohash': 'dp3wusufn', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3tq06w7', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.25}, {'geohash': 'dp3wktf7c', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3tgb1jv', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3ws0z4x', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3wmjbt8', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 9.64999961853027}, {'geohash': 'dp3wv6m81', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.25}, {'geohash': 'dp3wv7hrn', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 26.25}, {'geohash': 'dp3wvp426', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 11.8500003814697}, {'geohash': 'dp3qzwzu1', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 43.6500015258789}, {'geohash': 'dp3wsev5j', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.25}, {'geohash': 'dp3tqnxfr', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.4499998092651}, {'geohash': 'dp3tq8kgu', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 32.8499984741211}, {'geohash': 'dp3wkcp79', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.44999980926514}, {'geohash': 'dp3wk0bwp', 'count': 1, 'extras+avg': 5.0, 'fare+sum': 39.75}, {'geohash': 'dp3wked9f', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.8500003814697}, {'geohash': 'dp3wjnywf', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 9.25}, {'geohash': 'dp3wjnhfp', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.8500003814697}, {'geohash': 'dp3wjmh2p', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 8.25}, {'geohash': 'dp3wj2hgm', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkmng9', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 18.0499992370605}, {'geohash': 'dp3wey45q', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wewh6c', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 20.75}, {'geohash': 'dp3weuf2g', 'count': 1, 'extras+avg': 9.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3wsyhn0', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 6.84999990463257}, {'geohash': 'dp3wknx81', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 15.8500003814697}, {'geohash': 'dp3wd0grv', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.75}, {'geohash': 'dp3wsw0vp', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkpx2j', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.8500003814697}, {'geohash': 'dp3wsn3q5', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3tw4zbs', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.44999980926514}, {'geohash': 'dp3wsgu5x', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 28.0499992370605}, {'geohash': 'dp3wkrqy3', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3wsghq6', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 13.6499996185303}, {'geohash': 'dp3tttk9v', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.25}, {'geohash': 'dp3wsfhqv', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 29.0499992370605}, {'geohash': 'dp3trhxkz', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 46.0}, {'geohash': 'dp3wtp0w2', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3tqzm9d', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 57.25}, {'geohash': 'dp3wn15e6', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 0.0}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_10_RESULT = {'data': [{'geohash': 'dp3wmb5y3p', 'count': 895, 'extras+avg': 0.43435754189944137, 'fare+sum': 7642.2900059223175}, {'geohash': 'dp3wq0umdz', 'count': 500, 'extras+avg': 0.806, 'fare+sum': 4521.259998083115}, {'geohash': 'dp3wq42991', 'count': 386, 'extras+avg': 0.8018134715025906, 'fare+sum': 4033.2300107479095}, {'geohash': 'dp3wmfhqvd', 'count': 374, 'extras+avg': 0.6778074866310161, 'fare+sum': 3112.0099957082425}, {'geohash': 'dp3wt7dyg4', 'count': 358, 'extras+avg': 0.5519832392644615, 'fare+sum': 4049.5199956893925}, {'geohash': '7zzzzzzzzz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}, {'geohash': 'dp3wjxus66', 'count': 312, 'extras+avg': 0.6121794871794872, 'fare+sum': 2575.690001010895}, {'geohash': 'dp3wq4jbk3', 'count': 301, 'extras+avg': 0.707641196013289, 'fare+sum': 3094.2200043890625}, {'geohash': 'dp3wmf2jdj', 'count': 299, 'extras+avg': 0.6337792642140468, 'fare+sum': 2514.6099982261658}, {'geohash': 'dp3wmge6gg', 'count': 282, 'extras+avg': 0.44148936170212766, 'fare+sum': 3214.6300044059753}, {'geohash': 'dp3qzdncy9', 'count': 277, 'extras+avg': 2.4521660649819497, 'fare+sum': 9363.659996271133}, {'geohash': 'dp3wq58832', 'count': 224, 'extras+avg': 0.5714285714285714, 'fare+sum': 2129.800005197525}, {'geohash': 'dp3wkguh0z', 'count': 218, 'extras+avg': 0.5871559633027523, 'fare+sum': 2422.8500015735626}, {'geohash': 'dp3wnhqbrs', 'count': 212, 'extras+avg': 0.660377358490566, 'fare+sum': 2430.589998722077}, {'geohash': 'dp3wmrz96g', 'count': 202, 'extras+avg': 0.5841584158415841, 'fare+sum': 2192.4400038719177}, {'geohash': 'dp3wm8urw9', 'count': 199, 'extras+avg': 0.41708542713567837, 'fare+sum': 1629.880003452301}, {'geohash': 'dp3wq4v22b', 'count': 198, 'extras+avg': 0.5429292929292929, 'fare+sum': 1788.4300005435944}, {'geohash': 'dp3wnpe9s4', 'count': 176, 'extras+avg': 0.7130681818181818, 'fare+sum': 1527.6799974441528}, {'geohash': 'dp3wjnvmgb', 'count': 170, 'extras+avg': 0.37058823529411766, 'fare+sum': 2066.3799953460693}, {'geohash': 'dp3wnpc614', 'count': 153, 'extras+avg': 0.272875816993464, 'fare+sum': 2165.5400013923645}, {'geohash': 'dp3wmfnx50', 'count': 152, 'extras+avg': 0.84375, 'fare+sum': 1274.1300032138824}, {'geohash': 'dp3wq5ke2p', 'count': 149, 'extras+avg': 0.6879194630872483, 'fare+sum': 1451.9199991226196}, {'geohash': 'dp3wm2czqq', 'count': 137, 'extras+avg': 0.5218978102189781, 'fare+sum': 1092.809996843338}, {'geohash': 'dp3wtrdutf', 'count': 118, 'extras+avg': 0.5550847457627118, 'fare+sum': 1521.6299939155574}, {'geohash': 'dp3wv5mqq6', 'count': 111, 'extras+avg': 0.5045045045045045, 'fare+sum': 1464.2499966621401}, {'geohash': 'dp3wmykd2f', 'count': 110, 'extras+avg': 0.6772727272727272, 'fare+sum': 1076.3400044441225}, {'geohash': 'dp3wkrg3v9', 'count': 108, 'extras+avg': 0.6435185185185185, 'fare+sum': 1392.8299996852877}, {'geohash': 'dp3wnn73zq', 'count': 107, 'extras+avg': 0.9112149532710281, 'fare+sum': 1241.1899988651276}, {'geohash': 'dp3tenvtp4', 'count': 97, 'extras+avg': 1.922680412371134, 'fare+sum': 2773.190001964569}, {'geohash': 'dp3wq64nqm', 'count': 93, 'extras+avg': 0.7419354838709677, 'fare+sum': 853.4499983787537}, {'geohash': 'dp3wmv18ff', 'count': 73, 'extras+avg': 0.4863013698630137, 'fare+sum': 644.2300004959106}, {'geohash': 'dp3wjrf55x', 'count': 72, 'extras+avg': 0.4583333333333333, 'fare+sum': 570.0500001907349}, {'geohash': 'dp3wn46j99', 'count': 71, 'extras+avg': 0.823943661971831, 'fare+sum': 1019.849999666214}, {'geohash': 'dp3qz6r2b0', 'count': 70, 'extras+avg': 1.7285714285714286, 'fare+sum': 2008.1300034523015}, {'geohash': 'dp3wqj00yz', 'count': 66, 'extras+avg': 0.4772727272727273, 'fare+sum': 561.7000007629395}, {'geohash': 'dp3wqh0t6v', 'count': 64, 'extras+avg': 0.7109375, 'fare+sum': 574.3400025367737}, {'geohash': 'dp3wssqede', 'count': 63, 'extras+avg': 0.3253968253968254, 'fare+sum': 770.3499956130979}, {'geohash': 'dp3wmkx3cn', 'count': 62, 'extras+avg': 0.49193548387096775, 'fare+sum': 655.4200019836427}, {'geohash': 'dp3wu97ghf', 'count': 61, 'extras+avg': 0.5081967213114754, 'fare+sum': 909.520004272461}, {'geohash': 'dp3wmgsnxz', 'count': 59, 'extras+avg': 0.576271186440678, 'fare+sum': 543.9500012397766}, {'geohash': 'dp3wev3tr6', 'count': 58, 'extras+avg': 0.5344827586206896, 'fare+sum': 829.9500012397764}, {'geohash': 'dp3wmutpkf', 'count': 55, 'extras+avg': 0.6454545454545455, 'fare+sum': 492.84000062942505}, {'geohash': 'dp3wm7ke6f', 'count': 55, 'extras+avg': 0.6590909090909091, 'fare+sum': 430.49000048637396}, {'geohash': 'dp3tyb3hpp', 'count': 52, 'extras+avg': 1.0480769230769231, 'fare+sum': 1270.749999523163}, {'geohash': 'dp3wjtu65n', 'count': 50, 'extras+avg': 0.72, 'fare+sum': 545.8399968147276}, {'geohash': 'dp3wmgwqmz', 'count': 49, 'extras+avg': 0.7040816326530612, 'fare+sum': 367.1999993324279}, {'geohash': 'dp3wmzdvb4', 'count': 49, 'extras+avg': 0.5612244897959183, 'fare+sum': 516.3499989509581}, {'geohash': 'dp3wvp8ec1', 'count': 47, 'extras+avg': 0.3191489361702128, 'fare+sum': 745.7400002479551}, {'geohash': 'dp3wjyku25', 'count': 47, 'extras+avg': 0.5212765957446809, 'fare+sum': 341.0399994850159}, {'geohash': 'dp3wkuub31', 'count': 47, 'extras+avg': 0.776595744680851, 'fare+sum': 467.9999995231626}, {'geohash': 'dp3ws4dwkw', 'count': 41, 'extras+avg': 0.4268292682926829, 'fare+sum': 508.1399979591372}, {'geohash': 'dp3wuqnkyh', 'count': 39, 'extras+avg': 0.5256410256410257, 'fare+sum': 644.4400033950803}, {'geohash': 'dp3wn5ugf0', 'count': 39, 'extras+avg': 1.0384615384615385, 'fare+sum': 557.0899982452393}, {'geohash': 'dp3wm6m67v', 'count': 37, 'extras+avg': 0.7567567567567568, 'fare+sum': 372.6999988555908}, {'geohash': 'dp3wtkh4fu', 'count': 35, 'extras+avg': 0.8857142857142857, 'fare+sum': 426.19000148773176}, {'geohash': 'dp3wt2yq2k', 'count': 33, 'extras+avg': 0.8636363636363636, 'fare+sum': 416.8499965667726}, {'geohash': 'dp3wt8cyt6', 'count': 33, 'extras+avg': 0.9393939393939394, 'fare+sum': 414.24999713897694}, {'geohash': 'dp3wmqk71e', 'count': 31, 'extras+avg': 0.5, 'fare+sum': 302.10000085830694}, {'geohash': 'dp3wgb51ex', 'count': 30, 'extras+avg': 0.5, 'fare+sum': 425.1499981880186}, {'geohash': 'dp3tfb057x', 'count': 29, 'extras+avg': 1.9137931034482758, 'fare+sum': 889.6900062561035}, {'geohash': 'dp3wj4d7mx', 'count': 28, 'extras+avg': 0.2857142857142857, 'fare+sum': 355.3799991607667}, {'geohash': 'dp3wt7mvvs', 'count': 27, 'extras+avg': 0.6666666666666666, 'fare+sum': 272.27999830245966}, {'geohash': 'dp3wmvmhd8', 'count': 23, 'extras+avg': 0.34782608695652173, 'fare+sum': 214.19999909400934}, {'geohash': 'dp3wt9yxeq', 'count': 23, 'extras+avg': 0.6086956521739131, 'fare+sum': 250.60000228881842}, {'geohash': 'dp3wmxtkjc', 'count': 22, 'extras+avg': 0.25, 'fare+sum': 188.48999881744376}, {'geohash': 'dp3wtsex7w', 'count': 22, 'extras+avg': 0.5681818181818182, 'fare+sum': 267.62999963760376}, {'geohash': 'dp3wtdxsc4', 'count': 21, 'extras+avg': 0.5, 'fare+sum': 252.9399991035461}, {'geohash': 'dp3wt6q0dw', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 245.3500015735625}, {'geohash': 'dp3wm5s7dt', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 208.59999990463248}, {'geohash': 'dp3wmx9ux2', 'count': 21, 'extras+avg': 0.8571428571428571, 'fare+sum': 171.84999895095828}, {'geohash': 'dp3wtbcrxt', 'count': 20, 'extras+avg': 0.575, 'fare+sum': 252.5000004768371}, {'geohash': 'dp3whzz2ym', 'count': 20, 'extras+avg': 0.8, 'fare+sum': 222.50000047683713}, {'geohash': 'dp3wt66839', 'count': 20, 'extras+avg': 0.875, 'fare+sum': 173.5499982833863}, {'geohash': 'dp3wte3m5p', 'count': 20, 'extras+avg': 1.075, 'fare+sum': 256.6000008583069}, {'geohash': 'dp3wmrwkn1', 'count': 20, 'extras+avg': 0.7, 'fare+sum': 207.5000023841858}, {'geohash': 'dp3wb69xqk', 'count': 19, 'extras+avg': 2.236842105263158, 'fare+sum': 320.6000003814697}, {'geohash': 'dp3typy50z', 'count': 19, 'extras+avg': 0.6842105263157895, 'fare+sum': 261.8500003814699}, {'geohash': 'dp3wtwfx6t', 'count': 18, 'extras+avg': 0.16666666666666666, 'fare+sum': 233.08999872207642}, {'geohash': 'dp3wj8015p', 'count': 17, 'extras+avg': 0.7941176470588235, 'fare+sum': 322.1999998092651}, {'geohash': 'dp3whykby7', 'count': 17, 'extras+avg': 0.4117647058823529, 'fare+sum': 192.2899985313415}, {'geohash': 'dp3wm58g28', 'count': 17, 'extras+avg': 1.8529411764705883, 'fare+sum': 195.9900012016297}, {'geohash': 'dp3wcgnsqn', 'count': 17, 'extras+avg': 0.8529411764705882, 'fare+sum': 277.4400010108947}, {'geohash': 'dp3wmw64hv', 'count': 16, 'extras+avg': 0.90625, 'fare+sum': 156.7999997138977}, {'geohash': 'dp3wtktgcj', 'count': 16, 'extras+avg': 0.78125, 'fare+sum': 238.1399984359742}, {'geohash': 'dp3wmpsuwu', 'count': 15, 'extras+avg': 0.9333333333333333, 'fare+sum': 142.7399997711182}, {'geohash': 'dp3wdvkxut', 'count': 15, 'extras+avg': 0.5, 'fare+sum': 298.20000123977655}, {'geohash': 'dp3wjc4gu2', 'count': 15, 'extras+avg': 0.5333333333333333, 'fare+sum': 242.0000004768371}, {'geohash': 'dp3wkvpynb', 'count': 14, 'extras+avg': 0.6428571428571429, 'fare+sum': 150.40000104904186}, {'geohash': 'dp3wtqjpbw', 'count': 14, 'extras+avg': 0.6785714285714286, 'fare+sum': 183.70000171661368}, {'geohash': 'dp3wmrdgt5', 'count': 14, 'extras+avg': 3.892857142857143, 'fare+sum': 132.29000091552737}, {'geohash': 'dp3wtetbxd', 'count': 14, 'extras+avg': 0.42857142857142855, 'fare+sum': 157.30000066757194}, {'geohash': 'dp3wkgt4yc', 'count': 13, 'extras+avg': 0.9615384615384616, 'fare+sum': 145.6999998092651}, {'geohash': 'dp3wt4ppb6', 'count': 13, 'extras+avg': 0.7692307692307693, 'fare+sum': 207.29999971389762}, {'geohash': 'dp3wt9hzkd', 'count': 13, 'extras+avg': 0.11538461538461539, 'fare+sum': 126.45000052452089}, {'geohash': 'dp3tyen6sf', 'count': 13, 'extras+avg': 0.6153846153846154, 'fare+sum': 245.2000007629395}, {'geohash': 'dp3wtt6hk0', 'count': 12, 'extras+avg': 0.4166666666666667, 'fare+sum': 119.43999767303464}, {'geohash': 'dp3wmtjb6g', 'count': 12, 'extras+avg': 0.16666666666666666, 'fare+sum': 85.99999952316283}, {'geohash': 'dp3wtd9ecv', 'count': 12, 'extras+avg': 0.5833333333333334, 'fare+sum': 130.84999990463263}, {'geohash': 'dp3wtkd72q', 'count': 12, 'extras+avg': 0.3333333333333333, 'fare+sum': 144.84999942779535}, {'geohash': 'dp3wt9cx55', 'count': 12, 'extras+avg': 0.5416666666666666, 'fare+sum': 126.49999904632557}, {'geohash': 'dp3wfdnbrt', 'count': 11, 'extras+avg': 0.2727272727272727, 'fare+sum': 166.75000190734872}, {'geohash': 'dp3wkzpt5j', 'count': 11, 'extras+avg': 0.6818181818181818, 'fare+sum': 174.95000457763675}, {'geohash': 'dp3w7getd7', 'count': 11, 'extras+avg': 1.0454545454545454, 'fare+sum': 150.6999988555908}, {'geohash': 'dp3wtnpxku', 'count': 10, 'extras+avg': 0.25, 'fare+sum': 115.89999914169309}, {'geohash': 'dp3wt2ftzw', 'count': 10, 'extras+avg': 0.95, 'fare+sum': 101.59999990463251}, {'geohash': 'dp3wt45rrt', 'count': 9, 'extras+avg': 0.5, 'fare+sum': 82.64999914169313}, {'geohash': 'dp3tukeeu6', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 204.09999847412115}, {'geohash': 'dp3wteecp4', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 102.03999948501597}, {'geohash': 'dp3wv0vheb', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 132.80000114440915}, {'geohash': 'dp3wt76mk0', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 93.04000043869009}, {'geohash': 'dp3wmem3mn', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 64.95000076293945}, {'geohash': 'dp3wthghms', 'count': 8, 'extras+avg': 1.3125, 'fare+sum': 142.09999752044666}, {'geohash': 'dp3wt9uq3s', 'count': 8, 'extras+avg': 0.8125, 'fare+sum': 119.2000017166138}, {'geohash': 'dp3wktydzj', 'count': 8, 'extras+avg': 0.75, 'fare+sum': 101.80000019073483}, {'geohash': 'dp3wmezwm4', 'count': 8, 'extras+avg': 0.125, 'fare+sum': 63.199999332428}, {'geohash': 'dp3wkvuvny', 'count': 8, 'extras+avg': 1.5625, 'fare+sum': 101.40000152587892}, {'geohash': 'dp3wm4k3rq', 'count': 8, 'extras+avg': 0.0, 'fare+sum': 53.95000028610228}, {'geohash': 'dp3wkysfqj', 'count': 8, 'extras+avg': 0.5, 'fare+sum': 104.24999904632563}, {'geohash': 'dp3wtptd7q', 'count': 7, 'extras+avg': 0.7142857142857143, 'fare+sum': 105.49000120162967}, {'geohash': 'dp3wsbvzsn', 'count': 7, 'extras+avg': 0.7857142857142857, 'fare+sum': 92.34999847412101}, {'geohash': 'dp3wt8s97k', 'count': 7, 'extras+avg': 0.35714285714285715, 'fare+sum': 54.75000047683715}, {'geohash': 'dp3wjfdpf7', 'count': 7, 'extras+avg': 0.8571428571428571, 'fare+sum': 99.14000082016}, {'geohash': 'dp3wsgpygh', 'count': 7, 'extras+avg': 0.42857142857142855, 'fare+sum': 55.55000066757199}, {'geohash': 'dp3ty5yd5f', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 126.9500007629395}, {'geohash': 'dp3wt5cs34', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 82.74999999999991}, {'geohash': 'dp3twzxzkg', 'count': 7, 'extras+avg': 1.1428571428571428, 'fare+sum': 128.9999971389769}, {'geohash': 'dp3wt0gu9x', 'count': 7, 'extras+avg': 0.2857142857142857, 'fare+sum': 74.79999923706055}, {'geohash': 'dp3wv2zn01', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 74.10000038146975}, {'geohash': 'dp3twtx7d7', 'count': 6, 'extras+avg': 0.6666666666666666, 'fare+sum': 178.2999992370606}, {'geohash': 'dp3w5uqm28', 'count': 6, 'extras+avg': 1.1666666666666667, 'fare+sum': 109.7499990463257}, {'geohash': 'dp3tv70e1m', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 119.2500000000001}, {'geohash': 'dp3wkxt9j7', 'count': 6, 'extras+avg': 1.0833333333333333, 'fare+sum': 83.89999914169313}, {'geohash': 'dp3wegqnf5', 'count': 6, 'extras+avg': 0.5, 'fare+sum': 70.29999923706049}, {'geohash': 'dp3wgfcskm', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 37.34999942779544}, {'geohash': 'dp3wh08d7e', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 115.70000076293942}, {'geohash': 'dp3wm6219n', 'count': 6, 'extras+avg': 0.8333333333333334, 'fare+sum': 50.5}, {'geohash': 'dp3wubf5yu', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 62.74999952316281}, {'geohash': 'dp3wtn5h7f', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 58.45000028610226}, {'geohash': 'dp3wt5yucz', 'count': 5, 'extras+avg': 0.8, 'fare+sum': 53.64999961853038}, {'geohash': 'dp3wtmkbgm', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.650000095367446}, {'geohash': 'dp3twxdxnh', 'count': 5, 'extras+avg': 0.7, 'fare+sum': 105.2500000000001}, {'geohash': 'dp3wghb265', 'count': 5, 'extras+avg': 1.0, 'fare+sum': 67.13000011444086}, {'geohash': 'dp3tx4rqy6', 'count': 5, 'extras+avg': 0.5, 'fare+sum': 87.85000085830691}, {'geohash': 'dp3ws8v7yv', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w71cyrz', 'count': 5, 'extras+avg': 0.95, 'fare+sum': 73.34999895095817}, {'geohash': 'dp3wdbe5gx', 'count': 5, 'extras+avg': 0.0, 'fare+sum': 70.6499986648559}, {'geohash': 'dp3wkg9dm4', 'count': 5, 'extras+avg': 0.4, 'fare+sum': 48.35000038146973}, {'geohash': 'dp3wtrjrzu', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 64.5500001907349}, {'geohash': 'dp3wufpw53', 'count': 4, 'extras+avg': 1.125, 'fare+sum': 50.38999986648564}, {'geohash': 'dp3wsuu5su', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.59999990463259}, {'geohash': 'dp3wswntt2', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 56.99000024795523}, {'geohash': 'dp3wthwdzx', 'count': 4, 'extras+avg': 1.625, 'fare+sum': 73.99999999999997}, {'geohash': 'dp3wt55r72', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.39999961853028}, {'geohash': 'dp3wmhu5ct', 'count': 4, 'extras+avg': 1.0, 'fare+sum': 31.20000028610233}, {'geohash': 'dp3whpyd27', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 37.19999980926511}, {'geohash': 'dp3wjut7ek', 'count': 4, 'extras+avg': 0.875, 'fare+sum': 59.65000009536743}, {'geohash': 'dp3wkf3b1y', 'count': 4, 'extras+avg': 0.5, 'fare+sum': 32.40000009536743}, {'geohash': 'dp3wm42cje', 'count': 4, 'extras+avg': 1.25, 'fare+sum': 37.40000009536741}, {'geohash': 'dp3wkz3kkf', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 41.1999998092651}, {'geohash': 'dp3we81e02', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 61.0500001907349}, {'geohash': 'dp3wsfpyy6', 'count': 3, 'extras+avg': 1.3333333333333333, 'fare+sum': 53.19999980926514}, {'geohash': 'dp3whz8ckw', 'count': 3, 'extras+avg': 1.0, 'fare+sum': 25.350000381469698}, {'geohash': 'dp3wmwtthk', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 25.75}, {'geohash': 'dp3wszebet', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 40.950000286102274}, {'geohash': 'dp3wsxy6w2', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 42.3500003814697}, {'geohash': 'dp3wcxrbnd', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 80.1499996185302}, {'geohash': 'dp3wsuzevz', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 34.54999971389777}, {'geohash': 'dp3wsrz4m5', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 38.550000190734906}, {'geohash': 'dp3tuyyufw', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 32.55000019073486}, {'geohash': 'dp3wk7z03n', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 31.350000381469762}, {'geohash': 'dp3tu2tkhb', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 58.2000007629394}, {'geohash': 'dp3tkcsuww', 'count': 3, 'extras+avg': 2.3333333333333335, 'fare+sum': 69.10000157356262}, {'geohash': 'dp3wksvuq8', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 38.75}, {'geohash': 'dp3wkubssh', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 48.80000066757207}, {'geohash': 'dp3wv2cugb', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 43.1499996185303}, {'geohash': 'dp3ws2fffd', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 35.7500009536743}, {'geohash': 'dp3tmr69s5', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 28.2999992370605}, {'geohash': 'dp3wtcfrh9', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 14.3000001907349}, {'geohash': 'dp3wvhu5k5', 'count': 2, 'extras+avg': 1.25, 'fare+sum': 20.29999971389773}, {'geohash': 'dp3wjqs0r8', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 21.29999971389773}, {'geohash': 'dp3wv5s36f', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 23.90000057220464}, {'geohash': 'dp3tdv8ztq', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 71.6500015258789}, {'geohash': 'dp3wv4hysq', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 29.10000038146977}, {'geohash': 'dp3teeznw6', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 58.950000762939496}, {'geohash': 'dp3wuynj9s', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.899999618530302}, {'geohash': 'dp3tskmfwu', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w9ujs5k', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 45.1000003814698}, {'geohash': 'dp3tyc54y1', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 67.9000015258789}, {'geohash': 'dp3ty0nd4h', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 64.4500007629395}, {'geohash': 'dp3twxxzxw', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 37.5}, {'geohash': 'dp3tuz83uk', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 21.8999996185303}, {'geohash': 'dp3wuqp7qh', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 6.5}, {'geohash': 'dp3wu2zhj8', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wt5nzsq', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 11.09999990463257}, {'geohash': 'dp3wvq8x6r', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wkxd5k1', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 26.10000038146973}, {'geohash': 'dp3wt0zmc4', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 36.1000003814697}, {'geohash': 'dp3wssyg41', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 43.700000762939396}, {'geohash': 'dp3wksf7ue', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 19.5}, {'geohash': 'dp3ws1404c', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.30000019073486}, {'geohash': 'dp3wkw82yk', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 26.100000381469698}, {'geohash': 'dp3wkrdbr8', 'count': 2, 'extras+avg': 1.75, 'fare+sum': 28.0999994277954}, {'geohash': 'dp3wsecd2b', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 24.300000190734842}, {'geohash': 'dp3wmwj8pj', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 20.94999980926514}, {'geohash': 'dp3wkew1g6', 'count': 2, 'extras+avg': 0.25, 'fare+sum': 20.85000038146973}, {'geohash': 'dp3wsejmc5', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 20.100000381469762}, {'geohash': 'dp3wu6pn7k', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wu8ubvf', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3tgerw58', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 17.8500003814697}, {'geohash': 'dp3tjj3k6b', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.8499984741211}, {'geohash': 'dp3tjf3xe7', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.75}, {'geohash': 'dp3wubzg5j', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 14.6499996185303}, {'geohash': 'dp3thn34q2', 'count': 1, 'extras+avg': 3.0, 'fare+sum': 68.25}, {'geohash': 'dp3wugrpsr', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 21.0499992370605}, {'geohash': 'dp3tkpsdwv', 'count': 1, 'extras+avg': 4.0, 'fare+sum': 72.0}, {'geohash': 'dp3wk8yk7q', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3wuuyg1b', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.25}, {'geohash': 'dp3wusufn6', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3tq06w7x', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.25}, {'geohash': 'dp3wktf7ce', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3tgb1jvb', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3ws0z4xd', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3wmjbt8e', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 9.64999961853027}, {'geohash': 'dp3wv6m81u', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.25}, {'geohash': 'dp3wv7hrne', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 26.25}, {'geohash': 'dp3wvp426c', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 11.8500003814697}, {'geohash': 'dp3qzwzu1e', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 43.6500015258789}, {'geohash': 'dp3wsev5j2', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.25}, {'geohash': 'dp3tqnxfrf', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.4499998092651}, {'geohash': 'dp3tq8kgu9', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 32.8499984741211}, {'geohash': 'dp3wkcp79m', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.44999980926514}, {'geohash': 'dp3wk0bwpp', 'count': 1, 'extras+avg': 5.0, 'fare+sum': 39.75}, {'geohash': 'dp3wked9fy', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.8500003814697}, {'geohash': 'dp3wjnywf8', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 9.25}, {'geohash': 'dp3wjnhfpw', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.8500003814697}, {'geohash': 'dp3wjmh2p7', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 8.25}, {'geohash': 'dp3wj2hgm6', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkmng94', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 18.0499992370605}, {'geohash': 'dp3wey45q4', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wewh6cb', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 20.75}, {'geohash': 'dp3weuf2gj', 'count': 1, 'extras+avg': 9.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3wsyhn0k', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 6.84999990463257}, {'geohash': 'dp3wknx81s', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 15.8500003814697}, {'geohash': 'dp3wd0grve', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.75}, {'geohash': 'dp3wsw0vp1', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkpx2j8', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.8500003814697}, {'geohash': 'dp3wsn3q5e', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3tw4zbs1', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.44999980926514}, {'geohash': 'dp3wsgu5xx', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 28.0499992370605}, {'geohash': 'dp3wkrqy37', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3wsghq6p', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 13.6499996185303}, {'geohash': 'dp3tttk9vc', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.25}, {'geohash': 'dp3wsfhqv3', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 29.0499992370605}, {'geohash': 'dp3trhxkzz', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 46.0}, {'geohash': 'dp3wtp0w2e', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3tqzm9d4', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 57.25}, {'geohash': 'dp3wn15e6s', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 0.0}], 'visualization': 'Geo Map'}
    TS_GEO_HASH_PRECISION_11_RESULT = {'data': [{'geohash': 'dp3wmb5y3p0', 'count': 895, 'extras+avg': 0.43435754189944137, 'fare+sum': 7642.2900059223175}, {'geohash': 'dp3wq0umdzs', 'count': 500, 'extras+avg': 0.806, 'fare+sum': 4521.259998083115}, {'geohash': 'dp3wq42991q', 'count': 386, 'extras+avg': 0.8018134715025906, 'fare+sum': 4033.2300107479095}, {'geohash': 'dp3wmfhqvdd', 'count': 374, 'extras+avg': 0.6778074866310161, 'fare+sum': 3112.0099957082425}, {'geohash': 'dp3wt7dyg4w', 'count': 358, 'extras+avg': 0.5519832392644615, 'fare+sum': 4049.5199956893925}, {'geohash': '7zzzzzzzzzz', 'count': 320, 'extras+avg': 4.508125001192093, 'fare+sum': 8229.420015573502}, {'geohash': 'dp3wjxus66b', 'count': 312, 'extras+avg': 0.6121794871794872, 'fare+sum': 2575.690001010895}, {'geohash': 'dp3wq4jbk3u', 'count': 301, 'extras+avg': 0.707641196013289, 'fare+sum': 3094.2200043890625}, {'geohash': 'dp3wmf2jdjx', 'count': 299, 'extras+avg': 0.6337792642140468, 'fare+sum': 2514.6099982261658}, {'geohash': 'dp3wmge6ggv', 'count': 282, 'extras+avg': 0.44148936170212766, 'fare+sum': 3214.6300044059753}, {'geohash': 'dp3qzdncy9y', 'count': 277, 'extras+avg': 2.4521660649819497, 'fare+sum': 9363.659996271133}, {'geohash': 'dp3wq588329', 'count': 224, 'extras+avg': 0.5714285714285714, 'fare+sum': 2129.800005197525}, {'geohash': 'dp3wkguh0z4', 'count': 218, 'extras+avg': 0.5871559633027523, 'fare+sum': 2422.8500015735626}, {'geohash': 'dp3wnhqbrs6', 'count': 212, 'extras+avg': 0.660377358490566, 'fare+sum': 2430.589998722077}, {'geohash': 'dp3wmrz96gh', 'count': 202, 'extras+avg': 0.5841584158415841, 'fare+sum': 2192.4400038719177}, {'geohash': 'dp3wm8urw9c', 'count': 199, 'extras+avg': 0.41708542713567837, 'fare+sum': 1629.880003452301}, {'geohash': 'dp3wq4v22b2', 'count': 198, 'extras+avg': 0.5429292929292929, 'fare+sum': 1788.4300005435944}, {'geohash': 'dp3wnpe9s46', 'count': 176, 'extras+avg': 0.7130681818181818, 'fare+sum': 1527.6799974441528}, {'geohash': 'dp3wjnvmgbr', 'count': 170, 'extras+avg': 0.37058823529411766, 'fare+sum': 2066.3799953460693}, {'geohash': 'dp3wnpc6143', 'count': 153, 'extras+avg': 0.272875816993464, 'fare+sum': 2165.5400013923645}, {'geohash': 'dp3wmfnx50r', 'count': 152, 'extras+avg': 0.84375, 'fare+sum': 1274.1300032138824}, {'geohash': 'dp3wq5ke2pp', 'count': 149, 'extras+avg': 0.6879194630872483, 'fare+sum': 1451.9199991226196}, {'geohash': 'dp3wm2czqqm', 'count': 137, 'extras+avg': 0.5218978102189781, 'fare+sum': 1092.809996843338}, {'geohash': 'dp3wtrdutfr', 'count': 118, 'extras+avg': 0.5550847457627118, 'fare+sum': 1521.6299939155574}, {'geohash': 'dp3wv5mqq67', 'count': 111, 'extras+avg': 0.5045045045045045, 'fare+sum': 1464.2499966621401}, {'geohash': 'dp3wmykd2fz', 'count': 110, 'extras+avg': 0.6772727272727272, 'fare+sum': 1076.3400044441225}, {'geohash': 'dp3wkrg3v94', 'count': 108, 'extras+avg': 0.6435185185185185, 'fare+sum': 1392.8299996852877}, {'geohash': 'dp3wnn73zqu', 'count': 107, 'extras+avg': 0.9112149532710281, 'fare+sum': 1241.1899988651276}, {'geohash': 'dp3tenvtp48', 'count': 97, 'extras+avg': 1.922680412371134, 'fare+sum': 2773.190001964569}, {'geohash': 'dp3wq64nqmk', 'count': 93, 'extras+avg': 0.7419354838709677, 'fare+sum': 853.4499983787537}, {'geohash': 'dp3wmv18ff9', 'count': 73, 'extras+avg': 0.4863013698630137, 'fare+sum': 644.2300004959106}, {'geohash': 'dp3wjrf55xz', 'count': 72, 'extras+avg': 0.4583333333333333, 'fare+sum': 570.0500001907349}, {'geohash': 'dp3wn46j99j', 'count': 71, 'extras+avg': 0.823943661971831, 'fare+sum': 1019.849999666214}, {'geohash': 'dp3qz6r2b06', 'count': 70, 'extras+avg': 1.7285714285714286, 'fare+sum': 2008.1300034523015}, {'geohash': 'dp3wqj00yzg', 'count': 66, 'extras+avg': 0.4772727272727273, 'fare+sum': 561.7000007629395}, {'geohash': 'dp3wqh0t6vf', 'count': 64, 'extras+avg': 0.7109375, 'fare+sum': 574.3400025367737}, {'geohash': 'dp3wssqede1', 'count': 63, 'extras+avg': 0.3253968253968254, 'fare+sum': 770.3499956130979}, {'geohash': 'dp3wmkx3cnh', 'count': 62, 'extras+avg': 0.49193548387096775, 'fare+sum': 655.4200019836427}, {'geohash': 'dp3wu97ghfc', 'count': 61, 'extras+avg': 0.5081967213114754, 'fare+sum': 909.520004272461}, {'geohash': 'dp3wmgsnxze', 'count': 59, 'extras+avg': 0.576271186440678, 'fare+sum': 543.9500012397766}, {'geohash': 'dp3wev3tr6s', 'count': 58, 'extras+avg': 0.5344827586206896, 'fare+sum': 829.9500012397764}, {'geohash': 'dp3wmutpkf5', 'count': 55, 'extras+avg': 0.6454545454545455, 'fare+sum': 492.84000062942505}, {'geohash': 'dp3wm7ke6f2', 'count': 55, 'extras+avg': 0.6590909090909091, 'fare+sum': 430.49000048637396}, {'geohash': 'dp3tyb3hppp', 'count': 52, 'extras+avg': 1.0480769230769231, 'fare+sum': 1270.749999523163}, {'geohash': 'dp3wjtu65n9', 'count': 50, 'extras+avg': 0.72, 'fare+sum': 545.8399968147276}, {'geohash': 'dp3wmgwqmz7', 'count': 49, 'extras+avg': 0.7040816326530612, 'fare+sum': 367.1999993324279}, {'geohash': 'dp3wmzdvb4t', 'count': 49, 'extras+avg': 0.5612244897959183, 'fare+sum': 516.3499989509581}, {'geohash': 'dp3wvp8ec13', 'count': 47, 'extras+avg': 0.3191489361702128, 'fare+sum': 745.7400002479551}, {'geohash': 'dp3wjyku25p', 'count': 47, 'extras+avg': 0.5212765957446809, 'fare+sum': 341.0399994850159}, {'geohash': 'dp3wkuub31m', 'count': 47, 'extras+avg': 0.776595744680851, 'fare+sum': 467.9999995231626}, {'geohash': 'dp3ws4dwkwj', 'count': 41, 'extras+avg': 0.4268292682926829, 'fare+sum': 508.1399979591372}, {'geohash': 'dp3wuqnkyh7', 'count': 39, 'extras+avg': 0.5256410256410257, 'fare+sum': 644.4400033950803}, {'geohash': 'dp3wn5ugf0x', 'count': 39, 'extras+avg': 1.0384615384615385, 'fare+sum': 557.0899982452393}, {'geohash': 'dp3wm6m67vm', 'count': 37, 'extras+avg': 0.7567567567567568, 'fare+sum': 372.6999988555908}, {'geohash': 'dp3wtkh4fu4', 'count': 35, 'extras+avg': 0.8857142857142857, 'fare+sum': 426.19000148773176}, {'geohash': 'dp3wt2yq2kv', 'count': 33, 'extras+avg': 0.8636363636363636, 'fare+sum': 416.8499965667726}, {'geohash': 'dp3wt8cyt6d', 'count': 33, 'extras+avg': 0.9393939393939394, 'fare+sum': 414.24999713897694}, {'geohash': 'dp3wmqk71e5', 'count': 31, 'extras+avg': 0.5, 'fare+sum': 302.10000085830694}, {'geohash': 'dp3wgb51ex0', 'count': 30, 'extras+avg': 0.5, 'fare+sum': 425.1499981880186}, {'geohash': 'dp3tfb057xz', 'count': 29, 'extras+avg': 1.9137931034482758, 'fare+sum': 889.6900062561035}, {'geohash': 'dp3wj4d7mx4', 'count': 28, 'extras+avg': 0.2857142857142857, 'fare+sum': 355.3799991607667}, {'geohash': 'dp3wt7mvvsq', 'count': 27, 'extras+avg': 0.6666666666666666, 'fare+sum': 272.27999830245966}, {'geohash': 'dp3wmvmhd81', 'count': 23, 'extras+avg': 0.34782608695652173, 'fare+sum': 214.19999909400934}, {'geohash': 'dp3wt9yxeqk', 'count': 23, 'extras+avg': 0.6086956521739131, 'fare+sum': 250.60000228881842}, {'geohash': 'dp3wmxtkjcz', 'count': 22, 'extras+avg': 0.25, 'fare+sum': 188.48999881744376}, {'geohash': 'dp3wtsex7wf', 'count': 22, 'extras+avg': 0.5681818181818182, 'fare+sum': 267.62999963760376}, {'geohash': 'dp3wtdxsc4y', 'count': 21, 'extras+avg': 0.5, 'fare+sum': 252.9399991035461}, {'geohash': 'dp3wt6q0dwc', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 245.3500015735625}, {'geohash': 'dp3wm5s7dt0', 'count': 21, 'extras+avg': 0.6190476190476191, 'fare+sum': 208.59999990463248}, {'geohash': 'dp3wmx9ux20', 'count': 21, 'extras+avg': 0.8571428571428571, 'fare+sum': 171.84999895095828}, {'geohash': 'dp3wtbcrxtp', 'count': 20, 'extras+avg': 0.575, 'fare+sum': 252.5000004768371}, {'geohash': 'dp3whzz2ymk', 'count': 20, 'extras+avg': 0.8, 'fare+sum': 222.50000047683713}, {'geohash': 'dp3wt668394', 'count': 20, 'extras+avg': 0.875, 'fare+sum': 173.5499982833863}, {'geohash': 'dp3wte3m5p1', 'count': 20, 'extras+avg': 1.075, 'fare+sum': 256.6000008583069}, {'geohash': 'dp3wmrwkn1z', 'count': 20, 'extras+avg': 0.7, 'fare+sum': 207.5000023841858}, {'geohash': 'dp3wb69xqk7', 'count': 19, 'extras+avg': 2.236842105263158, 'fare+sum': 320.6000003814697}, {'geohash': 'dp3typy50z4', 'count': 19, 'extras+avg': 0.6842105263157895, 'fare+sum': 261.8500003814699}, {'geohash': 'dp3wtwfx6th', 'count': 18, 'extras+avg': 0.16666666666666666, 'fare+sum': 233.08999872207642}, {'geohash': 'dp3wj8015pw', 'count': 17, 'extras+avg': 0.7941176470588235, 'fare+sum': 322.1999998092651}, {'geohash': 'dp3whykby7j', 'count': 17, 'extras+avg': 0.4117647058823529, 'fare+sum': 192.2899985313415}, {'geohash': 'dp3wm58g28w', 'count': 17, 'extras+avg': 1.8529411764705883, 'fare+sum': 195.9900012016297}, {'geohash': 'dp3wcgnsqn5', 'count': 17, 'extras+avg': 0.8529411764705882, 'fare+sum': 277.4400010108947}, {'geohash': 'dp3wmw64hvn', 'count': 16, 'extras+avg': 0.90625, 'fare+sum': 156.7999997138977}, {'geohash': 'dp3wtktgcj9', 'count': 16, 'extras+avg': 0.78125, 'fare+sum': 238.1399984359742}, {'geohash': 'dp3wmpsuwum', 'count': 15, 'extras+avg': 0.9333333333333333, 'fare+sum': 142.7399997711182}, {'geohash': 'dp3wdvkxutd', 'count': 15, 'extras+avg': 0.5, 'fare+sum': 298.20000123977655}, {'geohash': 'dp3wjc4gu2m', 'count': 15, 'extras+avg': 0.5333333333333333, 'fare+sum': 242.0000004768371}, {'geohash': 'dp3wkvpynbj', 'count': 14, 'extras+avg': 0.6428571428571429, 'fare+sum': 150.40000104904186}, {'geohash': 'dp3wtqjpbwc', 'count': 14, 'extras+avg': 0.6785714285714286, 'fare+sum': 183.70000171661368}, {'geohash': 'dp3wmrdgt5w', 'count': 14, 'extras+avg': 3.892857142857143, 'fare+sum': 132.29000091552737}, {'geohash': 'dp3wtetbxdz', 'count': 14, 'extras+avg': 0.42857142857142855, 'fare+sum': 157.30000066757194}, {'geohash': 'dp3wkgt4ycx', 'count': 13, 'extras+avg': 0.9615384615384616, 'fare+sum': 145.6999998092651}, {'geohash': 'dp3wt4ppb6x', 'count': 13, 'extras+avg': 0.7692307692307693, 'fare+sum': 207.29999971389762}, {'geohash': 'dp3wt9hzkd6', 'count': 13, 'extras+avg': 0.11538461538461539, 'fare+sum': 126.45000052452089}, {'geohash': 'dp3tyen6sfz', 'count': 13, 'extras+avg': 0.6153846153846154, 'fare+sum': 245.2000007629395}, {'geohash': 'dp3wtt6hk08', 'count': 12, 'extras+avg': 0.4166666666666667, 'fare+sum': 119.43999767303464}, {'geohash': 'dp3wmtjb6gz', 'count': 12, 'extras+avg': 0.16666666666666666, 'fare+sum': 85.99999952316283}, {'geohash': 'dp3wtd9ecvn', 'count': 12, 'extras+avg': 0.5833333333333334, 'fare+sum': 130.84999990463263}, {'geohash': 'dp3wtkd72qm', 'count': 12, 'extras+avg': 0.3333333333333333, 'fare+sum': 144.84999942779535}, {'geohash': 'dp3wt9cx55j', 'count': 12, 'extras+avg': 0.5416666666666666, 'fare+sum': 126.49999904632557}, {'geohash': 'dp3wfdnbrt4', 'count': 11, 'extras+avg': 0.2727272727272727, 'fare+sum': 166.75000190734872}, {'geohash': 'dp3wkzpt5jz', 'count': 11, 'extras+avg': 0.6818181818181818, 'fare+sum': 174.95000457763675}, {'geohash': 'dp3w7getd7n', 'count': 11, 'extras+avg': 1.0454545454545454, 'fare+sum': 150.6999988555908}, {'geohash': 'dp3wtnpxkus', 'count': 10, 'extras+avg': 0.25, 'fare+sum': 115.89999914169309}, {'geohash': 'dp3wt2ftzw0', 'count': 10, 'extras+avg': 0.95, 'fare+sum': 101.59999990463251}, {'geohash': 'dp3wt45rrt4', 'count': 9, 'extras+avg': 0.5, 'fare+sum': 82.64999914169313}, {'geohash': 'dp3tukeeu6j', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 204.09999847412115}, {'geohash': 'dp3wteecp45', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 102.03999948501597}, {'geohash': 'dp3wv0vhebk', 'count': 9, 'extras+avg': 0.6111111111111112, 'fare+sum': 132.80000114440915}, {'geohash': 'dp3wt76mk0s', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 93.04000043869009}, {'geohash': 'dp3wmem3mnr', 'count': 9, 'extras+avg': 0.6666666666666666, 'fare+sum': 64.95000076293945}, {'geohash': 'dp3wthghmsk', 'count': 8, 'extras+avg': 1.3125, 'fare+sum': 142.09999752044666}, {'geohash': 'dp3wt9uq3sc', 'count': 8, 'extras+avg': 0.8125, 'fare+sum': 119.2000017166138}, {'geohash': 'dp3wktydzjc', 'count': 8, 'extras+avg': 0.75, 'fare+sum': 101.80000019073483}, {'geohash': 'dp3wmezwm4j', 'count': 8, 'extras+avg': 0.125, 'fare+sum': 63.199999332428}, {'geohash': 'dp3wkvuvnyy', 'count': 8, 'extras+avg': 1.5625, 'fare+sum': 101.40000152587892}, {'geohash': 'dp3wm4k3rqe', 'count': 8, 'extras+avg': 0.0, 'fare+sum': 53.95000028610228}, {'geohash': 'dp3wkysfqjw', 'count': 8, 'extras+avg': 0.5, 'fare+sum': 104.24999904632563}, {'geohash': 'dp3wtptd7qp', 'count': 7, 'extras+avg': 0.7142857142857143, 'fare+sum': 105.49000120162967}, {'geohash': 'dp3wsbvzsnz', 'count': 7, 'extras+avg': 0.7857142857142857, 'fare+sum': 92.34999847412101}, {'geohash': 'dp3wt8s97k0', 'count': 7, 'extras+avg': 0.35714285714285715, 'fare+sum': 54.75000047683715}, {'geohash': 'dp3wjfdpf75', 'count': 7, 'extras+avg': 0.8571428571428571, 'fare+sum': 99.14000082016}, {'geohash': 'dp3wsgpygh5', 'count': 7, 'extras+avg': 0.42857142857142855, 'fare+sum': 55.55000066757199}, {'geohash': 'dp3ty5yd5fs', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 126.9500007629395}, {'geohash': 'dp3wt5cs342', 'count': 7, 'extras+avg': 0.5714285714285714, 'fare+sum': 82.74999999999991}, {'geohash': 'dp3twzxzkg4', 'count': 7, 'extras+avg': 1.1428571428571428, 'fare+sum': 128.9999971389769}, {'geohash': 'dp3wt0gu9xv', 'count': 7, 'extras+avg': 0.2857142857142857, 'fare+sum': 74.79999923706055}, {'geohash': 'dp3wv2zn01n', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 74.10000038146975}, {'geohash': 'dp3twtx7d71', 'count': 6, 'extras+avg': 0.6666666666666666, 'fare+sum': 178.2999992370606}, {'geohash': 'dp3w5uqm28u', 'count': 6, 'extras+avg': 1.1666666666666667, 'fare+sum': 109.7499990463257}, {'geohash': 'dp3tv70e1mg', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 119.2500000000001}, {'geohash': 'dp3wkxt9j7x', 'count': 6, 'extras+avg': 1.0833333333333333, 'fare+sum': 83.89999914169313}, {'geohash': 'dp3wegqnf58', 'count': 6, 'extras+avg': 0.5, 'fare+sum': 70.29999923706049}, {'geohash': 'dp3wgfcskm5', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 37.34999942779544}, {'geohash': 'dp3wh08d7e4', 'count': 6, 'extras+avg': 0.16666666666666666, 'fare+sum': 115.70000076293942}, {'geohash': 'dp3wm6219ng', 'count': 6, 'extras+avg': 0.8333333333333334, 'fare+sum': 50.5}, {'geohash': 'dp3wubf5yuc', 'count': 6, 'extras+avg': 0.0, 'fare+sum': 62.74999952316281}, {'geohash': 'dp3wtn5h7fs', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 58.45000028610226}, {'geohash': 'dp3wt5yuczq', 'count': 5, 'extras+avg': 0.8, 'fare+sum': 53.64999961853038}, {'geohash': 'dp3wtmkbgmh', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.650000095367446}, {'geohash': 'dp3twxdxnh5', 'count': 5, 'extras+avg': 0.7, 'fare+sum': 105.2500000000001}, {'geohash': 'dp3wghb265u', 'count': 5, 'extras+avg': 1.0, 'fare+sum': 67.13000011444086}, {'geohash': 'dp3tx4rqy62', 'count': 5, 'extras+avg': 0.5, 'fare+sum': 87.85000085830691}, {'geohash': 'dp3ws8v7yvp', 'count': 5, 'extras+avg': 0.2, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w71cyrzk', 'count': 5, 'extras+avg': 0.95, 'fare+sum': 73.34999895095817}, {'geohash': 'dp3wdbe5gxf', 'count': 5, 'extras+avg': 0.0, 'fare+sum': 70.6499986648559}, {'geohash': 'dp3wkg9dm4p', 'count': 5, 'extras+avg': 0.4, 'fare+sum': 48.35000038146973}, {'geohash': 'dp3wtrjrzu5', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 64.5500001907349}, {'geohash': 'dp3wufpw530', 'count': 4, 'extras+avg': 1.125, 'fare+sum': 50.38999986648564}, {'geohash': 'dp3wsuu5sue', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.59999990463259}, {'geohash': 'dp3wswntt2b', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 56.99000024795523}, {'geohash': 'dp3wthwdzxt', 'count': 4, 'extras+avg': 1.625, 'fare+sum': 73.99999999999997}, {'geohash': 'dp3wt55r72t', 'count': 4, 'extras+avg': 0.75, 'fare+sum': 32.39999961853028}, {'geohash': 'dp3wmhu5ctf', 'count': 4, 'extras+avg': 1.0, 'fare+sum': 31.20000028610233}, {'geohash': 'dp3whpyd27r', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 37.19999980926511}, {'geohash': 'dp3wjut7ekr', 'count': 4, 'extras+avg': 0.875, 'fare+sum': 59.65000009536743}, {'geohash': 'dp3wkf3b1yq', 'count': 4, 'extras+avg': 0.5, 'fare+sum': 32.40000009536743}, {'geohash': 'dp3wm42cjew', 'count': 4, 'extras+avg': 1.25, 'fare+sum': 37.40000009536741}, {'geohash': 'dp3wkz3kkfx', 'count': 4, 'extras+avg': 0.0, 'fare+sum': 41.1999998092651}, {'geohash': 'dp3we81e02s', 'count': 4, 'extras+avg': 0.25, 'fare+sum': 61.0500001907349}, {'geohash': 'dp3wsfpyy6v', 'count': 3, 'extras+avg': 1.3333333333333333, 'fare+sum': 53.19999980926514}, {'geohash': 'dp3whz8ckwj', 'count': 3, 'extras+avg': 1.0, 'fare+sum': 25.350000381469698}, {'geohash': 'dp3wmwtthku', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 25.75}, {'geohash': 'dp3wszebetk', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 40.950000286102274}, {'geohash': 'dp3wsxy6w2c', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 42.3500003814697}, {'geohash': 'dp3wcxrbnde', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 80.1499996185302}, {'geohash': 'dp3wsuzevzs', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 34.54999971389777}, {'geohash': 'dp3wsrz4m5x', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 38.550000190734906}, {'geohash': 'dp3tuyyufwe', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 32.55000019073486}, {'geohash': 'dp3wk7z03ne', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 31.350000381469762}, {'geohash': 'dp3tu2tkhby', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 58.2000007629394}, {'geohash': 'dp3tkcsuwwm', 'count': 3, 'extras+avg': 2.3333333333333335, 'fare+sum': 69.10000157356262}, {'geohash': 'dp3wksvuq8x', 'count': 3, 'extras+avg': 0.0, 'fare+sum': 38.75}, {'geohash': 'dp3wkubssh2', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 48.80000066757207}, {'geohash': 'dp3wv2cugbj', 'count': 3, 'extras+avg': 0.3333333333333333, 'fare+sum': 43.1499996185303}, {'geohash': 'dp3ws2fffd5', 'count': 3, 'extras+avg': 0.6666666666666666, 'fare+sum': 35.7500009536743}, {'geohash': 'dp3tmr69s5b', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 28.2999992370605}, {'geohash': 'dp3wtcfrh9q', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 14.3000001907349}, {'geohash': 'dp3wvhu5k5q', 'count': 2, 'extras+avg': 1.25, 'fare+sum': 20.29999971389773}, {'geohash': 'dp3wjqs0r8e', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 21.29999971389773}, {'geohash': 'dp3wv5s36fh', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 23.90000057220464}, {'geohash': 'dp3tdv8ztqw', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 71.6500015258789}, {'geohash': 'dp3wv4hysqg', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 29.10000038146977}, {'geohash': 'dp3teeznw6g', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 58.950000762939496}, {'geohash': 'dp3wuynj9sh', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.899999618530302}, {'geohash': 'dp3tskmfwug', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 41.84999990463257}, {'geohash': 'dp3w9ujs5kq', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 45.1000003814698}, {'geohash': 'dp3tyc54y1r', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 67.9000015258789}, {'geohash': 'dp3ty0nd4hp', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 64.4500007629395}, {'geohash': 'dp3twxxzxw2', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 37.5}, {'geohash': 'dp3tuz83ukf', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 21.8999996185303}, {'geohash': 'dp3wuqp7qhu', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 6.5}, {'geohash': 'dp3wu2zhj8j', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wt5nzsq4', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 11.09999990463257}, {'geohash': 'dp3wvq8x6rs', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 32.2999992370606}, {'geohash': 'dp3wkxd5k13', 'count': 2, 'extras+avg': 0.5, 'fare+sum': 26.10000038146973}, {'geohash': 'dp3wt0zmc4h', 'count': 2, 'extras+avg': 1.5, 'fare+sum': 36.1000003814697}, {'geohash': 'dp3wssyg41q', 'count': 2, 'extras+avg': 1.0, 'fare+sum': 43.700000762939396}, {'geohash': 'dp3wksf7uew', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 19.5}, {'geohash': 'dp3ws1404ce', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 16.30000019073486}, {'geohash': 'dp3wkw82yk6', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 26.100000381469698}, {'geohash': 'dp3wkrdbr87', 'count': 2, 'extras+avg': 1.75, 'fare+sum': 28.0999994277954}, {'geohash': 'dp3wsecd2b4', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 24.300000190734842}, {'geohash': 'dp3wmwj8pj1', 'count': 2, 'extras+avg': 0.0, 'fare+sum': 20.94999980926514}, {'geohash': 'dp3wkew1g63', 'count': 2, 'extras+avg': 0.25, 'fare+sum': 20.85000038146973}, {'geohash': 'dp3wsejmc51', 'count': 2, 'extras+avg': 0.75, 'fare+sum': 20.100000381469762}, {'geohash': 'dp3wu6pn7kn', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wu8ubvf8', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3tgerw58f', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 17.8500003814697}, {'geohash': 'dp3tjj3k6bz', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.8499984741211}, {'geohash': 'dp3tjf3xe70', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.75}, {'geohash': 'dp3wubzg5j6', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 14.6499996185303}, {'geohash': 'dp3thn34q2z', 'count': 1, 'extras+avg': 3.0, 'fare+sum': 68.25}, {'geohash': 'dp3wugrpsrq', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 21.0499992370605}, {'geohash': 'dp3tkpsdwvq', 'count': 1, 'extras+avg': 4.0, 'fare+sum': 72.0}, {'geohash': 'dp3wk8yk7q8', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3wuuyg1b1', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.25}, {'geohash': 'dp3wusufn6f', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3tq06w7x6', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 36.25}, {'geohash': 'dp3wktf7ces', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3tgb1jvb3', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3ws0z4xd9', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 12.4499998092651}, {'geohash': 'dp3wmjbt8e8', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 9.64999961853027}, {'geohash': 'dp3wv6m81ux', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.25}, {'geohash': 'dp3wv7hrne6', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 26.25}, {'geohash': 'dp3wvp426cv', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 11.8500003814697}, {'geohash': 'dp3qzwzu1eg', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 43.6500015258789}, {'geohash': 'dp3wsev5j2b', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.25}, {'geohash': 'dp3tqnxfrfm', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.4499998092651}, {'geohash': 'dp3tq8kgu9q', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 32.8499984741211}, {'geohash': 'dp3wkcp79m2', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 7.44999980926514}, {'geohash': 'dp3wk0bwppf', 'count': 1, 'extras+avg': 5.0, 'fare+sum': 39.75}, {'geohash': 'dp3wked9fyb', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.8500003814697}, {'geohash': 'dp3wjnywf86', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 9.25}, {'geohash': 'dp3wjnhfpwk', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 18.8500003814697}, {'geohash': 'dp3wjmh2p7t', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 8.25}, {'geohash': 'dp3wj2hgm6g', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkmng94z', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 18.0499992370605}, {'geohash': 'dp3wey45q4f', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wewh6cbu', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 20.75}, {'geohash': 'dp3weuf2gj2', 'count': 1, 'extras+avg': 9.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3wsyhn0kv', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 6.84999990463257}, {'geohash': 'dp3wknx81s8', 'count': 1, 'extras+avg': 1.5, 'fare+sum': 15.8500003814697}, {'geohash': 'dp3wd0grved', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 35.75}, {'geohash': 'dp3wsw0vp1p', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.25}, {'geohash': 'dp3wkpx2j8d', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 14.8500003814697}, {'geohash': 'dp3wsn3q5ed', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 3.84999990463257}, {'geohash': 'dp3tw4zbs17', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.44999980926514}, {'geohash': 'dp3wsgu5xxt', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 28.0499992370605}, {'geohash': 'dp3wkrqy37c', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 6.05000019073486}, {'geohash': 'dp3wsghq6py', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 13.6499996185303}, {'geohash': 'dp3tttk9vcc', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 19.25}, {'geohash': 'dp3wsfhqv3b', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 29.0499992370605}, {'geohash': 'dp3trhxkzz3', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 46.0}, {'geohash': 'dp3wtp0w2eu', 'count': 1, 'extras+avg': 1.0, 'fare+sum': 4.05000019073486}, {'geohash': 'dp3tqzm9d4v', 'count': 1, 'extras+avg': 2.0, 'fare+sum': 57.25}, {'geohash': 'dp3wn15e6s4', 'count': 1, 'extras+avg': 0.0, 'fare+sum': 0.0}], 'visualization': 'Geo Map'}

    TS_ONE_GROUP_ONE_METRIC_TWO_FUNC_QUERY_RESULT = {
        'data': [
            {
                'group': ['2008-01-01 00:00:00'],
                'current': {
                    'count': 172456,
                    'metrics': {
                        'commission': {
                            'avg': 96.34,
                            'sum': 16614814.65
                        }
                    }
                }
            }
        ],
        'visualization': 'Bars'
    }
    TS_ONE_GROUP_ONE_QUERY_POINT_IN_NAME_RESULT = {'data': [{'group': ['All rock and pop music concerts'], 'current': {'count': 711, 'metrics': {'catid.1': {'sum': 6399.0}}}}], 'visualization': 'Bars'}
    TS_DISK_VISUALIZATION = {
        "data": [
            {
                "group": [
                    0
                ],
                "current": {
                    "count": 976,
                    "metrics": {
                        "easting_m": {
                            "sum": 244736657.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    1
                ],
                "current": {
                    "count": 879,
                    "metrics": {
                        "easting_m": {
                            "sum": 231838969.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    2
                ],
                "current": {
                    "count": 645,
                    "metrics": {
                        "easting_m": {
                            "sum": 177190308.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    3
                ],
                "current": {
                    "count": 549,
                    "metrics": {
                        "easting_m": {
                            "sum": 144888660.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    4
                ],
                "current": {
                    "count": 485,
                    "metrics": {
                        "easting_m": {
                            "sum": 129741036.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    5
                ],
                "current": {
                    "count": 510,
                    "metrics": {
                        "easting_m": {
                            "sum": 154114400.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    6
                ],
                "current": {
                    "count": 653,
                    "metrics": {
                        "easting_m": {
                            "sum": 208813231.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    7
                ],
                "current": {
                    "count": 876,
                    "metrics": {
                        "easting_m": {
                            "sum": 276302962.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    8
                ],
                "current": {
                    "count": 1207,
                    "metrics": {
                        "easting_m": {
                            "sum": 355581080.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    9
                ],
                "current": {
                    "count": 1377,
                    "metrics": {
                        "easting_m": {
                            "sum": 431933609.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    10
                ],
                "current": {
                    "count": 1525,
                    "metrics": {
                        "easting_m": {
                            "sum": 465358837.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    11
                ],
                "current": {
                    "count": 1641,
                    "metrics": {
                        "easting_m": {
                            "sum": 489143208.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    12
                ],
                "current": {
                    "count": 1671,
                    "metrics": {
                        "easting_m": {
                            "sum": 508642853.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    13
                ],
                "current": {
                    "count": 1780,
                    "metrics": {
                        "easting_m": {
                            "sum": 498389849.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    14
                ],
                "current": {
                    "count": 1805,
                    "metrics": {
                        "easting_m": {
                            "sum": 518877107.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    15
                ],
                "current": {
                    "count": 1871,
                    "metrics": {
                        "easting_m": {
                            "sum": 516457990.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    16
                ],
                "current": {
                    "count": 1880,
                    "metrics": {
                        "easting_m": {
                            "sum": 535832636.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    17
                ],
                "current": {
                    "count": 1942,
                    "metrics": {
                        "easting_m": {
                            "sum": 510790519.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    18
                ],
                "current": {
                    "count": 2187,
                    "metrics": {
                        "easting_m": {
                            "sum": 584813995.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    19
                ],
                "current": {
                    "count": 1950,
                    "metrics": {
                        "easting_m": {
                            "sum": 491509808.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    20
                ],
                "current": {
                    "count": 1822,
                    "metrics": {
                        "easting_m": {
                            "sum": 467875864.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    21
                ],
                "current": {
                    "count": 1494,
                    "metrics": {
                        "easting_m": {
                            "sum": 352830937.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    22
                ],
                "current": {
                    "count": 1350,
                    "metrics": {
                        "easting_m": {
                            "sum": 348890574.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    23
                ],
                "current": {
                    "count": 1172,
                    "metrics": {
                        "easting_m": {
                            "sum": 289768473.0
                        },
                        "hour_of_call": {
                            "unique": 1.0
                        }
                    }
                }
            }
        ],
        "visualization": "Disk"
    }
    TS_TREE_VISUALIZATION = {
        'data': [
            {'group': ['All non-musical theatre'],
             'current': {'count': 39223, 'metrics': {'pricepaid': {'sum': 25538940.0}}}},
            {'group': ['All opera and light opera'],
             'current': {'count': 9914, 'metrics': {'pricepaid': {'sum': 6455301.0}}}},
            {'group': ['All rock and pop music concerts'],
             'current': {'count': 97582, 'metrics': {'pricepaid': {'sum': 62434243.0}}}},
            {'group': ['Musical theatre'], 'current': {'count': 25737, 'metrics': {'pricepaid': {'sum': 16336947.0}}}}
        ], 'visualization': 'Tree'
    }
    TS_SANKEY_VISUALIZATION = {
        'data': [
            {'group': ['Aaron', 'Banks'], 'current': {'count': 2, 'metrics': {'commission': {'sum': 82.65}}}},
            {'group': ['Aaron', 'Booth'], 'current': {'count': 1, 'metrics': {'commission': {'sum': 5.25}}}},
            {'group': ['Aaron', 'Browning'], 'current': {'count': 2, 'metrics': {'commission': {'sum': 315.0}}}},
            {'group': ['Aaron', 'Burnett'], 'current': {'count': 7, 'metrics': {'commission': {'sum': 303.0}}}},
            {'group': ['Aaron', 'Casey'], 'current': {'count': 4, 'metrics': {'commission': {'sum': 283.5}}}},
            {'group': ['Aaron', 'Cash'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 268.5}}}},
            {'group': ['Aaron', 'Castro'], 'current': {'count': 6, 'metrics': {'commission': {'sum': 504.3}}}},
            {'group': ['Aaron', 'Dickerson'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 335.25}}}},
            {'group': ['Aaron', 'Dixon'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 98.7}}}},
            {'group': ['Aaron', 'Dotson'], 'current': {'count': 6, 'metrics': {'commission': {'sum': 584.25}}}},
            {'group': ['Aaron', 'Downs'], 'current': {'count': 2, 'metrics': {'commission': {'sum': 80.55}}}},
            {'group': ['Aaron', 'Evans'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 615.45}}}},
            {'group': ['Aaron', 'Forbes'], 'current': {'count': 6, 'metrics': {'commission': {'sum': 373.8}}}},
            {'group': ['Aaron', 'Fowler'], 'current': {'count': 5, 'metrics': {'commission': {'sum': 528.45}}}},
            {'group': ['Aaron', 'Garrison'], 'current': {'count': 8, 'metrics': {'commission': {'sum': 184.05}}}},
            {'group': ['Aaron', 'Glover'], 'current': {'count': 6, 'metrics': {'commission': {'sum': 250.35}}}},
            {'group': ['Aaron', 'Hanson'], 'current': {'count': 6, 'metrics': {'commission': {'sum': 1476.6}}}},
            {'group': ['Aaron', 'Hatfield'], 'current': {'count': 5, 'metrics': {'commission': {'sum': 761.55}}}},
            {'group': ['Aaron', 'Hoffman'], 'current': {'count': 2, 'metrics': {'commission': {'sum': 99.9}}}},
            {'group': ['Aaron', 'Holland'], 'current': {'count': 1, 'metrics': {'commission': {'sum': 38.85}}}},
            {'group': ['Aaron', 'Houston'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 121.8}}}},
            {'group': ['Aaron', 'Hunt'], 'current': {'count': 1, 'metrics': {'commission': {'sum': 28.2}}}},
            {'group': ['Aaron', 'Le'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 723.0}}}},
            {'group': ['Aaron', 'Lee'], 'current': {'count': 4, 'metrics': {'commission': {'sum': 292.5}}}},
            {'group': ['Aaron', 'Mcconnell'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 124.35}}}},
            {'group': ['Aaron', 'Mcdonald'], 'current': {'count': 4, 'metrics': {'commission': {'sum': 283.65}}}},
            {'group': ['Aaron', 'Mckenzie'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 375.0}}}},
            {'group': ['Aaron', 'Miranda'], 'current': {'count': 11, 'metrics': {'commission': {'sum': 1898.7}}}},
            {'group': ['Aaron', 'Moran'], 'current': {'count': 6, 'metrics': {'commission': {'sum': 684.6}}}},
            {'group': ['Aaron', 'Nichols'], 'current': {'count': 7, 'metrics': {'commission': {'sum': 604.95}}}},
            {'group': ['Aaron', 'Nicholson'], 'current': {'count': 5, 'metrics': {'commission': {'sum': 694.8}}}},
            {'group': ['Aaron', 'Richards'], 'current': {'count': 5, 'metrics': {'commission': {'sum': 2182.2}}}},
            {'group': ['Aaron', 'Small'], 'current': {'count': 1, 'metrics': {'commission': {'sum': 62.7}}}},
            {'group': ['Aaron', 'Smith'], 'current': {'count': 9, 'metrics': {'commission': {'sum': 643.35}}}},
            {'group': ['Aaron', 'Snow'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 133.65}}}},
            {'group': ['Aaron', 'Snyder'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 121.95}}}},
            {'group': ['Aaron', 'Strickland'], 'current': {'count': 8, 'metrics': {'commission': {'sum': 570.3}}}},
            {'group': ['Aaron', 'Sykes'], 'current': {'count': 2, 'metrics': {'commission': {'sum': 818.55}}}},
            {'group': ['Aaron', 'Trevino'], 'current': {'count': 11, 'metrics': {'commission': {'sum': 513.3}}}},
            {'group': ['Aaron', 'Wallace'], 'current': {'count': 6, 'metrics': {'commission': {'sum': 667.35}}}},
            {'group': ['Aaron', 'Warren'], 'current': {'count': 2, 'metrics': {'commission': {'sum': 109.65}}}},
            {'group': ['Aaron', 'Washington'], 'current': {'count': 4, 'metrics': {'commission': {'sum': 465.9}}}},
            {'group': ['Abbot', 'Barker'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 154.8}}}},
            {'group': ['Abbot', 'Barrera'], 'current': {'count': 6, 'metrics': {'commission': {'sum': 154.5}}}},
            {'group': ['Abbot', 'Bell'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 219.15}}}},
            {'group': ['Abbot', 'Blanchard'], 'current': {'count': 15, 'metrics': {'commission': {'sum': 895.5}}}},
            {'group': ['Abbot', 'Cantrell'], 'current': {'count': 3, 'metrics': {'commission': {'sum': 282.9}}}},
            {'group': ['Abbot', 'Cervantes'], 'current': {'count': 7, 'metrics': {'commission': {'sum': 557.55}}}},
            {'group': ['Abbot', 'Charles'], 'current': {'count': 5, 'metrics': {'commission': {'sum': 733.2}}}},
            {'group': ['Abbot', 'Cole'], 'current': {'count': 11, 'metrics': {'commission': {'sum': 453.45}}}}
        ], 'visualization': 'Sankey'
    }
    TS_SUNBURST_VISUALIZATION = {
        'data': [
            {'group': ['All non-musical theatre'], 'current': {'count': 39223, 'metrics': {}}},
            {'group': ['All opera and light opera'], 'current': {'count': 9914, 'metrics': {}}},
            {'group': ['All rock and pop music concerts'], 'current': {'count': 97582, 'metrics': {}}},
            {'group': ['Musical theatre'], 'current': {'count': 25737, 'metrics': {}}}
        ],
        'visualization': 'Sunburst'
    }
    TS_SLICER_BETWEEN_FILTER_VISUALIZATION = {
        "data": [
            {
                "group": [None
                ],
                "current": {
                    "count": 55,
                    "metrics": {
                        "extras": {
                            "unique": 6.0
                        },
                        "company": {
                            "unique": 0.0
                        }
                    }
                }
            },
            {
                "group": [
                    "Blue Ribbon Taxi Association Inc."
                ],
                "current": {
                    "count": 11,
                    "metrics": {
                        "extras": {
                            "unique": 3.0
                        },
                        "company": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    "Choice Taxi Association"
                ],
                "current": {
                    "count": 4,
                    "metrics": {
                        "extras": {
                            "unique": 2.0
                        },
                        "company": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    "Dispatch Taxi Affiliation"
                ],
                "current": {
                    "count": 24,
                    "metrics": {
                        "extras": {
                            "unique": 4.0
                        },
                        "company": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    "Northwest Management LLC"
                ],
                "current": {
                    "count": 8,
                    "metrics": {
                        "extras": {
                            "unique": 4.0
                        },
                        "company": {
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    "Taxi Affiliation Services"
                ],
                "current": {
                    "count": 44,
                    "metrics": {
                        "extras": {
                            "unique": 6.0
                        },
                        "company": {
                            "unique": 1.0
                        }
                    }
                }
            }
        ],
        "visualization": "Slicer"
    }

    TS_MULTIMETRIC_GAUGE_VISUALIZATION = {
        'data': [
            {
                'group': [],
                'current': {'count': 172456, 'metrics': {'commission': {'avg': 96.34}, 'pricepaid': {'avg': 642.28}}}
            }
        ],
        'visualization': 'Gauge'
    }

    TS_RANGE_FILTER_VISUALIZATION = {
        'data': [
            {'group': [], 'current': {
                'count': 172456,
                'metrics': {
                    'commission': {'max': 1893.6, 'min': 3.0},
                    'qtysold': {'max': 8.0, 'min': 1.0},
                    'venueseats': {'max': 91704.0, 'min': 0.0}
                }
            }
             }
        ],
        'visualization': 'Range Filter'
    }

    TTN_MULTI_METRIC_AREA_LINE = {
        "data": [
            {
                "group": [
                    "0"
                ],
                "current": {
                    "count": 678,
                    "metrics": {
                        "Age": {
                            "sum": 16765.0
                        },
                        "Fare": {
                            "sum": 17347.83
                        },
                        "Parch": {
                            "sum": 0.0,
                            "unique": 0.0
                        }
                    }
                }
            },
            {
                "group": [
                    "1"
                ],
                "current": {
                    "count": 118,
                    "metrics": {
                        "Age": {
                            "sum": 2686.42
                        },
                        "Fare": {
                            "sum": 5519.83
                        },
                        "Parch": {
                            "sum": 118.0,
                            "unique": 1.0
                        }
                    }
                }
            },
            {
                "group": [
                    "2"
                ],
                "current": {
                    "count": 80,
                    "metrics": {
                        "Age": {
                            "sum": 1170.75
                        },
                        "Fare": {
                            "sum": 5147.01
                        },
                        "Parch": {
                            "sum": 160.0,
                            "unique": 2.0
                        }
                    }
                }
            },
            {
                "group": [
                    "3"
                ],
                "current": {
                    "count": 5,
                    "metrics": {
                        "Age": {
                            "sum": 166.0
                        },
                        "Fare": {
                            "sum": 129.76
                        },
                        "Parch": {
                            "sum": 15.0,
                            "unique": 3.0
                        }
                    }
                }
            },
            {
                "group": [
                    "4"
                ],
                "current": {
                    "count": 4,
                    "metrics": {
                        "Age": {
                            "sum": 178.0
                        },
                        "Fare": {
                            "sum": 339.88
                        },
                        "Parch": {
                            "sum": 16.0,
                            "unique": 4.0
                        }
                    }
                }
            },
            {
                "group": [
                    "5"
                ],
                "current": {
                    "count": 5,
                    "metrics": {
                        "Age": {
                            "sum": 196.0
                        },
                        "Fare": {
                            "sum": 162.75
                        },
                        "Parch": {
                            "sum": 25.0,
                            "unique": 5.0
                        }
                    }
                }
            },
            {
                "group": [
                    "6"
                ],
                "current": {
                    "count": 1,
                    "metrics": {
                        "Age": {
                            "sum": 43.0
                        },
                        "Fare": {
                            "sum": 46.9
                        },
                        "Parch": {
                            "sum": 6.0,
                            "unique": 6.0
                        }
                    }
                }
            }
        ],
        "visualization": "Multimetric Area Line"
    }
    TTN_NONE_IN_EQUALS_FILTER = {'data': [{'group': [[None, None]], 'current': {'count': 177.0}}], 'visualization': 'Histogram'}
    TTN_NONE_IN_NOT_EQUALS_FILTER = {'data': [{'group': [[0.0, 11.368571428571428]], 'current': {'count': 68.0}}, {'group': [[11.368571428571428, 22.737142857142857]], 'current': {'count': 163.0}}, {'group': [[22.737142857142857, 34.105714285714285]], 'current': {'count': 247.0}}, {'group': [[34.105714285714285, 45.47428571428571]], 'current': {'count': 133.0}}, {'group': [[45.47428571428571, 56.84285714285714]], 'current': {'count': 68.0}}, {'group': [[56.84285714285714, 68.21142857142857]], 'current': {'count': 28.0}}, {'group': [[68.21142857142857, 79.58]], 'current': {'count': 6.0}}, {'group': [[79.58, 90.94857142857143]], 'current': {'count': 1.0}}], 'visualization': 'Histogram'}
    TTN_NONE_IN_IN_FILTER = {'data': [{'group': [None], 'current': {'count': 687, 'metrics': {'Age': {'sum': 14576.75}}}}], 'visualization': 'Bars'}
    TTN_NONE_IN_NOT_IN_FILTER = {'data': [{'group': ['C23 C25 C27'], 'current': {'count': 4, 'metrics': {'Age': {'sum': 130.0}}}}, {'group': ['B22'], 'current': {'count': 2, 'metrics': {'Age': {'sum': 106.0}}}}, {'group': ['D20'], 'current': {'count': 2, 'metrics': {'Age': {'sum': 106.0}}}}, {'group': ['B28'], 'current': {'count': 2, 'metrics': {'Age': {'sum': 100.0}}}}, {'group': ['C125'], 'current': {'count': 2, 'metrics': {'Age': {'sum': 98.0}}}}, {'group': ['D17'], 'current': {'count': 2, 'metrics': {'Age': {'sum': 97.0}}}}, {'group': ['B96 B98'], 'current': {'count': 4, 'metrics': {'Age': {'sum': 97.0}}}}, {'group': ['D33'], 'current': {'count': 2, 'metrics': {'Age': {'sum': 97.0}}}}, {'group': ['D'], 'current': {'count': 3, 'metrics': {'Age': {'sum': 95.0}}}}, {'group': ['E67'], 'current': {'count': 2, 'metrics': {'Age': {'sum': 91.0}}}}], 'visualization': 'Bars'}
    LFB_RUN_RAW_QUERY_WITH_DATE_FILTER = {'data': [
     {'rn': 1, 'incident_number': '021928-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 00:22:52'},
     {'rn': 2, 'incident_number': '021901-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 20:09:55'},
     {'rn': 3, 'incident_number': '022008-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 06:05:57'},
     {'rn': 4, 'incident_number': '022226-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 17:10:42'},
     {'rn': 5, 'incident_number': '022124-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 11:48:29'},
     {'rn': 6, 'incident_number': '022025-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 07:20:26'},
     {'rn': 7, 'incident_number': '022047-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 08:45:50'},
     {'rn': 8, 'incident_number': '021919-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 21:43:55'},
     {'rn': 9, 'incident_number': '022019-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 06:54:29'},
     {'rn': 10, 'incident_number': '021932-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 00:42:14'},
     {'rn': 11, 'incident_number': '022040-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 08:02:32'},
     {'rn': 12, 'incident_number': '022170-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:08:04'},
     {'rn': 13, 'incident_number': '022003-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 05:45:12'},
     {'rn': 14, 'incident_number': '021993-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 05:09:01'},
     {'rn': 15, 'incident_number': '022095-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 11:16:59'},
     {'rn': 16, 'incident_number': '022088-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 11:09:38'},
     {'rn': 17, 'incident_number': '022005-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 06:00:03'},
     {'rn': 18, 'incident_number': '021994-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 05:13:36'},
     {'rn': 19, 'incident_number': '021930-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 00:30:20'},
     {'rn': 20, 'incident_number': '022250-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 18:43:52'},
     {'rn': 21, 'incident_number': '021978-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 03:58:50'},
     {'rn': 22, 'incident_number': '022184-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:43:00'},
     {'rn': 23, 'incident_number': '021975-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 03:56:23'},
     {'rn': 24, 'incident_number': '021941-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 02:30:17'},
     {'rn': 25, 'incident_number': '021981-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 04:02:08'},
     {'rn': 26, 'incident_number': '022153-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 13:14:28'},
     {'rn': 27, 'incident_number': '022029-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 07:34:22'},
     {'rn': 28, 'incident_number': '022125-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 11:48:30'},
     {'rn': 29, 'incident_number': '022173-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:14:09'},
     {'rn': 30, 'incident_number': '022046-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 08:38:22'},
     {'rn': 31, 'incident_number': '021940-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 02:27:10'},
     {'rn': 32, 'incident_number': '022023-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 07:17:30'},
     {'rn': 33, 'incident_number': '022165-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 13:50:04'},
     {'rn': 34, 'incident_number': '022210-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:46:35'},
     {'rn': 35, 'incident_number': '022141-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 12:32:04'},
     {'rn': 36, 'incident_number': '022163-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 13:47:36'},
     {'rn': 37, 'incident_number': '022042-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 08:06:51'},
     {'rn': 38, 'incident_number': '021956-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 03:12:14'},
     {'rn': 39, 'incident_number': '022033-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 07:45:51'},
     {'rn': 40, 'incident_number': '021922-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 22:39:58'},
     {'rn': 41, 'incident_number': '022215-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 16:24:41'},
     {'rn': 42, 'incident_number': '022011-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 06:27:50'},
     {'rn': 43, 'incident_number': '021985-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 04:39:24'},
     {'rn': 44, 'incident_number': '022203-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:21:56'},
     {'rn': 45, 'incident_number': '022133-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 12:04:34'},
     {'rn': 46, 'incident_number': '021902-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 20:19:06'},
     {'rn': 47, 'incident_number': '022031-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 07:36:52'},
     {'rn': 48, 'incident_number': '021933-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 01:06:17'},
     {'rn': 49, 'incident_number': '022037-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 07:55:05'},
     {'rn': 50, 'incident_number': '022013-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 06:31:39'},
     {'rn': 51, 'incident_number': '022199-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:03:57'},
     {'rn': 52, 'incident_number': '022208-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:34:27'},
     {'rn': 53, 'incident_number': '021926-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 23:25:42'},
     {'rn': 54, 'incident_number': '021927-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 23:55:49'},
     {'rn': 55, 'incident_number': '022151-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 13:12:06'},
     {'rn': 56, 'incident_number': '022183-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:42:20'},
     {'rn': 57, 'incident_number': '021977-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 03:58:22'},
     {'rn': 58, 'incident_number': '022131-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 12:01:09'},
     {'rn': 59, 'incident_number': '021937-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 01:38:40'},
     {'rn': 60, 'incident_number': '022201-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:08:04'},
     {'rn': 61, 'incident_number': '021920-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 22:17:59'},
     {'rn': 62, 'incident_number': '021905-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 20:33:42'},
     {'rn': 63, 'incident_number': '021906-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 20:46:25'},
     {'rn': 64, 'incident_number': '022172-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:09:21'},
     {'rn': 65, 'incident_number': '021900-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 19:46:49'},
     {'rn': 66, 'incident_number': '022102-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 11:31:16'},
     {'rn': 67, 'incident_number': '021982-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 04:03:08'},
     {'rn': 68, 'incident_number': '022050-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 09:01:43'},
     {'rn': 69, 'incident_number': '021948-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 02:55:21'},
     {'rn': 70, 'incident_number': '022055-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 09:14:34'},
     {'rn': 71, 'incident_number': '022043-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 08:12:50'},
     {'rn': 72, 'incident_number': '022032-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 07:37:55'},
     {'rn': 73, 'incident_number': '022099-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 11:26:53'},
     {'rn': 74, 'incident_number': '022168-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:06:33'},
     {'rn': 75, 'incident_number': '022202-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:10:23'},
     {'rn': 76, 'incident_number': '022002-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 05:39:58'},
     {'rn': 77, 'incident_number': '022060-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 09:41:01'},
     {'rn': 78, 'incident_number': '022014-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 06:40:36'},
     {'rn': 79, 'incident_number': '021973-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 03:53:32'},
     {'rn': 80, 'incident_number': '022107-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 11:39:50'},
     {'rn': 81, 'incident_number': '022145-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 12:54:47'},
     {'rn': 82, 'incident_number': '022197-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:02:43'},
     {'rn': 83, 'incident_number': '022187-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:51:43'},
     {'rn': 84, 'incident_number': '022028-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 07:33:27'},
     {'rn': 85, 'incident_number': '021916-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 21:20:13'},
     {'rn': 86, 'incident_number': '022211-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:49:48'},
     {'rn': 87, 'incident_number': '021959-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 03:19:43'},
     {'rn': 88, 'incident_number': '022059-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 09:34:12'},
     {'rn': 89, 'incident_number': '021999-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 05:26:59'},
     {'rn': 90, 'incident_number': '022018-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 06:54:11'},
     {'rn': 91, 'incident_number': '022205-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:31:22'},
     {'rn': 92, 'incident_number': '022188-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:51:56'},
     {'rn': 93, 'incident_number': '022017-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 06:53:55'},
     {'rn': 94, 'incident_number': '021960-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 03:20:33'},
     {'rn': 95, 'incident_number': '022225-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 17:07:07'},
     {'rn': 96, 'incident_number': '022182-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 14:39:37'},
     {'rn': 97, 'incident_number': '021908-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-21 21:04:26'},
     {'rn': 98, 'incident_number': '022200-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 15:05:44'},
     {'rn': 99, 'incident_number': '022227-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 17:12:05'},
     {'rn': 100, 'incident_number': '022051-22022017', 'date_of_call': '2017-02-22',
      'timestamp_of_call': '2017-02-22 09:04:14'}]}

    # endregion
