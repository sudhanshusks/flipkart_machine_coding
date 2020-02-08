import sys

def read_file_byline(file_name):
    content= []
    try:
        with open(file_name, 'r') as f:
            for line in f.readlines():
                content.append(line.rstrip())
        f.close()
    except Exception as e:
        print(e)
    return content

def read_file_byelement(file_name):
    content= []
    try:
        with open(file_name, 'r') as f:
            for line in f.readlines():
                ls= line.split(",")
                content.append([x.rstrip() for x in ls])
        f.close()
    except Exception as e:
        print(e)
    return content

def sort_file(file_name, sort_type, sort_by):
    content= list(read_file_byelement(file_name))
    print(content)
    if(sort_type== "desc"):
        if(sort_by > len(content[0])):
            print("Column number is out of bound")
            return 
        print(sorted(content, key= lambda x:x[sort_by-1], reverse= True))
    elif(sort_type=="ascen"):
        if(sort_by > len(content[0])):
            print("Column number is out of bound")
            return 
        print(sorted(content, key= lambda x:x[sort_by-1]))
    else:
        print("Sort type is not correct")

def join_files(file1, col1, file2, col2):
    content1= read_file_byelement(file1)
    content2= read_file_byelement(file2)
    print(content1)
    print(content2)
    visited= []
    for i in range(len(content2)):
        visited.append(False)
    output= []
    for row1 in content1:
        val1= row1[col1-1]
        count= -1
        flag= False
        for row2 in content2:
            count= count+1
            val2= row2[col2-1]
            if(val1==val2):
                flag= True
                ls= list(row1)
                # print(ls)
                ls2= [row2[i] for i in range(len(row2)) if(i != col2-1)]
                # print(ls2)
                visited[count]= True
                ls.extend(ls2)
                output.append(ls)
        if(flag == False):
            ls= list(row1)
            ls2= ["NULL"*(len(content2[0])-1)]
            ls.extend(ls2)
            output.append(ls)
    for i in range(len(visited)):
        if(visited[i] == False):
            print("visited ", i, " is false")
            ls= ["NULL"*len(content1[0])]
            ls[col1-1]= content2[i][col2-1]
            ls2= [content2[i][j] for j in range(len(content2[i])) if(j != col2-1)]
            ls.extend(ls2)
            output.append(ls)
    print(output)

def comm_file(file1, file2, operation):
    content1= read_file_byline(file1)
    content2= read_file_byline(file2)
    print(content1)
    print(content2)
    output= []
    if(operation=="O1"):
        for line in content1:
            if(line not in content2):
                output.append(line)
    if(operation=="O2"):
        for line in content2:
            if(line not in content1):
                output.append(line)
    if(operation=="O3"):
        for line in content1:
            if(line in content2):
                output.append(line)
    if(operation=="O4"):
        for line in content1:
            output.append(line)
        for line in content2:
            if(line not in content1):
                output.append(line)
    print(output)

def fgrep_files(file1, file2):
    content1= read_file_byline(file1)
    content2= read_file_byline(file2)
    print(content1)
    print(content2)
    output= []
    for line in content1:
        for line2 in content2:
            if(line in line2):
                output.append(line)
    print(output)


if __name__=='__main__':
    args= sys.argv
    print(args)
    if(len(args) >1):
        if(args[1] == "sort"):
            col_num= args[2]
            order= args[3]
            file_name= args[4]
            sort_file(file_name, order, int(col_num))
        if(args[1] == "join"):
            file1= args[2]
            col1= args[3]
            file2= args[4]
            col2= args[5]
            join_files(file1, int(col1), file2, int(col2))
        if(args[1] == "comm"):
            operation= args[2]
            file1= args[3]
            file2= args[4]
            comm_file(file1, file2, operation)
        if(args[1]== "fgrep"):
            file1= args[2]
            file2= args[3]
            fgrep_files(file1, file2)
    else:
        print("nothing called")
