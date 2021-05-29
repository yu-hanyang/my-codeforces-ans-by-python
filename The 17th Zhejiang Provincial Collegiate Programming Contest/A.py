import calendar
import datetime
def d_d(y2,m2,d2):
    dd1=datetime.datetime(int(y2)-1,12,31)
    dd2=datetime.datetime(int(y2),int(m2),int(d2))
    interval=dd2-dd1
    return interval.days

# def y_y(y1,y2):
#     t=0
#
#     for i in range(int(y1),int(y2)):
#         if '202' in str(i):
#             if calendar.isleap(i):
#                 t += 366
#             else:
#                 t += 365
#         elif str(i)[-1] == '2':
#             if calendar.isleap(i):
#                 t += 30
#             else:
#                 t += 29
#         else:
#             t += 2
#
#     return t
#
def yd(y):
    out=0
    if int(y)==2000:
        return 0
    elif int(y)<=2020:
        out+=(2*(int(y)-2000))
        if int(y)>2012:
            out+=55
        elif int(y)>2002:
            out+=27
    elif int(y)<=2030:
        out+=(2*(int(y)-2000))
        out+=55
        out+=(363*(int(y)-2020))
        out+=1
        if int(y)<2025:
            out+=1
        elif int(y)<2029:
            out+=2
    elif



def md_md(y1,m1,d1):
    ou=0
    if '202' in y1:
        ou+=d_d(y1,m1,d1)
    elif y1[-1]=='2':
        if int(m1)<2:
            pass
        elif int(m1)==2:
            ou+=int(d1)
        elif int(m1)<13 and int(d1)<2:
            if calendar.isleap(int(y1)):
                ou+=29
            else:ou+=28
        else:
            if calendar.isleap(int(y1)):
                ou+=30
            else:ou+=29
    else:
        if int(m1) < 3 and int(d1)<2:
            pass
        elif int(m1)==12 and int(d1)>=2:
            ou+=2
        else:ou+=1
    return ou


for _ in range(int(input())):
    y1,m1,d1,y2,m2,d2=input().split()


    yd2=y_y(y1,y2)
    md1=md_md(y1,m1,d1)
    if md1==1:
        md1=0
    md2=md_md(y2,m2,d2)
    print(yd2+md2-md1)




