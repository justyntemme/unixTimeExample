from datetime import datetime, timedelta


def unix_to_datetime(unix_timestamp):
    """
    Convert a Unix timestamp to a datetime object.

    Parameters:
    unix_timestamp (int): Unix timestamp

    Returns:
    datetime: Datetime object corresponding to the Unix timestamp
    """
    return datetime.utcfromtimestamp(unix_timestamp)


def days_since(unix_timestamp):
    """
    Calculate the number of days since the given Unix timestamp.

    Parameters:
    unix_timestamp (int): Unix timestamp

    Returns:
    int: Number of days since the Unix timestamp
    """
    timestamp_datetime = unix_to_datetime(unix_timestamp)
    current_datetime = datetime.utcnow()
    delta = current_datetime - timestamp_datetime
    return delta.days


# Example usage
unix_timestamp_example = 1609459200  # Unix timestamp for 2021-01-01 00:00:00 UTC
converted_datetime = unix_to_datetime(unix_timestamp_example)
days_elapsed = days_since(unix_timestamp_example)

print(f"Converted datetime: {converted_datetime}")
print(f"Days since timestamp: {days_elapsed}")
