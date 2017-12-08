# GitHub Trending(Python)


## Intro
Tracking the most popular Java Github repos, updated daily(Python version)

It uses travis-ci to run the build once a day that produces and publishes the day's trending Java projects through the deployment feature.

inspired by [github-trending(Go Version)](https://github.com/josephyzhou/github-trending)

inspired by and forked from https://github.com/bonfy/github-trending

bonfy's special day (originally forked from):
- [2017-03-29](https://github.com/bonfy/github-trending/blob/master/2017-03-29.md) - my repo [qiandao](https://github.com/bonfy/qiandao) record by github-trending(python)

## Run

You need install `pyquery` & `requests`

```bash
  $ git clone https://github.com/bonfy/github-trending.git
  $ cd github-trending
  $ pip install -r requirements.txt
  $ python scraper.py
```

## Lisence

MIT
