import requests
from functools import lru_cache

#            name        song name                  surname   link st  link st 2    link st 3  link st 4    alternative
keywords = ["rickroll", "never gonna give you up", "astley", "dqw4w9", "iik25wqi", "d0tgbcc", "xvfzjo5pg", "wreck roll"]

@lru_cache(maxsize=32)
def rickroll(link):
    '''Description: checks if a link is a rickroll. Check antirickroll.keywords for their list. Returns None if link invalid. 
    WARNING: Can take long if there are many redirects, run this with asyncio!!!'''
    global keywords
    request = ""
    if "9saKj_npn" in link: return False
    if any(kw in link for kw in keywords): return True
    try: request = requests.get(link)
    except (requests.URLRequired, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.InvalidURL): return None
    t = request.text.lower()
    return any(i in t for i in keywords)

def findLinks(text):
    '''Description: Finds all links in a piece of text. 
    WARNING: Can be false activated (rarely)!!! Check links with the requests library!'''
    text += " "
    text = text.replace("\n", " ")
    linx = []
    def shortDaCode(c, cc):
        try:
            opt1 = text.split(cc)
            for i in range(1, len(opt1)):
                appd = opt1[i].split(c)[0]
                if " " in appd or ">" in appd: continue
                linx.append("http" + appd)
        except IndexError:
            pass
    shortDaCode(" ", "http")
    shortDaCode(">", "<http")
    #shortDaCode("\n")
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
    from pprint import pprint
    testString = """
Раздача Red Dead https://www.youtube.com/watch?v=xQNw8BBxRIs&ab_channel=Kairamen Redemption 2 всего лишь 24 часа!
1. Переходим на сайт - https://www.youtube.com/watch?v=dQw4w9WgXcQ
2. Создаем аккаунт и переходим в раздел "Giveaway" https://youtube.com
3. Выполняем простые задания (если что используйте переводчик) 
4. Получаем https://tinyurl.com/rdr2giveaway ключик
https://DryRespectfulSystemsanalysis-1.dacoconutnut.repl.co
https://www.youtube.com/watch?v=9saKj_npnYo
http protocol rickroll
<https://www.youtube.com/watch?v=gpg8g_JssGc>
"""
    print("test string: " + testString)
    import time
    start_time = time.time()
    pprint(findRickrolls(testString))
    print("--- %s seconds ---" % (time.time() - start_time))
