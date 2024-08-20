def check_transactions(arr):
    from collections import defaultdict, deque
    
    # Store requests by second
    second_count = defaultdict(int)
    
    # Store requests by time windows of 10 seconds and 60 seconds
    ten_second_windows = deque()
    minute_windows = deque()
    
    dropped = set()
    
    for i, second in enumerate(arr):
        # Count transactions for the current second
        second_count[second] += 1
        
        # Check for violations of 3 second limit
        if second_count[second] > 3:
            dropped.add(i)
            continue  # Move to the next transaction
        
        # Add to 10-second window
        ten_second_windows.append(second)
        
        # Remove old entries from the 10-second window
        while ten_second_windows and ten_second_windows[0] <= second - 10:
            ten_second_windows.popleft()
        
        # Check for violations of 10-second limit
        if len(ten_second_windows) > 20:
            dropped.add(i)
            continue  # Move to the next transaction
        
        # Add to 60-second window
        minute_windows.append(second)
        
        # Remove old entries from the 60-second window
        while minute_windows and minute_windows[0] <= second - 60:
            minute_windows.popleft()
        
        # Check for violations of 60-second limit
        if len(minute_windows) > 60:
            dropped.add(i)
            continue  # Move to the next transaction
    
    # Determine the result based on dropped indices
    result = len(dropped)
    print("Dropped indices:", sorted(dropped))
    print("Result:", result)
    
# Given array of transaction timestamps
arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]

# Execute the function
check_transactions(arr)
