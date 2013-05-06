grid = load ('gridcdata.dat');
grid (1, 1) = 0;
gray = grid ./ max (max (grid));
gray = gray .^ 0.2;
%imtool (gray);

grid (gray > .5) = 0;
gray = grid ./ max (max (grid));
gray = gray .^ .2;
gray (gray < .5) = 0;
imtool (gray);