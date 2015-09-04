#!usr/bin/env python

#import modules used here - sys is a very standard one
import sys

def report_status(scheduled_time, estimated_time):

    # report_status(14.3, 14.3)
    #  'On time'
    # report_status(12.5, 11.5)
    #  'early'
    # report_status(9.0, 9.5)
    #  'delayed'

    if scheduled_time == estimated_time:
        print("On time")
    elif scheduled_time > estimated_time:
        print("Early")
    else: 
        print("Delayed")


if __name__ == '__main__':
    report_status (12.5, 12.5)