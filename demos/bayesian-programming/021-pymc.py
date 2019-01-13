import pymc3 as pm

with pm.Model() as model:
    my_discrete_uniform_var = pm.DiscreteUniform('discrete_uniform_var', 0, 4)

with model:
    print(my_discrete_uniform_var.tag.test_value)

# you can examine a variable outside its model context once the variable has been defined.
print(my_discrete_uniform_var.tag.test_value)
# test value does not change if you sample it again.
print(my_discrete_uniform_var.tag.test_value)
