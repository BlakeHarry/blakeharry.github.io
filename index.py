from re import X
import pyodide

print("Hello Harry from .py")

def my_function(e):
    x = inputHandle.value
    try:
        x = int(x)
    except:
        outputHandle.innerText = "This should be a number!"
    else:
        if x % 2 == 0:
            outputHandle.innerText = "This is an even number!"
        else:
            outputHandle.innerText = "This is an odd number"


    

changeButtonHandle = document.getElementById('change_me')

inputHandle = document.getElementById('input')
outputHandle = document.getElementById('output')

changeButtonHandle.addEventListener('click', pyodide.create_proxy(my_function))
