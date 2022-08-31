from graphviz import Digraph

g = Digraph('G', filename='g_c_n.gv')
g.attr(bgcolor='white', label='agraph', fontcolor='Blue')

with g.subgraph(name='cluster1') as c:
    c.attr(fillcolor='blue:cyan', label='acluster', fontcolor='white',
           style='filled', gradientangle='270')
    c.attr('node', shape='box', fillcolor='red:yellow',
           style='filled', gradientangle='90')
    c.node('anode')

g.render('Datos/prueba',format='jpg')