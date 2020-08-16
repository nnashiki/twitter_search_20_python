# twitter_search_20_python
Twitter API v2 を python で実行してみる

# doc
- docs全体
   - https://developer.twitter.com/en/docs
- 認証
   - https://developer.twitter.com/en/docs/basics/getting-started

## Twitter API v2 に関して
2020/07に Twitter API v2 が登場し、developer portalも変更が加わったようです。  
https://blog.twitter.com/developer/ja_jp/topics/tools/2020/NewTwitterAPI.html

### Twitter Developer アカウントの作成
基本以下Qiita記事の通りです。ただし、登録申請後にすぐにdelveloper potralから使い始めることができました。
https://qiita.com/kngsym2018/items/2524d21455aac111cdee

`API key`、`API secret` 、`Bearer Token`が発行されました。
`Consumer API Keys` は発行されていない。

### 認証に関して
`Search Tweets` を使いたいので、OAuth 2.0 Bearer Token を使用します。  
https://developer.twitter.com/en/docs/authentication/overview

### Python client の選定に関して
コミュニティで開発されている、`twitter` というクライアントがBearer Tokenに対応していたので、そちらを利用しました。  
内部で`Twitter API v2`が叩かれているかは確認していない。

- https://github.com/sixohsix/twitter
- https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries
> twitter by the Python Twitter Tools developer team


### apiはここから試す事ができる
https://developer.twitter.com/en/portal/register/playground

### Search API standard に関して
> The Twitter Search API searches against a sampling of recent Tweets published in the past 7 days.

https://developer.twitter.com/en/docs/tweets/search/overview/standard

### recent search の新・旧の比較に関して
https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate

`since_id (polling) until_id` を使うのは変わっていないみたい。

### standard API の制限(rate limit)に関して

以下が存在

- Tweets cap
- call cap

#### Tweets cap

> *Recent search and filtered stream share a monthly Tweet cap limit of 500,000 Tweets. 

https://developer.twitter.com/en/docs/twitter-api/rate-limits


#### call cap

https://developer.twitter.com/en/docs/twitter-api/rate-limits


#### API 
変わってしまっている....
https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

## v1
### responseに関して

data['search_metadata']

```
{'completed_in': 0.099,
 'count': 100,
 'max_id': 1292037861424762881,
 'max_id_str': '1292037861424762881',
 'next_results': '?max_id=1291860773019385855&q=bigquery&count=100&include_entities=1',
 'query': 'bigquery',
 'refresh_url': '?since_id=1292037861424762881&q=bigquery&include_entities=1',
 'since_id': 0,
 'since_id_str': '0'} 
```

- データの取得の仕方としては、最新からからどんどん古いものにさかのぼっていく
   - next_resultsがあった存在した場合はより古いものが存在する。max_id=1291860773019385855を取得してパラメータとして渡してやる
- count = 100は常に指定しておく
- since_id: 指定したIDよりも大きい(新しい)結果を返します。
- max_id: 指定したID以下（つまり、指定したIDよりも古い）またはそれと同じIDの結果を返します。
- include_entities: The entities node will not be included when set to false.





