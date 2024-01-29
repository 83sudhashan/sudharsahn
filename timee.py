import time
def duration(fun):
    def inner():
        start=time.time()
        fun()
        end=time.time()
        print(f'the total time token to answer them question is {end-start}')
    return inner

@duration
def question1():
    print('what is u r name')
    respose=input('enter ur name:- ')

@duration
def question2():
    print('what is u r frd1 name')
    respose=input('enter u r frd1 name:- ')

@duration
def question3():
    print('what is u r  frd2 name')
    respose=input('enter u r frd2 name:- ')
