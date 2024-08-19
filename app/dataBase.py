def get_availability(month):
    next_month_availability = [
        "2024-09-03", "2024-09-04", "2024-09-10",
        "2024-09-11", "2024-09-17", "2024-09-24", "2024-09-25"
    ]
    current_month_availability = [
        #"2024-08-02", "2024-08-07", "2024-08-15", not available anymore, i.e. past tense
        "2024-08-22", "2024-08-29"
    ]
    return next_month_availability if month == 'next' else current_month_availability