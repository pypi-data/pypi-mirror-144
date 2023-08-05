python3 setup.py sdist
ls -lah dist
pip3 install /Users/frankie/PycharmProjects/PycharmProjectsShared/TradingProject/Directory_Library/dist/DirectoryFormulas-0.0.1.tar.gz

twine upload dist/DirectoryFormulas-0.0.1.tar.gz