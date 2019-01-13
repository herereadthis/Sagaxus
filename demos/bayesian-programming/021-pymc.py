import pymc3 as pm

with pm.Model() as model:
    my_discrete_uniform_var = pm.DiscreteUniform('discrete_uniform_var', 0, 4)

with model:
    print(my_discrete_uniform_var.tag.test_value)

# this seems to work too
print(my_discrete_uniform_var.tag.test_value)
