import requests

#            name        song name                  surname   link st  link st 2    link st 3  link st 4
keywords = ["rickroll", "never gonna give you up", "astley", "dqw4w9", "iik25wqi", "d0tgbcc", "xvfzjo5pg"]

def rickroll(link):
    '''Description: checks if a link is a rickroll. Check antirickroll.keywords for their list. Returns False if link invalid. 
    WARNING: Can take long if there are many redirects, run this with asyncio!!!'''
    
    request = ""
    if "9saKj_npn" in link: #exception for my own rickroll video MUHAHAHAHA
        return False
    try:
        request = requests.get(link)
    except (requests.URLRequired, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.InvalidURL):
        return False
    t = request.text.lower()
    global keywords
    for i in keywords:
        if i in t:
            return True
    return False

def findLinks(text):
    '''Description: Finds all links in a piece of text. 
    WARNING: Can be false activated (rarely)!!! Check links with the requests library!'''
    srt = text
    srt += " "
    linx = []
    def shortDaCode(c):
        try:
            opt1 = srt.split("http")
            for i in range(1, len(srt.split("http"))):
                appd = opt1[i].split(c)[0]
                if (" " in appd) or ("\n" in appd):
                    continue
                linx.append("http" + appd)
        except IndexError:
            pass
    shortDaCode(" ")
    shortDaCode("\n")
    return linx

def findRickrolls(srt):
    '''Description: Finds all links in a piece of text and checks then for rickrolls. Filters out invalid links if they exist(look antirickroll.findLinks). 
    Returns a dictionary with links as keys and if they are rickrolls as values. 
    WARNING: Can take long if there are many redirects and links in the text, run this with asyncio!!!'''
    retDict = {}
    #print(srt + "\n")
    linx = findLinks(srt)
    #print(linx)
    for i in linx:
        rickres = rickroll(i)
        if not rickres == None:
            retDict[i] = rickres
    return retDict

if __name__ == "__main__":
    testString = """
Раздача Red Dead Redemption 2 всего лишь 24 часа!

1. Переходим на сайт - https://www.youtube.com/watch?v=dQw4w9WgXcQ
2. Создаем аккаунт и переходим в раздел "Giveaway" https://youtube.com
3. Выполняем простые задания (если что используйте переводчик) 
4. Получаем https://tinyurl.com/rdr2giveaway ключик
https://DryRespectfulSystemsanalysis-1.dacoconutnut.repl.co
https://www.youtube.com/watch?v=9saKj_npnYo
http protocol rickroll


"""
    print("test string: " + testString)
    print(findRickrolls(testString))
