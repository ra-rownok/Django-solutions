from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pwd(request):
    var = str(request.POST['password'])

    def checkupper(var):
        upper=0
        upperlist = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'.split(',')
        for chr in var:
          if chr in upperlist:
            upper += 1
        if upper > 0:
            return True
        else:
            return False

    def checklower(var):
        lower=0
        lowerlist = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'.split(',')
        for chr in var:
          if chr in lowerlist:
            lower += 1
        if lower > 0:
          return True
        else:
          return False

    def checkspecial(var):
        special=0
        speciallist = '! @ $ % ^ & # * ( ) _ - + = { } [ ] |  \ , . > < / ? ~ ` \' " : ;'.split()
        for chr in var:
           if chr in speciallist:
              special += 1
        if special > 0:
           return True
        else:
           return False

    def checklength(var):
        if (len(var)>7):
           return True
        else:
           return False


    def checkfirst(var):
       if var[0].isnumeric():
         return True
       else:
         return False

    if checkfirst(var) == True:
      res = 'First digit cannot be number'

    elif checklength(var) == False:
      res = 'Password should have at least 8 digit'

    elif checklower(var) == False:
      res = 'Password should have Contain at least one Uppercase, Lowercase and special character'

    elif checkspecial(var) == False:
      res = 'Password should have Contain at least one Uppercase, Lowercase and special character'

    elif checkupper(var) == False:
      res = 'Password should have Contain at least one Uppercase, Lowercase and special character'

    else:
      res = 'Password is valid'

    return render(request, 'checker.html', {'result': res})