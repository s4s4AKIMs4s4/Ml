import pandas as pd

df_train=pd.read_csv('train/train.csv')
df_test=pd.read_csv('test/test.csv')

def preprocessingData():
    def Year(date):
      return date.split('-')[0]
    
    def Month(date):
        return date.split('-')[1]
    
    def Day(date):
        return date.split('-')[2]
    
    def Hour(time):
        return time.split(':')[0]
    
    def Minute(time):
        return time.split(':')[1]
    
    def Second(time):
        return time.split(':')[2]

    return {
        'Year': Year,
        Month: Month,
        Day: Day,
        Hour: Day,
        Minute: Minute,
        Second: Second
    }


props = preprocessingData()

df_train=pd.read_csv('train/train.csv')
df_test=pd.read_csv('test/test.csv')

def preprocessingData():
    def Year(date):
      return date.split('-')[0]
    
    def Month(date):
        return date.split('-')[1]
    
    def Day(date):
        return date.split('-')[2]
    
    def Hour(time):
        return time.split(':')[0]
    
    def Minute(time):
        return time.split(':')[1]
    
    def Second(time):
        return time.split(':')[2]

    return {
        'Year': Year,
        'Month': Month,
        'Day': Day,
        'Hour': Hour,
        'Minute': Hour,
        'Second': Second
    }


props = preprocessingData()
print(props)

df_train['Year']=df_train['date'].apply(lambda x: props['Year'](x))
df_test['Year']=df_test['date'].apply(lambda x: props['Year'](x))

df_train['Month']=df_train['date'].apply(lambda x: props['Month'](x))
df_test['Month']=df_test['date'].apply(lambda x: props['Month'](x))

df_train['Day']=df_train['date'].apply(lambda x: props['Day'](x))
df_test['Day']=df_test['date'].apply(lambda x: props['Day'](x))

df_train['Hour']=df_train['time'].apply(lambda x: props['Hour'](x))
df_test['Hour']=df_test['time'].apply(lambda x: props['Hour'](x))

df_train['Minute']=df_train['time'].apply(lambda x: props['Minute'](x))
df_test['Minute']=df_test['time'].apply(lambda x: props['Minute'](x))

df_train['Second']=df_train['time'].apply(lambda x: props['Second'](x))
df_test['Second']=df_test['time'].apply(lambda x: props['Second'](x))

df_train=df_train.drop('date', axis=1)
df_test=df_test.drop('date', axis=1)
df_train=df_train.drop('time', axis=1)
df_test=df_test.drop('time', axis=1)

df_train[['Year','Month', 'Day', 'price']]=df_train[['Year','Month', 'Day', 'price', ]].astype(int)
df_test[['Year','Month', 'Day', 'price']]=df_test[['Year','Month', 'Day', 'price']].astype(int)

df_train.to_csv('train/train_preprocessing.csv', index=False)
df_test.to_csv('test/test_preprocessing.csv', index=False)