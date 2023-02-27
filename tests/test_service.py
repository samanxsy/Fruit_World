import unittest
import pandas as pd
from app.service import fruits_data, fruit_mix, sorting


class TestService(unittest.TestCase):

  def test_fruits_data(self):
    """This should return the information of the given fruit"""
    result = fruits_data('apple')
    assert "Apple" in result
    assert "Malus" in result
    assert "0.3" in result
    assert "11.4" in result
    assert "0.4" in result
    assert "10.3" in result
    assert "52" in result


  def test_fruit_mix(self):
    """This should return the information of the given fruits"""
    result = fruit_mix('apple', 'banana', 'orange', 'mango')
    assert "Apple" in result
    assert "Banana" in result
    assert "Orange" in result
    assert "Mango" in result


  def test_sorting(self):
    """This should return the information of the given fruits sorted by the given nutrition"""
    result = sorting("Banana", "Apple", "Orange", nutrition="Calories")
    df = pd.read_html(result)[0] 
    assert df.iloc[0]["Name"] == "Banana" 
    
    result = sorting("Orange", "Apple", "Avocado", nutrition="Fat")
    df = pd.read_html(result)[0]
    assert df.iloc[0]["Name"] == "Avocado"
