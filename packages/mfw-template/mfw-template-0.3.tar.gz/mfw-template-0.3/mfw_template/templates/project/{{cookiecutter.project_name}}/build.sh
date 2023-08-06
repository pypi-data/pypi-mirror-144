#!/bin/bash

set -e

HERE=`dirname $0`
BUILDOUT_DIR=`realpath $HERE`

PYTHON='/usr/bin/python3.8'

cd $BUILDOUT_DIR;

if [ ! -d "./venv" ];then
    echo "Initializing Virtualenv"
    $PYTHON -m venv venv
fi

if [ ! -f "./bin/buildout" ];then
    echo "Bootstrap Buildout"
    ./venv/bin/pip install zc.buildout
    ./venv/bin/buildout bootstrap
fi

echo "Starting Build ..."

./bin/buildout -vvv $@

./bin/python -c "import nltk;nltk.download('punkt')"

sleep 2
cat > ./venv/bin/python.sh << EOF
#!/bin/bash

cd $BUILDOUT_DIR;
./venv/bin/python3 \$@;
EOF

chmod +x ./venv/bin/python.sh

echo "Build Complete!"
