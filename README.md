# py_github_update_checker #

A little library to ease the checking of new versions from github in python

### Installation ###
As github_update_checker is on PyPi, installing it is as simple as :

    pip install github_update_checker

However, if you prefer to install it manually, just download the archive and run :

    python setup.py install


### Usage ###
Using this module is as simple as:

    import github_update_checker
    new_update, latest_release = github_update_checker.update(Version, repo_owner, repo_name)
