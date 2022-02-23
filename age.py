l=input("Write your Dob in this format")
while True:
    import datetime,os
    from time import sleep
    p = datetime.datetime.now()
    # print(p)
    v=datetime.datetime.strptime(l,'%d/%m/%Y')
    # print(v)
    y=p-v
    # print(y)
    #years
    w=((y.total_seconds())/(365.242*24*3600))
    w_int=int(w)
    # print(w_int)
    #months
    m=(w-w_int)*12
    m_int=int(m)
    # print(m_int)
    #days
    d = (m-m_int)*(365.242/12)
    d_int=int(d)
    # print(d_int)
    #hours
    hh = (d-d_int)*24
    hh_int=int(hh)
    # print(hh_int)
    #minutes
    mm = (hh-hh_int)*60
    mm_int=int(mm)
    # print(mm_int)
    #seconds
    ss= (mm-mm_int)*60
    ss_int=int(ss)
    # print(ss_int)
    print('You are {0:d} years,{1:d} months,{2:d} days,{3:d} hours,{4:d} minutes,{5:d} seconds old.'.format(w_int,m_int,d_int,hh_int,mm_int,ss_int))
    sleep(1)