import tweepy

def get_timeline_html(twitter_keys):
    tweets = __get_timeline_tweets(twitter_keys)
    return __print_to_html(tweets)    

def __get_timeline_tweets(twitter_keys):
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
    return api.home_timeline(count=200, tweet_mode='extended', exclude_replies=True)

def __print_to_html(tweets):
    items_htmls = []
    for tweet in tweets:
        urls = [url['expanded_url'] for url in tweet.entities.get('urls',[])]
        html_uris = "<h4>Uris:</h4>"  + "<ul>" + ''.join([ f"<li><a href={u}>{u}</a></li>" for u in urls]) + "</ul>"
        if len(urls) == 0:
            html_uris = ""
        
        imgs = [ media['media_url'] for media in tweet.entities.get('media',[]) if media['type']=='photo']
        html_imgs = [f'<img src="{img}" alt="img">' for img in imgs]

        tweet_html = f"""
<div class=item>
    <h3>{tweet.user.name}</h3><h5>{tweet.created_at}</h5>
    <div class=text>
    {tweet.full_text} 
    {html_uris}
    </div>
    {''.join(html_imgs) }
</div>
"""
        items_htmls.append(tweet_html)
    
    css = """
.item  {border-style: solid; margin:10px; padding:5px}
.item .text { width = 70%; float=right;}
.item img { float=left; width:25%;}
"""
    
    html =  f"""
<html lang="en">
<style>    
{css}
</style>
<body>
{''.join(items_htmls)}
</body>
</html>
"""
    return html