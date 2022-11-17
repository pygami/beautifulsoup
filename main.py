from bs4 import BeautifulSoup

html_content = """
<html>
<head>
    <title>Sample HTML Page</title>
</head>
<body>
    <h1>Welcome to BeautifulSoup Example</h1>
    <p>This is a sample paragraph.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_content, 'html.parser')

title = soup.title.string
print("Title:", title)

paragraph = soup.find('p').text
print("Paragraph:", paragraph)

print("List Items:")
for item in soup.find_all('li'):
    print("-", item.text)
