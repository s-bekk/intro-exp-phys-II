import numpy as np
import math
from .base_distribution import BaseDistribution

class Dist_sb6187(BaseDistribution):
	def __init__(self):
		self.f_max = 0.2
		self.x_min = -2
		self.x_max = 4.5


	def pdf(self, x):
		"""This is your PDF"""
		return (1/13.06437166)*((math.sin(x)*math.cos(x))+2)

	def mean(self):
		"""This is the mean of the PDF"""
		return 1.344

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 1.902
