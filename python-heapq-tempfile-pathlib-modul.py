
import heapq
a = [1, 2, 3, 5, 6, 8, 7]
print(a) # [1, 2, 3, 5, 6, 8, 7]
print(heapq.heappop(a)) # # 1
print(a) # [2, 5, 3, 7, 6, 8]
print(heapq.heappop(a)) # # 2
print(a) # [3, 5, 8, 7, 6]
print(a.pop()) #  6






from heapq import *
def heapsort(iterable):
    h = []
    for  value in iterable:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]

print(heapsort([1,3,44,11,22,244])) #[1, 3, 11, 22, 44, 244]




import math
from io import StringIO
def show_tree(tree, total_width=60, fill=' '):
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

import heapq
heap = []
heapq.heappush(heap, (1, 'one', 2))
heapq.heappush(heap, (1, 'one', 3))
heapq.heappush(heap, (1,'one', 1))
heapq.heappush(heap, (1,'one', 4))
heapq.heappush(heap, (1,'one', 5))
heapq.heappush(heap, (1,'one', 6))
heapq.heappush(heap, (1,'one', 89))
show_tree(heap)





import heapq
mylist = [120, -34, 0, 56, 444, 78]
print(heapq.nlargest(2, mylist)) # [444, 120]
print(heapq.nsmallest(3, mylist)) # [-34, 0, 56]





from pathlib import Path
yeni_yol = Path("yenidizin", "yenidosya.txt")
print(yeni_yol) 
##  cıktı
## yenidizin/yenidosya.txt





from pathlib import Path

home = Path.home()
wave_absolute = Path(home, "yenidizin", "yenidosya.txt")
print(home) # /home/pcismi
print(wave_absolute) # /home/pcismi/yenidizin/yenidosya.txt




from pathlib import Path

dosya_yolu = Path("yenidizin", "yenidosya.txt")
print(dosya_yolu) #yenidizin/yenidosya.txt
print(dosya_yolu.name) # yenidosya.txt
print(dosya_yolu.suffix) # .txt






import tempfile
# gecici dosya yeri
print(tempfile.gettempdir())
#gecici dosya olusmadıysa none doner olusmus ise dosya ismini doner
#print(tempfile.tempdir)  # none





import tempfile


def edit(base):
    tmp = tempfile.NamedTemporaryFile(mode='w+')
    print(tempfile.tempdir) # /tmp
    #fname = tmp.name
    tmp.write(base)
    tmp.seek(0, 0)  # This will rewind the cursor
    #system('nano %s' % fname)
    content = tmp.readlines()
    tmp.close()
    return content

answer = "hi"
print(edit(answer))
