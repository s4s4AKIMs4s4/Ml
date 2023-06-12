from faker import Faker
import random
import pandas as pd
import os

index = -1
def Generator():
  Y = 3
  Z = 5
  def priceGenetorByDate(date):
      global index 
      index += 1;
      if(date.month>=9 and date.month<12):
        return index * Y**3 + Z + random.randint(1,5)
      elif(date.month<=2 or date.month>=12):
        return index * Y**2 + Z + random.randint(1,10)
      else:
        return index * Y + Z + random.randint(1,3)
  return priceGenetorByDate

def generatePriceDate(N):
  df = pd.DataFrame(
    [
        {
            
            "date": fake.date_this_century(),
            "time": fake.time(),
            "price": 0,
        }
        for _ in range(N)
    ]
  )
  generator = Generator()
  df['price'] = df['date'].apply(lambda x: generator(x))
  return df

def saveData(df, directory, path):
  if not os.path.isdir(directory):
      os.mkdir(directory)
  df.to_csv (path, index= False )


fake = Faker()

df_train = generatePriceDate(1000)
saveData(df_train,'train', 'train/train.csv')

df_test = generatePriceDate(300)
saveData(df_train,'test','test/test.csv')
