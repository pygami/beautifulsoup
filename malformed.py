from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<title>Sample HTML Document</title>
</head>
<body>
<p>This is <b>malformed HTML</p>
<p>But BeautifulSoup can handle it</b></p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())  
