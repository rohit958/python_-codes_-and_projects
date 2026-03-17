string='XVI'

ref={'I':1,
     'V':5,
     'X':10,
     'L':50,
     'C': 100,
     'M': 500
     }
def convert(string):
  result=0
  for x in range(len(string)-1):
    if ref[(string(x))]< ref[(string(x+1))]:
      result+=(ref[string(x+1)]-ref[string(x)])
    else:
      result+=ref[string(x)]
  return result

print(convert(string))