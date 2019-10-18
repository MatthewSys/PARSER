from bs4 import BeautifulSoup
import os,re,textwrap,requests


class main():

	def __init__(self):
		self.paragr = 'p'
		self.title = 'h1'
		self.empty = ''
		self.path = ''
		self.name = ''

	def Input(self):
		print("Введи URL")
		url = str(input(""))
		self.Engine(url)

	def Engine(self, url):
		res = BeautifulSoup(requests.get(url).content, 'html.parser')
		list = self.empty
		list_t=self.empty
		for tag in res.select(self.title):
			list_t += '{}\n'.format(tag.text)

		for tag in res.select(self.paragr):
			list += '{}\n'.format(tag.text)
		self.Formater(list,list_t,url)

	def Formater(self,list,list_t,url):
		list = textwrap.fill(list, width=80)
		list=list_t+list
		self.Saver(list,url)

	def Saver(self,list,url):
		url=url.split(':/')[1][:-1]
		self.path=os.getcwd()+url
		os.makedirs(self.path)
		print(url)
		self.name=re.findall(r'\w+$',url)[0]+'.txt'
		self.path=self.path+self.name
		file = open(self.path, 'w')
		file.write(list)
		file.close()


if __name__=='__main__':
	egz=main()
	egz.Input()
