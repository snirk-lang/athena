"""
Information passed into env vars by travis.

See https://docs.travis-ci.com/user/environment-variables#Default-Environment-Variables
"""

import os

class TravisInfo:
    """
    Information passed into env vars by travis
    """
    def __init__(self, local):
        self.local = local
        if not local:
            self.travis_job_id = os.environ["TRAVIS_JOB_ID"]
            self.type = os.environ["TRAVIS_EVENT_TYPE"]
            self.commit_range = os.environ["TRAVIS_COMMIT_RANGE"]
            if self.type == "push":
                self.branch = os.environ["TRAVIS_BRANCH"]
            elif self.type == "pull_request":
                self.pr_number = os.environ["TRAVIS_PULL_REQUEST"]
                self.pr_slug = os.environ["TRAVIS_PULL_REQUEST_SLUG"]
                self.pr_from = os.environ["TRAVIS_PULL_REQUEST_BRANCH"]
                self.pr_to = os.environ["TRAVIS_BRANCH"]
        else:
            print("Using local settings for travis")
