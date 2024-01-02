Purpose of this repository is to showcase some basic Python proficiancy and to give me space to work with and learn new techniques in Python.

Current State of the project
-------------------------------
Sucessfully grabs data using subprocess.run()
Parses the results using Regex to get the data and the and labels.
Properly displays the data in a format that is easily read and understood.

Future Features
-------------------------------
- The ability to run the script every minute or second could be implemented in python
using sleep but that is not the cleanest and is prone to errors. I will be looking to
implement a service that runs the data collection command periodically but that might be outside of the scope of this repository
- Add functionality to calculate the average/median utilization of each device. This will go hand in hand with making the script into a service.
- display all devices data at once. This was the initial idea but the format made the tables too small. Not a large fix but for development
it will be easier to catch mistakes in calculations with only one table displayed.
