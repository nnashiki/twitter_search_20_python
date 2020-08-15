import json

from ratelimit import limits
from twitter import *

BEARER_TOKEN = ""
twitter = Twitter(auth=OAuth2(bearer_token=BEARER_TOKEN))

# Now work with Twitter
data = twitter.search.tweets(q="bigquery", count=100)

for tweet_data in data["statuses"]:
    if "text" in tweet_data:
        print("\n" * 5 + tweet_data["text"])

FIFTEEN_MINUTES = 900


@limits(calls=15, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API response: {}".format(response.status_code))
    return response


global_tweet = []
FIFTEEN_MINUTES = 900


@limits(calls=15, period=FIFTEEN_MINUTES)
def search(params):
    return twitter.search.tweets(**params)


def main():
    search_word = "bigquery"
    tweet_data = []
    immutable_params = {
        "q": search_word,
        "count": 100,
    }
    params = {
        "q": search_word,
        "count": 100,
    }

    def parseToParam(parse_str, parse=None):
        if parse is None:
            parse = "&"
        return_params = {}
        parsed_str = parse_str.split(parse)
        for param_string in parsed_str:
            param, value = param_string.split("=", 1)
            if param != "q" and param != "count":
                return_params[param] = value
        return_params.update(immutable_params)
        print(return_params)
        return return_params

    tweet_count = 0

    while 1 == 1:
        print("done")
        tweets = search(params)
        print(params)
        print(tweets["search_metadata"])
        for tweet in tweets["statuses"]:
            global_tweet.append(tweet)
        # tweets['search_metadata']['next_results'] をパースしてparamへ
        if "next_results" in tweets["search_metadata"].keys():
            params = parseToParam(tweets["search_metadata"]["next_results"].lstrip("?"))
            tweet_count = tweet_count + 1
        else:
            break


main()

with open("./output/output.json", mode="w") as f:
    json.dump(global_tweet, f, ensure_ascii=False)
