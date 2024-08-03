import time

def breathe(cycles):
  """
  Performs a set number of 4-7-8 breathing cycles.

  Args:
      cycles: The number of breathing cycles to perform.
  """
  # Define breath durations in seconds based on a 1 second inhale
  inhale_time = 4
  hold_time = 7
  exhale_time = 8

  print("Get comfortable and close your eyes (optional).")

  for _ in range(cycles):
    # Inhale
    print(f"({_+1}/{cycles}) Inhale silently through your nose for a count of 4...")
    time.sleep(inhale_time)

    # Hold
    print("Hold your breath for a count of 7...")
    time.sleep(hold_time)

    # Exhale
    print("Exhale completely through your mouth with a whoosh sound for a count of 8...")
    time.sleep(exhale_time)

    print("Rest and repeat...")

# Example usage with 4 cycles
breathe(4)

print("Finished breathing exercise. Feel free to repeat!")
