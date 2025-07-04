
class PropertyHolder:
    def __init__(self):
        # Dynamically add worklogs attribute if it doesn't already exist
        if not hasattr(self, 'worklogs'):
            self.worklogs = []

# Example usage
holder = PropertyHolder()
holder.worklogs.append({'id': 1, 'description': 'Worklog entry'})
print(holder.worklogs)
