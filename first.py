from urllib.request import urlopen
html=urlopen("http://qjhjames.github.io")
print(html.read())