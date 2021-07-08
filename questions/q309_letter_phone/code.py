class Solution:

    def generateLetterMap(self) :
        self.letter_map = {str(i) : [] for i in range(10)}
        self.letter_map['0'] = ['0']
        self.letter_map['1'] = ['1']

        for i in range(15) :
            self.letter_map[str(i//3 + 2)].append(chr(i+97))
        self.letter_map['7'] = ['p', 'q', 'r', 's']
        self.letter_map['8'] = ['t', 'u', 'v']
        self.letter_map['9'] = ['w', 'x', 'y', 'z']
        #print(self.letter_map)


    def recurse(self, arr, stack) :

        n = len(arr)
        if n == 0 :
            self.ans.append(stack)
            return
        
        dig = arr[0]
        for ch in self.letter_map[dig] :
            self.recurse(arr[1:], stack+ch)



	# @param A : string
	# @return a list of strings
	def letterCombinations(self, A):

        self.generateLetterMap()

        self.ans = []
        self.recurse(A, "")

        return self.ans
