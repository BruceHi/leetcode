class CL:
    def __init__(self):
        print('ini')

    def __del__(self):
        print('del')


print(CL() == CL())
#
print(id(CL()) == id(CL()))
