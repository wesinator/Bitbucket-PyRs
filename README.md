# Bitbucket-PyRs

Python code snippets for creating Bitbucket PRs via the ["official" Atlassian Bitbucket Python API](https://bitbucket.org/atlassian/python-bitbucket) (Bitbucket cloud)

Atlassian (a company that makes products to support developers and PMs) couldn't bother to document their own client library, so here I am.

### Usage
App password in `bitbucket.cfg`

```python
import bitbucket_pr

# PR name, source branch, dest branch, source repo, dest repo
new_pr = bitbucket_pr.create_pr("PR name", "source_branch", "master", "user/repo", "user/repo")

# get url of PR
print(bitbucket_pr.get_pr_url(new_pr))
```

### Credits

Thanks to https://github.com/wbrefvem/python-bitbucket/blob/b5002a97f0dd9d02dfc60f81b3a13d966abad9aa/tests/test_pullrequest.py#L222 (fork of Bitbucket code hosted on Github) for pointing me in the right direction.
