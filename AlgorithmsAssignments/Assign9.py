from queue import Queue 
def pageFaults(pages, n, capacity): 
	
	s = set() 
	indexes = Queue() 
	page_faults = 0
	for i in range(n): 
		if (len(s) < capacity): 
			if (pages[i] not in s): 
				s.add(pages[i]) 
				page_faults += 1
				indexes.put(pages[i]) 
		else: 
			if (pages[i] not in s): 
				val = indexes.queue[0] 
				indexes.get() 
				s.remove(val) 
				s.add(pages[i]) 
				indexes.put(pages[i]) 
				page_faults += 1
	return page_faults 

if __name__ == '__main__': 
    pages = []
    n = int(input("Enter the size of pages : "))
    print("Enter the pages:")
    for i in range(0, n):
       
        item = int(input())
        pages.append(item)
    print("User page list is ", pages)
    capacity = int(input("Enter the capacity for the pages : "))
    print(pageFaults(pages, n, capacity))