import requests
from bs4 import BeautifulSoup
import os

url = 'https://en.wikipedia.org/wiki/Five_Suns'

def get_text_element(bs, tag, class_=None):
    result = bs.find(tag, class_=class_)
    if result:
        return result.text.strip()
    return ''

page_content = ''

if not os.path.exists('wiki.html'):
    print("Loading page from the internet...")
    page = requests.get(url)
    page_content = page.content.decode()

    with open('wiki.html', 'w') as outfile:
        outfile.write(page_content)
else:
    print("Reading html from file...")
    with open('wiki.html', 'r') as infile:
        page = infile.read()
    page_content = page.encode('utf-8')

soup = BeautifulSoup(page_content, 'html.parser')

title = soup.find('span', class_='mw-page-title-main').text.strip()
info = soup.find('div', class_='mw-parser-output').text.strip()   
headers = soup.find_all('span', class_='mw-headline')
 
print(f"Article Title: {title}\n")
print("Headers in article:\n ")
for header in headers:
    print(header.text.strip(),"\n")

paragraphs = soup.find_all('p')

print("Paragrphs: \n")
for p in paragraphs:
    print(p.text.strip(),"\n")


references = soup.find(id="References")
ol_reference = soup.find("ol", class_="references")


print(references.text.strip())
print("_______________________\n")
print(ol_reference.text.strip(),"\n")

print("Image Tags:")
print("_______________________\n")

images = soup.find_all("div", class_="thumbinner") 




print(f"Found {len(images)} img tags")

for image in images: 
    img = image.find('div', class_="thumbcaption").text.strip()
    print(img)
