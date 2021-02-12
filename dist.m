function d = dist(i, j)
    global DATA_transformed W weights_char weights_vocal;
    song1 = DATA_transformed(i, :);
    song2 = DATA_transformed(j, :);
    song1 = table2array(song1(:, 2:13));
    song2 = table2array(song2(:, 2:13));
    d = sqrt(sum((song1(:, 1:7) - song2(:, 1:7)) .* (song1(:, 1:7) - song2(:, 1:7)) .* weights_char) * W(1) + sum((song1(:, 8:12) - song2(:, 8:12)) .* (song1(:, 8:12) - song2(:, 8:12)) .* weights_vocal) * W(2));
end