grid = load ('gridcdata.dat');
grid (1, 1) = 0;
gray = mat2gray (grid);
gray = gray .^ 0.2;
medianfilter = @(block_struct) block_struct.data > ...
    median(block_struct.data (:));
bw = blockproc (gray, [16, 16], medianfilter);
pull (gray, bw);