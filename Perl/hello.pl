#!/usr/bin/perl

print "Hello, world!\n";

@arrays = qw(socks shoes shorts);
print "the array contains ", $#arrays+1, " items\n";
print "The first of the items in arrays is \"", ${arrays[0]}, "\".\n" ;
