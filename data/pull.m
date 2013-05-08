function pull (gray, bw)
close all;
imtool (gray);
map = bw;
for i = 2:size (bw,1) -1
    for j = 2:size(bw,2) -1
        if bw(i,j) > 0
            continue
        end
        for x = i-1:i+1
            for y = j-1:j+1
                if gray (x, y) < gray(i,j) * 1.3
                    map (x, y) = 0;
                end
            end
        end
    end
end
figure,imshow (map);
bw = map;
for i = 2:size (bw,1) -1
    for j = 2:size(bw,2) -1
        if bw(i,j) == 0
            continue
        end
        for x = i-1:i+1
            for y = j-1:j+1
                if gray (x, y) < gray(i,j) * 0.85
                    map (x, y) = 0;
                end
            end
        end
    end
end
figure,imshow (map);
bw=map;
for i = 2:size (bw,1) -1
    for j = 2:size(bw,2) -1
        if bw(i,j) == 0
            continue
        end
        for x = i-1:i+1
            for y = j-1:j+1
                if gray (x, y) > gray(i,j) * 0.9
                    map (x, y) = 1;
                end
            end
        end
    end
end
figure,imshow (map);
bw=map;
for i = 2:size (bw,1) -1
    for j = 2:size(bw,2) -1
        if bw(i,j) == 0
            continue
        end
        for x = i-1:i+1
            for y = j-1:j+1
                if gray (x, y) > gray(i,j) * 0.95
                    map (x, y) = 1;
                end
            end
        end
    end
end
bw=map;
for i = 2:size (bw,1) -1
    for j = 2:size(bw,2) -1
        if bw(i,j) == 0
            continue
        end
        for x = i-1:i+1
            for y = j-1:j+1
                if gray (x, y) > gray(i,j) * 0.95
                    map (x, y) = 1;
                end
            end
        end
    end
end
figure, imshow (map);
end