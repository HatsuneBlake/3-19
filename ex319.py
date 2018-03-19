class N(object):

	def __init__(self,name,value):
		self._name = name
		self._value = value

	def __getattr__(self,attr):
		print 'Get:',attr
		if attr == 'name':
			return self._name
		if attr == 'value':
			return self._value**2
			

	def __setattr__(self,attr,value):
		print 'Change',attr
		if attr == 'name':
			attr = '_name'
		if attr == 'value':
			attr = '_value'
		self.__dict__[attr] = value
		
		

			
if __name__ == '__main__':
	x = N('J',2)
	print x.name
	print x.value
	print
	
	x.value = 3
	print x.value