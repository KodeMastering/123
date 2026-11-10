def  check_window(window, n):

    try:
        valid = (n >= window >= 1) and (int(window) == window)
    except ValueError:
        return "ValueError"
    if valid is False:
        return "wrong"
    return valid

# def  simple_moving_average(data, window):
#     for i in range(len(data) - window + 1): 
#         result.append(sum(data[i:i+window]) / window) 

def running_sum(data, window):
    valid = check_window(window, len(data))
    
    running = sum(data[:window]) 
    result = [running / window] 

    for i in range(window, len(data)): 
        running += data[i] - data[i - window] 
        result.append(running / window)
    
    return print(result) if valid is True else print(valid)