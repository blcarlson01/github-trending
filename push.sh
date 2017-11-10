#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git add . *.md
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git checkout master
  git push "https://${GITHUB_TOKEN}@github.com/blcarlson01/github-trending.git" origin HEAD:master > /dev/null 2>&1
}

setup_git
commit_website_files
upload_files