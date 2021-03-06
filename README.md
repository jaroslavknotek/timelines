
Timelines
---

This repository contains my personal implementation of custom timelines
- Twitter timeline
- Notes reminder

# Installation

The requirements file for functions is [here](azure_functions/requirements.txt). But for development tools (like flask for running it locally) use also this [requirements file](tools/requirements.dev.txt).


# Rudimentary Twitter Home Timeline 

**In twitter app, my home timeline shows far more than it should. I decided to filter it out.**

There is a script to which you give [twitter credentials](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) and it will download tweets from your home timeline and create a rudimentary html code with it's content. That code can be then hosted on a stateless service (e.g. [azure function](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview)). In the end you have your web page without adds, retweets (optional), "you might like" sections and others. 

See how it looks [here](notebooks/visualisation.ipynb)

## Content

- `azure_functions/shared_code/tw2html.py` - script that gives you the html representing your timeline
- `visualisation.ipynp` - notebook that renders the html (so you can see it, try to open it within this repo)
- `azure_fucntions/twtimeline` - directory with azure function stuff (see [this](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python) for more info about what it does exactly)

## Run

You need to create file `local.setting.json` with the following values. This is a format that is given by the azure function so I decided to reuse it too. 

```json
{
"Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "",
    "api_key":"your api key",
    "api_secret":"your api_secret",
    "access":"your access key",
    "secret":"your secret"
  }
}
```

You can then run [the notebook](visualisation.ipynb) and see your own timeline. If you want to have your own public website, then you can use Azure Function. You should be able to get their free credit. 

# Notes

I have plenty of notes. Some of them should be read again. Those are marked with `#show_me` tag.

The timeline is similar to the twitter one except the data source - the notes are stored in azure table. Filling it is not in scope of this repository. 

