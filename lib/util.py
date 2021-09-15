# Utility methods for Python-for-JavaScript-Developers notebooks

# libraries
import sys
import traceback
from IPython.core.display import HTML

def testHTML():
    display(HTML('<h1>HELLO!</h1>'))

def printError():
    """
    Simple error handling while allowing the rest of the notebook to continue.
    
    Note that this uses the latest error and prints to the display.
    (No arguments or return results)
    """
    
    # use the latest error
    exType, exValue, exTraceback = sys.exc_info()
    traceBack = traceback.extract_tb(exTraceback)
    
    stackTrace = list()
    for trace in traceBack:
        stackTrace.append(f"File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Message: {trace[3]}")
        
    if (exType is None):
        print('printError(): no recent error found')
        return
    
    # print("Exception type : %s " % exType.__name__)
    # print("Exception message : %s" %exValue)
    # print("Stack trace : %s" %stackTrace)
    errorMsg = f"""
<div><pre style='background-color:rgb(255,221,221);'>
---------------------------------------------------------------------------
<span style='color:rgb(231,92,88);'>ErrorType: {exType.__name__}</span>
Message: {exValue}
Stack trace:
{stackTrace}
---------------------------------------------------------------------------
</pre></div>
"""
    
    display(HTML(errorMsg))