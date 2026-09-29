import csv
import numpy as np
import pandas as pd

b=pd.read_csv('placement_readiness.csv')
py=np.array(b['Python_Score'])

"""avg=np.mean(py)
print("Average Python Score:", avg)

highest=np.max(py)
print("Highest Python Score:", highest)

lowest=np.min(py)
print("Lowest Python Score:",lowest)

com=np.array(b['Communication_Score'])
print("Number of students who scored above average:", np.sum(com>70))

pys=np.array(b['Python_Score'])
coms=np.array(b['Communication_Score'])
sql=np.array(b['SQL_Score'])
apti=np.array(b['Aptitude_Score'])
total=[]
total=np.array([pys,coms,sql,apti])

min=np.min(total,axis=0)
max=np.max(total,axis=0)
total_diff=max-min
print(total_diff)

print(b.head)
print(b.shape)
print(b.columns)
print(b.describe)
print(b[b['Python_Score']>75])

print(b.sort_values(by='Aptitude_Score',ascending=False))
print(b.sort_values(by='Python_Score',ascending=False).head(10))
print(b[(b['Python_Score']>b['Python_Score'].mean() )&( b['Communication_Score']<b['Communication_Score'].mean())])
"""

b['Total_Score']=(b['Python_Score']+b['Aptitude_Score']+b['Communication_Score']+b['SQL_Score'])
print(b.head(2))
b['Average_Score']=b['Total_Score']/4
#b['Weakest_Skill_Score']=b[['Aptitude_Score','Communication_Score','Python_Score','SQL_Score']].min(axis=1)
b['Readiness_Score']=(b['Average_Score']+(2 * b['Projects_Completed'])+b['Mock_Interviews_Attended']).clip(upper=100)
