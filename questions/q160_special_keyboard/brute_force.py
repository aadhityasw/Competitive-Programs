class Solution:

    def recursiveCount(self, options_left, current_count, buffer_count) :
        if options_left == 0 :
            if current_count > self.max_count :
                self.max_count = current_count
            return

        if options_left > 3 and buffer_count < current_count:
            self.recursiveCount(options_left - 3, current_count * 2, current_count)
        
        if buffer_count > 1 :
            self.recursiveCount(options_left - 1, current_count + buffer_count, buffer_count)
        else :
            self.recursiveCount(options_left - 1, current_count + 1, buffer_count)


    def optimalKeys(self, N):
        self.max_count = N

        self.recursiveCount(N, 0, 0)

        return self.max_count
