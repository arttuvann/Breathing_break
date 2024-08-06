#!/usr/bin/env python

"""
Script that assists in breathing exercises from command line.
Distraction free experience, just start the script from command line with desired arguments.

Author: Arttu Vanninen
License: CC0 1.0 Universal
Date created: 2024-08-03
Date modified: 2024-08-03

-t or --type for type of exercise (4-7-8, box or equal breathing)
-d or --duration for duration of exercise in seconds (will be fixed by the script based on number of breathing cycles)

Happy break-taking!

"""

import time
import argparse

def prepare_countdown(t):
  """
  Print countdown for preparation.

  Args:
    t: seconds to count down
  """
  while t > -1: 
       mins, secs = divmod(t, 60) 
       timer = 'Take a moment to prepare: {:02d}:{:02d}'.format(mins, secs) 
       print(timer, end="\r") 
       time.sleep(1) 
       t -= 1

  print("\n")

def seconds_countdown(t):
  """
  Print countdown for breathing exercise phases.

  Args:
    t: seconds to count down from
  """
  # debug
  #print("went to seconds_countdown() function")

  for i in range(t,0,-1):
    print(f"{i}", end="\r", flush=True)
    time.sleep(1)
  print("Cycle finished.", end="\r", flush=True)

def breathe_box(duration_seconds):
  """
  Performs a set number of box breathing cycles.

  Args:
      duration_seconds: The duration of the exercise in seconds.
  """
  # Define breath durations in seconds
  inhale_time = 4
  hold_time = 4
  exhale_time = 4
  #duration_seconds = cycles * inhale_time + hold_time + exhale_time + hold_time
  cycles = duration_seconds // (inhale_time + hold_time + exhale_time) # Calculate number of cycles based on given duration.

  # recalculate duration based on number of cycles
  duration_seconds = (inhale_time + hold_time + exhale_time) * cycles

  duration_formatted = time.strftime('%H:%M:%S', time.gmtime(duration_seconds))


  print(f"Starting box breathing exercise\nCycles: {cycles}\nDuration : {duration_formatted}")
  time.sleep(1)
  prepare_countdown(3)

  for c in range(cycles):
    print("##########")
    # Inhale
    print(f"Cycle : {c+1}/{cycles}\nInhale silently through your nose for a count of {inhale_time}...")
    seconds_countdown(inhale_time)

    # Hold
    print(f"Hold for a count of {hold_time}...")

    seconds_countdown(hold_time)

    # Exhale
    print(f"Exhale through your nose for a count of {exhale_time}...")
    seconds_countdown(exhale_time)

    # Hold
    print(f"Hold your breath for a count of {hold_time}...")
    seconds_countdown(hold_time)
    print("\n")

def breathe_equal(duration_seconds):
  """
  Performs a set number of equal breathing cycles.

  Args:
      duration_seconds: The duration of the exercise in seconds.
  """
    # Define breath durations in seconds
  inhale_time = 4
  hold_time = 4
  exhale_time = 4

  cycles = duration_seconds // (inhale_time + hold_time + exhale_time) # Calculate number of cycles based on given duration.

  # recalculate duration based on number of cycles
  duration_seconds = (inhale_time + hold_time + exhale_time) * cycles

  duration_formatted = time.strftime('%H:%M:%S', time.gmtime(duration_seconds))
  
  print(f"Starting equal breathing exercise\nCycles: {cycles}\nDuration : {duration_formatted}")
  time.sleep(1)
  prepare_countdown(3)

  for c in range(cycles):
    print("##########")
    # Inhale
    print(f"Cycle : {c+1}/{cycles}\nInhale silently through your nose for a count of {inhale_time}..")
    seconds_countdown(inhale_time)

    # Exhale
    print(f"Exhale through your nose for a count of {exhale_time}...")
    seconds_countdown(exhale_time)

    # Hold
    #print(f"Hold your breath for a count of {hold_time}...")
    #time.sleep(hold_time)
    print("\n")



def breathe_478(duration_seconds):
  """
  Performs a set number of 4-7-8 breathing cycles.

  Args:
      duration_seconds: The duration of the exercise in seconds.
  """
  # Define breath durations in seconds based on a 1 second inhale
  inhale_time = 4
  hold_time = 7
  exhale_time = 8
  #duration_seconds = cycles * inhale_time + hold_time + exhale_time
  cycles = duration_seconds // (inhale_time + hold_time + exhale_time) # Calculate number of cycles based on given duration.
  # recalculate duration based on number of cycles
  duration_seconds = (inhale_time + hold_time + exhale_time) * cycles
  duration_formatted = time.strftime('%H:%M:%S', time.gmtime(duration_seconds))

  print(f"Starting 4-7-8 breathing exercise.\nDuration : {duration_formatted}\nCycles: {cycles}")
  time.sleep(1)
  prepare_countdown(3)

  for _ in range(cycles):
    print("\n##########")
    # Inhale
    print(f"Cycle : {_+1}/{cycles}\nInhale silently through your nose for a count of {inhale_time}...")
    seconds_countdown(inhale_time)

    # Hold
    print(f"Hold your breath for a count of {hold_time}...")
    seconds_countdown(hold_time)

    # Exhale
    print(f"Exhale completely through your mouth with a whoosh sound for a count of {exhale_time}...")
    seconds_countdown(exhale_time)




def main(type, duration):
  print("\n##########")
  if type == "4-7-8":
    breathe_478(duration)
  elif type == "box":
    breathe_box(duration)
  elif type == "equal":
    breathe_equal(duration)
  elif duration != None:
    breathe_box(duration)
  else:
    breathe_box(60)


  print("##########\nFinished breathing exercise. Feel free to repeat!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Do breathing exercises using Python.')
    parser.add_argument('-t', '--type', help='breathing exercise type (4-7-8, box, or equal)')
    parser.add_argument('-d', '--duration', help='desired duration of breathing exercise in seconds')
    args = parser.parse_args()

    # Error handling if duration is not set
    if args.duration == None:
      args.duration = 60

    main(args.type, int(args.duration))
