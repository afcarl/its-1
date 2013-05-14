function bw = genmap ()
    %% preprocess to get gray pic
    close all;
    grid = load ('gridcdata.dat');
    grid (1, 1) = 0;
    gray = mat2gray (grid);
    gray = gray .^ 0.2;
    %imshow (gray);
    %title ('gray');


    %% median filter
    medianfilter = @(block_struct) block_struct.data > ...
        median(block_struct.data (:));
    bw1 = blockproc (gray, [16, 16], medianfilter);
    bw2 = blockproc (gray, [20, 20], medianfilter);
    bw3 = blockproc (gray, [24, 24], medianfilter);
    bw4 = blockproc (gray, [28, 28], medianfilter);
    bw = bw1 .* bw2 .* bw3 .* bw4;
    %figure, imshow (bw);
    %title ('blockproc');
    

    %% pull down pixels
    bw = pull_down (bw, gray, 1);
    %figure, imshow (bw);
    %title ('pull down');
    %% pull up high pixels
    bw = pull_up (bw, gray, 0.9);
    %figure, imshow (bw);
    %title ('pull up');

    %bw = bwmorph (bw, 'clean');
    

    %% push down low pixels
    bw = push_down (bw, gray, 0.8);
    %figure,imshow (bw);
    %title ('push down');

    
    %% pull up high pixels
    bw = pull_up(bw, gray, 0.8);
    %figure, imshow (bw);
    %title ('pull up'); 
    
    %%
	bw = bwmorph (bw, 'clean');
	%figure, imshow (bw);
	%title ('clean');
	%% leave biggest connecting component
    cc = bwconncomp (bw);
    labeled = labelmatrix(cc);
    %bw = connect_labeled (labeled, gray);
    bw = labeled == 1;
    imshow (bw);
    
    
    %bw = labeled == 1;
    %RGB_label = label2rgb(labeled, @copper, 'c', 'shuffle');
    %imshow(RGB_label,'InitialMagnification','fit');
%     figure, imshow (bw);
%     title ('connect component');
    %bw = bwmorph (bw, 'thin', Inf);
%     figure, imshow (bw);
%     title ('thin');
    %branch = bwmorph (bw, 'branchpoints');
%     imshow (branch);
%     figure, imshow (bw - branch);
    
    %cc = bwconncomp (bw - branch);
    %labeled = labelmatrix(cc);
    %imtool (labeled);
   % RGB_label = label2rgb(labeled, @jet, 'k', 'shuffle');
    %imshow(RGB_label,'InitialMagnification','fit');
end

