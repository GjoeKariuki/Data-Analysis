from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<span class="text-white text-xs">another one</span>
<span class="text-white text-xs">another one</span>
<span class="text-white text-xs">another one</span>
<span class="text-white text-xs">another one</span>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# "lxml",'lxml-xml/xml','html5lib'
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.span)
print(soup.span.string)
print(soup.a)
print(soup.find(id='link3'))

for x in soup.find_all('span', {'class':'text-white text-xs'}):
    print(x.string)

print(soup.find_all('span', {'class':'text-white text-xs'}).string)

# extracting all urls
for link in soup.find_all('a'):
    print(link.get('href'))

# extracting all text
print(soup.get_text())

print(soup.prettify())
