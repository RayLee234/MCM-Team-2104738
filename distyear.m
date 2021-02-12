function output = distyear(data,r1,r2)
%returns the similarity of year at r1 and year at r2

global W weights_char weights_vocal;
song1 = table2array(data(r1,3:14));
song2 = table2array(data(r2,3:14));
    output = sqrt(sum((song1(:, 1:7) - song2(:, 1:7)) .* (song1(:, 1:7) - song2(:, 1:7)) .* weights_char) * W(1) + sum((song1(:, 8:12) - song2(:, 8:12)) .* (song1(:, 8:12) - song2(:, 8:12)) .* weights_vocal) * W(2));
