#!/usr/bin/perl
@lines = `man man`;
foreach (@lines) {
s/\w<([^>]+)>/\U$1/g;
print;
}
