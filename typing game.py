from time import time


def tperror(prompt):
    global inwords

    words = prompt.split()
    errors=0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if words[i]==words[i]:
                continue
            else:
                errors=errors+1
        else:
            if inwords[i]==words[i]:
                if(inwords[i+1]==words[i+1]) & (inwords[i-1]==words[i-1]):
                    continue
                else:
                    errors +=1
            else:
                errors +=1
        return errors

def speed(inprompt , stime, etime):
    global time
    global inwords

    inwords=inprompt.split()
    twords=len(inwords)
    speed=twords/time

    return speed
def elasedtime(stime,etime):
    time=etime-stime
    return time

if __name__=="__main__":
    prompt="python is an interpreted,high-level,general-purpose programming language.Created by Guido van Rossum and first released in 1991,python"
    print("Tyepe this:- ",prompt,"")

    input("Press enter when you are ready to check your speed!!")

    stime=time()
    inprompt=input()
    etime=time()

    time=round(elasedtime(stime,etime),2)
    speed=speed(inprompt,stime,etime)
    errors=tperror(prompt)

    print("total time elapsed:",time,"seconds")
    print("yout average speed was",speed,"words per minute(w/m)")
    print("words the total of ",errors,"errors")

