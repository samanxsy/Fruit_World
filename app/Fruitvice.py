import requests
import pandas as pd

def fruits_data(fruit):
  """
  This functions receives the Fruit name as input, and will sort out the information about the fruit
  """

  url = f"https://fruityvice.com/api/fruit/{fruit}"
  response = requests.get(url)
  data = response.json()
  ntr = data['nutritions']

  information = [{'Name': data['name'], 'Genus': data['genus'], 'Family': data['family']}]
  nutrition = [{'Carbohydrates': ntr['carbohydrates'], 'Protein': ntr['protein'], 'Fat': ntr['fat'], 'Calories': ntr['calories'], 'Sugar': ntr['sugar']}]

  df = pd.DataFrame(information)
  df2 = pd.DataFrame(nutrition)

  information_table = df.to_html(index=False, classes="info_table")
  nutrition_table = df2.to_html(index=False, classes="ntr_table")

  full_table = f"""
  <div class="about">About</div>
  {information_table}
  <div class="ntr_facts">Nutrition Facts (in 100g)</div>
  {nutrition_table}
  """

  return full_table

def fruit_mix(*fruits):
  """
  This function creates a table of all the selected fruits, and sums all the nutritions
  """

  fruit_table = []
  for fruit in fruits:
    url = f"https://fruityvice.com/api/fruit/{fruit}"
    response = requests.get(url)
    data = response.json()
    ntr = data['nutritions']
    fruit_table.append({'Name': data['name'], 'Carbohydrates': ntr['carbohydrates'], 'Protein': ntr['protein'], 'Fat': ntr['fat'], 'Calories': ntr['calories'], 'Sugar': ntr['sugar']})

  df3 = pd.DataFrame(fruit_table)
  df3 = df3.append({'Name': 'Total', 'Carbohydrates': df3['Carbohydrates'].sum(), 'Protein': df3['Protein'].sum(), 'Fat': df3['Fat'].sum(), 'Calories': df3['Calories'].sum(), 'Sugar': df3['Sugar'].sum()}, ignore_index=True)

  mix_table = df3.to_html(index=False, classes="mix_table")

  return mix_table

def sorting(*fruits, nutrition=None):

  """
  This function will sort the table based on user need
  """

  fruit_table = []
  for fruit in fruits:
    url = f"https://fruityvice.com/api/fruit/{fruit}"
    response = requests.get(url)
    data = response.json()
    ntr = data['nutritions']
    fruit_table.append({'Name': data['name'], 'Carbohydrates': ntr['carbohydrates'], 'Protein': ntr['protein'], 'Fat': ntr['fat'], 'Calories': ntr['calories'], 'Sugar': ntr['sugar']})

  df3 = pd.DataFrame(fruit_table)
  if nutrition:
    df3 = df3.sort_values(by=nutrition, ascending=False)

  df3 = df3.append({'Name': 'Total', 'Carbohydrates': df3['Carbohydrates'].sum(), 'Protein': df3['Protein'].sum(), 'Fat': df3['Fat'].sum(), 'Calories': df3['Calories'].sum(), 'Sugar': df3['Sugar'].sum()}, ignore_index=True)

  mix_table = df3.to_html(index=False, classes="mix_table")

  return mix_table
