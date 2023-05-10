from bs4 import BeautifulSoup
import optparse
import requests

def opt_func():
    instance = optparse.OptionParser()
    instance.add_option('-u','--url',dest='url',help='which url you want')
    user_input,arguments = instance.parse_args()
    return user_input.url

def request_site(req_url):
    url = req_url
    site_map = requests.get(url)
    return site_map.content

def get_link(html_doc):
    soup = BeautifulSoup(html_doc,'lxml')
    for link in soup.findAll('a'):
        with open('site_link','a') as file:
            file.write(link.get('href') + '\n')

def get_content(html_doc):
    soup = BeautifulSoup(html_doc,'lxml')
    with open('site_content','a') as file:
        file.write(soup.get_text())


get_link(request_site(opt_func()))
get_content(request_site(opt_func()))



