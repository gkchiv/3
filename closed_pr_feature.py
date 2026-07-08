"""
Closed PR Test Feature - Dashboard filtering for closed pull requests.
"""

def filter_closed_prs(prs):
    """Filter and return only closed pull requests."""
    return [pr for pr in prs if pr['state'] == 'closed']


def count_closed_prs(prs):
    """Count the number of closed pull requests."""
    return len(filter_closed_prs(prs))
