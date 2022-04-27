Rudimentary Twitter Home Timeline 
---

**In twitter app, my home timeline shows far more than it should. I decided to filter it out.**

There is a script to which you give [twitter credentials](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) and it will download tweets from your home timeline and create a rudimentary html code with it's content. That code can be then hosted on a stateless service (e.g. [azure function](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview)). In the end you have your web page without adds, retweets (optional), "you might like" sections and others. 

See how it looks [here](visualisation.ipynb)

# Content

- `azure_functions/shared_code/tw2html.py` - script that gives you the html representing your timeline
- `visualisation.ipynp` - notebook that renders the html (so you can see it, try to open it within this repo)
- `azure_fucntions/twtimeline` - directory with azure function stuff (see [this](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python) for more info about what it does exactly)

