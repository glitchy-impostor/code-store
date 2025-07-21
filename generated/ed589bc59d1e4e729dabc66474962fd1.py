
import argparse
import datetime as dt
import matplotlib.pyplot as plt

def parse_arguments():
    parser = argparse.ArgumentParser(description="Ticket analysis for the past week")
    parser.add_argument('--data', required=True, help='Path to the CSV file containing ticket data')
    return parser.parse_args()

def read_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def filter_tickets_by_date(data, start_date, end_date):
    return data[(data['date'] >= start_date) & (data['date'] <= end_date)]

def categorize_tickets(tickets):
    pending = tickets[tickets['status'] == 'pending']
    completed = tickets[tickets['status'] == 'completed']
    return pending, completed

def count_tickets_per_person(tickets):
    return tickets.groupby('person').size().reset_index(name='count')

def get_last_week():
    today = dt.date.today()
    start_date = today - dt.timedelta(days=today.weekday() + 7)
    end_date = start_date + dt.timedelta(days=6)
    return start_date, end_date

def plot_results(data):
    people = data['person']
    pending_counts = data[data['status'] == 'pending']['count']
    completed_counts = data[data['status'] == 'completed']['count']

    x_pos = [i for i, _ in enumerate(people)]
    
    plt.bar(x_pos, pending_counts, color='red', align='center', alpha=0.75, label='Pending')
    plt.bar([x + 0.3 for x in x_pos], completed_counts, color='green', align='center', alpha=0.75, label='Completed')

    plt.xticks(x_pos, people)
    plt.xlabel('Person')
    plt.ylabel('Number of Tickets')
    plt.title('Ticket Status Over the Last Week')
    plt.legend()

    plt.show()

def driver_function(file_path):
    args = parse_arguments()
    data = read_data(args.data)
    
    start_date, end_date = get_last_week()
    tickets = filter_tickets_by_date(data, start_date, end_date)
    
    pending, completed = categorize_tickets(tickets)
    pending_counts = count_tickets_per_person(pending)
    completed_counts = count_tickets_per_person(completed)

    result = pd.concat([pending_counts, completed_counts], axis=1).fillna(0)
    result['status'] = 'pending'
    result.loc[:, 'count'] = result['pending']
    del result['pending']
    
    result['status'] = 'completed'
    result.loc[:, 'count'] = result['completed']
    del result['completed']

    plot_results(result)

if __name__ == "__main__":
    driver_function('path_to_your_data.csv')
