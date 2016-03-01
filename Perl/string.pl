#!/usr/bin/perl

@anArray = [ 1, 1, 12, 12];
print "that " x 3 . "\n" . 3*3 . "\n";

# and here's a quoted list

@new = qw/ new thing is also very popular although not necessaryly efficient /;

print "also @new \n";

while ($#new >= 0 ) {
    print $new[-1]. "\n";
    pop @new;
};
print "\n";
print $new[-1]. "\n";    
