#createion 
# d={}
# d[100]="durga"
# d[200]="ravi"
# d[300]="shiva"
# print(d)

# d={100: 'durga', 200: 'ravi', 300: 'shiva'}
# print(d[300])

# to update 
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d)
# d[400]="pavan"
# print(d)

# to ddelet elemets
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d)
# del d[100]
# print(d)

# to clear all 
# d={100:"durga",200:"ravi",300:"shiva"}
# d.clear()
# print(d)

# to delete dict 
# d={100:"durga",200:"ravi",300:"shiva"}
# del d
# print(d)

# fucntions
# 1.dict 
# d={100:"durga",200:"ravi",300:"shiva"}
# dict(d)
# 2.len()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(len(d))
# 3.clear() 
# d={100:"durga",200:"ravi",300:"shiva"}
# d.clear()
# print(d)
# print(clear(d))
# 4.get()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.get(100))
# 5.pop()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.pop(100))
# print(d)
# 6.pop_item()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.popitem())
# print(d)
# 7.keys()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.keys())
# print(d)
# 8.values()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.values())
# print(d)
# 9.items()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.items())
# print(d)
# 10.copy()
d={100:"durga",200:"ravi",300:"shiva"}
d1=d.copy()
print(d1)
# 11.setdefualt()
d={100:"durga",200:"ravi",300:"shiva"}
print(d.setdefault(10,"a"))
print(d)
# 12.update()
d={100:"durga",200:"ravi",300:"shiva"}
x={20:"A",10:"B"}
print(d.update(x))
print(d)