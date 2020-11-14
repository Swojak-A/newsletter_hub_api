from django.utils import timezone


def localized_time(date_to_localize, format_string="%b %d %Y %H:%M:%S"):
    return timezone.localtime(date_to_localize).strftime(format_string)
