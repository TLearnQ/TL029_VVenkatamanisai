Attendance=[{}]
marks=[]
def classify(rec):
    Attendance=rec[Attendance]
    marks=rec[marks]
    avg=sum(marks)/len(marks)
    if  Attendance<=30 and avg<=35:
        return "Failing"
    if  Attendance>=90 and avg>=95:
        return "Excellent"
    elif  Attendance>=70 and avg>=70:
        return "On Track"
    else:
        return "At Risk"
print(classify({"Attendance":70,"marks":[50,96,94]}))