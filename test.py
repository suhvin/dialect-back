# from scheduler.day1.day1 import do_day1
# from scheduler.day2.day2 import do_day2

# do_day1()
# do_day2()

# 다운받을 이미지 url


# python3
from urllib import request
from io import BytesIO
from PIL import Image

url = 'https://dispatch.cdnser.be/cms-content/uploads/2020/04/09/a26f4b7b-9769-49dd-aed3-b7067fbc5a8c.jpg'
# url = "blob:http://localhost:3000/40759941-adf9-4955-8697-a551b176baa5"
# fake user agent of Safari
# request.urlopen()

res = request.urlopen(url).read()
img = Image.open(BytesIO(res))


