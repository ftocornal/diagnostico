import urllib.request, json

with urllib.request.urlopen("https://www.kaggle.com/datasets/prathamsharma123/farmers-protest-tweets-dataset-raw-json") as url:
    data = json.loads(url.read().decode())
    print(data)

//function to find the biggest RetweetCount on data
def first_function ():
    




    