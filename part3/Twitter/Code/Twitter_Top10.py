import pandas as pd
## Code for extracting top 10 from nytimes for word count
data=pd.read_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\tweetword.txt", sep='\t', encoding='ISO-8859-1')
data.columns=['Word', 'Count']
data=data.sort_values('Count', ascending=False)
print(data)
top_ten_data=data[0:10]
top_ten_data.reset_index(drop = True, inplace = True)
top_ten_data.to_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\top_10_tweetword.txt",sep='\t',header=False, index=False)


## Code for extracting top 10 from nytimes for word cooccurrence
data=pd.read_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\tweetco.txt", sep='\t', encoding='ISO-8859-1')
data.columns=['Word', 'Count']
data=data.sort_values('Count', ascending=False)
print(data)
top_ten_data=data[0:10]
top_ten_data.reset_index(drop = True, inplace = True)
top_ten_data.to_csv("D:\\MS\\2ndSem\\DIC\\\Lab2\\output\\top_10_tweetco.txt",sep='\t',header=False, index=False)