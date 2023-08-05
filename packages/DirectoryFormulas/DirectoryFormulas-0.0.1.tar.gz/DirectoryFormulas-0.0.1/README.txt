python3 setup.py sdist
ls -lah dist
pip3 install /Users/frankie/PycharmProjects/PycharmProjectsShared/TradingProject/Directory_Library/dist/Directory-0.0.1.tar.gz

twine upload dist/Directory-0.0.1.tar.gz