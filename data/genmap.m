function bw = genmap ()
    %% preprocess to get gray pic
    close all;
    grid = load ('gridcdata.dat');
    grid (1, 1) = 0;
    gray = mat2gray (grid);
    gray = gray .^ 0.2;
    %imtool (gray);
    imshow (gray);
    %title ('gray');


    %% median filter
    figure, imshow (gray);
    medianfilter = @(block_struct) block_struct.data > ...
        median(block_struct.data (:));
    bw1 = blockproc (gray, [13, 13], medianfilter);
    bw2 = blockproc (gray, [31, 31], medianfilter);
    bw = bw1 .* bw2;
    %figure, imshow (bw1);
    %figure, imshow (bw2);
    figure, imshow (bw);
    title ('blockproc');
    

    %% pull down pixels
    %remain = pull_down (bw, gray, 1.1);
    %down = bw - remain;
    %bw = remain;
    %figure, imshow (bw);
    %title ('pull down');
    %% pull up high pixels
    %bw = pull_up (bw, gray, down == 0, 0.7);
    %figure, imshow (bw);
    %title ('pull up');

    %bw = bwmorph (bw, 'clean');
    

    %% push down low pixels
    remain = push_down (bw, gray, 0.8);
    down = bw - remain;
    figure,imshow (remain);
    title ('push down');

    
    %% pull up high pixels
    bw = pull_up(remain, down, gray, 0.8);
    figure, imshow (bw);
    title ('pull up'); 
    
%     %%
% 	bw = bwmorph (bw, 'clean');
% 	figure, imshow (bw);
% 	title ('clean');
	%% leave biggest connecting component
    CC = bwconncomp (bw);
    L = zeros(CC.ImageSize,'uint32');
    index = 1;
    for k = 1 : CC.NumObjects
        if numel (CC.PixelIdxList{k}) >= 3
            L(CC.PixelIdxList{k}) = index;
            index = index + 1;
        end
    end
    %bw = connect_labeled (labeled, gray);
    bw = L > 0;
    bw = lineup (bw, gray);
    %bw = labeled == 1;
    %RGB_label = label2rgb(labeled, @copper, 'c', 'shuffle');
    %imshow(RGB_label,'InitialMagnification','fit');
%     figure, imshow (bw);
%     title ('connect component');
%     bw = bwmorph (bw, 'thin', Inf);
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

