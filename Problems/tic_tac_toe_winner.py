def tic_tac_toe_winner(arr):
    matches = [[0,3,6], [1,4,7], [2,5,8],[0,1,2], [3,4,5], [6,7,8],[0,4,8], [2,4,3]]
    
    for i in range(8):
        if arr[matches[i][0]] == "x" and arr[matches[i][1]] == "x" and arr[matches[i][2]] == "x":
            return "Player A wins"
        
        if arr[matches[i][0]] == "o" and arr[matches[i][1]] == "o" and arr[matches[i][2]] == "o":
            return "Player B wins"                                            
    
    if "." not in arr:
        return "Tie"
    return "Play in Progress"

a = [".","x","x","o","o",".",".", ".", "."]
print(tic_tac_toe_winner(a))

#[x,o,x,o,x,o,x,0,x] - Tie
a = ["x","o","x","o","x","o","o", "x", "o"]
print(tic_tac_toe_winner(a))
