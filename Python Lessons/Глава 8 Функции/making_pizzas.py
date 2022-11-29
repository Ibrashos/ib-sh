from pizza import *
make_pizza(16, 'peperoni')
make_pizza(12, 'peperoni','mushrooms','extra cheese')


import pizza as pz
pz.make_pizza(16, 'peperoni')
pz.make_pizza(12, 'peperoni','mushrooms','extra cheese')

from pizza import make_pizza
make_pizza(16, 'peperoni')
make_pizza(12, 'peperoni','mushrooms','extra cheese')


from pizza import make_pizza as mp
mp(16, 'peperoni')
mp(12, 'peperoni','mushrooms','extra cheese')