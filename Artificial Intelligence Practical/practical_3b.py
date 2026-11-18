# ===== 3b. Hill Climbing Problem =====
def hill_climbing():
  states =[1,3,5,7,9,8,6,4]
  current=0
  while current < len(states)-1:
    next_state = current + 1
    if states[next_state] > states[current]:
      current = next_state
    else:
      break
  print("Maximum Value:",states[current])
  print("Best Position:",current)
hill_climbing()
