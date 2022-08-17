import urllib.request, json

with urllib.request.urlopen("https://www.kaggle.com/datasets/prathamsharma123/farmers-protest-tweets-dataset-raw-json") as url:
    data = json.loads(url.read().decode())
    print(data)

/function to find the biggest RetweetCount on data json
def first_function ():
    max_retweet_count = 0
    for i in data:
        if i['retweet_count'] > max_retweet_count:
            max_retweet_count = i['retweet_count']
            print(max_retweet_count)
    # no alcance por el timpo, cambie el computador, no sabia que se requeria tener lenguajes instalados como python para estas pruebas
    return max_retweet_count

    




    