function triangulo()
    disp('Classificador de Triangulos');

    a = input('Digite o lado a: ');
    b = input('Digite o lado b: ');
    c = input('Digite o lado c: ');

    if (a <= 0 | b <= 0 | c <= 0)
        disp('Erro: Medidas devem ser positivas.');
    else
        
        if ((a + b) > c & (a + c) > b & (b + c) > a)
            
            if ((a == b) & (b == c))
                disp('Triangulo equilatero valido');
            elseif ((a == b) | (a == c) | (b == c))
                disp('Triangulo isosceles valido');
            else
                disp('Triangulo escaleno valido');
            end
            
        else
            disp('Medidas invalidas (nao forma um triangulo)');
        end
        
    end
    
end
