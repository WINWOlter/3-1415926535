import requests
from colorama import Fore, Back, Style

#help(requests)

r = requests.get('https://www.python.org')


print(r)

class Brouser:

  def __init__(self,url):
    self.url = url

  def load_page(self):
    r = requests.get(self.url)
    if r.status_code == 200:
      print(Fore.GREEN + "Page is loaded")
    else:
      print(Fore.RED + "Some error")

my_b = Brouser("https://mail.google.com/mail/u/0/#inbox")
my_b.load_page()