class A:
    @staticmethod
    def met_static(x):
        print(x)

    def met_not_static(self, x):
        print(x)

if __name__ == '__main__':
    A.met_static('jose')
    b = A()
    b.met_not_static(1)

