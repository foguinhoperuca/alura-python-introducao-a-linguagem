from priority_queue import PriorityQueue
from normal_queue import NormalQueue

pq = PriorityQueue()
pq.update_queue()
pq.update_queue()
pq.update_queue()
print(pq.call_client(10))
print(pq.statistics('1993-01-10', 198, 'detail'))

nq = NormalQueue()
nq.update_queue()
nq.update_queue()
nq.update_queue()
print(nq.call_client(5))
print(nq.call_client(10))


estatistica = {'quantidade de clientes atendidos': 0}

estatistica['quantidade de clientes atendidos'] = \
    len('TESTER')

print(estatistica)

estatistica['quantidade de clientes atendidos'] = (
    len('LALALALALA')
)

print(estatistica)
