import pickle
import os
while 1:
    class Product:
        __id=1
        def __init__(self,name,group,subgroup,price):
            self.__id=Product.__id
            Product.__id=Product.__id+1
            self._name=name
            self._group=group
            self._subgroup=subgroup
            self._price=price
        def getid(self):
            return self.__id
        def getname(self):
            return self._name
        def getgroup(self):
            return self._group
        def getsubgroup(self):
            return self._subgroup
        def setid(self,id):
            self.__id=id
        def setname(self,name):
            self._name=name
        def setgroup(self,group):
            self._group=group
        def setsubgroup(self,subgroup):
            self._subgroup=subgroup
        def getprice(self):
            return self._price
        def setprice(self,price):
            self._price=price
        
        


        

    class Admin:
        __id=1
        def __init__(self,name):
            self.__id=Admin.__id
            Admin.__id=Admin.__id+1
            self.__name=name
        def getid(self):
            return self.__id
        def getname(self):
            return self.__name
        def setname(self,name):
            self.__name=name
        def VeiwProduct(self):
            pickle_in=open("dict.pickle","rb")
            example_dict=pickle.load(pickle_in)
            print "hello"
            for i in example_dict:
                print "Name  : "+ example_dict[i].getname()
                print "ProdID: ", example_dict[i].getid()
                print "Group : "+ example_dict[i].getgroup()
                print "SubGrp: "+ example_dict[i].getsubgroup()
                print "Price : ", example_dict[i].getprice()

            pass
        def AddProduct(self):
            if(os.path.isfile("dict.pickle")):
                
            #check if nothing is there in file'
                    print "Enter Product name"
                    name=raw_input()
                    print "Enter Product Group" 
                    group=raw_input()
                    print "Enter Product Subgroup"
                    subgroup=raw_input()
                    print "Enter Product Price"
                    price=input()
                    example_dict={}
                    pickle_in=open("dict.pickle","rb")
                    example_dict=pickle.load(pickle_in)
                    pd=Product(name,group,subgroup,price)
                    example_dict[pd.getid()]=pd
                    pickle_in.close()
                    pickle_out=open("dict.pickle","wb")
                    pickle.dump(example_dict,pickle_out)
                    pickle_out.close()
                    print "Inserted Product with id ",pd.getid()
                    # self.VeiwProduct()
            else:
                    print "Enter Product name"
                    name=raw_input()
                    print "Enter Product Group" 
                    group=raw_input()
                    print "Enter Product Subgroup"
                    subgroup=raw_input()
                    print "Enter Product Price"
                    price=input()  
                    example_dict={}
                    pd=Product(name,group,subgroup,price)
                    example_dict[pd.getid()]=pd
                    pickle_out=open("dict.pickle","wb")
                    pickle.dump(example_dict,pickle_out)
                    pickle_out.close()
                    print "Inserted Product with id ",pd.getid()
                    # self.VeiwProduct()
            pass
        def DeleteProduct(self):
            example_dict={}
            pickle_in=open("dict.pickle","rb")
            example_dict=pickle.load(pickle_in)
            print "Enter the Product Id to Remove"
            id2=input()
            if(id2 in example_dict):

                #pd=Product("Tshirt","garments","Men",100)
                del example_dict[id2]
                pickle_in.close()
                pickle_out=open("dict.pickle","wb")
                pickle.dump(example_dict,pickle_out)
                pickle_out.close()
                print "Deleted Product with id ",id2
                # self.VeiwProduct()
            else:
                print "Not a valid Key"
            pass
        def ModifyProduct(self):  
            example_dict={}
            pickle_in=open("dict.pickle","rb")
            example_dict=pickle.load(pickle_in)
            print "Enter the Product Id to Modify"
            id2=input()
            if(id2 in example_dict):
            #pd=Product("Tshirt","garments","Men",100)
                p4=example_dict[id2]
                print "Enter Product name"
                name=raw_input()
                print "Enter Product Group" 
                group=raw_input()
                print "Enter Product Subgroup"
                subgroup=raw_input()
                print "Enter Product Price"
                price=input()
                p4.setname(name)
                p4.setgroup(group)
                p4.setsubgroup(subgroup)
                p4.setprice(price)
                example_dict[id2]=p4
                # del example_dict[id2]
                # p4=example_dict[id2]
                # print "Press 1 For Modifying ID"
                pickle_in.close()
                pickle_out=open("dict.pickle","wb")
                pickle.dump(example_dict,pickle_out)
                pickle_out.close()
                print "Modified Product with id ",id2
            else:
                print "Not a Valid Key"
            pass 
        def MakeShipment(self):
            pass
        def ConfirmDelivery(self):
            pass

    class Customer:
        __id=1
        def __init__(self,name,Address,Phno):
            self.__id=Customer.__id
            Customer.__id=Customer.__id+1
            self._name=name
            self._Address=Address
            self._Phno=Phno
        def getid(self):
            return self.__id
        def getname(self):
            return self._name
        def setname(self,name):
            self._name=name
        def getAddress(self):
            return self._Address
        def setAddress(self,Address):
            self._Address=Address
        def getPhno(self):
            return self._Phno
        def setPhno(self,Phno):
            self._Phno=Phno
        def VeiwProduct(self):
            pickle_in=open("dict.pickle","rb")
            example_dict=pickle.load(pickle_in)
            #print "hello"
            for i in example_dict:
                print "Name  : "+ example_dict[i].getname()
                print "ProdID: ", example_dict[i].getid()
                print "Group : "+ example_dict[i].getgroup()
                print "SubGrp: "+ example_dict[i].getsubgroup()
                print "Price : ", example_dict[i].getprice()

            pass
        def BuyProduct(self):
        
            print "Enter the Product id you want to buy"
            id2=input()
            pickle_in=open("dict.pickle","rb")
            example_dict=pickle.load(pickle_in)
            if(id2 in example_dict):
                print "Press 1 to add this product to cart"
                print "Press 2 to directly buy this product"
                x=input()
                if(x==1):
                   self.AddToCart(id1)
                elif(x==2):
                   self.MakePayment(id1)
            else:
                print "No Product with Given id"
      
            pass
        def MakePayment(self,id1):
            pass
        def AddToCart(self):
            pr=[]
            # cart1={1:pr}
            print "Enter The product id you want to add to cart"
            id1=input()
            if(os.path.isfile("dict.pickle")):
                pickle_in=open("dict.pickle","rb")
                example_dict=pickle.load(pickle_in)
                if(id1 in example_dict):
                    if(os.path.isfile("cart.pickle")):
                        cart_in=open("cart.pickle","rb")
                        cart_dict=pickle.load(cart_in)
                        if(self.__id in cart_dict):
                            ct=cart_dict[self.__id]
                            pr=ct.getproductlist()
                            ct.setproductno=ct.getproductno()+1
                            ct.settotal(ct.gettotal()+example_dict[id1].getprice())
                            pr.append(example_dict[id1])
                            ct.setproductlist(pr)
                            # ct=Cart()
                            cart_dict[self.__id]=ct
                            cart_in.close()
                            cart_in=open("cart.pickle","wb")
                            # cart_dict=pickle.load(cart_in)

                        else:
                            
                            pr.cart_dict[self.__id]=prappend(example_dict[id1])
                            ct=Cart(1,example_dict[id1].getprice(),pr)
                            cart_dict[self.__id]=ct
                            cart_in.close()
                            cart_in=open("cart.pickle","wb")
                            # cart_dict=pickle.load(cart_in)
                        pickle.dump(cart_dict,cart_in)
                        cart_in.close()
                        pickle_in.close()
                    else:
                        
                        cart_in=open("cart.pickle","wb")
                        cart_dict={}
                        pr.append(example_dict[id1])
                        ct=Cart(1,example_dict[id1].getprice(),pr)
                        cart_dict[self.__id]=ct
                        pickle.dump(cart_dict,cart_in)
                        cart_in.close()
                        pickle_in.close()
                        

                else:
                    print "Not a valid Product id"
            else:
                print "Oops Something went wrong with database"
            pass   
        def DeleteFromCart(self):
            print "Enter the product id You want to delete"
            id1=input()
            if(os.path.isfile("cart.pickle")):
                cart_in=open("cart.pickle","rb")
                cart_dict=pickle.load(cart_in)
                cart_in.close()
                if(self.__id in cart_dict):
                    cartobj=cart_dict[self.__id]
                    pr=cartobj.getproductlist()
                    for j in pr:
                        if(j.getid()==id1):
                             pr.remove(j)
                    cartobj.setproductlist(pr)
                    cart_dict[self.__id]=cartobj
                    cart_in=open("cart.pickle","wb")
                    pickle.dump(cart_dict,cart_in)
                    cart_in.close()
                else:
                    print "Your Cart is Empty"
            else:
                print "Your Cart is Empty"
            pass
        def VeiwCart(self):
            cart_in=open("cart.pickle","rb")
            cart_dict=pickle.load(cart_in)
            print "Cart of User : ",self._name
            print
            cartobj=cart_dict[self.__id]
            pr=cartobj.getproductlist()
            for j in pr:
                print "Name  : "+ j.getname()
                print "ProdID: ", j.getid()
                print "Group : "+ j.getgroup()
                print "SubGrp: "+ j.getsubgroup()
                print "Price : ", j.getprice()
                
            pass
    class Guest:
        __Guest_Number=1
        def __init__(self):
            self.__Guest_Number=Guest.__Guest_Number
            Guest.__Guest_Number=Guest.__Guest_Number+1
        def getid(self):
            return self.__Guest_Number
        def VeiwProduct(self):
            pickle_in=open("dict.pickle","rb")
            example_dict=pickle.load(pickle_in)
            #print "hello"
            for i in example_dict:
                print "Name  : "+ example_dict[i].getname()
                print "ProdID: ", example_dict[i].getid()
                print "Group : "+ example_dict[i].getgroup()
                print "SubGrp: "+ example_dict[i].getsubgroup()
                print "Price : ", example_dict[i].getprice()
            pass
        def GetRegistered(self):
            if(os.path.isfile("cust.pickle")):
                
            #check if nothing is there in file
                    print "Enter Your Name"
                    name=raw_input()
                    print "Enter Your Address" 
                    add=raw_input()
                    print "Enter Your Phone Number"
                    phno=input()
                    example_dict={}
                    pickle_in=open("cust.pickle","rb")
                    example_dict=pickle.load(pickle_in)
                    pd=Customer(name,add,phno)
                    example_dict[pd.getid()]=pd
                    pickle_in.close()
                    pickle_out=open("cust.pickle","wb")
                    pickle.dump(example_dict,pickle_out)
                    pickle_out.close()
                    print "Inserted Customer with id ",pd.getid()
                    # self.VeiwProduct()
            else: 
                    print "Enter Your Name"
                    name=raw_input()
                    print "Enter Your Address" 
                    add=raw_input()
                    print "Enter Your Phone Number"
                    phno=input()
                    example_dict={}
                    pd=Customer(name,add,phno)
                    example_dict[pd.getid()]=pd
                    pickle_out=open("cust.pickle","wb")
                    pickle.dump(example_dict,pickle_out)
                    pickle_out.close()
                    print "Inserted Customer with id ",pd.getid()

            pass
    class Cart:
        __id=1
        def __init__(self,NumOfProduct,Total,ProductList):
            self.__id=Cart.__id
            Cart.__id=Cart.__id+1
            self._NumOfProduct=NumOfProduct
            self._ProductList=ProductList
            self._Total=Total
        def getid(self):
            return self.__id
        def getproductno(self):
            return self._NumOfProduct
        def getproductlist(self):
            return self._ProductList
        def gettotal(self):
            return self._Total
        def settotal(self,Total):
            self._Total=Total
        def setproductno(self,NumOfProduct):
            self._NumOfProduct=NumOfProduct
        def setproductlist(self,ProductList):
            self._ProductList=ProductList
    # class Payment:
    #     def __init__(self,custid,prodname,cardtype,cardno):
    #         self.__custid=cust_id
    #         # Cart.__id=Cart.__id+1
    #         self._prodname=NumOfProduct
    #         self._ProductList=ProductList
    #         self._Total=Total    
        


    # p1 = Product("Dhawal","1","1")
    # print p1.getname()
    # print p1.getid()
    # p2 = Product("Darshan","1","1")
    # print p2.getname()
    # print p2.getid()
    # print p2.getgroup()
    # print p2.getsubgroup()

    # p3 = Admin("Dhawal")
    # print "Welcome "+p3.getname()
    # print p3.getid()
    # while 1:
    #     p3.AddProduct()
    # p4 = Admin("Darshan")
    # print p4.getname()
    # print p4.getid()
    # p5 = Customer("Dhawal","dbdjkk",9759)
    # print p5.getname()
    # print p5.getid()
    # print p5.getAddress()
    # print p5.getPhno()
    # p6 = Customer("Darshan","sjkks",7854)
    # print p6.getname()
    # print p6.getid()
    # print p6.getAddress()
    # print p6.getPhno()
    print "Press 1 For Admin"
    print "Press 2 For Customer"
    print "Press 3 For GuestUser"
    type1=input()
    if(type1==1):
        print "Enter your Name"
        name=raw_input()
        p3 = Admin(name)
        print "Hello "+name
        while(1):
            print "Press 1 For AddProduct"
            print "Press 2 For Deleteproduct"
            print "Press 3 For VeiwProduct"
            print "Press 4 For ModifyProduct"
            print "Press 5 For MakeShipment"
            print "Press 6 For Logout"
            x=input()
            if(x==1):
                p3.AddProduct()
            if(x==2):
                p3.DeleteProduct()
            if(x==3):
                p3.VeiwProduct()
            if(x==4):
                p3.ModifyProduct()
            if(x==5):
                p3.MakeShipment()
            if(x==6):
                break
    elif(type1==2):
        print "Enter your Name"
        name=raw_input()
        print "Enter Your Address"
        add=raw_input()
        print "Enter Your Phone Number"
        phno=input()
        p3 = Customer(name,add,phno)
        while(1):
            print "Press 1 For VeiwProduct"
            print "Press 2 For Buyproduct"
            print "Press 3 For MakePayment"
            print "Press 4 For AddToCart"
            print "Press 5 For DeleteFromCart"
            print "Press 6 For VeiwCart"
            print "Press 7 For Logout"
            x=input()
            if(x==1):
                p3.VeiwProduct()
            if(x==2):
                p3.BuyProduct()
            if(x==3):
                p3.MakeProduct()
            if(x==4):
                p3.AddToCart()
            if(x==5):
                p3.DeleteFromCart()
            if(x==6):
                p3.VeiwCart()
            if(x==7):
                break

    elif(type1==3):
        p3 = Guest()
        while(1):
            print "Press 1 For Veiw Product"
            print "Press 2 For Get registered"
            # print "Press 3 For Logout"
            x=input()
            if(x==1):
                p3.VeiwProduct()
            if(x==2):
                p3.GetRegistered()
                print "You Are Registered Please Login As Customer"
                break
            
    


    
