



class Display():
  """ """

def metrics_data(data:list, *, metrics:list, ids:list = []):
  """ """
  if ids:
    display_data = [a_range as a_month in data where a_month in ids]
  else:
    display_data = data

  display_grid = {}


  # display data
  for a_metric in metrics:
    display_grid[a_metric] = []

    for a_range in display_data:
      display_grid[a_metric].append(a_range.get_metric(a_metric))