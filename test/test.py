a = [(0,0),(0 ,1) ,(1,0),(0 ,2)]
win_state = [
    [(0 ,0) ,(0 ,1) ,(0 ,2)] ,
    [(1 ,0) ,(1 ,1) ,(1 ,2)] ,
    [(2 ,0) ,(2 ,1) ,(2 ,2)] ,
    [(0 ,0) ,(1 ,0) ,(2 ,0)] ,
    [(0 ,1) ,(1 ,1) ,(2 ,1)] ,
    [(0 ,2) ,(1 ,2) ,(2 ,2)] ,
    [(0 ,0) ,(1 ,1) ,(2 ,2)] ,
    [(2 ,0) ,(1 ,1) ,(0 ,2)]
]
c = 0

subset_found = False
# Iterate through elements in a
for state in win_state:
    if all(element in a for element in state):
        subset_found = True
        break



print(subset_found)

