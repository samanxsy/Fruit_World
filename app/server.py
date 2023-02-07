from flask import Flask, request
import Fruitvice

fruit_list = []

app = Flask("Fruit World", static_folder="./app/static")

@app.route('/')
def home():
  
  """
  The main page 
  """
    
  page = ""
  f = open("app/templates/layout.html", "r")
  page = f.read()
  f.close()
  
  fruit_info = Fruitvice.fruits_data("Apple")
  page = page.replace("Tap a fruit!", fruit_info)
  
  return page

@app.route('/fruits')
def fruits():
  
  """ 
  This function adds the new fruits to the table
  """
  
  page = ""
  f = open("app/templates/layout.html", "r")
  page = f.read()
  f.close()
  
  fruit = request.args.get("fruit")
  
  if fruit not in fruit_list:
    fruit_list.append(fruit)
    
  fruit_info = Fruitvice.fruits_data(fruit)
  mix_fruits = Fruitvice.fruit_mix(*fruit_list)
  
  page = page.replace("Tap a fruit!", fruit_info)
  page = page.replace("Tap more fruits!", mix_fruits)

  return page

@app.route('/re_sort')
def re_sort():
  
  """ 
  This function re-sorts the table based on user decision
  """
  
  page = ""
  f = open("app/templates/layout.html", "r")
  page = f.read()
  f.close()
  
  sort_type = request.args.get("sorting_type")
  mix_fruits = Fruitvice.fruit_mix(*fruit_list)
  fruit = fruit_list[1]
  fruit_info = Fruitvice.fruits_data(fruit)
  
  if sort_type == "Protein":
    sort_table = Fruitvice.sorting(*fruit_list, nutrition="Protein")
    page = page.replace("Tap more fruits!", sort_table)
    
  elif sort_type == "Sugar": 
    sort_table = Fruitvice.sorting(*fruit_list, nutrition="Sugar")
    
    page = page.replace("Tap a fruit!", fruit_info)
    page = page.replace("Tap more fruits!", sort_table)
    
  elif sort_type == "Carbohydrates": 
    sort_table = Fruitvice.sorting(*fruit_list, nutrition="Carbohydrates")
    
    page = page.replace("Tap a fruit!", fruit_info)
    page = page.replace("Tap more fruits!", sort_table)
    
  elif sort_type == "Calories":
    sort_table = Fruitvice.sorting(*fruit_list, nutrition="Calories")
    
    page = page.replace("Tap a fruit!", fruit_info)
    page = page.replace("Tap more fruits!", sort_table)
    
  elif sort_type == "Fat": 
    sort_table = Fruitvice.sorting(*fruit_list, nutrition="Fat")
    
    page = page.replace("Tap a fruit!", fruit_info)
    page = page.replace("Tap more fruits!", sort_table)
  
  else:
    
    page = page.replace("Tap a fruit!", fruit_info)
    page = page.replace("Tap more fruits!", mix_fruits)
  
  return page
  
@app.route('/reset')
def reset_list():
  
  """ 
  This function resets the list
  """
  
  global fruit_list
  fruit_list = []
  
  return home()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)