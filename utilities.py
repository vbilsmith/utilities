"""Here is a workspace to develop new utilities for bioinformatics computing in the lab"""
import pandas as pd
import numpy as np

"""Below, I'm just showing an example of how you might split this up into pieces
to make testing easier. I have not run this and I am not totally sure how your
function worked, so you will likely need to do some tweaking to get it to run.
I would recommend starting with a function that just calculates the MAD for a single
series (either row or column) and then once you have that working, you can expand
it to run on a whole dataframe.
"""

def mad(series): 
  """Function to calculate median absolute deviation for a Series
  Parameters:[change below to match your function's requirements]
  argument1 (int): Description of arg1

  Returns: [change below to match your function]
  int:Returning value
  """
  overall_med = series.median(numeric_only=True)
  abs_diff_vector = abs(series - overall_med)
  return abs_diff_vector.median(axis='rows', numeric_only=True)

def test_mad():
  assert mad[0, 0, 0, 0] == 0
  
