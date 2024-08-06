#!/usr/bin/env python

"""
Script that assists in breaks during work.
Distraction free experience, just start the script from command line with desired arguments.

Author: Arttu Vanninen
License: CC0 1.0 Universal
Date created: 2024-08-04
Date modified: 2024-08-04

-t or --type for type of exercise (4-7-8, box or equal breathing)
-d or --duration for duration of exercise in seconds (will be fixed by the script based on number of breathing cycles)

Happy break-taking!

"""
import time
import argparse
import datetime

def hhmm_timestamp(delta_min=0):
    """
    Print timestamp for function runtime or defined delta in minutes
    """
    delta_sec = delta_min * 60

    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.timestamp() + delta_sec

    formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime("%H:%M")
    return formatted_timestamp

def mmss_countdown(t_min):
  """
  Print countdown for preparation.

  Args:
    t_min: minutes to count down from (length of break)
  """
  t = t_min * 60 # t is time in seconds

  while t > -1: 
       mins, secs = divmod(t, 60) 
       timer = 'On a break... {:02d}:{:02d}'.format(mins, secs) 
       print(timer, end="\r") 
       time.sleep(1) 
       t -= 1

  print("\n")

def break_timer(t_min):
    """
    Wrapper function for taking a break. Prints header and footer and
    possible extra information.
    """
    print("##########")
    print("Taking a break until :", hhmm_timestamp(t_min))
    mmss_countdown(t_min)
    print("##########\nFinished break. Happy working :)")

def main(type, duration):
    hhmm_timestamp(5)
    break_timer(5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Break timer using Python.')
    parser.add_argument('-t', '--type', help='type of break: offscreen or reflection, default: offscreen')
    parser.add_argument('-d', '--duration', help='desired duration of break in minutes')
    args = parser.parse_args()

    # Error handling if duration is not set
    if args.duration == None:
      args.duration = 60

    main(args.type, int(args.duration))
