"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format
The first line contains an integer, n, denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above.

Constraints
The elements added to the list must be integers.

Output Format
For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

#Solution
if __name__ == '__main__':
    N = int(raw_input())
    a=[]
    for i in range(N):
        x=raw_input().split(" ")
        command=x[0]
        if command == 'append':
            a.append(int(x[1]))
        if command == 'print':
            print(a)
        if command == 'insert':
            a.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            a = a[::-1]
        if command == 'pop':
            a.pop()
        if command == 'sort':
            a = sorted(a)
        if command == 'remove':
            a.remove(int(x[1]))
