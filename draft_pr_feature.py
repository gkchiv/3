"""
Draft PR Test Feature - Dashboard filtering for draft pull requests.
"""

def filter_draft_prs(prs):
    """Filter and return only draft pull requests."""
    return [pr for pr in prs if pr.get('draft', False) is True]


def count_draft_prs(prs):
    """Count the number of draft pull requests."""
    return len(filter_draft_prs(prs))
