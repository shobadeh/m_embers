#- Tel=>> @CYROSIF
from requests import get
from time import sleep
from threading import Thread
url     = 'https://dast2.com/api/1.0/category/1?page={}'
headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Cookie':'XSRF-TOKEN=eyJpdiI6IkRQVlk2aGR2MEU0MzdxUGZjOFFMWVE9PSIsInZhbHVlIjoiS1NaYklQK2JZWEViNVNoSWRlTW9xUFFcL0pyWUtXalNXVTVadEQrTFRhRmtNZVwvMXJHR2JtcUNLVHViWE5SUHRaRDlyVFlDUHFHSmRITEZnXC8rZW9YUUJXb3JnaGRucys5TG00bk5mUnVUOXF0N2JqS3hjSUJqQmJmRDN3QlFNdlwvIiwibWFjIjoiZWY4YWRlZGIyNTdjYjJlNDYwZThkZDAzODJhYmJlM2FhNzUwYjZiYjhiNzJiOGE3MmU3NGIwMGVmN2Q0NWU5ZiJ9; laravel_session=eyJpdiI6ImZtTUZLOUR6ajBZa01YZlNEWHRVTVE9PSIsInZhbHVlIjoicHJFckVlXC9HRXRLV0ZkaHpjWkVscG1OK1d4MDRhOGdiampRMVFBaU9QczkrbDlWOTZpNzVwdllVaDFoeVM5WUNIZTIxQjU1c1BZZ29jRnQ0ZDRacklxNlJ5bDFsMzZ0a2tOQmFHRUJqUENEQVdBbDBYVXF6all0YnR6ZWhkczRQIiwibWFjIjoiMDBhZTk5ZDBkZTc0ZDQ5NTkyYTUzODM3MzJlZGIzZmM1OWU3NDk2OWUxYThlYmMxOTg1ZjNiOGU1MjhkNDE2OSJ9; _ga=GA1.2.496500745.1641204427; _gid=GA1.2.1622359339.1641204427',
    'Host':'dast2.com',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'TE':'trailers',
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'X-CSRF-TOKEN':'GFzMHarexN4Z0aoh8eVUEIrLyRYC9eRNVRsIcDiP',
    'X-Requested-With':'XMLHttpRequest',
    'X-XSRF-TOKEN':'eyJpdiI6IkRQVlk2aGR2MEU0MzdxUGZjOFFMWVE9PSIsInZhbHVlIjoiS1NaYklQK2JZWEViNVNoSWRlTW9xUFFcL0pyWUtXalNXVTVadEQrTFRhRmtNZVwvMXJHR2JtcUNLVHViWE5SUHRaRDlyVFlDUHFHSmRITEZnXC8rZW9YUUJXb3JnaGRucys5TG00bk5mUnVUOXF0N2JqS3hjSUJqQmJmRDN3QlFNdlwvIiwibWFjIjoiZWY4YWRlZGIyNTdjYjJlNDYwZThkZDAzODJhYmJlM2FhNzUwYjZiYjhiNzJiOGE3MmU3NGIwMGVmN2Q0NWU5ZiJ9'
}
ok = []
def checkNum(x):
    res = get(url.format(x), headers=headers)
    if not res.status_code == 200: return print('Not Found')
    jRes = res.json()
    if jRes['success']:
        nums = jRes['data']['advertises']['data']
        for phone in nums:
            Num = phone['owner_mobile']
            if Num not in ok: print(Num)
            ok.append(Num)
x = 1
while True:
    Thread(target=checkNum, args=[x]).start(), sleep(0.1)
    x += 1