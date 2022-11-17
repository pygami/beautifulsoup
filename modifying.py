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

soup.find('h1').string = 'New Title'
soup.find('a')['href'] = 'https://newexample.com'

print(soup.prettify())  
