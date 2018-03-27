#!/usr/bin/env bash
LINK=$(echo $PATH | sed "s/:.*//" | sed "s/$/\/git-gud/")
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sudo ln -s $DIR/git-gud $LINK
