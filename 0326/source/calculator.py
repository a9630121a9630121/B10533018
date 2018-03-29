

def cal(key,*args):
    args=list(args)
    if key=='+':
        return sum(args)
    elif key=='-':
        for i in args[1:len(args)]:
            args[0]-=i
        return args[0]
    elif key=='*':
        for i in args[1:len(args)]:
            args[0]*=i
        return args[0]
    elif key=='/':
        for i in args[1:len(args)]:
            args[0]/=i
        return args[0]
    else:
    	return '運算符號錯誤'

def calcu():
	try:
	    x1=input('請輸入運算符號:')   
	    x2=float(input('請輸入數字:')) 
	    x3=input('請輸入數字:')
	    x4=cal(x1,x2,float(x3))
	except:
		x4='輸入有誤'
	finally:
		print(x4)

