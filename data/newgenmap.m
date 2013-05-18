close all;
clear all;
grid = load ('grid.datx');
bw = vote (grid);
imshow (bw);
pd = push_down (bw, grid, .5);
figure, imshow (pd);
pu = pull_up (pd, bw - pd, grid, 0.6);
figure, imshow (pu);
    CC = bwconncomp (pu);
    filter = zeros(CC.ImageSize,'uint32');
    for k = 1 : CC.NumObjects
        if numel (CC.PixelIdxList{k}) >= 3
            filter(CC.PixelIdxList{k}) = 1;
        end
    end
    filter = filter > 0;
    figure, imshow (filter);
map = lineup (filter, grid);
figure, imshow (map);
