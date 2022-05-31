def print_L(n,m):

    for i in range(1,n+1):

        for j in range(1,m+1):

            if(i == 1 or j == 1 or i == n or j == m):

                print(' *', end='')

            else:

                print('  ', end='')

        print('')

rows = 5

columns = 5

print_L(rows, columns)