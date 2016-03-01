#!/usr/bin/perl

print "Enter some text: ";
chomp($line = <STDIN>);
if ($line eq "\n"){
    print "You didn't supply any result. Exiting ...";
    quit();
}else {
    print "You typed: $line". "\n";
}
@rocks = qw{ flintstone slate rubble };
print "quartz (@rocks) limestone\n";

foreach @reverse(@rocks){
    print $_ . "\n";
};
