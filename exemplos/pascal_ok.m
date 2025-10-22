n = input('n (>=1): ');
if (n < 1)
  error('n deve ser >= 1');
end

for i = 0:n-1
  c = 1;
  for j = 0:i
    fprintf('%d ', c);
    c = c * (i - j) / (j + 1);
  end
  fprintf('\n');
end
