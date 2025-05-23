x=lambda a:"*" if a==1 else "*   "*a+"\n\n\n" + x(a-1)
print(x(5))