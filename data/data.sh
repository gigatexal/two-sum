python3 -c "import random; l=[str(random.randint(1,1024)) for x in range(33)]; print(' '.join(l),end=''); print(' '); print(int(random.choice(l))+int(random.choice(l)), end='')" > ./data.txt
