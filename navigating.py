from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<title>Sample HTML Document</title>
</head>
<body>
<div id="main">
    <h1>Title</h1>
    <p class="content">Paragraph 1</p>
    <p class="content">Paragraph 2</p>
    <a href="https://example.com">Link</a>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.find('p'))  
print(soup.find_all('p'))  

print(soup.find_all(class_='content'))

print(soup.find(id='main'))

print(soup.find('p').parent)  
print(soup.find('a').get('href'))  
