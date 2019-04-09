import traceback

#huffman_encode: Takes in a single String input_string, which is
# the string to be encoded.  Computes the optimal binary encoding
# of the string and encodes it, returning a String of 0s and 1s.
# This is not an actual Python binary string, just a normal String
# that happens to contain only 0s and 1s.
class Node:
    def __init__(self,char,frq):
        self.c = char
        self.f = frq
        self.parent = None
        self.left = None
        self.right = None
    def __repr__(self):
        return "{:5}:{}".format(self.c,self.f)
def min_heapify(key,i):
    left = i*2+1
    right = i*2+2
    parent = i//2
    l = len(key)
    smallest = i
    if left < l and key[left].f < key[i].f:
        smallest = left
    if right < l and key[right].f < key[i].f:
        smallest = right
    if parent < l and key[parent].f > key[i].f:
        min_heapify(key,parent)
    if smallest != i:
        temp = key[i]
        key[i] = key[smallest]
        key[smallest] = temp
        # print('min',key,smallest)
        min_heapify(key,smallest)
        min_heapify(key,i)
def build_min_heap(key):
    heap_size = len(key)
    i = 0
    while i <= heap_size//2:
        min_heapify(key,i)
        # print(i,key)
        i+=1
def extract_min(key):
    if len(key)<=0:
        return 'error'
    min = key[0]
    # print(key[0])
    key[0] = key[len(key)-1]
    del key[len(key)-1]
    min_heapify(key,0)
    return min
def cout(character,input_string):
    i = 0
    for x in input_string:
        if x == character:
            i +=1
    return i
def min_heap_insert(key,node):
    key.append(node)
    i = len(key)-1
    while i>0 and key[i//2].f > key[i].f:
        temp = key[i]
        key[i] = key[i//2]
        key[i//2] = temp
        i = i//2
def build_huffman_tree(key):
    build_min_heap(key)
    l = len(key)
    i = 0
    # print(key)
    while i <l-1 :
        # print(key)
        # print("i:",i)
        low =extract_min(key)
        low2 = extract_min(key)
        super_char = low.c +low2.c
        super_fre = low.f +low2.f
        super_node = Node(super_char,super_fre)
        super_node.left = low
        super_node.right = low2
        min_heap_insert(key,super_node)
        i+=1
        # print('low',low,'low2',low2)
        # print('key',key)
    return extract_min(key)
def huffman_encode(input_string):
    #cout the string
    key = []
    counted = []
    result = ''
    for x in input_string:
        if x not in counted:
            counted.append(x)
            fre = cout(x,input_string)
            key.append(Node(x,fre))
    # print(key)
    root = build_huffman_tree(key)
    for y in input_string:
        z = root
        # print(y)
        while y != z.c and z != None:
            # print(z)
            if y in z.left.c:
                result+='0'
                z = z.left
                # print('left')
            elif y in z.right.c:
                result +='1'
                z = z.right
                # print('right')
    return result



#  DO NOT EDIT BELOW THIS LINE

tests = ['message0.txt','message1.txt','message2.txt','message3.txt',
         'message4.txt','message5.txt']
correct = ['message0encoded.txt','message1encoded.txt',
           'message2encoded.txt','message3encoded.txt',
           'message4encoded.txt','message5encoded.txt']


#Run test cases, check whether encoding correct
count = 0

try:
    for i in range(len(tests)):
        ("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Reading message from:",tests[i])
        fp = open(tests[i])
        message = fp.read()
        fp.close()
        print("Reading encoded message from:",correct[i])
        fp2 = open(correct[i])
        encoded = fp2.read()
        fp2.close()
        output = huffman_encode(message)
        if i < 5:
            print("Running: huffman_encode on '"+message+"'\n")
            print("Expected:",encoded,"\nGot     :",output)
        assert encoded == output, "Encoding incorrect!"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(tests),"tests passed.")
