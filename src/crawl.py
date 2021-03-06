import json

from ratelimit import limits  # type: ignore
from twitter import OAuth2, Twitter  # type: ignore

BEARER_TOKEN = ""
twitter = Twitter(auth=OAuth2(bearer_token=BEARER_TOKEN))

global_tweet = []
FIFTEEN_MINUTES = 900
RECENT_SEARCH_CALL_CAP_FOR_FIFTEEN_MINUTES = 170


@limits(calls=RECENT_SEARCH_CALL_CAP_FOR_FIFTEEN_MINUTES, period=FIFTEEN_MINUTES)
def search(params):
    return twitter.search.tweets(**params)


def main():
    search_word = "bigquery"
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

    while True:
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
