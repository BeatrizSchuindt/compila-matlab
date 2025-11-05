% Exemplo de código 'MatlabLike'
a = 1;
b = 0;

while a < 10
    if a == 5
        b = b + 10;
    elseif a == 6 && b > 5
        b = b * 2;
    else
        b = b + 1;
    end

    a = a + 1;
end

% Loop for
total = 0;
for i = 1:10
    total = total + i;
end