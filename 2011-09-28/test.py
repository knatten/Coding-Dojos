import unittest

class Brett:
	def lag_brett(self, dim):
		brett = list()
		for i in range(0, dim):
			brett.append([False]*3)
		return brett

	def __init__(self,dim):        
		self.brett = self.lag_brett(dim)

	def gi_liv(self,x,y):
		self.brett[x][y] = True

	#def gi_liv_liste(self, liste):
	#	for i in range(0,len(liste))

	def er_levende(self, x, y):
		if 0 <= x < len(self.brett) and 0 <= y < len(self.brett):
			return self.brett[x][y]
		return False		

	def neste_runde(self):
		nytt_brett = self.lag_brett(len(self.brett))
		for i in range(0,len(nytt_brett)):
			for j in range(0,len(nytt_brett)):
				nytt_brett[i][j] = self.oppstaar(i,j) or self.overlever(i,j)
		self.brett = nytt_brett

	def antall_naboer(self, x, y):
		return self.er_levende(x-1,y-1)+self.er_levende(x,y-1)+self.er_levende(x+1,y-1)+\
			self.er_levende(x-1, y)+self.er_levende(x+1,y)+\
			self.er_levende(x-1,y+1)+self.er_levende(x,y+1)+self.er_levende(x+1,y+1)

	def oppstaar(self, x, y):
		return self.antall_naboer(x,y) == 3

	def overlever(self,x,y):
		return self.er_levende(x,y) and 2 <= self.antall_naboer(x,y) <=3

	def __repr__(self):
		string = "\n"		
		for i in range(0,len(self.brett)):
			for j in range(0,len(self.brett)):
				string += "*" if self.er_levende(i,j) else 'o'
			string += "\n"
		return string

#def __main__(self):
#	brett = Brett(10)
	

class TestNabo(unittest.TestCase):
	def test_antall_naboer_med_null_naboer(self):
		brett = Brett(3)
		antall_naboer = brett.antall_naboer(1,1)
		self.assertEqual(0,antall_naboer)

	def test_lever(self):
		brett = Brett(3)
		brett.gi_liv(2,2)
		self.assertTrue(brett.er_levende(2,2))
		self.assertFalse(brett.er_levende(1,1))
		self.assertFalse(brett.er_levende(0,0))
		self.assertFalse(brett.er_levende(2,1))
		self.assertFalse(brett.er_levende(1,2))

	def test_antall_naboer_med_en_nabo(self):
		brett = Brett(3)
		brett.gi_liv(0,0)
		self.assertEqual(1,  brett.antall_naboer(1,1))
		brett.gi_liv(0,1)
		self.assertEqual(2,  brett.antall_naboer(1,1))
	
	def test_er_fortsatt_levende_med_to_naboer(self):
		brett = Brett(3)
		brett.gi_liv(1,1)
		brett.gi_liv(0,0)
		brett.gi_liv(0,1)
		brett.neste_runde()
		self.assertTrue(brett.er_levende(1,1))

	def test_doer_hvis_kun_en_nabo(self):
		brett = Brett(3)
		brett.gi_liv(1,1)
		brett.gi_liv(2,1)
		brett.neste_runde()
		self.assertFalse(brett.er_levende(1,1))

	def test_oppstaar_med_tre_naboer(self):
		brett = Brett(3)
		brett.gi_liv(0,0)
		brett.gi_liv(1,0)
		brett.gi_liv(2,0)
		self.assertTrue(brett.oppstaar(1,1))

	def test_oppstaar_ikke__med_fler_enn_tre_naboer(self):
		brett = Brett(3)
		brett.gi_liv(0,0)
		brett.gi_liv(1,0)
		brett.gi_liv(2,0)
		brett.gi_liv(2,1)
		self.assertFalse(brett.oppstaar(1,1))
	
	def test_oppstaar_ikke_med_to_naboer(self):
		brett = Brett(3)
		brett.gi_liv(0,0)
		brett.gi_liv(1,0)
		self.assertFalse(brett.oppstaar(1,1))	
	
	def test_overlever_med_to_naboer(self):
		brett = Brett(3)
		brett.gi_liv(0,0)
		brett.gi_liv(1,0)
		brett.gi_liv(1,1)
		self.assertTrue(brett.overlever(1,1))
		
	def test_doer_med_fire_naboer(self):
		brett = Brett(3)
		brett.gi_liv(0,0)
		brett.gi_liv(1,0)
		brett.gi_liv(2,2)
		brett.gi_liv(2,0)
		
		brett.gi_liv(1,1)
		self.assertFalse(brett.overlever(1,1))

unittest.main()
