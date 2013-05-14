function L = markmap (filteredmap)
neighbor = zeros (size (filteredmap), 'uint32');
thin = bwmorph (filteredmap, 'thin', Inf);
for i = 2:size (thin, 1) - 1
    for j = 2:size (thin, 2) - 1
        if thin (i,j) == 0
            continue
        end
        s = 0;
        for x = i-1:i+1
            for y = j-1:j+1
                s = s + thin (x, y);
            end
        end
        neighbor (i,j) = s -1;
    end
end
road = (neighbor == 2) + (neighbor == 1);
intersection = (neighbor > 0) - road;
close all;
imshow (thin);
figure, imshow (road);
ccroad = bwconncomp (road);
disp (ccroad);
figure, imshow(intersection);
ccinter = bwconncomp (intersection);
disp (ccinter);

L = zeros(ccinter.ImageSize,'uint32');
for k = 1 : ccinter.NumObjects
        L(ccinter.PixelIdxList{k}) = k;
end
for k = 1 : ccroad.NumObjects
    L (ccroad.PixelIdxList{k}) = k + 10000;
end
end