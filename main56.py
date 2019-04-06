
f1=open("fileio.text")
try:
    f=open("vishal.text")
except Exception as e:
    print(e)
else:
    print("This will run only if except is not running")
finally:
    print("run this anyway...............")
    # f.close()
    f1.close()

print("important stuff")


