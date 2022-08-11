import pyodide

print("Hello Harry from .py")

def my_function(e):
    outputHandle.innerText = int(inputHandle.value) * 2

changeButtonHandle = document.getElementById('change_me')

inputHandle = document.getElementById('input')
outputHandle = document.getElementById('output')

changeButtonHandle.addEventListener('click', pyodide.create_proxy(my_function))
