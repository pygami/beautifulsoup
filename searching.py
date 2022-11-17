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

print(soup.find('p', text='Paragraph 1'))

print(soup.find('a', href='https://example.com'))

print(soup.select('div#main h1')) 
