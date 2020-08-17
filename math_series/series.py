

def fibonacci(i):
  if i == 0:
    return 0
  elif i == 1:
    return 1  
  return fibonacci(i-1)+fibonacci(i-2)  

# ----------------------------------------------------------------

def lucas(i):
  if i == 0:
    return 2
  elif i == 1:
    return 1  
  return lucas(i-1)+lucas(i-2) 

# ------------------------------------------------------------------

def sum_series(i, p1=0, p2=1):
    
    if i == 0:
        return p1
    elif i == 1:
        return p2
    return sum_series(i-1, p1, p2) + sum_series(i-2, p1, p2)
        
