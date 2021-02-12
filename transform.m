function output = transform(A)
T = A;
%Normalize and reshape the data in A;
num_cols = 2:16; %numerical cols
[nr,nc] = size(T);

for i = 2:12;
    if i ~= 7
        col = table2array(T(:,i));
        sk = skewness(col);

        if abs(sk) > 2
            col = normalize(boxcox(normalize(col, 'range',[1 2])),'range', [0 1]);
        else
            col = normalize(col, 'range', [0 1]);
        end
    T(:,i) = array2table(col);

    end
    
end


for i = 2:16
    figure(i);
    histogram(table2array(T(:,i)));
end

output = T;
    

