#!/bin/sh
pip install codecov nose
cd /tmp
nosetests --cover-package=mapek_framework --with-coverage --cover-xml --cover-xml-file /tmp/a.xml $TARGET_REPO_PATH/mapek_framework/src
cd $TARGET_REPO_PATH
codecov -f /tmp/a.xml -t $CODECOV_TOKEN