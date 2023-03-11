import requests

#help(requests)

r = requests.get('https://www.python.org')


print(r)

class Brouser:

  def __init__(self,url):
    self.url = url

  def load_page(self):
    r = requests.get(self.url)
    if r.status_code == 200:
      print("Page is loaded")
    else:
      print("Some error")

my_b = Brouser("https://mystat.itstep.org/ru/main/dashboard/page/index")
my_b.load_page()