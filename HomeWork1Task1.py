

def domain_name(url: str):
    if url.find('//') != -1:
        url = url.split('//')[1]
    splitted_url = url.split('.')

    if 'www.' in url:
        domain = splitted_url[1]
    else:
        domain = splitted_url[0]

    return domain;

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

