# Basic Weather App
import requests
print("\t\tWelcome to the weather Forecaster!\n\n")
print("Just Enter the City you want the weather report for and click on the buttom! It's that simple!\n\n")
city_name = input("Enter the name of the City:")
print("\n\n")
def Gen_report(C):
    # Function to generate report 
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occured"
    print(T)
Gen_report(city_name)