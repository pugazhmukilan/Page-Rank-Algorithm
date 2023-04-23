# page rank algorith implementation
import numpy as np

#the information
'''here the page and their link are given like a dictionary '''



pages={'A':['B','C','D'],'B':['D'],'C':['A','D'],'D':[]}
order=len(pages)
pagelist=['A','B','C','D']


#initial matrix with one  as the element
initial_matrix=np.ones((order,1))

def find_matrix(pages,pagelist):
    #find the ranke of the pages
    #main fucntion for the program to operate

    #creation of matrix

    page_matrix = np.zeros((order, order))
    row=0
    column=0
    for i in (pages):
        row=0
        if (len(pages[i])!=0):
                share=1/(len(pages[i]))
                
                share2=0

        else:
            share2=(1/order)
            
            share=share2
            
        for j in (pagelist):
            
            
            if (j in pages[i]):
                page_matrix[row,column]=share
                
            else:
                page_matrix[row,column]=share2
                
            

            #this condition is for when the oage dosent link any oof the other pages

           
            
            row+=1
            
        column+=1
    print("Page Matrix is : \n",page_matrix)
    return page_matrix



def find_rank(page_matrix,initial_matrix1):
    initial=initial_matrix1
     #find the rank of the pages
    global master_order
    master_order=[]
    def orderlist(matrix):
         #find the order  of the list
        
        sort_matrix=np.sort(matrix, axis=0)[::-1]
        
        num=1
        order_list=[]
        for i in (sort_matrix):
            row_indices, column_indices = np.where(matrix == i)    
            order_list.insert(row_indices[0],num)
            num+=1
        master_order.append(order_list)
        return orderlist
    
    bool=True
    num=0
    while(bool):
        
        initial_matrix=np.matmul(page_matrix,initial)
        
        
        initial=initial_matrix
        
       
        orderlist(initial_matrix)
        if num>0:
            
            if master_order[len(master_order)-2]==master_order[len(master_order)-1]:
                
                bool=False
                num+=1
                break
            else:
                num+=1
        else:
            num+=1
            pass

    
    #giving the rank to the pages final method
    unsortlist=master_order[len(master_order)-2]
    sortlist=master_order[len(master_order)-1]
    sortlist.sort()
    


    rank_list=[]
    num=0
    
    for i in (sortlist[::-1]):
        rank_list.insert(num,pagelist[(unsortlist.index(i))])
        num+=1

    rank=1
    for i in rank_list:
        print("Rank ",rank,"------",i)
        rank+=1



    

    
    
find_rank(find_matrix(pages,pagelist),initial_matrix)
