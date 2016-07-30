import sys


if __name__=="__main__":
	if(len(sys.argv)<3):
		print("缺少参数:duplicate.py file1.txt file2.txt")
		exit(0)
	baseFile = open(sys.argv[1],'r')  #基准数据
	checkFile= open(sys.argv[2],'r')  #比对数据
	baseData = set([line.strip('\n') for line in baseFile.readlines()])
	checkData= set([line.strip('\n') for line in checkFile.readlines()])
	dstFile=open("dstFile.txt",'w')
	for line in checkData-baseData:  #从比对数据中去除与基准有交集的
		dstFile.write(line+'\n')
	dstFile.close()
	baseFile.close()
	checkFile.close()
	print('done')