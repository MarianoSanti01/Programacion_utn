import sys
path=sys.path[0]
splited_path=path.split("/")
splited_path.pop()
current_path='/'.join(splited_path)
current_path=current_path+"/"
print(current_path)