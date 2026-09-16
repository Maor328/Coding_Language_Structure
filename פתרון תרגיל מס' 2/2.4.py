from datetime import datetime, timedelta

def generate_dates(start_date_str, num_dates, skip_days):
    # Receives a Gregorian date, number of requested dates, and skip days
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
    
    # Use HOF (map) to generate the requested dates
    dates_gen = map(lambda i: (start_date + timedelta(days=i * skip_days)).strftime("%d/%m/%Y"), range(num_dates))
    
    return list(dates_gen)

# Example usage
print(generate_dates("01/01/2026", 5, 7))