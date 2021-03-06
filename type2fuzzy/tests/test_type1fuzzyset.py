import unittest
from type2fuzzy.membership.type1fuzzyset import Type1FuzzySet


class TestType1FuzzySet(unittest.TestCase):

	def test_name_property_repr(self):
		set_representation = '''0.100/1.000 + 0.200/2.000
				+ 0.300/3.000 + 0.400/4.000'''
		t1fs = Type1FuzzySet.from_representation(set_representation, 'test')

		self.assertEqual(t1fs.name, 'test')

	def test_name_property_trian(self):
		low = 0
		mid = 0.5
		hi = 1
		univ_low = 0
		univ_hi = 1
		univ_res = 11

		t1fs = Type1FuzzySet.create_triangular(univ_low, univ_hi, univ_res, low, mid, hi, 'test')

		self.assertEqual(t1fs.name, 'test')





	def test_from_representation(self):

		set_representation = '''0.100/1.000 + 0.200/2.000
				+ 0.300/3.000 + 0.400/4.000'''
		t1fs = Type1FuzzySet.from_representation(set_representation)

		self.assertEqual(t1fs[1], 0.1)
		self.assertEqual(t1fs[2], 0.2)
		self.assertEqual(t1fs[3], 0.3)
		self.assertEqual(t1fs[4], 0.4)

	def test_to_representation(self):

		set_representation = '0.100/1.000 + 0.200/2.000 + 0.300/3.000 + 0.400/4.000'

		t1fs = Type1FuzzySet.from_representation(set_representation)

		rep_result = t1fs.__str__()

		self.assertEqual(rep_result, set_representation)

	def test_generate_triangular_1(self):
		low = 0
		mid = 0.5
		hi = 1
		univ_low = 0
		univ_hi = 1
		univ_res = 11

		t1fs = Type1FuzzySet.create_triangular(univ_low, univ_hi, univ_res, low, mid, hi)

		self.assertEqual(t1fs[0.0], 0.0)
		self.assertEqual(t1fs[0.1], 0.2)
		self.assertEqual(t1fs[0.2], 0.4)
		self.assertEqual(t1fs[0.3], 0.6)
		self.assertEqual(t1fs[0.4], 0.8)
		self.assertEqual(t1fs[0.5], 1.0)
		self.assertEqual(t1fs[0.6], 0.8)
		self.assertEqual(t1fs[0.7], 0.6)
		self.assertEqual(t1fs[0.8], 0.4)
		self.assertEqual(t1fs[0.9], 0.2)
		self.assertEqual(t1fs[1.0], 0)


	def test_generate_triangular_2(self):
		low = 0
		mid = 0
		hi = 1
		univ_low = 0
		univ_hi = 1
		univ_res = 11

		t1fs = Type1FuzzySet.create_triangular(univ_low, univ_hi, univ_res, low, mid, hi)

		self.assertEqual(t1fs[0.0], 1.0)
		self.assertEqual(t1fs[0.1], 0.9)
		self.assertEqual(t1fs[0.2], 0.8)
		self.assertEqual(t1fs[0.3], 0.7)
		self.assertEqual(t1fs[0.4], 0.6)
		self.assertEqual(t1fs[0.5], 0.5)
		self.assertEqual(t1fs[0.6], 0.4)
		self.assertEqual(t1fs[0.7], 0.3)
		self.assertEqual(t1fs[0.8], 0.2)
		self.assertEqual(t1fs[0.9], 0.1)
		self.assertEqual(t1fs[1.0], 0.0)

	def test_generate_triangular_3(self):
		low = 0
		mid = 1
		hi = 1
		univ_low = 0
		univ_hi = 1
		univ_res = 11

		t1fs = Type1FuzzySet.create_triangular(univ_low, univ_hi, univ_res, low, mid, hi)

		self.assertEqual(t1fs[0.0], 0.0)
		self.assertEqual(t1fs[0.1], 0.1)
		self.assertEqual(t1fs[0.2], 0.2)
		self.assertEqual(t1fs[0.3], 0.3)
		self.assertEqual(t1fs[0.4], 0.4)
		self.assertEqual(t1fs[0.5], 0.5)
		self.assertEqual(t1fs[0.6], 0.6)
		self.assertEqual(t1fs[0.7], 0.7)
		self.assertEqual(t1fs[0.8], 0.8)
		self.assertEqual(t1fs[0.9], 0.9)
		self.assertEqual(t1fs[1.0], 1.0)

	def test_create_triangular_ex(self):

		primary_domain = list(range(0,11))

		set_1 = Type1FuzzySet.create_triangular_ex(primary_domain, 0,5,10)

		self.assertEqual(set_1[0], 0.0)
		self.assertEqual(set_1[1], 0.2)
		self.assertEqual(set_1[2], 0.4)
		self.assertEqual(set_1[3], 0.6)
		self.assertEqual(set_1[4], 0.8)
		self.assertEqual(set_1[5], 1.0)
		self.assertEqual(set_1[6], 0.8)
		self.assertEqual(set_1[7], 0.6)
		self.assertEqual(set_1[8], 0.4)
		self.assertEqual(set_1[9], 0.2)
		self.assertEqual(set_1[10], 0.0)
		
	def test_domain_limits(self):

		set_representation = '''0.000/1.000 + 0.200/2.000
				+ 0.300/3.000 + 0.400/4.000'''
		t1fs = Type1FuzzySet.from_representation(set_representation)

		domain_limits = t1fs.domain_limits()

		self.assertEqual(domain_limits.left, 1.0)
		self.assertEqual(domain_limits.right, 4.0)