from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
stack = gateway.entry_point.getStack()
stack.get_work_time()
internal_list = stack.getInternalList()
print(internal_list)