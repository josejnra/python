import os

ls = os.system("cd ~ && pwd && ls | cat -n")
print(ls)
