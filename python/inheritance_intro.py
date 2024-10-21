# class syn:
#     def python():
#         print('python')
#     def php():
#         print('php')
#     def mern():
#         print('mern')
# class novavi(syn):
#     def web_dev():
#         print('web_dev')
#     def dm():
#         print('dm')
# student1 = syn
# student1.python()
# staff1 = novavi
# staff1.python()
# staff1.dm()

class adidas:
    def shoes(self):
        print('shoes')
    def t_shirts(self):
        print('t_shirts')
class flipkart(adidas):
    def clothes(self):
        print('clothes')
    def watch(self):
        print('watch')
cust1=adidas()
cust1.t_shirts()
cust2=flipkart()
cust2.shoes()
cust2.watch()

