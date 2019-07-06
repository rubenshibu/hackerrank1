a = 1
try:
    q = int(input())
except ZeroDivisionError:
    print("0")

except:
    print("1")
else:
    print("2")
finally:
    pass
print("3")