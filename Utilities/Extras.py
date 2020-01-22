"""Utlities.Extras"""
import datetime
import Utilities.Constants as ct


def decorate_break_message(message):
    print("*" * 30 + message + "*" * 30)


def display_job_card(data):
    print("\n" + "-" * 30)
    print(ct.Name + str(data[0]))
    print(ct.Age + str(data[1]))
    print(ct.Gender + str(data[2]))
    print(ct.Area + str(data[3]))
    print(ct.Address + str(data[4]))
    print("-" * 30)


def convert_string_to_date(date_str):
    format_str = '%d-%m-%Y'
    date_result = datetime.datetime.strptime(date_str, format_str)
    return date_result.date()

