def table(operation,num_rows,num_columns):   
    for i in range(1,num_rows+1):
        print()
        for j in range(1,num_columns+1):
            print(operation(i,j),end="\t" )

table(lambda x, y: x * y,6,6)