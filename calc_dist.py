#Purpose: To observe whether approximation of KC calculations are similar to values of KC described in research papers
from kc import *

#random strings should have high complexity
string = "n[:V2<uP'o(yQl.L`^OgyTCu0.czT7z'6+yN]\$U;v}" 
KC = approximate_KC_string(string)
print "\nRandom string KC = %f" % KC

string = "8tQ{TC2d~/sl5|yE_~_|P-4`X.$rG8J^zp))263[g#|" 
KC = approximate_KC_string(string)
print "\nRandom string KC = %f" % KC

string = "3Q8yJ9S21uHPQ73yFWG7rnRlWQYOp2dAK0kyLXqbnHn" 
KC = approximate_KC_string(string)
print "\nRandom string KC = %f" % KC

string = "77174C77CFD9004025E13A11D0A2AE1AD3309C52487" 
KC = approximate_KC_string(string)
print "\nRandom string KC = %f" % KC

#non-random strings should have low complexity
string = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
KC = approximate_KC_string(string)
print "\nNon-random string KC = %f" % KC

#non-random strings should have low complexity
string = "1231231231231231231231231123123123123123123"
KC = approximate_KC_string(string)
print "\nNon-random string KC = %f" % KC

#non-random strings should have low complexity
string = "ATCGATCGATGCATCGATCGATCGATCGATCGATCGATCGATC"
KC = approximate_KC_string(string)
print "\nNon-random string KC = %f" % KC

#two identical sequences should have NID=0
x = "AAAAAAA"
y = "AAAAAAA"
distance = approximate_NID(x, y)
print "\nIdentical sequence NID = %f" % distance
distance = approximate_NID_v2(x, y)
print "\nIdentical sequence NID v2 = %f" % distance

x = "123412341234"
y = "123412341234"
distance = approximate_NID(x, y)
print "\nIdentical sequence NID = %f" % distance
distance = approximate_NID_v2(x, y)
print "\nIdentical sequence NID v2 = %f" % distance

x = "3Q8yJ9S21uHPQ73yFWG7rnRlWQYOp2dAK0kyLXqbnHn"
y = "3Q8yJ9S21uHPQ73yFWG7rnRlWQYOp2dAK0kyLXqbnHn"
distance = approximate_NID(x, y)
print "\nIdentical sequence NID = %f" % distance
distance = approximate_NID_v2(x, y)
print "\nIdentical sequence NID v2 = %f" % distance

#sequences that share no information should have NID=1
x = "%\QzyGV2UV%7J0WW'PYr|B_Q["
y = "xm2hJch1fFUyFDc74IP1orUQ"
distance = approximate_NID(x, y)
print "\nNon-identical sequence NID = %f" % distance
distance = approximate_NID_v2(x, y)
print "\nNon-identical sequence NID v2 = %f" % distance

x = "HU;r[7OGuWdWx@MCu(wBsJ5eQu]"
y = "abcd"
distance = approximate_NID(x, y)
print "\nNon-identical sequence NID = %f" % distance
distance = approximate_NID_v2(x, y)
print "\nNon-identical sequence NID v2 = %f" % distance

#we should have D(x,y) = D(y,x) (symmetry)
x = "AAAAA"
y = "AAAAA"
distance1 = approximate_NID(x, y)
distance2 = approximate_NID(y, x)
print "\nD(x,y) = D(y,x): %f = %f" % (distance1, distance2)
distance1 = approximate_NID_v2(x, y)
distance2 = approximate_NID_v2(y, x)
print "\nD(x,y) = D(y,x): %f = %f" % (distance1, distance2)

x = "3Q8yJ9S21uHPQ73yFWG7rnRlWQYOp2dAK0kyLXqbnHn"
y = "lkasdfnaefinwpeofindnf2309ru0fhq2ef"
distance1 = approximate_NID(x, y)
distance2 = approximate_NID(y, x)
print "\nD(x,y) = D(y,x): %f = %f" % (distance1, distance2)
distance1 = approximate_NID_v2(x, y)
distance2 = approximate_NID_v2(y, x)
print "\nD(x,y) = D(y,x): %f = %f" % (distance1, distance2)

#we should have D(x,y) <= D(x,z) + D(z,y) (triangle inequality)
x = "abcd"
y = "#$NLNDF"
z = "23423"
distance1 = approximate_NID(x, y)
distance2 = approximate_NID(x, z)
distance3 = approximate_NID(z, y)
print "\nD(x,y) <= D(x,z) + D(z,y): %f <= %f + %f" % (distance1, distance2, distance3)

x = "abcd"
y = "#$NLNDF"
z = "23423"
distance1 = approximate_NID_v2(x, y)
distance2 = approximate_NID_v2(x, z)
distance3 = approximate_NID_v2(z, y)
print "\nD(x,y) <= D(x,z) + D(z,y): %f <= %f + %f" % (distance1, distance2, distance3)
