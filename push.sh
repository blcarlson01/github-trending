#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout master
  git add . *.md
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote set-url origin https://blcarlson01@github.com/blcarlson01/github-trending.git > /dev/null 2>&1
  git push --force --quiet "https://blcarlson01:${github_token}@github.com/blcarlson01/github-trending.git" orgin master > /dev/null 2>&1
}

setup_git
commit_website_files
upload_files