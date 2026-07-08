"""
Open PR Test Feature - Dashboard filtering for open pull requests.
"""

def filter_open_prs(prs):
    """Filter and return only open pull requests."""
    return [pr for pr in prs if pr['state'] == 'open']


def count_open_prs(prs):
    """Count the number of open pull requests."""
    return len(filter_open_prs(prs))
