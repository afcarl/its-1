function pull (gray, bw)
close all;
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
cc = bwconncomp (map);
labeled = labelmatrix(cc);
map = labeled == 1;

%RGB_label = label2rgb(labeled, @copper, 'c', 'shuffle');
%imshow(RGB_label,'InitialMagnification','fit');

%% push down low pixels
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

%% push up high pixels
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