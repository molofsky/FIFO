# Circular Buffer Implementation
def push(flit):
  mem[tail] = flit
  tail += 1
  if tail > LAST:
    tail = FIRST

def pop():
  flit = mem[head]
  head += 1
  if head > LAST
    head = FIRST
  return flit

# Linked List <-- allows for multiple FIFOs
"""
def push(flit):
  mem[free] = flit
  if tail != None:
    ptr[tail] = Free
  tail = free
  free = ptr[free]
  ptr[tail] = None
  if head == None:
    head = tail
"""
