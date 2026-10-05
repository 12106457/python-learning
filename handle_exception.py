try:
    with open('dumps.txt','r') as file:
        data=file.read()
        print(data)
except Exception as e:
    print("Something went wrong:", e)