function genmap ()
    %% preprocess to get gray pic
    close all;
    grid = load ('gridcdata.dat');
    grid (1, 1) = 0;
    gray = mat2gray (grid);
    gray = gray .^ 0.2;
    imshow (gray);


    %% median filter
    medianfilter = @(block_struct) block_struct.data > ...
        median(block_struct.data (:));
    bw = blockproc (gray, [16, 16], medianfilter);
    bw = bwmorph (bw, 'clean');
    figure, imshow (bw);

    %% pull down pixels
    bw = pull_down (bw, gray, 1.3);

    %% pull up high pixels
    bw = pull_up (bw, gray, 0.9);


    %% leave biggest connecting component
    cc = bwconncomp (bw);
    labeled = labelmatrix(cc);
    bw = labeled == 1;
    %RGB_label = label2rgb(labeled, @copper, 'c', 'shuffle');
    %imshow(RGB_label,'InitialMagnification','fit');


    %% push down low pixels
    bw = push_down (bw, gray, 0.85);
    figure,imshow (bw);


    %% push up high pixels
    bw = push_up(bw, gray, 0.9);
    bw = push_up (bw, gray, 0.95);


    map = bw;
    figure, imshow (map);
end

