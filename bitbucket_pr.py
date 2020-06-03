#!/usr/bin/env python3
from pybitbucket.auth import BasicAuthenticator
from pybitbucket.bitbucket import Client
from pybitbucket.pullrequest import PullRequest, PullRequestPayload
from pybitbucket.repository import Repository

from configparser import RawConfigParser


def bitbucket_login():
    bitbucket_config = RawConfigParser()
    try:
        bitbucket_config.read("bitbucket.cfg")
    except FileNotFoundError:
        print("missing API config file")
        exit(1)

    try:
        user = bitbucket_config.get("bitbucket", "user")
        app_password = bitbucket_config.get("bitbucket", "app_password")
        email = bitbucket_config.get("bitbucket", "email")
    except:
        print("error reading Bitbucket API config")
        exit(1)

    bitbucket = Client(BasicAuthenticator(user, app_password, email))
    return bitbucket


# specified user/repo , get repo obj
def get_repo(repo_project_path):
    bitbucket = bitbucket_login()

    repos = Repository
    repo = repos.find_repository_by_full_name(
                    full_name=repo_project_path,
                    client=bitbucket
    )
    #print(repo, repo.clone['ssh'])
    return repo


def create_pr(pr_title, source_branch, dest_branch, source_repo_name, dest_repo_name):
    bitbucket = bitbucket_login()

    # https://github.com/wbrefvem/python-bitbucket/blob/b5002a97f0dd9d02dfc60f81b3a13d966abad9aa/tests/test_pullrequest.py#L222
    pr_payload = PullRequestPayload() \
            .add_title(pr_title) \
            .add_source_branch_name(source_branch) \
            .add_source_repository_full_name(source_repo_name) \
            .add_destination_branch_name(dest_branch) \
            .add_destination_repository_full_name(dest_repo_name)

    response = PullRequest.create(pr_payload, client=bitbucket)
    return response


# given pr response object, get URL link to PR in BB
def get_pr_url(pr_response):
    return pr_response.links.get("html", {}).get("href", "")
