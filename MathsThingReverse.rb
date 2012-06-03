#!/usr/bin/ruby
# script to calculate a and b such that N = a/(2^b) +e for a given N and e
#
require "bigdecimal"
require "bigdecimal/math"

include BigMath

n = BigDecimal(ARGV[0])
e = BigDecimal(ARGV[1])
nn = BigDecimal("0")
a = 1
b = 0

# 1) Find the nearest power of 2
# 2) Determine a
# 3) See if e is small enough

until (n - nn).abs < e do

	if 2**b > a 
		a += 1
		b = 0
	else 
		b += 1
	end

	nn = BigDecimal(a.to_s)/(2**b)
#	print "a = " + a.to_s + "\n"
#	print "b = " + b.to_s + "\n"
#	print "Nn = " + nn.to_s + "\n"
#	print "N - Nn = " + (n - nn).to_s + "\n"
end

print "N = " + n.to_s + "\n"
print "a = " + a.to_s + "\n"
print "b = " + b.to_s + "\n"
print "Nn = " + nn.to_s + "\n"
