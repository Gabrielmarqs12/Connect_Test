def frequency_select(frequency):
    with open('FreqList.txt', 'r') as freq:
        list = freq.readlines()
        for ln in list:
           data = ln.split(':')
           data[1] = data[1].replace('\n', '')
           if data[0] == frequency:
               return(data[2], '[V] Connected')
               break
    pass       
pass