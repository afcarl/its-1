close all;
clear all;
grid = load ('grid.datx');

imshow (grid);
title ('grid');
gray = mat2gray (grid);
gray = gray .^ 0.2;
gray = histeq (gray);
gray (gray == max (gray(:))) = 1.0;
showmap (gray, 'enhanced');
bw = vote (grid);
showmap (bw, 'voted');
pd = push_down (bw, grid, .5);
showmap (pd, 'push down');
pu = pull_up (pd, bw - pd, grid, 0.6);
showmap (pu, 'pull up');
thinn = bwmorph (pu > 0, 'thin', Inf);
showmap (thinn, 'thin');

    CC = bwconncomp (thinn);
    filter = zeros(CC.ImageSize,'uint32');
    for k = 1 : CC.NumObjects
        if numel (CC.PixelIdxList{k}) >= 3
            filter(CC.PixelIdxList{k}) = 1;
        end
    end
    filter = filter > 0;
showmap (filter, 'filter');
map = lineup (filter, grid);
showmap (map, 'line up');
