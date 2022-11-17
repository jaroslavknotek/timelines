
Timelines
---

This repository contains my own twitter timeline view without adds, you might like section and retweets.  

# Installation

```
pip install -r requirements
```

# Config
The properties below must be set. You can get them from [Twitter developer portal](https://developer.twitter.com/en/portal/petition/essential/basic-info)

- `TW_API_KEY` - Twitter API key
- `TW_API_SECRET` - Twitter API Secret 
- `TW_ACCESS_TOKEN` - Twitter Token
- `TW_TOKEN_SECRET` - Twitter Token Secret

# Run

Execute the following command to run the app localy

```
./run_flask.sh
```

# Deployment

The application can be deployed to [fly.io](https://fly.io/docs/). Should you have `flyctl` installed and configured, add all the secrets as above:

```
flyctl secrets set TW_API_KEY=...
flyctl secrets set TW_API_SECRET=...
flyctl secrets set TW_ACCESS_TOKEN=...
flyctl secrets set TW_TOKEN_SECRET=...
```

Then execute

```
flyctl deploy
```
