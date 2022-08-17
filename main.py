import urllib.request, json

with urllib.request.urlopen("https://www.kaggle.com/datasets/prathamsharma123/farmers-protest-tweets-dataset-raw-json") as url:
    data = json.loads(url.read().decode())
    print(data)
    
def first_function ():
    max_retweet_count = 0
    for i in data:
        if i['retweet_count'] > max_retweet_count:
            max_retweet_count = i['retweet_count']
            print(max_retweet_count)
    # no alcance por el timpo, cambie el computador, no sabia que se requeria tener lenguajes instalados como python para estas pruebas
    return max_retweet_count

def second_function ():
    max_tweet_users = 0
    return max_tweet_users

def third_function ():
    count = 0
    return count

def last_function ():
    count = 0
    return count

def main():
    first_function()
    second_function()
    third_function()
    last_function()