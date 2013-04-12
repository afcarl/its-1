BEGIN {
	FS = ","
    ominx = 0#116.330
    omaxx = 180#116.372
    ominy = 0#39.964
    omaxy = 90#39.990

    dminx = 116.370
    dmaxx = 116.409
    dminy = 39.887
    dmaxy = 39.910
}
{
	if (inorig($5, $6) && indest($8, $9)) {
		print 
	}
}
function inorig (x, y)
{
	return (x >= ominx && x < omaxx &&
	       	y >= ominy && y < omaxy)
}
function indest (x, y) 
{
	return (x >= dminx && x < dmaxx &&
	       	y >= dminy && y < dmaxy)
}
