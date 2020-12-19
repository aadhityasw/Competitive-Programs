# Pattern Matching (Python)

# string is already given to you. Please don't edit this string.

stringData = "qwe sdf dsld dssdfsqwe sdlcsd fdslkcsdsdk sdvnsdnvs dsvd d d dddqwelkmvl sdlksf qwelkmdsldm dsfkmsdf ds lknvnv dsdfdfnoiewqwek sdjnsdf djndsjnnqwnewefsjdc kqwj fsdfjsldnlsqwelkwnekennlksnq dlkneknqwn wqenln qlwn qlwknr wkernwen dkfndks ewqsdkslf efwekwkewqwen mdfsdfsdfskdnlknqwenknfsd lsklksna kasndasndqweq we qkewkwj e kjnqwne sd kqjwnekjqnwda kjqwnej dajqkjwe k wd qwekqwle kjnwqkejqw qwe jqnwjnqw djwnejwd"



pattern = input()
n = len(pattern)

count = 0
for i in range(len(stringData)-n+1) :
    if pattern == stringData[i:i+n] :
        count += 1
print(count)
