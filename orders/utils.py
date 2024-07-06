from datetime import timedelta


def calculate_next_delivery_date(current_date, recurrence):
    if recurrence == 'monthly':
        return current_date + timedelta(days=30)
    return None
