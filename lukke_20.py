'''On the 1024th day of Christmas my true love gave to me

1024 cores computing
⋮
12 ladies dancing
11 …

Med den modifiserte utgaven av sangen, hvor mange gaver må vår true love skaffe?

For de som ikke gidder å høre på sangen, er dette de tre første versene.

On the first day of Christmas,
my true love sent to me
A partridge in a pear tree.

On the second day of Christmas,
my true love sent to me
Two turtle doves,
And a partridge in a pear tree.

On the third day of Christmas,
my true love sent to me
Three French hens,
Two turtle doves,
And a partridge in a pear tree.'''

# (1) (1,2) (1,2,3)


print(sum(sum(range(i+1)) for i in range(1025)))
