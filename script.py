def my_function(): 
    if True:
        local_var = "Hello"
    print(local_var)  # This is in local scope

my_function() # This this works fine
print(local_var) # This will raise a NameError
