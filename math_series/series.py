
def sum_series(i, p1=0, p2=1):
  """
  Generate ageneric serise based on aregument

  Areguments :

  i {integer} -- [index use to generate a serise]
  p1 {integer} -- [to determine the base case for index 0]
  p2 {integer} -- [to determine the base case for index 1]
  Returns :
  {integer}  --  [generic math serise based on p1,p2]

  """
  if i == 0: #case 0
    return p1
  elif i == 1: #case 1
    return p2
  return sum_series(i-1, p1, p2) + sum_series(i-2, p1, p2)

  
    


def fibonacci(i):
  """
  it like sum serise with base value 0 for i=0 and 1 for i =1

  """
  if i == 0:
    return 0
  elif i == 1:
    return 1  
  return fibonacci(i-1)+fibonacci(i-2)  

# ----------------------------------------------------------------

def lucas(i):
  """
    it like sum serise with base value 2 for i=0 and 1 for i =1

  """
  if i == 0:
    return 2
  elif i == 1:
    return 1  
  return lucas(i-1)+lucas(i-2) 

# ------------------------------------------------------------------
        
