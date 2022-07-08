import plotly.figure_factory as ff
import pandas as pd
import statistics as st
import random as rd
import plotly.graph_objects as plo

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
fig=ff.create_distplot([data] , ["Data for Math Scores"] , show_hist=False)
#fig.show()
mean=st.mean(data)
std=st.stdev(data)
print(f"The mean is {mean}")
print(f"The Standard Deviation is {std}")

def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        r=rd.randint(0,len(data) - 1 )
        value=data[r]
        dataSet.append(value)
    mean=st.mean(dataSet)
    return mean

meanList=[]
for i in range(0,1000):
    s=randomSetOfMean(100)
    meanList.append(s)
mean=st.mean(meanList)
std=st.stdev(meanList)
print(f"The mean of the sample is {mean}")
print(f"The standard deviation of the sample is {std}")


firstStdStart,firstStdend=mean-std, mean+std
secondStdStart,secondStdend=mean-(2*std), mean+(2*std)
thirdStdStart,thirdStdend=mean-(3*std), mean+(3*std)
print(firstStdStart)
fig=ff.create_distplot([meanList] , ["Distribution Plot for Mean List"] , show_hist=False)
fig.add_trace(plo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(plo.Scatter(x=[firstStdStart, firstStdStart], y=[0, 0.17], mode="lines", name="First Std Start"))
fig.add_trace(plo.Scatter(x=[firstStdend, firstStdend], y=[0, 0.17], mode="lines", name="First Std End"))
fig.add_trace(plo.Scatter(x=[secondStdStart, secondStdStart], y=[0, 0.17], mode="lines", name="Second Std Start"))
fig.add_trace(plo.Scatter(x=[secondStdend, secondStdend], y=[0, 0.17], mode="lines", name="Second Std End"))
fig.add_trace(plo.Scatter(x=[thirdStdStart, thirdStdStart], y=[0, 0.17], mode="lines", name="Third Std Start"))
fig.add_trace(plo.Scatter(x=[thirdStdend, thirdStdend], y=[0, 0.17], mode="lines", name="Third Std End"))
#fig.show()

# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
meanSample1=st.mean(data)
fig=ff.create_distplot([meanList] , ["Distribution Plot for Mean List"] , show_hist=False)
fig.add_trace(plo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(plo.Scatter(x=[meanSample1, meanSample1], y=[0, 0.17], mode="lines", name="MEANSAMPLELINE"))
fig.add_trace(plo.Scatter(x=[firstStdend, firstStdend], y=[0, 0.17], mode="lines", name="First Std End"))
#fig.show()


# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.
df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
meanSample2=st.mean(data)
fig=ff.create_distplot([meanList] , ["Distribution Plot for Mean List"] , show_hist=False)
fig.add_trace(plo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEANSAMPLE2"))
fig.add_trace(plo.Scatter(x=[meanSample2, meanSample2], y=[0, 0.17], mode="lines", name="MEANSAMPLELINE"))
fig.add_trace(plo.Scatter(x=[firstStdend, firstStdend], y=[0, 0.17], mode="lines", name="First Std End"))
fig.add_trace(plo.Scatter(x=[secondStdend, secondStdend], y=[0, 0.17], mode="lines", name="Second Std End"))
#fig.show()



# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.
df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
meanSample3=st.mean(data)
fig=ff.create_distplot([meanList] , ["Distribution Plot for Mean List"] , show_hist=False)
fig.add_trace(plo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEANSAMPLE2"))
fig.add_trace(plo.Scatter(x=[meanSample3, meanSample3], y=[0, 0.17], mode="lines", name="Mean Sample 3"))
fig.add_trace(plo.Scatter(x=[firstStdend, firstStdend], y=[0, 0.17], mode="lines", name="First Std End"))
fig.add_trace(plo.Scatter(x=[secondStdend, secondStdend], y=[0, 0.17], mode="lines", name="Second Std End"))
fig.add_trace(plo.Scatter(x=[thirdStdend, thirdStdend], y=[0, 0.17], mode="lines", name="Third Std End"))
#fig.show()

#finding the z-score
#zScore = (New Sample Mean - Sampling Distribution Mean) / standard deviation
zScore1=(meanSample1-mean)/std
zscore2=(meanSample2-mean)/std
zscore3=(meanSample3/mean)/std
print(f"Z Score 1 ={zScore1}")
print(f"Z score 2 = {zscore2}")
print(f"Z score 3 = {zscore3}")
#Because the Zscore 1 value is less than one, the tablet did not make much of a difference
#Becuase the Zscore2 value is greater than one, the classes made the largest difference.
#Because the Zscore3 value is less than one, the funsheet did not make much of a difference, but it was higher than than the tablet.