import os, inspect
if '__file__' not in locals():
    fx = inspect.getframeinfo(inspect.currentframe())[0]
else:
    fx = __file__
os_dir = os.path.dirname(os.path.abspath(fx))
print(os_dir)