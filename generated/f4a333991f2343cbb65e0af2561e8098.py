
import sys
from datetime import datetime, timedelta
from collections import Counter
from typing import Dict

from jira import JIRA
import matplotlib.pyplot as plt


def get_completed_issues_per_person(jira_server: str, jira_user: str, jira_token: str, jql_project: str) -> Dict[str, int]:
    """
    Connect to JIRA and get the count of completed issues per assignee in the last week.

    Args:
        jira_server (str): URL of the JIRA server.
        jira_user (str): JIRA username/email.
        jira_token (str): JIRA API token or password.
        jql_project (str): JQL project key or query to filter issues.

    Returns:
        Dict[str, int]: Mapping of assignee display name to number of completed issues.
    """
    jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_token))

    one_week_ago = (datetime.utcnow() - timedelta(days=7)).strftime('%Y-%m-%d')
    # JQL to find issues resolved in the last week in the specified project
    jql = (
        f'project = {jql_project} AND statusCategory = Done AND resolved >= "{one_week_ago}"'
    )

    issues = jira.search_issues(jql, maxResults=False)

    assignee_counts = Counter()
    for issue in issues:
        assignee = issue.fields.assignee
        if assignee:
            assignee_name = assignee.displayName
        else:
            assignee_name = 'Unassigned'
        assignee_counts[assignee_name] += 1

    return dict(assignee_counts)


def create_and_save_bar_graph(data: Dict[str, int], output_file: str) -> None:
    """
    Create a bar graph with spaced bars and visible labels and save it to a file.

    Args:
        data (Dict[str, int]): Mapping of labels to values.
        output_file (str): Path to save the graph image.
    """
    names = list(data.keys())
    counts = list(data.values())

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(names, counts, width=0.6)

    # Add spacing between bars by adjusting x-axis limits and bar width
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=45, ha