import webbrowser

# Note:- get function didn't work, have to figure out what's wrong

url1 = "https://www.python.org/"

# webbrowser.open(url, new=1)
# webbrowser.open_new(url)
# webbrowser.open_new_tab(url)
# webbrowser.get(using=None)


# help(webbrowser)      # help command will show the information regarding the modules and classes

# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=';', end=' ')   # end parameter is new line by default

# webbrowser.register('google-chrome', preferred=True)
# chrome1 = webbrowser.get(using='google-chrome')
# chrome1.open_new_tab("https://www.python.org/")

# chrome1 = webbrowser.get(using='google-chrome %s')
# chrome1.open(url1)

#########################################
# Below example is searched on internet #
#########################################
# Below example is not working
# chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s'
#
# chrome = webbrowser.get(chrome_path).open_new_tab(url1)
