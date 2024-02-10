
import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  solve = np.array(list)
  print(solve)

  mean_row = [solve[0,1,2].mean(), solve[3,4,5].mean(), solve[6,7,8].mean()]

  mean_col= [solve[0,3,6].mean(), solve[1,4,7].mean(), solve[2,5,8].mean()]
  mean_all = solve.mean()
  var_row = [solve[0,1,2].var(), solve[3,4,5].var(),solve[6,7,8].var()]
  var_col = [solve[0,3,6].var(), solve[1,4,7].var(),solve[2,5,8].var()]
  var_all = solve.var()
  std_col =  [solve[0,3,6].std(), solve[1,4,7].std(), solve[2,5,8].std()]
  std_row =  [solve[0,1,2].std(), solve[3,4,5].std(), solve[6,7,8].std()]
  std_all = solve.std()
  max_col =  [solve[0,3,6].max(), solve[1,4,7].max(), solve[2,5,8].max()]
  max_row =  [solve[0,1,2].max(), solve[3,4,5].max(), solve[6,7,8].max()]
  max_all = solve.max()
  min_col =  [solve[0,3,6].min(), solve[1,4,7].min(), solve[2,5,8].min()]
  min_row =  [solve[0,1,2].min(), solve[3,4,5].min(), solve[6,7,8].min()]
  min_all = solve.min()
  
  return {'mean' : [mean_col,mean_row,mean_all],
          'variance': [var_col,var_row,var_all],
          'standard_deviation': [std_col,std_row,std_all],
          'max': [max_col,max_row,max_all],
          'min': [min_col,min_row,min_all]
          
         }