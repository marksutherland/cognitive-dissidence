#!/usr/bin/ruby
# script to calculate a and b such that N = a/(2^b) +e for a given N and e
#
require "bigdecimal"
require "bigdecimal/math"

include BigMath

n = BigDecimal(ARGV[0])
e_min = BigDecimal(ARGV[1])
e_max = BigDecimal(ARGV[2])
nn = BigDecimal("0")
a = 1
b = 0

until (n - nn).abs < e_max do

	if 2**b > a 
		a += 1
		b = 0
	else 
		b += 1
	end

	nn = BigDecimal(a.to_s)/(2**b)
	if (n - nn).abs < e_min 
		print "a = " + a.to_s + ", " + "b = " + b.to_s + "\n"
		print "en = " + (n - nn).to_s + "\n"
	end
end

print "N = " + n.to_s + "\n"
print "a = " + a.to_s + "\n"
print "b = " + b.to_s + "\n"
print "Nn = " + nn.to_s + "\n"
