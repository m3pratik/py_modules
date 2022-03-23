#File Handling

f = open('student.txt','w')

print('File Name: ', f.name)
print('File Mode', f.mode)
print('Is file Readable: ',f.readable())
print('Is file Writable: ',f.writable())
print('Is file Closed: ',f.closed)

f.close()

print('Is file Closed: ',f.closed)
