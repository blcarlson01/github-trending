#!/bin/sh

mkdir results
cp *.md results/
cp *.json results/
git clone -b gh-pages https://github.com/blcarlson01/github-trending.git
cp github-trending/*.md results/
cp github-trending/*.json results/