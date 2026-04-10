From datetime import datetime, timedelta


def has_expired (check_in_time):

"""calculates when the 2 hours end"""
    expiry_time = check_in_time + timedelta(hours=2)

"""gets the current time"""
    current_time = datetime.now()

"""check if current time has passed the expiry time"""
    if current_time > expiry_time:
        return True
    else:
        return false