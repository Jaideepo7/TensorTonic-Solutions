def percent_change(series):
    delperc = []
    for i in range(len(series)-1):
        if series[i]==0:
            delperc.append(0)
        else:
            delperc.append((series[i+1]-series[i])/series[i])
    return delperc
        
        