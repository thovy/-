article = input()

cword = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

answer = 0

newarticle = article
for i in cword:
  answer += newarticle.count(i)
  newarticle = newarticle.replace(i,"*")

print(len(newarticle))